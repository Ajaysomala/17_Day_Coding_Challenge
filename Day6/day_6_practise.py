#--- Day OOP Object Oriented Programming Part 1 --- #
# List Of Conecpts 
"""
1. Classes & Obejcts 
2. __init__() constructor 
3. Instance variable & Methods
4. Self Keyword 

"""
### Challenge ------ MINI Project : STUDENT MANAGEMENT SYSTEM (OOP BASICS) -------

#  Let start with basic.......
#--- Step 1 : Creating a class and an object 

# class Student1:
#     pass

# std1 = Student1()

# #--- Step 2 : Adding Instance Variables.......

# class student1:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

# std1 = student1("Ajay", 16, "10th")
# std2 = student1("Aj", 15, "9th")

# print(std1.name, std1.age, std1.grade)

# #--- Step 3 : Adding a Method ( Function Inside Class )

# class Student1:
#     def __init__(self, name):
#         self.name = name
    
#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# std1 = Student1("Ajay")
# std1.greet()

# #--- Step 4 : Creating a Multiple Objects

# std2 = Student1("Aj")
# std2.greet()

# std3 = Student1("A")
# std3.greet()

# #--- Step 5 : Modifying Obejct Data

# std1 = "Ajay1"

#

class Student:
    total_students = 0
    school_name = "Greenwood High"
    all_students = []  # To store all students

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1
        Student.all_students.append(self)  # Save this student object

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

    @classmethod
    def update_school_name(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def school_guidelines():
        print("1. Be respectful.\n2. Attend classes on time.\n3. Submit assignments before deadlines.")


# Create student objects
s1 = Student("Alice", 14, "8th")
s2 = Student("Bob", 15, "9th")
s3 = Student("Charlie", 13, "7th")
s4 = Student("David", 16, "10th")
s5 = Student("Eve", 12, "6th")
s6 = Student("Ajay", 16, "10th")
s7 = Student("Aj", 15, "9th")
s8 = Student("A", 15, "9th")
s9 = Student("Ajay1", 16, "10th")
s10 = Student("Aj1", 15, "9th")


# Display details of all students

# Print table header
print("+----------+-----+--------+")
print("| Name     | Age | Grade  |")
print("+----------+-----+--------+")

# Print each student's data in row format
for s in Student.all_students:
    print(f"| {s.name:<8} | {s.age:<3} | {s.grade:<6} |")

print("+----------+-----+--------+")
print("Total Students:", Student.total_students)
print("School Name:", Student.school_name)

# Update school name and print again
Student.update_school_name("Sunrise Public School")
print("Updated School Name:", Student.school_name)

Student.school_guidelines()
