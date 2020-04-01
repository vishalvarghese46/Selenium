from collections import namedtuple
from pprint import PrettyPrinter
import json

pp = PrettyPrinter(indent=4)

shaddy=[]
Store = namedtuple("Store", "no name elecMeter")

data = json.load(jsonFile := open("elecDatabase.json"))
for site in data:
    shaddy.append(ob:=Store(site['no'],site['store'],site['device']))
pp.pprint(tuple(shaddy))

