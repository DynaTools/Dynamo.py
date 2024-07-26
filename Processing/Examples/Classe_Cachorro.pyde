class Dog: #letra maiscula
    def __init__(self,name,legs): 
        self.name = name
        self.legs = legs
        
    def speak(self):
        print('Bark!')
        
    def pernas(self):
        print(self.name + 'tem' + str(self.legs))
        
lola = Dog('Lola',4)
thor = Dog('Thor',4)

lola.pernas()
