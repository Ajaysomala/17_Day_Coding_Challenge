class Student:
    total_students = 0
    school_name = "Greenwood High"
    all_students = []  # List to store all student objects

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Student.total_students += 1
        Student.all_students.append(self)

    def display_details(self):
        print(f"--- Student Info ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")
        print(f"School: {Student.school_name}\n")

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        print(f"School name updated to: {cls.school_name}")

    @staticmethod
    def print_guidelines():
        print("\n--- School Guidelines ---")
        print("1. Respect everyone.")
        print("2. Be punctual.")
        print("3. Complete homework on time.\n")


# Main program
if __name__ == "__main__":
    Student.print_guidelines()

    print("Welcome to Student Management System\n")

    while True:
        # Input student details
        name = input("Enter student name: ").strip()
        age = input("Enter student age: ").strip()
        grade = input("Enter student grade: ").strip()

        # Validation
        if not (name and age.isdigit() and grade):
            print("Invalid input. Please enter valid name, age (number), and grade.\n")
            continue

        # Create student object
        Student(name, int(age), grade)
        print("✅ Student added successfully!\n")

        # Ask if user wants to continue
        choice = input("Do you want to add another student? (yes/no): ").strip().lower()
        if choice != 'yes':
            break

    # Display student table
    print("\n+----------+-----+--------+")
    print("| Name     | Age | Grade  |")
    print("+----------+-----+--------+")
    for s in Student.all_students:
        print(f"| {s.name:<8} | {s.age:<3} | {s.grade:<6} |")
    print("+----------+-----+--------+")
    print(f"Total Students Enrolled: {Student.total_students}")
    print(f"School Name: {Student.school_name}")

    # Optional: Change school name
    choice = input("\nDo you want to change the school name? (yes/no): ").strip().lower()
    if choice == 'yes':
        new_name = input("Enter new school name: ").strip()
        Student.change_school_name(new_name)
