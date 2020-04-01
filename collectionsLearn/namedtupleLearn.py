from collections import namedtuple, deque

Point = namedtuple('Point', 'x y')
Color = namedtuple('Color','red,green blue')

p = Point(11,4)
c = Color(255,255,255)
Pixel = namedtuple("Pixel", Color._fields + Point._fields)
pi = Pixel(255,255,255,11,22)
print(pi._asdict())