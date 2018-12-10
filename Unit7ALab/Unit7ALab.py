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


myPet1 = Pet('dog','corona','scotish terrier')
print(myPet1.petType)
print(myPet1.getType())
print(myPet1.getName())
print(myPet1.getBreed())

myPet2 = Pet('cat','')
class Cage():
    petType = 'caged pet'

    def __init__(self,cType,cDanger):
        self.type = cType
        self.danger = cDanger

    def getType(self):
        return(self.type)
    def getDanger(self):
        return(self.danger)

