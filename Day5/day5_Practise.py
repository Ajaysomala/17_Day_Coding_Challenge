# Topics:

# Dictionaries (Basics, Methods, Nesting)

# Sets (Basics, Operations)

# Practice Quiz / Mini App: Contact Book CLI or Student Grades Tracker

#----- Dictionary -----#

person = {
    "name": "Ajay",
    "age": 24,
    "City" : "New York"
}

print(person)

# To update the data 
person.update({"name":"Beru"})
person["gender"] = "Male"

print(person)


#--To Print only values
print(person.values())

#--To Print only keys
print(person.keys())

# The safer way to access values .../
print(person.get("name"))

# To Delete Value and clear ..../
person.pop("age")
print(person)

person.clear()
print(person)

#--Looping through dictionary----
student = {"name": "Bob", "grade": "A"}

for key in student:
    print(key, "->", student[key])

# OR

for key, value in student.items():
    print(f"{key}: {value}")

# Nested Dictionaries.../
students = {
    "101": {"name": "John", "grade": "A"},
    "102": {"name": "Emma", "grade": "B"}
}

print(students["101"]["name"])  # John

# Loop through nested dictionary
for roll_no, details in students.items():
    print(f"Roll No: {roll_no}")
    for key, value in details.items():
        print(f"  {key}: {value}")


#----- Sets -----#

my_set = {1, 2, 3, 4}
print(my_set)  # {1, 2, 3, 4}

# Set Operations 
A = {1, 2, 3}
B = {3, 4, 5}

print("Union:", A | B)              # {1, 2, 3, 4, 5}
print("Intersection:", A & B)      # {3}
print("Difference (A - B):", A - B) # {1, 2}
print("Symmetric Diff:", A ^ B)     # {1, 2, 4, 5}

# Set Methods 

my_set = {1, 2}
my_set.add(3)
print(my_set)  # {1, 2, 3}

my_set.remove(2)
my_set.discard(5)  # No error if 5 not present
print(my_set)

"""pop $ Clear """

element = my_set.pop()   # Removes a random element
print("Removed:", element)
print(my_set)

my_set.clear()
print(my_set)  # Empty set: set()

# set comaprisons 

A = {1, 2}
B = {1, 2, 3, 4}

print("Subset:", A.issubset(B))      # True
print("Superset:", B.issuperset(A))  # True
print("Disjoint:", A.isdisjoint({5, 6}))  # True
