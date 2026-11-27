from pathlib import Path
import urllib.request,json,hashlib,datetime,concurrent.futures
P=Path(__file__).resolve().parent;R=P/'raw'
def call(n,q=None,u='https://api.hyperliquid.xyz/info'):
 m={'url':u,'request':q,'start_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(u,data=json.dumps(q).encode()if q else None,headers={'Content-Type':'application/json'}),timeout=25)as r:b=r.read();m['status']=r.status
  (R/(n+'.response')).write_bytes(b);m['sha256']=hashlib.sha256(b).hexdigest()
  try:d=json.loads(b)
  except:d=None
 except Exception as e:m['error']=str(e);d=None
 m['end_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat();(R/(n+'.json')).write_text(json.dumps(m,indent=2));return d
if __name__=='__main__':
 a='0x207700bd207df757825f9193ef9c648c1c65e06a';jobs=[]
 for t in ['spotClearinghouseState','clearinghouseState','userFills','userFillsByTime','userNonFundingLedgerUpdates','userFunding','historicalOrders','userRateLimit','userFees']:
  q={'type':t,'user':a}
  if t in ['userFillsByTime','userNonFundingLedgerUpdates','userFunding']:q['startTime']=0
  jobs.append((t,q))
 for t in ['userFillsByTime','userNonFundingLedgerUpdates']:
  for start in [1795580888797,1795500000000]:jobs.append((t+'_'+str(start),{'type':t,'user':a,'startTime':start}))
 with concurrent.futures.ThreadPoolExecutor(5)as e:list(e.map(lambda j:call(*j),jobs))
 for n,u in [('hosting_primary','https://status.1984.is/api/status-page/public'),('hosting_heartbeat','https://status.1984.is/api/status-page/heartbeat/public')]:call(n,u=u)
 for n,a in [('treasury','0x3980feaade07f42cd5b93916996a4b1afdc113d9'),('recipient','0x19c46f4bb8f50a74e4cc14d97ac070a0d8bc5221')]:
  for t in ['userNonFundingLedgerUpdates','userFillsByTime']:call(n+'_'+t,{'type':t,'user':a,'startTime':1795607300000})
