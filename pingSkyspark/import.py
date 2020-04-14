import json

data=json.load(open('sites.json'))
output=open('site601-700.csv','w+')
output.write(f"no,ob\n")
for site in data:
    if(int(site['storeNo']<=700 and int(site['storeNo']>600))):
        print(f"{site['storeNo']},{site['store']}")
        output.write(f"{site['storeNo']},{site['store']}\n")