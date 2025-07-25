# 🔥 Day 10: Lambda Functions & Functional Programming Tools

### 🚀 Mission:
Master Python's **Lambda Expressions** and functional tools like **map()**, **filter()**, and **reduce()**, then build a **Lambda Shortener App** that intelligently converts functional code to list comprehension!

---

## 🧠 Concepts Covered

- ✅ Lambda Functions (Anonymous Functions)
- ✅ `map()` with lambda ➝ apply function to each item
- ✅ `filter()` with lambda ➝ filter items based on condition
- ✅ `reduce()` with lambda ➝ reduce list to a single value
- ✅ List Comprehensions as equivalent expressions
- ✅ Real-world examples (Price conversion, Age filtering, Parcel weights)
- ✅ User input + lambda practice
- ✅ Mini-App: `lambda_shortener()` that converts `map()` and `filter()` expressions into list comprehensions

---

## 🛠️ Code Highlights

```python
# Square using lambda
square = lambda x: x**2
print(square(5))  # ➝ 25

# Convert USD to INR using map()
usd_prices = [10, 25, 50, 100]
inr_prices = list(map(lambda price: price * 83, usd_prices))
# ➝ [830, 2075, 4150, 8300]

# Filter adults (age >= 18)
ages = [12, 17, 18, 24, 30]
adults = list(filter(lambda age: age >= 18, ages))
# ➝ [18, 24, 30]

# Reduce total weight
from functools import reduce
weights = [1.2, 3.5, 2.0, 0.8]
total_weight = reduce(lambda x, y: x + y, weights)
# ➝ 7.5

💡 Bonus User Challenges
🌡️ Convert Celsius to Fahrenheit using map()

🔢 Filter odd numbers using filter()

✖️ Multiply all numbers using reduce()

💻 Main App: Lambda Shortener
Converts map() and filter() lambda functions to clean list comprehensions.
✍🏼✍🏼✍🏼
def lambda_shortener(code_str):
    # Detects lambda usage in map/filter
    # Converts into equivalent Python list comprehension


🔍 Examples:
lambda_shortener("map(lambda x: x * 2, nums)")
# ➝ [x * 2 for x in nums]

lambda_shortener("filter(lambda x: x > 10, my_list)")
# ➝ [x for x in my_list if x > 10]
