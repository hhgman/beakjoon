count = int(input())

numList = str(input())

Array = numList.split(" ")

numArray = []
for i in Array:

    numArray.append(int(i))


print("{} {}".format(min(numArray),max(numArray)))

