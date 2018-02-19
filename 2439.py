num = int(input())

for i in range(1,num+1):
    star = "*"*i
    space = " "*(num-i)
    print(space+star)
