#Student Grades Tracker 
def show_menu():
    print("\n===== Student Grades Tracker =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

students = {}

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ").strip()
        num_subjects = int(input("How many subjects? "))
        subjects = {}
        for _ in range(num_subjects):
            subject = input("Enter subject name: ").strip()
            marks = int(input(f"Enter marks for {subject}: "))
            subjects[subject] = marks
        students[name] = subjects
        print(f"✅ Student {name} added.")

    elif choice == "2":
        if students:
            print("\n🎓 Student List:")
            for name, grades in students.items():
                print(f"\n{name}'s Grades:")
                for subject, marks in grades.items():
                    print(f"  {subject}: {marks}")
        else:
            print("No students found.")

    elif choice == "3":
        search_name = input("Enter student name to search: ").strip()
        if search_name in students:
            print(f"\n📖 {search_name}'s Grades:")
            for subject, marks in students[search_name].items():
                print(f"  {subject}: {marks}")
        else:
            print("❌ Student not found.")

    elif choice == "4":
        print("👋 Exiting... Bye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter 1-4.")
