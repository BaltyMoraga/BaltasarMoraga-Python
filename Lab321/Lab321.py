def main():
    myClass = (input('What grade are you in '))
    resultAnswer = yearInSchool(myClass)
    print('you are ' + resultAnswer)

    myList = [62.1,74.9,86.5,92.5]
    print (len(myList))
    myList = (input('whats your percent grade in school '))
    resultGrade = getAverageGrade(myList)
    print('you are ' + resultGrade)

    myList2 = [54.9,66.1,74.9,86.5,92.5]
    print(myList2)
    myList2 = (input('what is your percent grade again?'))
    resultLetter = getLetterGrade(myList2)
    print('you have an' + resultLetter)

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


def getAverageGrade(list):
    if (list) <= '92.5':
        listResult = 'passing'
    elif (list) <= '86.5':
        listResult = 'passing'
    elif (list) <= '74.9':
        listResult = 'passing'
    elif (list) <= '62.1':
        listResult = 'failing'
    else:
        listResult = 'failing'

    return listResult


def getLetterGrade(list2):
     if (list2) <= '92.5':
        listResult2 = 'A'
    elif (list2) <= '86.5':
        listResult2 = 'B'
    elif (list2) <= '74.9':
        listResult2 = 'C'
    elif (list2) <= '66.1':
        listResult2 = 'D'
    else:
        listResult2 = 'F'

    return listResult2
