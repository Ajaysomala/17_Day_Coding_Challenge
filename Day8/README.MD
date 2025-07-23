# 🚀 Day 8 – Object-Oriented Programming Part 2 (Practice)

This repository contains my hands-on practice with advanced OOP concepts in Python.  
The goal was to **understand and demonstrate** key concepts like Inheritance, Polymorphism, Encapsulation, and Abstraction through short, simple, and engaging examples.

---

## 📚 Concepts Covered

1. ✅ Inheritance (Single, Multilevel, Multiple)
2. ✅ Polymorphism (Method Overriding)
3. ✅ Encapsulation (Private Members with Logic)
4. ✅ Abstraction (ABC with abstract methods)

---

## 🔎 Highlights

### 🔐 Encapsulation – With a Fun Twist  
I created a **Locker class** that stores a private PIN.  
Instead of boring logic, it gives a **hint-based unlock challenge**, making the concept fun to understand and interactive to use.

> 💡 “Hint: It's a 4-digit number. The first two digits are '12', and the last two add up to 7.”

### 🎮 Abstraction – Made Easy to Relate  
I built a **Game abstract class**, and subclassed it with a `RacingGame` that forces the use of `play()` and `exit()` methods — making it super easy to grasp the core idea of abstraction.

---

## 🧠 Why This Matters

- Practicing **polymorphism with real-life roles** (Mom, Kid, Person) makes overriding relatable.
- Using **fun and creative class names** helps in long-term memory retention of OOP principles.
- You don’t need boring enterprise examples to learn — you just need **clarity and creativity**.

---

## 🛠 How to Run

Make sure Python 3.x is installed.

```bash
python day8_practice.py

↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕↕ 💛⏬

This is a beginner-friendly console-based **Banking System** built using Python’s Object-Oriented Programming concepts.

---

## 🧠 Concepts Implemented:

1. **Abstraction** – Abstract base class `BankAccount` with `@abstractmethod withdraw()`.
2. **Encapsulation** – Private balance using `__balance` with public/protected accessors.
3. **Inheritance** – `SavingsAccount` inherits from `BankAccount`.
4. **Polymorphism** – Withdraw method is overridden with specific logic for `SavingsAccount`.

---

## ⚙️ Features:

- 🎯 Account creation with random 6-digit account number
- 💰 Deposit system with amount validation
- 💸 Withdraw with balance checks
- 🧾 View current balance
- 🧠 Error handling for wrong inputs
- 📦 Account data stored in a dictionary (runtime only)

---

## 🔐 Special Logic:

- **Balance is fully private** (`__balance`) and cannot be accessed directly.
- Only the `get_balance()` and `_update_balance()` control balance state.
- Account number is used to uniquely identify and operate on user accounts.

---

## 🧪 How to Use

1. Run the Python file in any terminal or IDE:
```bash
python banking_system.py
