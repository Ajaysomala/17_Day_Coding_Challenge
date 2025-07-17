#--List, Tuples Manipulations

#---- List Manipulation ---#

fruits = ["Apple", "Banana","Cherry","Grape","Orange"]
fruits.append("Mango")

fruits.pop(1)

fruits.sort()

print("sorted fruits list:",fruits)
print(len(fruits))

# Create a list of squares from 1 to 10 using list comprehension
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)



# Create a tuple of cities
cities = ("Hyderabad", "Delhi", "Mumbai", "Chennai", "Kolkata")

# Try modifying it (expect error)
try:
    cities[0] = "Bangalore"
except TypeError as e:
    print("Error:", e)

# Convert to list, modify, and convert back
city_list = list(cities)
city_list[0] = "Bangalore"
cities = tuple(city_list)

print("Updated Tuple:", cities)
