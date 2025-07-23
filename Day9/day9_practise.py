## ----- DAY 9 OOPS Concepts Part 3 ----- ##

# List of Concepts....../

"""
1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Super() FUnction
5. isInstance() and issubsclass()

"""
## -- Single Inheritance -- ##

class Father:
    def speak(self):
        print("I speak Hindi.")

class Son(Father):
    pass

s = Son()
s.speak()  # Output: I speak Hindi.

## -- Multilevel Inheritance -- ##

class Grandfather:
    def legacy(self):
        print("I passed down traditions.")

class Father(Grandfather):
    pass

class Son(Father):
    pass

s = Son()
s.legacy()  # Output: I passed down traditions.

## -- Multiple Inheritance -- ##

class Student:
    def study(self):
        print("Studying...")

class Teacher:
    def teach(self):
        print("Teaching...")

class TeachingAssistant(Student, Teacher):
    pass

ta = TeachingAssistant()
ta.study()
ta.teach()

## -- Super() Function --

class Student:
    def __init__(self, name):
        self.name = name

class CollegeStudent(Student):
    def __init__(self, name, college):
        super().__init__(name)  # Calls Student's __init__
        self.college = college

cs = CollegeStudent("Alice", "XYZ University")
print(cs.name)  # Output: Alice

print(cs.college)  # Output: XYZ University

## -- isinstance() and issubclass() -- ##

s = TeachingAssistant()

print(isinstance(s, Student))    
print(isinstance(s, Teacher))     
print(issubclass(TeachingAssistant, Student))  
print(issubclass(TeachingAssistant, Teacher))  

## -- Method Overriding -- ##

class Employee:
    def introduce(self):
        print("I am an employee.")

class Manager(Employee):
    def introduce(self):
        print("I am a manager.")

class Developer(Employee):
    def introduce(self):
        print("I am a developer.")

for emp in [Employee(), Manager(), Developer()]:
    emp.introduce()

## -- Polymorphism -- ##

class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

for animal in [Dog(), Cat()]:
    animal.speak()

## -- Class Variables -- ##

class Pizza:
    total_pizzas = 0  # Class variable

    def __init__(self):
        Pizza.total_pizzas += 1

p1 = Pizza()
p2 = Pizza()
print(Pizza.total_pizzas)  # Output: 2

## -- Instance Variables -- ##

class Student:
    def __init__(self, name):
        self.name = name  # Instance variable
        self.grades = []  # Instance

s1 = Student("Alice")
s2 = Student("Bob")
s1.grades.append(90)
s2.grades.append(8)
print(s1.name)  # Output: Alice
print(s2.name)  # Output: Bob
