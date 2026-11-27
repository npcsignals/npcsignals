from collect import call,P
import json
u='0x207700bd207df757825f9193ef9c648c1c65e06a';d=json.loads((P/'raw/userNonFundingLedgerUpdates.response').read_text());rows=d[:];pages=[len(d)]
for i in range(1,50):
 if len(d)<500:break
 cursor=max(r['time']for r in d);d=call('issuer_ledger_page_'+str(i),{'type':'userNonFundingLedgerUpdates','user':u,'startTime':cursor})
 if not isinstance(d,list):break
 pages.append(len(d));rows.extend(d)
 if not d or max(r['time']for r in d)<=cursor:break
(P/'issuer_pagination.json').write_text(json.dumps({'pages':pages,'records':rows},indent=2))
call('spotDeployState',{'type':'spotDeployState','user':u})
h=json.loads((P/'raw/hosting_primary.response').read_text());(P/'hosting_statement.json').write_text(json.dumps({k:v for k,v in h.items()if k!='config'and k!='publicGroupList'},indent=2));print('pages',pages);print((P/'hosting_statement.json').read_text()[:6000])
