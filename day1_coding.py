### Task1
## programm that asks for the name and age 

name = input("Enter your name? ")
age = input("Enter your age? ")
city = input("Enter the city you live in? ")

print(f"Hello {name}, your age {age} years old and live in {city}")


### Task 2
## Simple Counter 

# step 1
num1 = float(input("Enter The Number 1: "))
num2 = float(input("Enter The Number 2: "))

# step 2
# Enter the Operator to perform 

Operation = input("Enter The Operation you want to perform (Add, Sub, Mul, Div): ")

# step 3 
# using looping statements to perform basic operation

if Operation == 'Add':
    result = num1 + num2
elif Operation == 'Sub':
    result = num1 - num2
elif Operation == 'Mul':
    result = num1 * num2
elif Operation == 'Div':
    # Step 3.1: Handle the division by zero error
    if num2 == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operator."

# Step 4: Display the final result
if result is not None:
    if isinstance(result, (int, float)):
        # Check if the number is a whole number (e.g., 10.0)
        if result.is_integer():
            # Convert to an integer to remove the .0
            print(f"The result of {num1} {Operation} {num2} is: {int(result)}")
        else:
            # Display with decimals for non-whole numbers
            print(f"The result of {num1} {Operation} {num2} is: {result}")
            
    else:
        print(result)


### Task 3
## Type Checker 

# Takes user input as a string
user_input = input("Enter a value: ")

print("\n--- Original Input ---")
print(f"Your input was: '{user_input}'")
print(f"Original data type: {type(user_input)}")

print("\n--- Type Casting Results ---")

try:
    as_int = int(user_input)
    print(f"As an integer: '{as_int}'")
    print(f"Data type is: {type(as_int)}")

# The 'except' block catches the ValueError if the conversion fails
except ValueError:
    print("Cannot be cast to an integer.")

# A separate 'try-except' block is used for the float conversion
try:
    as_float = float(user_input)
    print(f"As a float: '{as_float}'")
    print(f"Data type is: {type(as_float)}")

except ValueError:
    print("Cannot be cast to a float.")


### Bonus Challenge 
## Convert from celsius to Fahrenheit

Celsius = float(input("Enter Celsius: "))

#Celsius to Fahrenheit Conversion using this Formula 
fahrenheit = (Celsius * 9/5) + 32

print("Celsius to Fahrenheit: ", fahrenheit)




