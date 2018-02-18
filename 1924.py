month ={
    1:[i for i in range(1,32)],    2:[i for i in range(1,29)],
    3:[i for i in range(1,32)],    4:[i for i in range(1,31)],
    5:[i for i in range(1,32)],    6:[i for i in range(1,31)],
    7:[i for i in range(1,32)],    8:[i for i in range(1,32)],
    9:[i for i in range(1,31)],    10:[i for i in range(1,32)],
    11:[i for i in range(1,31)],   12:[i for i in range(1,32)]
}

calender = []
oneDay = input()

mon_day= list(oneDay.split(" "))
mon = int(mon_day[0])
day = int(mon_day[1])

plusDay = [i for i in range(1,day+1)]
for i in range(1,mon):
    calender += month[i]
calender += plusDay


# print(calender)
lenth = len(calender)%7

if lenth == 0:
    print("SUN")
elif lenth ==1:
    print("MON")
elif lenth ==2:
    print("TUE")
elif lenth ==3:
    print("WED")
elif lenth ==4:
    print("THU")
elif lenth ==5:
    print("FRI")
elif lenth ==6:
    print("SAT")
