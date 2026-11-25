from collect import call
import json
from pathlib import Path
P=Path(__file__).resolve().parent;cursor=0;rows={};pages=[]
for i in range(12):
 q={'type':'userFillsByTime','user':'0x1464dacaceb0d511f9964cdac5eba50ea42220bf','startTime':cursor}
 d=call('seller_raw_page_'+str(i),q)
 if not isinstance(d,list):break
 pages.append({'page':i,'start':cursor,'rows':len(d)})
 for x in d:rows[(x['hash'],x['tid'])]=x
 if len(d)<2000:break
 nxt=max(x['time'] for x in d)
 if nxt<=cursor:break
 cursor=nxt
(P/'evidence/seller_raw_pagination.json').write_text(json.dumps({'pages':pages,'fills':sorted(rows.values(),key=lambda x:(x['time'],x['tid']))},indent=2));print(pages,flush=True)
