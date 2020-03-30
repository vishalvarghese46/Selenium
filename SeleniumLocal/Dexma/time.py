import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
thirdday = today - datetime.timedelta(2)
fourthday = today - datetime.timedelta(3)
fifthday = today - datetime.timedelta(4)
sixthday = today - datetime.timedelta(5)
seventhday = today - datetime.timedelta(6)
eighthday = today - datetime.timedelta(7)

print(eighthday.strftime("%d/%m/%Y"))
print(seventhday.strftime("%d/%m/%Y"))
print(sixthday.strftime("%d/%m/%Y"))
print(fifthday.strftime("%d/%m/%Y"))
print(fourthday.strftime("%d/%m/%Y"))
print(thirdday.strftime("%d/%m/%Y"))
print(yesterday.strftime("%d/%m/%Y"))
print(today.strftime("%d/%m/%Y"))

