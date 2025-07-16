#---- MINI CHALLENGE ----#

"Write a program that :"
#--1 Asks the user for their name,age and height in cm 
#--2 Converts height to meters 
#--3 print a sentence like :
"Hello [Your_name], you are [Your_age] years old and [Your_height] meters tall"
 



#  Starter Code
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height_cm = float(input("Enter your height in cm: "))

height_m = height_cm / 100

print(f"Hello {name}, you are {age} years old and {height_m} meters tall.")


#--- Revised Code for this same version ---#
#--- To Calculate Weight | BMI ---#

weight = float(input("Enter your weight in kg: "))

BMI = weight / (height_m ** 2)

print(f"Hello {name}, you are {age} years old and your weight is {weight}")

print(f"YOUR BMI is : {BMI}")