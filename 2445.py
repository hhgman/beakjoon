num = int(input())

for i in range(1,num+1):
    star = "*"*(i)
    space = " "*(num-i)
    print(star+space*2+star)
for i in range(1,num+1):
    star = "*"*(num-i)
    space = " "*(i)
    print(star+space*2+star)
