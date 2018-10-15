def main():
    myLists = [54.9,66.1,74.9,86.5,92.5]
    print(len(myLists))
    myLists = (input('what is your percent grade again?'))
    resultLetter = getLetterGrade(myLists)
    print('you have an ' + resultLetter)


def getLetterGrade(lists):
    if (lists) >= '92.5':
        listResults = 'A'
    elif (lists) >= '86.5':
        listResults = 'B'
    elif (lists) >= '74.9':
        listResults = 'C'
    elif (lists) >= '66.1':
        listResults = 'D'
    else:
        listResults = 'F'

    return listResults

main()
