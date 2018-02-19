num = int(input())

for i in range(1,num+1):
    tmp = ""
    space = " "*(num-i)
    for j in range(0,2*i):
        if j%2 ==0:
            tmp += "*"
        else:
            tmp += " "
    print(space+tmp)
