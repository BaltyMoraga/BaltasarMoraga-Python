class Pet():
    petType = 'cage free pet'

    def __init__(self,pType,pName,pBreed):
        self.type = pType
        self.name = pName
        self.breed = pBreed

    def getType(self):
        return(self.type)
    def getName(self):
        return(self.name)
    def getBreed(self):
        return(self.breed)
    def whatIsIt(self):
        print(self.petType)
        print(self.getType())
        print(self.getName())
        print(self.getBreed())

myPet1 = Pet('dog','corona','scotish terrier')
myPet1.whatIsIt()

input('----------')

myPet2 = Pet('cat','sally','egyptian mau')
print(myPet2.petType)
print(myPet2.getType())
print(myPet2.getName())
print(myPet2.getBreed())

input('----------')

class Cage():
    petType = 'caged pet'

    def __init__(self,cType,cDanger):
        self.type = cType
        self.danger = cDanger

    def getType(self):
        return(self.type)
    def getDanger(self):
        if self.danger == 'true':
            return('Is Dangerous')
        elif self.danger == 'false':
            return ('Isnt Dangerous')


myCagedPet1 = Cage('snake','true')
print(myCagedPet1.petType)
print(myCagedPet1.getType())
print(myCagedPet1.getDanger())

input('----------')

myCagedPet2 = Cage('rat','false')
print(myCagedPet2.petType)
print(myCagedPet2.getType())
print(myCagedPet2.getDanger())
