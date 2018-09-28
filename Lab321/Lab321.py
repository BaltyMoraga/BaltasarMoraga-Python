def main():
    myClass = (input('What grade are you in '))
    resultAnswer = yearInSchool(myClass)
    print('you are ' + resultAnswer)

    listGrade = [68.2,74.9,86.5,92.5]
    print (len(listGrade))
    myListGrade = (input('whats your percent grade in school '))
    resultGrade = getAverageGrade(myListGrade)
    print('you are ' + resultGrade)

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


def getAverageGrade(listGrade):
    if (listGrade) <
        GradeResult == ('passing')
