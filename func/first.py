#functional programming work with immutable data structures

from collections import namedtuple
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

Scientist = namedtuple('Scientist', "name field born nobel")
ada = Scientist("Ada Lovelace", "math", 1815, nobel=False)
emmy = Scientist("Emmy Noether", "math", 1882, nobel=False)
mar = Scientist("Marie Curie", "physics", 1867, nobel=True)
tu = Scientist("Tu Youyou", "chemistry", 1930, nobel=True)
sal = Scientist("Sally Ride", "physics", 1928, nobel=False)

shaddy = (ada,emmy,mar,tu,sal)
fs = filter(lambda x:x.nobel is False , shaddy)
pp.pprint(list(fs))