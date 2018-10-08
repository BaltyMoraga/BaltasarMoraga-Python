num = input('how many numbers? - ')
print(num)
numList = []

for i in range(0, int(num)):
    myNum = input('number please - ')
    numList.append(int(myNum))
    print(myNum)

total = 0
for i in numList:
    total = total + 1
    print('i = ' + str(i))
    print('total = ' + str(total))
    input('pause')

average = total / int(num)
print('total ' + str(total + ' / ' + num))
print(average)
