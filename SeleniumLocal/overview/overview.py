import json

file=open("overview.json")
data=json.load(file)
for location in data:
    name = location['store'].capitalize()
    print(str(location['no'])+" - "+name)