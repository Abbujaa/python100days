class house:
    number_of_windows = 3
    width = 5000
    breadth = 2500

    def __init__(self,color,window_size):
        self.color = 'red'
        self.roof_color = color
        self.window_size = window_size

houses = [house("red","sm"), house("blue","lg"), house("green","red")]        
print([[house.number_of_windows for house in houses]])
print([[house.roof_color for house in houses]])
print([[house.window_size for house in houses]])

# constructor and destructor

class house:
    number_of_windows = 3
    width = 5000
    breadth = 2500

    def __init__(self,color,window_size):
        self.color = 'red'
        self.roof_color = color
        self.window_size = window_size
    
    def __del__(self):
        print('deleted', id(self))

houses = [house("red","sm"), house("blue","lg"), house("green","red")]        
print([[house.number_of_windows for house in houses]])
print([[house.roof_color for house in houses]])
print([[house.window_size for house in houses]])

del houses[1]


# In Python, constructors and destructors are special methods that initialize and clean up objects, respectively. They are important concepts in object-oriented programming. 
# Constructors Initialize an object's attributes with default or given values, Set up the object's initial state, Allocate resources, Defined with the init method, and Automatically called when an object is created. 
# Destructors 
# Perform cleanup actions like releasing resources, closing files, or freeing memory
# Clean up before an object is destroyed
# Defined with the __del__ method
# Automatically called when an object is about to be destroyed
# Differences between constructors and destructors 
# Purpose: Constructors initialize objects, while destructors clean them up
# Invocation: Constructors are called when an object is created, while destructors are called when an object is deleted
# Resource management: Constructors acquire resources, while destructors release them

# Types of methods

# instance class and static

# In Python, the three main types of methods are instance, class, and static. Each type has different characteristics and is used in different situations. 
# Instance methods: Can access both class and instance attributes, Receive the caller object as the first parameter, and Require no decorator. 
# Class methods: 
# Can access class attributes, but not instance attributes
# Receive the caller class as the first parameter
# Require the @classmethod decorator
# Used when the method needs to access or modify class-level attributes
# Static methods: 
# Do not have access to class attributes or instance attributes
# Do not take any necessary parameter
# Require the @staticmethod decorator
# Used when the method's behavior does not depend on instance-specific or class-specific data



#instance method:
def print_house_info(houses):
    print([[house.number_of_windows for house in houses]])
    print([[house.roof_color for house in houses]])
    print([[house.window_size for house in houses]])
    print("------------------------")


class house:
    number_of_windows = 3
    width = 5000
    breadth = 2500

    def __init__(self,color,window_size):
        self.color = 'red'
        self.roof_color = color
        self.window_size = window_size
    
    def __del__(self):
        print('deleted', id(self))

    def do_paint_job(self, new_color):
        self.color = new_color

houses = [house("red","sm"), house("blue","lg"), house("green","red")] 

def print_house_info(houses):
    print([[house.number_of_windows for house in houses]])
    print([[house.roof_color for house in houses]])
    print([[house.window_size for house in houses]])

print_house_info(houses)

houses[1].do_paint_job("maroon")

print_house_info(houses)




# static method

class House:
    number_of_windows = 5
    width = 5000
    breadth = 2500

    def __init__(self, color, window_size):
        self.color = color
        self.roof_color = "dark_red"
        self.window_size = window_size

    def __del__(self):
        print("destroyed house", id(self))

    def do_paint_job(self, new_color):
        self.color = new_color

    def get_data(self):
        self.find_area(self.width, self.breadth )
        return self.color, self.roof_color, self.window_size , self.find_area(self.width, self.breadth )

    @staticmethod
    def find_area(length, width):
        return length * width
    
    @classmethod
    def red_house(cls, windows_size):
        return cls("red", windows_size)
    
    def __add__( self, other):



# Example function to print house information
     def print_house_info(houses):
        for index, house in enumerate(houses):
            print(f"House {index + 1}: {house.get_data()}")


# Create house objects
houses = [House("red", "sm"), House("blue", "lg"), House("green", "md")]

# Print house information
print_house_info(houses)

# Access specific house data
print(houses[1].get_data())

# Calculate area using static method
area = House.find_area(100, 100)
print(f"Area: {area}")

print(houses[0] + houses[1])
