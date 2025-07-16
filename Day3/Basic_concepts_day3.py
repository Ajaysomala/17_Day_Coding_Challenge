#---Todays Concepts---#
#------Challenges------#

#----INT, FLOAT, STR, BOOL----#

# Basic method to check class type  

a = 12
print(type(a))

#---INT & | Type Conversion | ---#

int_input = 123

to_str = str(int_input)
# converts to string
print(to_str, type(to_str))

to_float = float(a)
# converts to float
print(to_float, type(to_float))


#--- STR & | Type Conversion ---#

str_input = "123"
print(type(str_input))

to_int = int(str_input)
# converts str to int
print(to_int, type(to_int))

to_float = float(str_input)
# converts str to float
print(to_float, type(to_float))


#--- FLOAT & | Type Conversion ---#

float_input = 123.45
print(type(float_input))

to_int = int(float_input)
# converts float to int
print(to_int, type(to_int))

to_str = str(float_input)
# converts float to str
print(to_str, type(to_str))


#--- BOOL to check whether the condition or logic is trur / false
#--- '0' will always becomes false
a = 0
b = 1
print(bool(a))
print(bool(b))

A = 0.0
A = 1.0
print(bool(A))
print(bool(A))