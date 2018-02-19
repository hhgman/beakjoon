num = int(input())

for i in range(1,num+1):
    star = "*"*(2*i-1)
    space = " "*(num-i)
    print(space+star)
