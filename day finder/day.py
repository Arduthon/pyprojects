import datetime

a = int(input("Birth Year :"))
b = int(input("Till year :"))
c = int(input("Month :"))
d = int(input("Date :"))

#get the weekday 
e = int(datetime.date(a,c,d).weekday())

days=["Mon","Tues","Wed","Thus","Fri","Sat","Sun"]

for x in range(a, b):
    weekDay_num =datetime.date(x,c,d).weekday()
    if weekDay_num == e:
        print(days[weekDay_num],x)