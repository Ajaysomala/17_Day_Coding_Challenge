## >>>>>> Simple Notes Manager App <<<<<<<<<<

def show_menu():
    print("\n--- Notes Manager ---")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

file_path = "notes.txt"

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Enter your note: ")
        with open(file_path, "a") as f:
            f.write(note + "\n")
    elif choice == "2":
        with open(file_path, "r") as f:
            print("\n--- Your Notes ---")
            print(f.read())
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
