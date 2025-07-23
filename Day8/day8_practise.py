# -------- DAY 8 Practise ------- #

# List of Concepts........./

"""
1. Inheritance
2. Polymorphism
3. Abstraction
4. Encapsulation
5. Multilevel Inheritance
6. Multiple Inheritance
 
"""

## --- INHERITANCE --- ##

# Single Inheritance

class Vehicle:
    def start(self):
        print("Vehicle started")

class Bike(Vehicle):
    pass

b = Bike()
b.start()  # Output: Vehicle started

# Multilevel Inheritance

class GreatGrandfather:
    def legacy(self):
        print("This is the great-grandfather's legacy.")

class Father(GreatGrandfather):
    pass

class Son(Father):
    pass

s = Son()
s.legacy()  # Output: This is the great-grandfather's legacy.

# Multiple Inheritance

class Student:
    def study(self):
        print("Studying...")

class Teacher:
    def teach(self):
        print("Teaching...")

class TeachingAssistant(Student, Teacher):
    pass

ta = TeachingAssistant()
ta.study()  # Output: Studying...
ta.teach()  # Output: Teaching...

# Polymorphism (Method Overriding)

class Person:
    def clean_room(self):
        print("Cleaned room normally.")

class Mom(Person):
    def clean_room(self):
        print("Mom cleaned with perfection.")

class Kid(Person):
    def clean_room(self):
        print("Kid just hid everything under the bed.")

people = [Mom(), Kid(), Person()]
for p in people:
    p.clean_room()

# Encapsulation

class Locker:
    def __init__(self):
        self.__pin = 1234  # Private variable

    def hint(self):
        print("🔐 Hint: It's a 4-digit number. The first two digits are '12', and the last two add up to 7.")

    def unlock(self):
        self.hint()
        try:
            entered_pin = int(input("Enter the PIN to unlock the locker: "))
            if entered_pin == self.__pin:
                print("✅ Locker opened!")
            else:
                print("❌ Wrong PIN!")
        except ValueError:
            print("Please enter a valid number.")

# Create the locker and try to unlock it
my_locker = Locker()
my_locker.unlock()

# Abstraction

from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def exit(self):
        pass

class RacingGame(Game):
    def play(self):
        print("Racing started!")

    def exit(self):
        print("Exiting Racing Game...")

g = RacingGame()
g.play()     # Output: Racing started!
g.exit()     # Output: Exiting Racing Game...
