class Person:
    total_people = 0

    def __init__(self, name):
        self.name = name
        Person.total_people += 1

    def get_details(self):
        print(f"👤 Person: {self.name}")


class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def get_details(self):
        print(f"🎓 Student: {self.name}, Grade: {self.grade}")


class ClassLeader(Student):  # Multilevel Inheritance
    def __init__(self, name, grade, responsibility):
        super().__init__(name, grade)
        self.responsibility = responsibility

    def get_details(self):
        print(f"⭐ Class Leader: {self.name}, Grade: {self.grade}, Duty: {self.responsibility}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def get_details(self):
        print(f"📚 Teacher: {self.name}, Subject: {self.subject}")


class Mentor(Student, Teacher):  # Multiple Inheritance
    def __init__(self, name, grade, subject):
        Student.__init__(self, name, grade)  # Resolve MRO
        self.subject = subject

    def get_details(self):
        print(f"🧑‍🏫 Mentor: {self.name}, Grade: {self.grade}, Guides in: {self.subject}")


# Input-based Smart System
members = []

print("\n===== Smart School System =====")
while True:
    print("\nChoose Role to Add:")
    print("1. Student")
    print("2. Class Leader")
    print("3. Teacher")
    print("4. Mentor")
    print("5. Show All Members")
    print("6. Show Total People")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        members.append(Student(name, grade))
        print("✅ Student added successfully!")

    elif choice == "2":
        name = input("Enter class leader name: ")
        grade = input("Enter grade: ")
        responsibility = input("Enter responsibility: ")
        members.append(ClassLeader(name, grade, responsibility))
        print("✅ Class Leader added successfully!")

    elif choice == "3":
        name = input("Enter teacher name: ")
        subject = input("Enter subject: ")
        members.append(Teacher(name, subject))
        print("✅ Teacher added successfully!")

    elif choice == "4":
        name = input("Enter mentor name: ")
        grade = input("Enter mentor's student grade: ")
        subject = input("Enter subject they guide: ")
        members.append(Mentor(name, grade, subject))
        print("✅ Mentor added successfully!")

    elif choice == "5":
        print("\n📋 All Members and Details:")
        for member in members:
            member.get_details()
        print()

    elif choice == "6":
        print(f"\n🔢 Total People in System: {Person.total_people}")

    elif choice == "7":
        print("👋 Exiting system. Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please try again.")
