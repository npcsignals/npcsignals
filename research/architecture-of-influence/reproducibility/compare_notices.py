#!/usr/bin/env python3
"""Compare original and corrected TikTok H2 2025 notices report ZIPs."""
import argparse, csv, io, json, zipfile
from pathlib import Path

def find_csv(z, suffix):
    found=[n for n in z.namelist() if not n.startswith('__MACOSX/') and n.endswith(suffix)]
    if len(found)!=1: raise ValueError(f'expected one {suffix}, found {found}')
    return found[0]

def load(path,suffix):
    with zipfile.ZipFile(path) as z:
        bad=z.testzip()
        if bad: raise ValueError(f'corrupt zip member: {bad}')
        name=find_csv(z,suffix)
        raw=list(csv.reader(io.StringIO(z.read(name).decode('utf-8-sig'))))
    heads=raw[0]; data=raw[1:]
    if any(len(row)!=len(heads) for row in data): raise ValueError('non-rectangular CSV row')
    duplicates={h:[i for i,v in enumerate(heads) if v==h] for h in heads if heads.count(h)>1}
    for h,pos in duplicates.items():
        if any(len({row[i] for i in pos})!=1 for row in data): raise ValueError(f'conflicting duplicate header values: {h}')
    unique=[]
    for i,h in enumerate(heads):
        if h not in unique: unique.append(h)
    rows=[]
    for row in data:
        d={}
        for i,h in enumerate(heads):
            if h not in d: d[h]=row[i]
        rows.append(d)
    return {'member':name,'physical_columns':len(heads),'unique_columns':len(unique),'duplicate_headers':{h:[i+1 for i in ix] for h,ix in duplicates.items()},'headers':unique,'rows':rows}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('original');ap.add_argument('corrected');ap.add_argument('--out',default='comparison.json');a=ap.parse_args()
    old=load(a.original,'4_notices.csv'); new=load(a.corrected,'4_notices_updated_28082026.csv')
    code='Category of illegal content'
    def keyed(o):
        parent='';out={}
        for r in o['rows']:
            v=r.get(code,'')
            if v.startswith('STATEMENT_CATEGORY_'): parent=v
            k=(parent,v)
            if k in out: raise ValueError(f'duplicate category key: {k}')
            out[k]=r
        return out
    x,y=keyed(old),keyed(new)
    if x.keys()!=y.keys(): raise ValueError('category keys differ; investigate row/category alignment')
    shared=set(old['headers'])&set(new['headers'])
    changes=[]
    for k in x:
        for field in sorted(shared):
            if x[k].get(field)!=y[k].get(field): changes.append({'key':list(k),'field':field,'old':x[k].get(field),'new':y[k].get(field)})
    parent_totals={}
    for label,codeprefix in [('category_10','STATEMENT_CATEGORY_RISK_FOR_PUBLIC_SECURITY'),('category_13','STATEMENT_CATEGORY_UNSAFE_AND_PROHIBITED_PRODUCTS')]:
        pk=next(k for k in y if k[1]==codeprefix); childkeys=[k for k in y if k[0]==codeprefix and k!=pk]
        parent_totals[label]={'corrected_parent':y[pk].get('Number of notices received'),'numeric_child_subtotal':sum(int(y[k]['Number of notices received']) for k in childkeys if y[k].get('Number of notices received','').isdigit()),'blank_children':sum(not y[k].get('Number of notices received','') for k in childkeys)}
    out={'row_count':{'original':len(old['rows']),'corrected':len(new['rows'])},'columns':{'original':{x:old[x] for x in ('physical_columns','unique_columns','duplicate_headers')},'corrected':{x:new[x] for x in ('physical_columns','unique_columns','duplicate_headers')}},'distinct_headers_removed':sorted(set(old['headers'])-set(new['headers'])),'distinct_headers_added':sorted(set(new['headers'])-set(old['headers'])),'changed_shared_cells':len(changes),'changes':changes,'corrected_parent_child_arithmetic':parent_totals,'warning':'Arithmetic only. Do not infer category additivity, event identity, transfer, cause, or intent.'}
    Path(a.out).write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'out':a.out,'rows':out['row_count'],'columns':out['columns'],'changed_shared_cells':len(changes)},indent=2,ensure_ascii=False))
if __name__=='__main__': main()
