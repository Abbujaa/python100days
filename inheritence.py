# taking from parents

class animals: #parent class
    def __init__(self, health,strength, speed):
        self.health = health
        self.strength=strength
        self.speed=speed

    def eat(self, replenishment):
        self.health += replenishment
    
class Lion(animals): #child class
    def __init__(self, pack_no):
        super().__init__(100,5000,50)
        self.no_of_lioness = pack_no

    def sleep(self):
        print("lion slept")
        print("Lion woke up")
    
class fish:
    def __init__(self):
        self.no_of_fins=0

    def breadth(self):
        pass

class whale(animals,fish): #child class
    def __init__(self,multiplier):
        super().__init__(1000000,5000,25)
        size_multiplier = multiplier

    def eat(self, no_of_shrimp):
        self.health+=no_of_shrimp * 2
    
    def kill_kraken(self):
        print("killed kraken" )


animal = whale(100)
animal.kill_kraken()
animal.breadth()

animal = Lion(5)
print(animal.strength, animal.health, animal.speed)
print(animal.no_of_lioness)