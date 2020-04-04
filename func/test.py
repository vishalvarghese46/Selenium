from collections import namedtuple
from pprint import PrettyPrinter
import json

pp = PrettyPrinter(indent=4)

shaddy=[]
Store = namedtuple("Store", "no name elecMeter gasMeter")

data = json.load(open("meterRef.json"))

for site in data:
    g =lambda x: None if x == "" else x
    shaddy.append(ob:=Store(site['id'],site['site'],site['elecMeter'], g(site['gasMeter'])))
database = tuple(shaddy)

pp.pprint(database)
'''
g = filter(lambda x:x.gasMeter is not None, database)
for i in g:
    print(i)
'''