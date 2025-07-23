💻 Day 9: Object-Oriented Programming (OOP) – Part 3
📅 17-Day Python Challenge - 📘 Smart School System – OOP Project (Day 8 + Day 9)

📂 Focus: OOP – Inheritance, Overriding, Polymorphism, Class & Instance Variables
🔍 Topics Covered
Single Inheritance

Multilevel Inheritance

Multiple Inheritance

The super() Function

isinstance() and issubclass() Functions

Method Overriding

Polymorphism

Class Variables vs Instance Variables

🧠 Concepts Explained
1. Single Inheritance
This occurs when a child class inherits from a single parent class, gaining its methods and attributes.

2. Multilevel Inheritance
In this type of inheritance, a class is derived from a class which is also derived from another class, forming a chain of inheritance.

3. Multiple Inheritance
A class can inherit from multiple parent classes. This helps in combining behaviors from more than one class but must be handled carefully due to method resolution order.

4. super() Function
This built-in function allows us to call methods from the parent class. It is especially useful during method overriding and constructors in inheritance.

5. isinstance() and issubclass()
These are used to check relationships:

isinstance() checks if an object is an instance of a class.

issubclass() checks if a class is a subclass of another.

6. Method Overriding
A child class can redefine methods of its parent class. This allows the child to provide a different implementation for inherited behavior.

7. Polymorphism
Polymorphism allows objects of different classes to respond to the same method call in different ways. It enhances flexibility and reusability in code design.

8. Class Variables vs Instance Variables
Class Variables are shared across all instances of the class.

Instance Variables are unique to each object and define object-specific data.

🚀 Summary
Day 9 covered deeper OOP concepts like inheritance types, the super() function, method overriding, and polymorphism. These are essential for structuring complex programs with reusable, maintainable code.

Day
⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬⏬

This Python project demonstrates the concepts of Object-Oriented Programming such as:

Inheritance (Single, Multilevel, and Multiple)

Class & Instance Variables

Method Overriding

Polymorphism

super() usage and MRO (Method Resolution Order)

💡 Project Overview
The Smart School System simulates a basic role management system in a school. It allows you to create and manage various roles such as:

👤 Person (Base Class)

🎓 Student

⭐ Class Leader (Multilevel Inheritance)

📚 Teacher

🧑‍🏫 Mentor (Multiple Inheritance)

All members are stored in a list and can be displayed or counted using the menu options.

📌 Features
✅ Add Students, Class Leaders, Teachers, and Mentors

📋 View all added members with details

🔢 Track total number of people added to the system

👋 Exit the program gracefully

🧠 Concepts Covered
OOP Concept	Where it's used
Class & Object	Person, Student, Teacher, etc.
Inheritance	Student(Person), Mentor(Student, Teacher)
Multilevel	ClassLeader(Student)
Multiple Inheritance	Mentor(Student, Teacher)
super()	Used to call parent constructor
Method Overriding	get_details() is overridden in each class
Polymorphism	Unified call to get_details() method

🛠️ How to Run

python smart_school_system.py
Make sure Python 3 is installed on your system.

🖼️ Sample Output

===== Smart School System =====

Choose Role to Add:
1. Student
2. Class Leader
3. Teacher
4. Mentor
5. Show All Members
6. Show Total People
7. Exit

🔚 End Note

This project wraps up Day 8 & Day 9 of our OOP learning journey. It’s a smart, interactive terminal-based simulation to build real-world object design and logic flow using Python OOP.