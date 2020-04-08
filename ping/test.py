from collections import namedtuple
from pprint import PrettyPrinter
from functools import reduce

pp = PrettyPrinter(indent=4)

Store = namedtuple("Store", "no name ip")

yData = open("07042020.csv")
tData = open("08042020.csv")



def nTupleCreation(fileOb, database):
    for line in fileOb:
        ob = Store(line.rstrip().split(",")[0], line.rstrip().split(",")[1], line.rstrip().split(",")[2])
        database.append(ob)
    return database


t = nTupleCreation(tData, tDatabase := [])
y = nTupleCreation(yData, yDatabase := [])


yOfflineNo = list(map(lambda x: x.no, y))
tOfflineNo = list(map(lambda x: x.no, t))

newOffline = filter(lambda x: True if x.no not in yOfflineNo else False, t)
#newOffline = filter(lambda x: True if x not in listo else False, today)
newOnline = filter(lambda x: True if x.no not in tOfflineNo else False, y)


print(f"\nNew offline: ")
for i in newOffline:
    print(f"{i.no}, {i.name}, {i.ip}")


print(f"\nNew Online: ")
for i in newOnline:
    print(f"{i.no}, {i.name}, {i.ip}")

#newOfflineCount = reduce(lambda acc, val: acc + 1, newOffline,0)
