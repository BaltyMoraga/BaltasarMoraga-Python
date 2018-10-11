for i in range(0,5):
    print(i)
    answer = (i+10)
    skrt = (i*10)
    input('pause')
    print(str(i) + '+ 10 =' + str(answer))
    print(str(i) + '* 10 =' + str(skrt))

myList = [10,20,30,40,50]
print(myList)

for a in range(0, len(myList)):
    list = []
    myList[a] = myList[a] * 10
    print(myList)
