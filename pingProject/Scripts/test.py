from collections import namedtuple
from pprint import PrettyPrinter
from functools import reduce
from datetime import datetime, timedelta

pp = PrettyPrinter(indent=4)

source = r'F:\Python\Selenium\pingProject\ping'
destination = r'F:\Python\Selenium\pingProject\googleSheetPost'


Store = namedtuple("Store", "no name ip")

todayDate = datetime.today().strftime("%d-%m-%Y")
yesterdayDate = (datetime.today() - timedelta(1)).strftime("%d-%m-%Y")

yData = open(f"{source}\{yesterdayDate}-ping.csv")
tData = open(f"{source}\{todayDate}-ping.csv")

def nTupleCreation(fileOb, database):
    for line in fileOb:
        ob = Store(line.rstrip().split(",")[0], line.rstrip().split(",")[1], line.rstrip().split(",")[2])
        database.append(ob)
    return database


t = nTupleCreation(tData, tDatabase := [])
y = nTupleCreation(yData, yDatabase := [])

yData.close()
tData.close()

yOfflineNo = list(map(lambda x: x.no, y))
tOfflineNo = list(map(lambda x: x.no, t))

newOffline = filter(lambda x: True if x.no not in yOfflineNo else False, t)
newOnline = filter(lambda x: True if x.no not in tOfflineNo else False, y)


#print(f"\nNew offline: ")
newOfflineList = []
for i in newOffline:
    newOfflineList.append(f"{i.no}, {i.name}, {i.ip}")
#pp.pprint(newOfflineList)

#print(f"\nNew Online: ")
newOnlineList = []
for i in newOnline:
    newOnlineList.append(f"{i.no}, {i.name}, {i.ip}")
#pp.pprint(newOnlineList)

todayOfflineCount = reduce(lambda acc, val: acc + 1, t,0)
mappo = map(lambda x: f"{x.no},{x.name},{x.ip}",t)

output = open(f"{destination}\{todayDate}-google.csv","w+")
output.write(f",Total offline stores today | {datetime.today().strftime('%d %b %Y')}:,{todayOfflineCount}\n")
output.write("\n")
output.write("no,store,ip\n")
for i in mappo:
    output.write(f"{i}\n")
output.write("\n")
output.write("\n")
output.write(f",New offline today:,{len(newOfflineList)}\n")
output.write("\n")
output.write("no,store,ip\n")
for n in newOfflineList:
    output.write(f"{n}\n")
output.write("\n")
output.write("\n")
output.write(f",Back online today:,{len(newOnlineList)}\n")
output.write("\n")
output.write("no,store,ip\n")
for o in newOnlineList:
    output.write(f"{o}\n")
output.close()

