import json,datetime,hashlib,zipfile,csv
from pathlib import Path
from decimal import Decimal as D
P=Path(__file__).resolve().parent;R=P/'evidence/raw';E=P/'evidence'
def load(n):return json.loads((R/(n+'.response')).read_text())
def utc(n):return datetime.datetime.fromtimestamp(n/1000,datetime.timezone.utc).isoformat()
def save(n,d):(E/n).write_text(json.dumps(d,indent=2)+'\n')
with zipfile.ZipFile(E/'frogman_baseline_evidence.zip') as z:
 base='frogman_baseline/';m=json.loads(z.read(base+'SHA256SUMS.json'));assert all(hashlib.sha256(z.read(base+n)).hexdigest()==h for n,h in m.items())
 baseline=json.loads(z.read(base+'summary.json'));accounts=json.loads(z.read(base+'accounts.json'));assert len(accounts)==36 and sum(D(x['current_xmr1']) for x in accounts)==D('3586.887420')
 costs=json.loads(z.read(base+'baseline_cost_evidence/accounts_35.json'));extra=json.loads(z.read(base+'baseline_cost_evidence/additional_36_fills.json'));cost=sum(D(x['usdc_spent']) for x in costs)+sum(D(x['sz'])*D(x['px']) for x in extra);assert cost==D('2029761.5937')
 for n in ['price_1m.csv','accounts.csv','summary.json','accounts.json']:(E/('baseline_'+n)).write_bytes(z.read(base+n))
save('baseline_validation.json',{'verified_manifest_entries':len(m),'accounts':36,'xmr1':'3586.887420','execution_cost_usdc':str(cost),'cutoff':baseline['cutoff_utc'],'classification':'CONFIRMED: saved checkpoint integrity and arithmetic; no new account collection'})
meta=load('spotMeta');tokens=[]
for n in ['XMR1','HXMR','ZEC1','TAO1','TRX1']:
 t=next(x for x in meta['tokens'] if x['name']==n);d=load(n+'_details');balances=load(n+'_issuer_spot')['balances'];bal=next((D(x['total']) for x in balances if x['token']==t['index']),D(0));tokens.append({'name':n,'metadata':t,'deployer':d['deployer'],'deployment_timestamp_as_returned':d['deployTime'],'max_supply':d['maxSupply'],'total_supply':d['totalSupply'],'api_circulating_supply':d['circulatingSupply'],'genesis':d['genesis'],'issuer_current_inventory':str(bal),'issuer_share_of_total_percent':str(100*bal/D(d['totalSupply'])),'classification':'CONFIRMED api metadata/inventory, not monero reserves or liabilities'})
save('token_comparison.json',tokens)
for name in ['HXMR_deployer_signers','HXMR_treasury_signers']:
 d=load(name);assert d['threshold']==2 and len(d['authorizedUsers'])==3
issuer=load('issuer_incident_ledger_no_end');seller=load('seller_incident_ledger_no_end');transfers=[x for x in issuer if x['delta'].get('token')=='XMR1'];assert sum(D(x['delta']['amount']) for x in transfers)==D('5200000');assert all(any(x['hash']==y['hash'] and x['delta']==y['delta'] for y in seller) for x in transfers)
a=load('seller_aggregated');b=load('seller_fills_no_end');assert a==b
assert len(a)<2000 and len({(x['hash'],x['tid']) for x in a})==len(a)
x=[r for r in a if r['coin']=='@260'];sells=[r for r in x if r['side']=='A'];buys=[r for r in x if r['side']=='B'];cut=int(datetime.datetime(2026,11,20,13,tzinfo=datetime.timezone.utc).timestamp()*1000);early=[r for r in sells if r['time']<cut]
out=[r for r in seller if r['delta'].get('user')=='0x1464dacaceb0d511f9964cdac5eba50ea42220bf' and r['delta'].get('token')=='XMR1'];outq=sum(D(r['delta']['amount']) for r in out)
system=[r for r in seller if r['delta'].get('token')=='USDC' and r['delta'].get('destination')=='0x2000000000000000000000000000000000000000'];gross=sum(D(r['sz'])*D(r['px']) for r in sells);fees=sum(D(r['fee']) for r in sells if r.get('feeToken')=='USDC');qty=sum(D(r['sz']) for r in sells);spot=load('seller_spot')['balances'];actual=D(next(r['total'] for r in spot if r['token']==404))
f={'issuer_transfers':[{'utc':utc(r['time']),**r} for r in transfers],'issuer_transferred_xmr1':'5200000','side_transfers_xmr1':str(outq),'side_transfer_count':len(out),'xmr1_buy_quantity':str(sum(D(r['sz']) for r in buys)),'xmr1_sold_all_returned':str(qty),'gross_proceeds_all_returned_usdc':str(gross),'usdc_trade_fees_all_returned':str(fees),'net_xmr1_sale_proceeds_usdc':str(gross-fees),'last_sale_utc':utc(max(r['time'] for r in sells)),'first_sale_utc':utc(min(r['time'] for r in sells)),'through_13utc_quantity':str(sum(D(r['sz']) for r in early)),'through_13utc_gross_usdc':str(sum(D(r['sz'])*D(r['px']) for r in early)),'system_usdc_transfers':str(sum(D(r['delta']['amount']) for r in system)),'system_transfer_count':len(system),'system_transfer_warning':'HyperCore system destination; not independently matched to all Arbitrum receipts; never count as a second loss','expected_xmr1_before_unexplained_adjustment':str(D('5200000')-outq-qty),'observed_seller_xmr1':str(actual),'xmr1_residual_unresolved':str(actual-(D('5200000')-outq-qty)),'coverage':'two identical aggregated responses below 2000; unaggregated older response was capped; no consensus replay; explicitly timestamped current observations'}
save('financial_reconciliation.json',f);save('issuer_transfers.json',transfers);save('seller_transfers.json',seller)
with (E/'seller_aggregated_fills.csv').open('w') as o:w=csv.DictWriter(o,fieldnames=sorted(set().union(*(r.keys() for r in a))));w.writeheader();w.writerows(a)
# independently reproduced EVM examples and fixed-block native holdings
examples=[]
for n,c in [('tornado','ethereum'),('bridge','arbitrum'),('onward','ethereum')]:
 t=load(n+'_tx')['result'];r=load(n+'_receipt')['result'];b=load(n+'_block')['result'];assert t['hash']==r['transactionHash'] and t['blockHash']==r['blockHash']==b['hash'] and int(r['status'],16)==1 and t['hash'] in b['transactions'];examples.append({'stage':n,'chain':c,'hash':t['hash'],'from':t['from'],'to':t['to'],'native_value_eth':str(D(int(t['value'],16))/10**18),'block':int(b['number'],16),'utc':utc(int(b['timestamp'],16)*1000),'classification':'CONFIRMED execution; full bridge protocol association not reproduced'})
positions=[]
for chain,addrs in [('ethereum',['0x1464dacaceb0d511f9964cdac5eba50ea42220bf','0xf32d7842611a5d63b875075dadd19c55f3f1dc59']),('arbitrum',['0x1464dacaceb0d511f9964cdac5eba50ea42220bf'])]:
 assert int(load(chain+'_chain')['result'],16)==(1 if chain=='ethereum' else 42161);block=load(chain+'_snapshot_block')['result']
 for a in addrs:positions.append({'chain':chain,'address':a,'eth':str(D(int(load(chain+'_'+a+'_balance')['result'],16))/10**18),'nonce':int(load(chain+'_'+a+'_nonce')['result'],16),'block':int(block['number'],16),'block_utc':utc(int(block['timestamp'],16)*1000)})
save('evm_examples.json',examples);save('destination_positions.json',{'positions':positions,'total_eth':str(sum(D(r['eth']) for r in positions)),'scope':'three chain/address positions, two literal addresses; native holdings only, no freeze/recovery or exclusive source allocation'})
# candidate distributions, not assigned refunds
ours={r['address'] for r in accounts};dist=[]
for n in ['HXMR_treasury_ledger','distribution_a_ledger','distribution_b_ledger']:
 d=load(n);out=[r for r in d if r['delta'].get('type')in['send','spotTransfer']];dist.append({'source':n,'records_returned':len(d),'at_or_over_500':len(d)>=500,'events':out,'frogman_address_matches':sorted({a.lower() for r in out for a in [r['delta'].get('user',''),r['delta'].get('destination','')] if a.lower()in ours}),'meaning':'observable transfers; eligibility, compensation purpose and recipient identity not established'})
save('candidate_distributions.json',dist)
print(json.dumps(f,indent=2));print('positions',positions)
