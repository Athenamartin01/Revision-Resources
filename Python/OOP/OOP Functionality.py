#4 principles:
#1. Inheritence 
#2. Polymorphism
#3. Abstraction
#4. Encapsulation

class Cat: #class is used to create objects 
    'Contents of __doc__'
               ##Functions in the class are known as methods
               ##All methods must have first parameter self
    def __init__(self,colour): # __init__ is a method called when an object is created 
        self.colour = colour
        self._colours = colour # _colours is a semi private variable
        self.__colours = colour # __colors is a private variable, to access outside of the class, use _Cat__colors
    def meow(self):
        passur = self.colour #self sets a value to the attribute of the object
    def __add__(self, other): # There are other 'magic' methods such as __add__ which reassigns +
        return(Cat)
    
#Types of Magic methods include:
#__add__
#__sub__
#__str__
#__lt__
#__le__
#__eq__

class Persian(Cat): #having a class as an attribute gives it all the properties of that class
    def __init__(self,colour):
        super.__init__(colour) #super is used to call methods from superclasses

    @classmethod #runs a special case for the class
    def new_meow(cls, meow):
        return cls(meow)
    pass
        
    @staticmethod #like a normal function except it can be called from a class instnace
    def old_meow(meow):
        return(meow)

    @property #Provides a way to customize access to attributes (makes it read only)
    def meow_allowed(self):
        return False

    @meow_allowed.setter #Sets the corresponding property's value 
    def meow_allowed(self, value):
        self.meow_allowed = True

    @meow_allowed.getter #Gets the corresponding property's value
    def meow_allowed(self):
        pass


felix = Cat("ginger") #This is an object 
felix.colour #returns the value 'ginger'
felix.meow #runs the meow method for felix attributes
hasattr(felix, 'colours') #checks to see if object has given attribute
delattr(felix, 'meow') # deletes attribute

issubclass(Persian, Cat) #Checks to see if 'Persian' is a subclass of 'Cat'
isinstance(felix, Cat) #Checks to see if object is in class of subclass

Cat.__doc__ #Returns class description
Cat.__name__#Returns class name
Cat.__module__#Returnsdule the class came from eg. __main__

if __name__ == "__main__": # only runs if the file isnt imported
    pass