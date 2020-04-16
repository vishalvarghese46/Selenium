import os
import json
from datetime import datetime
import time
from collections import namedtuple
from pprint import PrettyPrinter
import concurrent.futures

pp = PrettyPrinter(indent=4)
Store = namedtuple("Store", "no name ip sur man")


def calcDate():
    today = datetime.today()
    reportDate = datetime.strftime(today, "%d-%m-%Y")
    return reportDate

def ping(store):
    response = os.system("ping -c 1 " + store.ip)
    if response != 0:
        return f"{store.no},{store.name},{store.ip},{store.sur},{store.man}"


def nTupleCreation(no, store, ip, sur, man, database):
    ob = Store(no, store, ip, sur, man)
    return database.append(ob)

def main():
    source = r"F:\Python\Selenium\pingProject\Scripts"
    destination = r"F:\Python\Selenium\pingProject\Scripts"

    file = open(f"{source}\sitesv2.json")
    data = json.load(file)

    output = open(f"{destination}\{calcDate()}-ping.csv", "w+")
    database = []
    start = time.time()
    for site in data:
        no = site['no']
        store = site['store']
        ip = site['ip']
        sur = site['surveyor']
        man = site['manager']
        nTupleCreation(no, store, ip, sur, man, database)

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
