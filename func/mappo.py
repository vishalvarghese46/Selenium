'''
a = [1,2,3,4,5]

lol = map(lambda x: x*2, a)
for num in lol:
    print(num, end="")
    '''
from pprint import PrettyPrinter
from collections import namedtuple

pp = PrettyPrinter(indent=4)

Scientist = namedtuple('Scientist', "name field born nobel")
ada = Scientist("Ada Lovelace", "math", 1815, nobel=False)
emmy = Scientist("Emmy Noether", "math", 1882, nobel=False)
mar = Scientist("Marie Curie", "physics", 1867, nobel=True)
tu = Scientist("Tu Youyou", "chemistry", 1930, nobel=True)
jab = Scientist("Jabeena Ubaid", "chemistry", 1928, nobel=False)
sal = Scientist("Sally Ride", "physics", 1928, nobel=False)
ligi = Scientist("Ligi KL", "math",1930, nobel=True)
shaddy = (ada,emmy,mar,tu,sal,ligi)
#pp.pprint(shaddy)
'''
lol = tuple(map(lambda x: {
    'name': x.name, 'age': 2020-x.born}, shaddy))

pp.pprint(lol)

'''

#pp.pprint(lor := [{'name': x.name, 'age':2020-x.born } for x in shaddy])
lol = filter(lambda x:x.nobel is True, shaddy)
for i in lol:
    print(i.name)