def show_menu():
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠️ Input cannot be empty. Try again.")

contacts = {}

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = get_non_empty_input("Enter name: ").title()
        phone = get_non_empty_input("Enter phone number: ")

        if name in contacts:
            confirm = input(f"⚠️ Contact '{name}' exists. Overwrite? (y/n): ").lower()
            if confirm != 'y':
                print("❌ Operation cancelled.")
                continue

        contacts[name] = phone
        print(f"✅ Contact saved for {name}.")

    elif choice == "2":
        if contacts:
            print("\n📇 Contact List:")
            for name, phone in contacts.items():
                print(f"Name: {name}, Phone: {phone}")
        else:
            print("No contacts found.")

    elif choice == "3":
        search_name = get_non_empty_input("Enter name to search: ").title()
        contact = contacts.get(search_name)
        if contact:
            print(f"🔎 Found: {search_name} - {contact}")
        else:
            print("❌ Contact not found.")

    elif choice == "4":
        del_name = get_non_empty_input("Enter name to delete: ").title()
        if del_name in contacts:
            confirm = input(f"Are you sure you want to delete {del_name}? (y/n): ").lower()
            if confirm == 'y':
                contacts.pop(del_name)
                print(f"🗑️ Contact for {del_name} deleted.")
            else:
                print("❌ Deletion cancelled.")
        else:
            print("❌ Contact not found.")

    elif choice == "5":
        print("👋 Exiting... Bye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter a number between 1 and 5.")
