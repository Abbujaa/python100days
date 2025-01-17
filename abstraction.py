from abc import ABC , abstractmethod

class Mob(ABC):
    def __init__(self, health, speed):
        self.health = health
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def kill(self):
        print("killed")
        pass

    @abstractmethod
    def reviving(self):
        pass

class Zombie:
    def __init__(self) :
        super().__init__(100,20)

    def move(self):
        print("moved")

    def kill(self):
     pass

mob = Zombie()

