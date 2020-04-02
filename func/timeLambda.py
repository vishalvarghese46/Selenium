from datetime import datetime

shitDate = "12=09=2020"

f = lambda x: datetime.strptime(x, "%d=%m=%Y")
g = lambda x: x.strftime("%d|%m|%Y")

for i in map(f, ["12=09=2020", "25=09=2020", "12=09=2020", "02=09=2020", "22=09=2020"]):
    print(g(i))