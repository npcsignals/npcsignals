"""Offline verification of preserved bytes and material arithmetic. No network calls."""
from pathlib import Path
import json,hashlib,zipfile,re,xml.etree.ElementTree as ET
from decimal import Decimal as D
P=Path(__file__).resolve().parent;E=P/'evidence';R=E/'raw'
def load(n):return json.loads((R/(n+'.response')).read_text())
checks=[]
def ok(name,condition):assert condition,name;checks.append(name)
for p in R.glob('*.meta.json'):
 m=json.loads(p.read_text());q=p.with_name(p.name.replace('.meta.json','.response'));ok('response hash '+q.name,hashlib.sha256(q.read_bytes()).hexdigest()==m['sha256'])
zp=E/'frogman_baseline_evidence.zip'
ok('published baseline evidence identity',hashlib.sha256(zp.read_bytes()).hexdigest()=='8d354228029f5a0d405bb98b77dee5c6b55644b002ec2bf886f3a137dfc46e5b')
with zipfile.ZipFile(zp)as z:
 b='frogman_baseline/';man=json.loads(z.read(b+'SHA256SUMS.json'))
 for n,h in man.items():ok('baseline '+n,hashlib.sha256(z.read(b+n)).hexdigest()==h)
 a=json.loads(z.read(b+'accounts.json'));ok('36 quantities',len(a)==36 and sum(D(x['current_xmr1'])for x in a)==D('3586.887420'))
 costs=json.loads(z.read(b+'baseline_cost_evidence/accounts_35.json'));extra=json.loads(z.read(b+'baseline_cost_evidence/additional_36_fills.json'));ok('baseline acquisition cost',sum(D(x['usdc_spent'])for x in costs)+sum(D(x['sz'])*D(x['px'])for x in extra)==D('2029761.5937'))
i=load('issuer_incident_ledger_no_end');s=load('seller_incident_ledger_no_end');i=[r for r in i if r['delta'].get('token')=='XMR1']
ok('issuer amount',sum(D(r['delta']['amount'])for r in i)==D('5200000'))
ok('matched ledger events',all(any(x['hash']==y['hash']and x['delta']==y['delta']for y in s)for x in i))
raw={}
for n in range(3):
 for r in load('seller_raw_page_'+str(n)):raw[(r['hash'],r['tid'])]=r
ok('raw pagination count',len(raw)==4594)
f=json.loads((E/'financial_reconciliation.json').read_text())['raw_fill_reconciliation'];ok('saved pagination identity',sorted(raw.values(),key=lambda x:(x['time'],x['tid']))==json.loads((E/'seller_raw_pagination.json').read_text())['fills'])
for name,lo,hi in [('all_returned',0,10**20),('after_issuer_funding',1795150018926,10**20),('after_funding_through_13utc',1795150018926,1795179600000)]:
 ls=[r for r in raw.values()if r['coin']=='@260'and r['side']=='A'and lo<=r['time']<hi];m=f['metrics'][name];ok(name+' quantity',sum(D(r['sz'])for r in ls)==D(m['sold_xmr1']));g=sum(D(r['px'])*D(r['sz'])for r in ls);fees=sum(D(r['fee'])for r in ls if r.get('feeToken')=='USDC');ok(name+' gross and net',g==D(m['gross_usdc'])and g-fees==D(m['net_usdc']))
for n in ['HXMR_deployer_signers','HXMR_treasury_signers']:d=load(n);ok(n,d['threshold']==2 and len(set(d['authorizedUsers']))==3)
ok('old issuer no returned multisig configuration',load('XMR1_issuer_signers')is None)
for n in ['tornado','bridge','onward']:
 t=load(n+'_tx')['result'];r=load(n+'_receipt')['result'];b=load(n+'_block')['result'];ok(n+' inclusion',t['hash']==r['transactionHash']and t['blockHash']==r['blockHash']==b['hash']and t['hash']in b['transactions']and int(r['status'],16)==1)
p=json.loads((E/'destination_positions.json').read_text());ok('eth position sum',sum(D(r['eth'])for r in p['positions'])==D(p['total_eth']))
for n in P.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',n.read_text()):
  if not target.startswith(('https:','http:','#')):ok('local link '+n.name+' '+target,(n.parent/target.split('#')[0]).exists())
for n in (P/'visuals').glob('*.svg'):ET.parse(n);ok('svg '+n.name,True)
man=P/'SHA256SUMS.json'
if man.exists():
 for n,h in json.loads(man.read_text()).items():ok('manifest '+n,hashlib.sha256((P/n).read_bytes()).hexdigest()==h)
# publication-specific integrity checks, additional to the editorial evidence checks
source=json.loads((E/'original_editorial_manifest.json').read_text())
for q in list(R.glob('*'))+list((E/'historical_docs').glob('*'))+list((P/'visuals').glob('*.svg')):
 if q.is_file():ok('original evidence/figure '+q.name,hashlib.sha256(q.read_bytes()).hexdigest()==source[str(q.relative_to(P))])
original=json.loads((E/'original_baseline_manifest.json').read_text())
with zipfile.ZipFile(zp)as z:
 selected=json.loads(z.read('frogman_baseline/SHA256SUMS.json'))
 for n,h in selected.items():ok('original baseline byte identity '+n,h==original[n])
claims=json.loads((E/'claim_matrix.json').read_text())
ok('34 claims preserved',len(claims)==34)
ok('10 finalized svg figures',len(list((P/'visuals').glob('*.svg')))==10)
register=(P/'SOURCE_REGISTER.md').read_text()
ids=set(re.findall(r'\| (s\d+) \|',register))
for c in claims:ok('claim source '+c['id'],all(x.strip()in ids for x in c['sources'].split(',')))
for n in ['EDITORIAL_REVISION.md','PUBLICATION_READINESS.md','write_archive.py','complete_archive.py','make_visuals.py']:
 ok('excluded internal file '+n,not(P/n).exists())
print(json.dumps({'result':'PASS','checks':len(checks),'network_requests':0,'scope':'byte integrity, baseline arithmetic, matched transfers, fill pagination/proceeds, signer configuration, sampled EVM inclusion, links and SVG XML'},indent=2))
