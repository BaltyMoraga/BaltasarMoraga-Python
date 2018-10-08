def main():
    myClass = (input('What grade are you in '))
    resultAnswer = yearInSchool(myClass)
    print('you are ' + resultAnswer)

    myLists = [54.9,66.1,74.9,86.5,92.5]
    print(len(myLists))
    myLists = (input('what is your percent grade again?'))
    resultLetter = getLetterGrade(myLists)
    print('you have an ' + resultLetter)

def yearInSchool(Class):
    if (Class) == '9':
        classResult = 'freshman'
    elif (Class) == '10':
        classResult = 'Sophomore'
    elif (Class) == '11':
        classResult = 'Junior'
    elif (Class) == '12':
        classResult = 'Senior'
    else:
        classResult = 'not in highschool'

    return classResult


def getAverageGrade():
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


def getLetterGrade(lists):
    if (lists) <= '92.5':
        listResults = 'A'
    elif (lists) <= '86.5':
        listResults = 'B'
    elif (lists) <= '74.9':
        listResults = 'C'
    elif (lists) <= '66.1':
        listResults = 'D'
    else:
        listResults = 'F'

    return listResults

main()
