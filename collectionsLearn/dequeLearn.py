from collections import Counter
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

d = deque('ghi')
d.append('j')
d.appendleft('f')
print(list(d)) #list the contents of the deque
print(d, d[0])

d.extend('klm') #add multiple elements at once
d.extendleft('cde') #extendsLeft() reverses the order though
print(d)
d.pop() # delete the rightmost element
d.popleft() # pops from the left
print(d)
d.rotate()
print(d)