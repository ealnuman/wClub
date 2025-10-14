import os, sys, json, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIX=os.path.join(ROOT,'fixtures')

def fail(m):
    print('❌',m); sys.exit(1)

def ok(m):
    print('✅',m)
for f in ['hooks.py','modules.txt','patches.txt','config/desktop.py','config/docs.py']:
    p=os.path.join(ROOT,f)
    if not os.path.isfile(p) or os.path.getsize(p)==0: fail(f'Missing or empty: {f}')
ok('Core files present')
if not os.path.isdir(FIX): fail('fixtures missing')
for name in ['roles.json','workflows.json','reports.json','workspace_wclub.json','email_template.json','dashboard_chart.json','notification.json']:
    p=os.path.join(FIX,name)
    if not os.path.isfile(p): fail('Missing fixture: '+name)
    with open(p,'r',encoding='utf-8') as fh:
        data=json.load(fh)
        if not data: fail('Empty fixture: '+name)
ok('Fixtures validated')
for dt in ['member','class_session','booking']:
    d=os.path.join(ROOT,'doctype',dt)
    if not os.path.isdir(d) or not glob.glob(os.path.join(d,'*.json')): fail('Doctype JSON missing: '+dt)
ok('Doctypes present')
print('✅ Validation passed')
