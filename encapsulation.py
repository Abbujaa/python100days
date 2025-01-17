import uuid
#encapsulation

#nested classes
#private 
#getter and setter

class vehicle:
        class engine: 
            def __init__(self, size):
                self.engine_size = size

            def power(self):
                 return self.engine_size * 5

        def __init__ (self, name, model, color, engine_size):
            self.name = name
            self.model = model
            self.color = color
            self.engine = self.engine(engine_size)
            self.__model_id = uuid.uuid4()

        @property
        def id(self):
             return str(self.__model_id)
        
        @id.setter
        def change_id(self, new_id):
             self.__model_id = new_id
        
        @property
        def model_info(self):
             return f"(self.name)({ self.model}) - {self.color}"
        
        # def set_color(self , new_color):
        #      self.color = new_color

car = vehicle("toyota", "suv", "white", 45)
# print(dir(car))
# print(type(car.engine), dir(car.engine))

# car = vehicle("toyota", "SUV", "White", 45)
# print(dir(car))
# print(car.id)

# car.id="abdul"
# print(car.set_color("red"))
print(car.id)



