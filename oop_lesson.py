# Defining a class and its attributes
# Creating instances (objects) of a class
# Class methods (functions belonging to a class)
# Inheritance & Polymorphism
# Method of overriding
class Dog:
    def __init__(self, no_of_eyes, color, no_of_legs, gender):
        self.no_of_eyes = no_of_eyes
        self.color = color 
        self.no_of_legs = no_of_legs
        self.gender = gender

    def barking(self):
        print("woof woof!")

german_shepherd = Dog(no_of_eyes=2, color='Grey', no_of_legs=4, gender='male') 
doger = Dog(no_of_eyes=1, color='white', no_of_legs=4, gender='female')
dobberman = Dog(2, 'brown', 4, 'female')

print(german_shepherd.color, german_shepherd.no_of_eyes, german_shepherd.no_of_legs)
print(doger.no_of_eyes, doger.no_of_legs)
print(dobberman.color, dobberman.no_of_legs, dobberman.gender)

dobberman.color = 'dark-brown'
print(dobberman.color)
print(dobberman.barking())

