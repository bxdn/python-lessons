# A CLASS is a custom type defined by you! :)
# A class is defined by 2 things, ATTRIBUTES and METHODS

# A class can be thought of as a blueprint for an apartment.
# There is only one blueprint, but many instances of the apartment can be created, with different furniture, decorations, etc.

# Attributes can be thought of as nouns (sometimes adjectives) (Things it HAS)
# Methods can be though of as verbs (Things it DOES)

# An instance of a class could, for instance, have a color, a list of customers, a price, a personality, or existential dread.  All these are ATTRIBUTES
# An instance of a class could, for instance, purchase, sell, delete, kill, create, or wallow.  All these are METHODS

# To define a class, use the 'class' keyword
class Dog:
    # To define a method on the class, use the 'def' keyword, just like standalone functions
    # However, an additional argument must be provided.  The "self" argument refers to the dog itself, and is required for methods.
    def bark(self):
        print('woof')
        
    
# To make an instance of a class, you call its CONSTRUCTOR.  A constructor will build an instance of the class and return it.
spot = Dog()
lucky = Dog()
fido = Dog()
# The type of these dogs is Dog.
print(type(spot))   # prints <class '__main__.Dog'>
print(type(lucky))  # prints <class '__main__.Dog'>
print(type(fido))   # prints <class '__main__.Dog'>

# To call a method on an instance of a class, use the '.' notation.  (Think about strings, sets, lists etc.  All have methods called on the instances of those types)
# Notice, we do not have to provide the 'self' argument specified in the class definition.  This is because 'self' is already known to be spot or lucky or fido, depending on who is doing the barking.
spot.bark()         # prints 'woof'
lucky.bark()        # prints 'woof'
fido.bark()         # prints 'woof'

# Let's create another class, Cat, to illustrate how to use ATTRIBUTES.
class Cat:
    # Remember the CONSTRUCTOR called earlier.  When the you do not specify a constructor, Python will create one for you with 0 arguments that does nothing except create the instance and return it.
    # Maybe, however, we want to create a cat with a name.  It would make sense to create our own constructor that takes in a 'name' argument and remembers it as the cat's name for future reference.
    # To create a constructor, you must define a method with the __init__ name.  Just like all other methods, the __init__ must take in a 'self' argument as well.
    def __init__(self, name):
        # An attribute can be saved to an instance of a class by using the '.' notation, just like methods.
        # This creates and saves a 'name' attribute on the specific cat, using the name provided in the constructor.
        self.name = name

    # Let's say we have a very smart cat, who knows how to talk.  We would like to implement a greet() method, where the cat will introduce themself.
    def greet(self):
        # Notice that we do not have to pass the name into the method, because the "name" attribute is saved on the cat from the constructor.
        print("Meow.  Hello, my name is " + self.name)

# Notice, we still do not have to provide the 'self' argument, but now, our custom constructor demands a 'name' argument be provided.
fluffy = Cat('Fluffy')
whiskers = Cat('Whiskers')
luna = Cat('Luna')

fluffy.greet()      # prints "Meow.  Hello, my name is Fluffy"
whiskers.greet()    # prints "Meow.  Hello, my name is Whiskers"
luna.greet()        # prints "Meow.  Hello, my name is Luna"