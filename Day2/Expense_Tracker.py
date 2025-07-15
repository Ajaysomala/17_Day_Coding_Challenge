##------ EXPENSE Tracker ------##

import csv
from datetime import datetime

FILENAME = "expenses.csv"

def add_expense():
    amount = input("Enter amount: ₹ ")
    category = input("Enter category (food, travel, etc.): ")
    note = input("Optional note: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("✅ Expense recorded!")

def view_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No expenses found yet.")

def total_today():
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].startswith(today):
                    total += float(row[1])
        print(f"💸 Total spent today: ₹{total}")
    except FileNotFoundError:
        print("No expenses found yet.")

def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spent Today")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_today()
        elif choice == '4':
            break
        else:
            print("❌ Invalid option")

if __name__ == "__main__":
    main()
