## ---- Day 10 CONCEPTS ---- ##

## List of concepts to master Day 10 Python....../

"""
1. Lambda Function
2. Map() + lambda 
3. Filter() + lambda 
4. Reduce() + lambda 

"""

## Lambda Function

square = lambda x: x**2
print(square(5))  # ➝ 25



## Map() + lambda 

print(list(map(lambda x: x * 2, [1, 2, 3, 4])))  # ➝ [2, 4, 6, 8]

######### BEST EXAMPLE FOR MAP() FUNCTION #########

#---->>>> Convert Prices from USD to INR using map()
usd_prices = [10, 25, 50, 100]

inr_prices = list(map(lambda price: price * 83, usd_prices))
print(inr_prices)  # ➝ [830, 2075, 4150, 8300]
#>>>>>> List Comprehension <<<<<<
inr_prices_lc = [price * 83 for price in usd_prices]


## Filter() + lambda

print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4])))  # ➝ [1, 3]

######### BEST EXAMPLE FOR FILTER() FUNCTION #########

#---->>>> Filter Out people under 18 using filter ()
ages = [12, 17, 18, 24, 30, 15]

adults = list(filter(lambda age: age >= 18, ages))
print(adults)  # ➝ [18, 24, 30]
#>>> List Comprehension <<<<
adults_lc = [age for age in ages if age >= 18]


## Reduce() + lambda

print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4])))  # ➝ [1, 3]

######## BEST EXAMPLE FOR REDUCE() FUNCTION #########

#---->>>> Calculate total weight of parcels using reduce()

from functools import reduce

weights = [1.2, 3.5, 2.0, 0.8]  # kg

total_weight = reduce(lambda x, y: x + y, weights)
print(total_weight)  # ➝ 7.5


# >>>>>>>>>>>>>>>>>>>>>>>>> BONUS CHALLENGE <<<<<<<<<<<<<<<<<<<<<<<<<<<


# convert celsius to fahrenheit using map()

celsius_input = input("Enter Celsius temperatures separated by space: ")
celsius = list(map(float, celsius_input.split()))

fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

# filters Odd Numbers from user input using filter()

nums_input = input("Enter numbers separated by space: ")
nums = list(map(int, nums_input.split()))

odds = list(filter(lambda x: x % 2 != 0, nums))
print("Odd numbers:", odds)

# multiply all numbers with reduce using reduce()

from functools import reduce

nums_input = input("Enter numbers separated by space: ")
nums = list(map(int, nums_input.split()))

product = reduce(lambda x, y: x * y, nums)
print("Product of all numbers:", product)
