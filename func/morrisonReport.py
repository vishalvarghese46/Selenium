import requests
import datetime as DT
import sys
import json
import ssl
from datetime import datetime
import random
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

class report:
    def __init__(self, num, name, device, lyFromDate, lsToDate, tyFromDate, tyToDate, param, file):
        self.storeNo = num
        self.storeName = name
        self.meter = device
        self.lyFromDate = lyFromDate
        self.lsToDate = lsToDate
        self.tyFromDate = tyFromDate
        self.tyToDate = tyToDate
        self.param = param
        self.file = file

    def fetch(self, fromDate, toDate):
        total = 0
        auth = self.keyGen()
        url = f'http://api.dexcell.com/v3/readings?from={fromDate}T00:00:00&to={toDate}T23:59:59&device_id={self.meter}&parameter_key={self.param}&resolution=D&operation=DELTA'
        try:
            self.req = requests.get(url, headers=auth)
            data = self.req.json()
        except Exception as e:
            print(f'Problem meter: {self.meter}')
            print(f'{e} happened :(')
        for values in data['values']:
            sum = values['v']
            total += sum
        return total

    def keyGen(self):
        keys = ["85b4b72c40907800f752","2c2a5ae4c650bc833d89","3cd9772e61c284195258","859d26d241b4cda63ce6","95b0d0b85bf4a5a00a8c"]
        auth = {
            "x-dexcell-token": str(random.choice(keys)),
            "Accept": "application/json",
            "Accept-Charset": "utf-8",
            "Content-Type": "application/json"
        }
        return auth

    def fileWrite(self):
        lastYear = self.fetch(self.lyFromDate, self.lsToDate)
        thisYear = self.fetch(self.tyFromDate, self.tyToDate)
        print(f'{self.storeNo},{self.storeName},{lastYear},{thisYear}')
        self.file.write(f'{self.storeNo},{self.storeName},{lastYear},{thisYear}\n')

    def limit(self):
        self.bakki = self.req.headers
        print("\n\n\n")
        print(f"Request remaining: {self.bakki['X-Ratelimit-Hour-Remaining']}")

def calcDate(thisEndDate, lastEndDate):
    period = dict()
    tyToDate = datetime.strptime(thisEndDate, "%d-%m-%Y")
    tyFromDate = tyToDate - DT.timedelta(days=6)
    lyToDate = datetime.strptime(lastEndDate, "%d-%m-%Y")
    lyFromDate = lyToDate - DT.timedelta(days=6)
    period['thisYear'] = tyToDate.strftime("%Y")
    period['lastYear'] = lyToDate.strftime("%Y")
    period['lastFrom'] = lyFromDate.strftime("%Y-%m-%d")
    period['lastTo'] = lyToDate.strftime("%Y-%m-%d")
    period['thisFrom'] = tyFromDate.strftime("%Y-%m-%d")
    period['thisTo'] = tyToDate.strftime("%Y-%m-%d")
    return period

def fileCreate(reportName):
    dates = calcDate(thisEndDate,lastEndDate)
    output = open(f'{reportName}_{dates["thisFrom"]} to {dates["thisTo"]}.csv',"w+")
    output.write(f'No,Store,{dates["lastYear"]},{dates["thisYear"]}\n')
    return output

thisEndDate = str(input('Enter THIS YEAR END date (dd-mm-yyyy): '))
lastEndDate = str(input('Enter LAST YEAR END date (dd-mm-yyyy): '))
reportType = str(input('Enter report type yo (gas|elec|pfs): '))
if reportType == "gas":
    database = open("gasDatabase.json")
    param = "GASENERGY"
    reportName = "GAS DATA"
    file = fileCreate(reportName)
elif reportType == "elec":
    database = open("elecDatabase.json")
    param = "EACTIVE"
    reportName = "ELEC DATA"
    file = fileCreate(reportName)
elif reportType == "pfs":
    database = open("pfsDatabase.json")
    param = "EACTIVE"
    reportName = "PFS DATA"
    file = fileCreate(reportName)
else:
    print('Dafuq! dude >:(')
    sys.exit()

reportDate = calcDate(thisEndDate, lastEndDate)
siteInfo = json.load(database)
print(f'\n\nFetching {reportName} with THIS YEAR PERIOD :⇨ {reportDate["thisFrom"]} to {reportDate["thisTo"]} ...')
print(f'Fetching {reportName} with LAST YEAR PERIOD :⇨ {reportDate["lastFrom"]} to {reportDate["lastTo"]} ...\n\n')
for site in siteInfo:
    lyFromDate = reportDate['lastFrom']
    lsToDate = reportDate['lastTo']
    tyFromDate = reportDate['thisFrom']
    tyToDate = reportDate['thisTo']
    num = site['no']
    name = site['store']
    device = str(site['device'])
    ob = report(num, name, device, lyFromDate, lsToDate, tyFromDate, tyToDate, param, file)
    ob.fileWrite()
ob.limit()





