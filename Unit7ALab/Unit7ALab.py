class Pet():
    petType = 'cage free pet'

    def __init__(self,pType,pName,pBreed):
        self.type = pType
        self.name = pName
        self.bread = pBreed

    def whatIsIt(self):

class Cage():
    petType = 'caged pet'

    def __init__(self,cType,cDanger):
        self.type = cType
        self.denger = cDanger

    def whatDanger(self):

myPet1 = Pet('dog','corona''scotish terrier')
