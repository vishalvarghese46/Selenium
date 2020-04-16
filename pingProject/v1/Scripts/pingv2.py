import os
import json
from datetime import datetime
import time
from collections import namedtuple
from pprint import PrettyPrinter
import multiprocessing

pp = PrettyPrinter(indent=4)
Store = namedtuple("Store", "no name ip")


def calcDate():
    today = datetime.today()
    reportDate = datetime.strftime(today, "%d-%m-%Y")
    return reportDate

def ping(store):
    response = os.system("ping -c 1 " + store.ip)
    if response != 0:
        return f"{store.no},{store.name},{store.ip}"


def nTupleCreation(no, name, ip, database):
    ob = Store(no, name, ip)
    return database.append(ob)

def main():
    source = r"F:\Python\Selenium\pingProject\Scripts"
    destination = r"F:\Python\Selenium\pingProject\Scripts"

    file = open(f"{source}\sites.json")
    data = json.load(file)

    output = open(f"{destination}\{calcDate()}-ping.csv", "w+")
    database = []
    start = time.time()
    for site in data:
        no = site['storeNo']
        name = site['store']
        ipAddress = site['ipAddress']
        nTupleCreation(no, name, ipAddress, database)

    pool = multiprocessing.Pool()
    result = pool.map(ping, database)

    for o in list(result):
        if o!=None:
            output.write(f"{o}\n")
    file.close()

    output.close()
    end = time.time()
    print(f"time taken: {end-start:.2f}s")
if __name__ == '__main__':
    main()
