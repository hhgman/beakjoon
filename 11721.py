string = str(input())

tmp = ""
for i,cha in enumerate(string):
    tmp += cha
    if (i+1)% 10 ==0:
        print(tmp)
        tmp =""
    if (i+1) == len(string):
        print(tmp)


