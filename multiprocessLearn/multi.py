from collections import namedtuple
from pprint import PrettyPrinter
import json

pp = PrettyPrinter(indent=4)

Store = namedtuple('Store', "id name elecMeter gasMeter")
data = json.load(open(r"F:\Python\Selenium\func\meterRef.json"))

database = []

f = lambda x: {
               'id': x['id'],
                'name': x['site'],
                'elecMeter': x['elecMeter'],
                    'gasMeter': None if x['gasMeter']=='' else x['gasMeter']}

x = map(f,data)

for i in x:
    database.append(Store(i['id'],i['name'],i['elecMeter'],i['gasMeter']))


database = tuple(database)
pp.pprint(database)
print("\n")

g = filter(lambda x: x.gasMeter is not None, database)
pp.pprint(tuple(g))





