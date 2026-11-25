from collect import call,P
import json,concurrent.futures
URL={'ethereum':'https://mainnet.gateway.tenderly.co','arbitrum':'https://arbitrum.gateway.tenderly.co'}
def rpc(n,chain,m,p):
 d=call(n,{'jsonrpc':'2.0','id':1,'method':m,'params':p},URL[chain]);return d.get('result') if d else None
for c in URL:
 rpc(c+'_chain',c,'eth_chainId',[]);b=rpc(c+'_snapshot_block',c,'eth_getBlockByNumber',['latest',False])
 if b:
  for a in (['0x1464dacaceb0d511f9964cdac5eba50ea42220bf','0xf32d7842611a5d63b875075dadd19c55f3f1dc59'] if c=='ethereum' else ['0x1464dacaceb0d511f9964cdac5eba50ea42220bf']):
   rpc(c+'_'+a+'_balance',c,'eth_getBalance',[a,b['number']]);rpc(c+'_'+a+'_nonce',c,'eth_getTransactionCount',[a,b['number']])
jobs=[('tornado','ethereum','0x33513047a342ea41bbcc6503aa8c889a8b5d05a4ef332354fba682fdc60b53ee'),('bridge','arbitrum','0x1b6f68247603d6c3d1754680d9f73aee87d1791a8e51ec92bea1dfa58a47733e'),('onward','ethereum','0x74a704c0b00bd9cb6c671e339f361718c7d885d5776d13074ecb0ed17edf4752')]
def one(j):
 n,c,h=j;t=rpc(n+'_tx',c,'eth_getTransactionByHash',[h]);r=rpc(n+'_receipt',c,'eth_getTransactionReceipt',[h])
 if t:rpc(n+'_block',c,'eth_getBlockByNumber',[t['blockNumber'],False])
list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(one,jobs))
