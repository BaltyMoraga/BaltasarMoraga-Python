def myFunc():
    print('sus')
    print('sauce')
    print('you are fine')

print('starts here')
myFunc()


def howManyDaysOld():
    age = input('how old are you?')
    daysOld = (int(age) * 365)
    print('you are ' + str(daysOld) + ' days old')

print('starts here')
howManyDaysOld()


def homeBase():
    home = input('what city are you from? - ')
    schoolYears = input('how many years have you been in school? - ')
    print('you are from ' + str(home))
    print('you have been in school for ' + str(schoolYears) + ' years')

print('starst here')
homeBase()


from random import *

def randomNumber():
    x = input('what is my start value?')
    y = input('what is my end value')
    myNumber = randint(int(x), int(y))
    print(str(myNumber) + ' is a random number between ')
    print(str(x) + ' and ' + str(y))

print('starts here')
randomNumber()

