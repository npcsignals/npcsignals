import json,datetime
from decimal import Decimal as D
from pathlib import Path
P=Path(__file__).resolve().parent;E=P/'evidence';f=json.loads((E/'financial_reconciliation.json').read_text());d=json.loads((E/'seller_raw_pagination.json').read_text());a=d['fills'];x=[r for r in a if r['coin']=='@260'];s=[r for r in x if r['side']=='A'];b=[r for r in x if r['side']=='B'];fund=1795150018926
metrics={}
for name,ls in [('all_returned',s),('after_issuer_funding',[r for r in s if r['time']>=fund]),('after_funding_through_13utc',[r for r in s if fund<=r['time']<1795179600000])]:
 gross=sum(D(r['sz'])*D(r['px'])for r in ls);fees=sum(D(r['fee'])for r in ls if r.get('feeToken')=='USDC');metrics[name]={'fills':len(ls),'sold_xmr1':str(sum(D(r['sz'])for r in ls)),'gross_usdc':str(gross),'usdc_fees':str(fees),'net_usdc':str(gross-fees),'first_utc':datetime.datetime.fromtimestamp(min(r['time']for r in ls)/1000,datetime.timezone.utc).isoformat(),'last_utc':datetime.datetime.fromtimestamp(max(r['time']for r in ls)/1000,datetime.timezone.utc).isoformat()}
expected=D('5200000')+sum(D(r['sz'])for r in b)-sum(D(r['fee'])for r in x if r.get('feeToken')=='XMR1')-D('6000')-sum(D(r['sz'])for r in s)
f['raw_fill_reconciliation']={'pages':d['pages'],'unique_all_market_fills':len(a),'metrics':metrics,'prior_buy_xmr1':str(sum(D(r['sz'])for r in b)),'xmr1_buy_fees':str(sum(D(r['fee'])for r in x if r.get('feeToken')=='XMR1')),'expected_closing_xmr1':str(expected),'observed_closing_xmr1':f['observed_seller_xmr1'],'unallocated_residual_xmr1':str(D(f['observed_seller_xmr1'])-expected),'classification':'CONFIRMED first-party API arithmetic; residual retained; not consensus replay','correction':'raw unaggregated fills supersede aggregate price-times-size precision; tests before first issuer funding are separated'}
f['coverage']='raw pagination with overlapping timestamps, deduplicated hash/tid; 2000/2000/715 records; aggregate responses cross-check quantities; no-endTime queries resolve earlier empty bounded results; actual response times bound collection'
(E/'financial_reconciliation.json').write_text(json.dumps(f,indent=2));print(json.dumps(f['raw_fill_reconciliation'],indent=2))
