###------ DAy 7 Topic on Functions mastery - Intermediate to Advanced -----###

# List Of Concepts.....

"""
1. Default Arguments
2. Keyword vs Positional Arguments 
3. *args and **kwargs
4. Keyword Only Parameters
5. Return Values - Error Handlingin Functions

"""

## ---- Default Arguments ---- ##

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()             # No name given
greet("Ajay")   
greet("Beru")    # Name given

## ---- Positional Vs Keyword Arguments ---- ##

def order(drink):
    print(f"Soft Drink Ordered:{drink}")

order("Coke")
order("Pepsi")

## ---- *args ---- ##

def average(*args):
    if not args:
        return "No data"
    return sum(args) / len(args)

# Examples
print(f"Total Bill Amount: {average(10, 20, 30)}")   # 20.0
print(average())             # "No data"

## ---- **kwargs ---- ##
def user_info(name, age, **kwargs):
    location = kwargs.get("location", "Unknown")
    print(f"Name: {name}, Age: {age}, Location: {location}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info("Ajay", 25, email="ajay@example.com", phone="1234567890")

## ---- Keyword Only Parameters ---- ##

def login(username, password):
    if len(password) < 6:
        print("Warning: Password too short!")
    else:
        print(f"Login success! Welcome, {username}")

login(username="Ajay", password="secret")
login(username="Ajay", password="123")

## ---- Return Values + Error Handling ---- ##

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print(divide(10, 2))
print(divide(5, 0))

## ---- Recursion ---- ##

def countdown(n):
    if n == 0:
        print("Blastoff! 🚀")
    else:
        print(n)
        countdown(n - 1)

countdown(5)
