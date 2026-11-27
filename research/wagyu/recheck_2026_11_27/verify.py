"""Offline public-edition verification. No network requests and no repository writes."""
from pathlib import Path
from decimal import Decimal as D
import json,hashlib,csv,zipfile,re,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent;E=P/'evidence';count=0
sha=lambda b:hashlib.sha256(b).hexdigest()
def check(x,n):
 global count
 assert x,n
 count+=1
for n,h in json.loads((P/'SHA256SUMS.json').read_text()).items():check(sha((P/n).read_bytes())==h,n)
original=json.loads((E/'original_supplement_manifest.json').read_text())
with zipfile.ZipFile(E/'ledger_pages.zip')as z:
 for n,h in json.loads(z.read('SHA256SUMS.json')).items():check(sha(z.read(n))==h==original[n],n)
 for n in z.namelist():
  if n.endswith('.json')and n.startswith('raw/'):
   d=json.loads(z.read(n))
   if d.get('sha256'):check(sha(z.read(n.removesuffix('.json')+'.response'))==d['sha256'],n+' response')
with zipfile.ZipFile(E/'inherited_evidence.zip')as z:
 old={n.strip().removeprefix('./'):h for h,n in (line.split(None,1)for line in z.read('ORIGINAL_SHA256SUMS').decode().splitlines())}
 selected=json.loads(z.read('SHA256SUMS.json'))
 for n,h in selected.items():check(sha(z.read(n))==h==old[n],n)
load=lambda n:json.loads((P/'raw'/n).read_text())
for p in (P/'raw').glob('*.json'):
 d=json.loads(p.read_text())
 if d.get('sha256'):check(sha(p.with_suffix('.response').read_bytes())==d['sha256'],p.name)
for p in list((P/'raw').glob('*'))+list((P/'visuals').rglob('*')):
 if p.is_file():check(sha(p.read_bytes())==original[str(p.relative_to(P))],'original byte identity '+str(p.relative_to(P)))
e=json.loads((E/'matched_transfer.json').read_text())['matched_event'];a=load('treasury_userNonFundingLedgerUpdates.response');b=load('recipient_userNonFundingLedgerUpdates.response');check(e in a and e in b and D(e['delta']['amount'])==10000,'matched transfer')
rows=list(csv.DictReader((E/'frogman_36_accounts.csv').open()));check(len(rows)==36 and sum(D(r['xmr1'])for r in rows)==D('3586.887420'),'36 accounts')
check(D('3586.887420')*D('.0018')==D('6.456397356'),'bid arithmetic');check(D('13398820.7090639602')-D('13398815.44801162')==D('5.2610523402'),'issuer arithmetic')
for p in (P/'visuals').rglob('*.svg'):ET.parse(p);check(True,p.name)
for p in P.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',p.read_text()):
  if not target.startswith(('http:','https:','#')):check((p.parent/target.split('#')[0]).exists(),p.name+' -> '+target)
old=json.loads((E/'original_reader_SHA256SUMS.json').read_text());check(sha((E/'original_reader_START_HERE.md').read_bytes())==old['START_HERE.md'],'historical reader identity')
current=json.loads((P.parent/'SHA256SUMS.json').read_text());check({k:v for k,v in old.items()if k!='START_HERE.md'}=={k:v for k,v in current.items()if k!='START_HERE.md'},'unchanged original evidence checksum entries')
check((P.parent/'START_HERE.md').read_bytes().startswith((E/'original_reader_START_HERE.md').read_bytes()),'append-only original reader navigation')
check(len(list((P/'visuals').glob('*.svg')))==3,'three updated figures');check(len(list((P/'visuals/historical_2026_11_25').glob('*.svg')))==3,'three historical figures')
print(json.dumps({'result':'PASS','checks':count,'network_requests':0,'scope':'publication digests, archive members, original byte identity, request/response hashes, transfer/account arithmetic, links and SVG syntax'},indent=2))
