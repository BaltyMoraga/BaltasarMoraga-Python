class parent():
    class pet():
        petType = 'cage free pet'

        def __init__(self,pName,pBreed):
            self.name = pName
            self.breed = pBreed

        def getName(self):
            return(self.name)
        def getBreed(self):
            return(self.breed)

    mypet = pet('corona','scotish terrier')
