def main():
    myClasses = input('What grade are you in - ')
    resultAnswer = yearInSchool(myClasses)

    print('you are a - ' + resultAnswer)




def yearInSchool(Class):
    if (Class) == '9':
        classResult = 'freshman'
    elif (Class) == '10':
        classResult = 'Sophomore'
    elif input(11):
        print('junior')
    elif input(12):
        print('senior')
    else:
        print('your not in highschool')





