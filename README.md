<p align="center">
  <img src="https://raw.githubusercontent.com/github/explore/main/topics/python/python.png" alt="Python Logo" width="120" height="120">
</p>

<h1 align="center">🐍 Advanced Python — Teaching Beyond the Basics</h1>
<p align="center">
  <strong>By Muhammad Faizan | Python Mentor </strong><br/>
  <em>Master advanced Python concepts with real-world depth, clear logic, and hands-on demonstrations.</em>
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Level-Advanced-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Learning%20Platform-HGPT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Instructor-Muhammad%20Faizan-red?style=for-the-badge">
</p>

---

## 🧠 About the Repository
This repository is a complete **teaching and learning resource** for understanding the **advanced layers of Python**.  
Created as part of my teaching sessions at **HGPT**, it covers both theoretical explanations and practical demonstrations of some of Python’s most powerful features.

---

## 🚀 Topics Covered

### ⚙️ 1. *Args and *Kwargs
Learn about **modular architecture** and **command grouping**, improving the scalability of large Python applications.

- How to separate logic into modular “*Args”
- How **kwargs (Args and *Kwargs) help with lightweight modular scripting
- Real-world structure for organized, extensible codebases

### 🧩 2. Instance, Class, and Static Methods
Master Python’s **three method types** and when to use each:

| Type | Accessed Through | Use Case |
|------|------------------|-----------|
| `Instance Method` | Object | Modify instance-specific data |
| `Class Method` | Class | Modify class-level data |
| `Static Method` | Class/Object | Utility or helper functions |

```python
class Student:
    total_students = 0

    def __init__(self, name):
        self.name = name
        Student.total_students += 1

    @classmethod
    def count(cls):
        return cls.total_students

    @staticmethod
    def greet():
        return "Welcome to HGPT Advanced Python!"
🧠 3. Decorators with Arguments
Decorators that take custom arguments for advanced use cases like timing, logging, or validation.

python
Copy code
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello, HGPT students!")
🧮 4. Functional Programming — map(), filter(), and reduce()
Learn how to process data elegantly without explicit loops.

python
Copy code
from functools import reduce

nums = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, nums))
even = list(filter(lambda x: x % 2 == 0, nums))
sum_all = reduce(lambda x, y: x + y, nums)

print(squared, even, sum_all)
✅ map() – applies a function to every element

✅ filter() – filters based on a condition

✅ reduce() – reduces a list to a single value

🧰 5. Error Handling & Exception Flow
Learn to gracefully handle runtime errors and design robust code.

python
Copy code
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Execution successful.")
finally:
    print("Program ended.")
📊 Visual Representation
🧭 Python Concept Progress
Concept	Understanding	Practical Mastery
Decorators	████████████░░░░ 90%	████████████░░░░ 90%
Map/Filter/Reduce	████████████░░░░ 95%	███████████░░░░░ 85%
Error Handling	██████████████░░ 98%	████████████░░░░ 90%
Class Methods	████████████████ 100%	███████████████ 95%
Cogs & Quags	███████████░░░░░ 80%	██████████░░░░░ 75%

🧩 Folder Structure
matlab
Copy code
Advanced-Python/
│
├── decorators/
│   └── decorator_with_arguments.py
│
├── methods/
│   ├── instance_method.py
│   ├── class_method.py
│   └── static_method.py
│
├── functional_programming/
│   ├── map_filter_reduce.py
│
├── error_handling/
│   └── try_except_finally.py
│
└── README.md
📸 Example Output
bash
Copy code
> python map_filter_reduce.py
Squared: [1, 4, 9, 16, 25]
Even: [2, 4]
Sum: 15```


🧑‍🏫 About the Instructor
Muhammad Faizan — a passionate Python mentor, Data Science instructor, and AI researcher.
At HGPT, Faizan has taught hundreds of students advanced Python topics through hands-on projects, blending clarity with creativity.

“Coding is not about syntax — it’s about logic, structure, and creativity.” — Faizan

🌐 Connect With Me
<p align="center"> <a href="https://github.com/faizan-ai"><img src="https://img.shields.io/badge/GitHub-faizan--ai-black?style=for-the-badge&logo=github"></a> <a href="https://www.linkedin.com/in/faizan"><img src="https://img.shields.io/badge/LinkedIn-Muhammad%20Faizan-blue?style=for-the-badge&logo=linkedin"></a> <a href="mailto:faizan@example.com"><img src="https://img.shields.io/badge/Email-faizan%40gmail.com-red?style=for-the-badge&logo=gmail"></a> </p>
⭐ Contribution & Feedback
Contributions, corrections, and feedback are always welcome!
If you have a better approach or a creative example, open a Pull Request or drop an Issue.

<p align="center">Made with 💚 by Muhammad Faizan | HGPT Python Mentor</p> 
