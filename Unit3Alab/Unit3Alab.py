def myFunc():
    print('sus')
    print('sauce')
    print('you are fine')

print('starts here')
myFunc()


def howManyYearsAtSchool():
    myGrade = input('what grade are you in at school? - ')
    print('you have been in school for ' + str(myGrade) + ' years')

howManyYearsAtSchool()


def homeBase():
    home = input('what city are you from? - ')
    schoolYears = input('how many years have you been in school? - ')
    print('you are from - ' + str(home))
    print('you are in grade - ' + str(schoolYears))

print('starts here')
homeBase()


from random import *

def randomNumber():
    x = input('what is my start value? - ')
    3y = input('what is my end value? - ')
    myNumber = randint(int(x), int(y))
    print(str(myNumber) + ' is a random number between - ')
    print(str(x) + ' and ' + str(y))

print('starts here')
randomNumber()



def boxArea(L, W):
    area = int(L) * int(W)
    perimeter = int(L) *2 + int(W) *2
    print('perimeter of the box is ' + str(perimeter))
    print('area of the box is ' + str(area))

L = input('what is the length of the box? - ')
w = input('what is the width of the box? - ')
boxArea (L, W)

boxArea(length, width)
