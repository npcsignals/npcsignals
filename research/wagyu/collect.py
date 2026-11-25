"""read-only public evidence collector. no transactions, signing or private data."""
import urllib.request,datetime,json,hashlib,concurrent.futures
from pathlib import Path
P=Path(__file__).resolve().parent;R=P/'evidence/raw'
def call(n,q=None,url='https://api.hyperliquid.xyz/info'):
 m={'url':url,'request':q,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,data=json.dumps(q).encode() if q is not None else None,headers={'Content-Type':'application/json','User-Agent':'npcsignals-public-research'})
  with urllib.request.urlopen(req,timeout=25) as r:b=r.read();m['http_status']=r.status
  (R/(n+'.response')).write_bytes(b);m.update(retrieved_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),sha256=hashlib.sha256(b).hexdigest());(R/(n+'.meta.json')).write_text(json.dumps(m,indent=2))
  try:return json.loads(b)
  except:return None
 except Exception as e:m['error']=str(e);m['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();(R/(n+'.error.json')).write_text(json.dumps(m,indent=2));return None
if __name__=='__main__':
 meta=call('spotMeta',{'type':'spotMeta'});tokens=[x for x in meta['tokens'] if x['name'] in ['XMR1','HXMR','ZEC1','TAO1','TRX1']]
 def token(t):
  d=call(t['name']+'_details',{'type':'tokenDetails','tokenId':t['tokenId']})
  if d and d.get('deployer'):
   call(t['name']+'_issuer_role',{'type':'userRole','user':d['deployer']});call(t['name']+'_issuer_spot',{'type':'spotClearinghouseState','user':d['deployer']})
 list(concurrent.futures.ThreadPoolExecutor(max_workers=4).map(token,tokens))
 for n,a in [('seller','0x1464dacaceb0d511f9964cdac5eba50ea42220bf'),('issuer','0x207700bd207df757825f9193ef9c648c1c65e06a')]:
  call(n+'_explorer',{'type':'userDetails','user':a},'https://api.hyperliquid.xyz/explorer')
  call(n+'_spot',{'type':'spotClearinghouseState','user':a})
 call('seller_aggregated',{'type':'userFillsByTime','user':'0x1464dacaceb0d511f9964cdac5eba50ea42220bf','startTime':0,'aggregateByTime':True})
