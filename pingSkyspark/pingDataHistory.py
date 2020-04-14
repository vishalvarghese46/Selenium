import os
import json
from datetime import datetime
import time
from collections import namedtuple
from pprint import PrettyPrinter
import concurrent.futures

pp = PrettyPrinter(indent=4)
Store = namedtuple("Store", "no name ip")


def calcDate():
    today = datetime.today()
    reportDate = datetime.strftime(today, "%d-%m-%Y %H.%M")
    return reportDate

def ping(store):
    response = os.system("ping -c 1 " + store.ip)
    if response != 0:
        return f"{datetime.today().strftime('%d-%m-%Y %H:%M')},{store.no},{store.name},{store.ip},true"
    else:
        return f"{datetime.today().strftime('%d-%m-%Y %H:%M')},{store.no},{store.name},{store.ip},false"

def nTupleCreation(no, name, ip, database):
    ob = Store(no, name, ip)
    return database.append(ob)

def main():
    source = r"F:\Python\Selenium\pingSkyspark"
    destination = r"F:\Python\Selenium\pingSkyspark"

    file = open(f"{source}\sites.json")
    data = json.load(file)

    output = open(f"{destination}\{calcDate()}.csv", "w+")
    output.write(f"ts,no,objectName,ip,objectValue\n")
    database = []
    start = time.time()
    for site in data:
        no = site['storeNo']
        name = site['store']
        ipAddress = site['ipAddress']
        nTupleCreation(no, name, ipAddress, database)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(ping, database)

    for o in list(result):
        if o!=None:
            output.write(f"{o}\n")
    file.close()

    output.close()
    end = time.time()
    print(f"time taken: {end-start:.2f}s")
if __name__ == '__main__':
    main()
