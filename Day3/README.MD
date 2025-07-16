# 🐍 Python Basics & BMI Calculator

Welcome to my first Python learning project! This repository contains beginner-level Python programs focused on:

- 🧠 Understanding basic data types
- 🔁 Type conversions
- 📏 BMI calculation with user input

---

## 📘 Topics Covered

### 🧩 Python Basics

Python is a beginner-friendly language. It is used for:

- Web development 🌐
- Data analysis 📊
- Automation 🤖
- AI & machine learning 🧠

---

## 🔤 Data Types Explained

| Type   | Example      | Meaning                    |
|--------|--------------|----------------------------|
| `int`  | `10`, `-5`    | Whole numbers              |
| `float`| `10.5`, `3.14`| Numbers with decimals       |
| `str`  | `"Hello"`     | Text or characters         |
| `bool` | `True`, `False`| Logical values (Yes/No)  |

---

## 🔁 Type Conversion (Type Casting)

Python allows you to convert between data types:

- `int("10")` → 10
- `float("3.5")` → 3.5
- `str(100)` → `"100"`
- `bool("")` → `False`
- `bool("Hi")` → `True`

You can use `type()` to check what kind of data you're working with.

---

## 💡 Today's Concepts & Challenges

### ✅ Type Checking

```python
type(123)  → <class 'int'>
type("abc") → <class 'str'>

✅ Converting Types
int ➡️ str → str(123) → "123"

str ➡️ int → int("123") → 123

float ➡️ int → int(12.7) → 12

str ➡️ float → float("3.14") → 3.14

float ➡️ str → str(45.6) → "45.6"

✅ Boolean Checks
Value	bool(value)
0, 0.0, "" → False	
Non-zero numbers, "text" → True	

🧍‍♂️ BMI Calculator Project
A small script that asks the user for:

Name

Age

Height in cm

Weight in kg

Then it:

Converts height to meters

Calculates BMI using the formula:

BMI = weight / (height_in_meters ** 2)
Prints a nice summary like:

#---OUTPUT
Hello Ajay, you are 24 years old and 1.66 meters tall.
Your weight is 60 kg.
Your BMI is 21.77
🛠️ How to Run
Open a Python environment like:

VS Code

Thonny

Replit.com

Copy-paste the Python file into it

Run the file and enter the details when asked

🧑‍💻 About Me
Hi! I'm Ajay (Somala), currently learning Python from scratch.
This is my personal learning journey 🚀
More projects and challenges coming soon... 🔥


