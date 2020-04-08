from datetime import datetime, timedelta

todayDate = datetime.today().strftime('%b %d, %Y')
yesterdayDate = (datetime.today() - timedelta(1)).strftime("%d-%m-%Y")

print(todayDate)
print(yesterdayDate)


shaddy = []

shaddy.append(2)
shaddy.append(3)

shaddy.insert(0,1)
print(shaddy)