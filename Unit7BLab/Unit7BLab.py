class pet():
    petType = 'cage free pet'

    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def info(self):
        return(self.name + ' ' + self.breed)

mypet = pet('corona','scotish terrier')
print(mypet.info())

class child():
    y = 1

class dog(pet):
    def __init__(self,name,breed):
        pet.__init__(self,name,breed)

    def info(self):
        return('This is ' + self.name + ' a ' + self.breed)

    def action(self):
         self.activity = 'running'
         return('This is a '+ self.petType + ' who is a ' + self.breed + ' named ' + self.name + ' who is currently ' + self.activity + '.')

mypet1 = pet('Corona','Scotish Terrier')
print(mypet1.info())

mypet2 = dog('Corona','Scotish Terrier')
print(mypet2.action())
