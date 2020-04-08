import os
import json
from datetime import datetime, timedelta

startTime = datetime.now()
totalStores = 494

def runTime():
    exeTime = datetime.now()-startTime
    return f"{int(exeTime.seconds/60)} min {exeTime.seconds%60} sec"

def calcDate():
    today = datetime.today()
    reportDate = datetime.strftime(today, "%d-%m-%Y")
    return reportDate

file = open("sites.json")
result = open(f"{calcDate()}-ping.csv", "w+")

offlineCount=0
checkCount=0
data = json.load(file)

for site in data:
    no = site['storeNo']
    name = site['store']
    ipAddress = site['ipAddress']
    response = os.system("ping -c 1 " + ipAddress)
    if response == 0:
        print(name, "is Online")
    else:
        offlineCount += 1
        print(name, "is Offline")
        print(f'{str(no)},{str(name)},{str(ipAddress)}')
        result.write(f'{str(no)},{str(name)},{str(ipAddress)}\n')
    checkCount+=1
    print(f"[progress: {format(checkCount / totalStores * 100, '.2f')}% done... ({checkCount}/{totalStores}) completed.]\n")

result.write(f'\n\n\n,{str(offlineCount)} Sites Offline!')
print(f'***Task completed in {runTime()}')

file.close()
result.close()


