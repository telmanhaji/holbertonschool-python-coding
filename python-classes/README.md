# Python - Classes and Objects

## 📚 Resources

**Read or watch these in the order presented:**

1.  **Object Oriented Programming** (*Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod`, and `staticmethod` yet.*)
2.  **Object-Oriented Programming** (*Read General Introduction, First-class Everything, A Minimal Class in Python, Attributes, Methods, The `__init__` Method, Data Abstraction, Encapsulation, and Information Hiding, Public, Protected, and Private Attributes.*)
3.  **Properties vs. Getters and Setters**
4.  **Learn to Program 9 : Object Oriented Programming**
5.  **Python Classes and Objects**
6.  **Object Oriented Programming**

---

## 🎯 Learning Objectives

At the end of this project, you are expected to be able to **explain to anyone**, **without the help of Google**:

### General
* Why Python programming is awesome
* What is **OOP**
* What is meant by "first-class everything"
* What is a **class**
* What is an **object** and an **instance**
* What is the difference between a class and an object or instance
* What is an **attribute**
* What are and how to use **public**, **protected**, and **private** attributes
* What is `self`
* What is a **method**
* What is the special `__init__` method and how to use it
* What is **Data Abstraction**, **Data Encapsulation**, and **Information Hiding**
* What is a **property**
* What is the difference between an attribute and a property in Python
* What is the Pythonic way to write getters and setters in Python
* How to dynamically create arbitrary new attributes for existing instances of a class
* How to bind attributes to objects and classes
* What is the `__dict__` of a class and/or instance of a class and what does it contain
* How does Python find the attributes of an object or class
* How to use the `getattr` function

---

## ⚙️ Requirements

### General
* **Allowed editors:** `vi`, `vim`, `emacs`
* **Environment:** All your files will be interpreted/compiled on **Ubuntu 14.04 LTS** using `python3` (version 3.4.3)
* **Line Endings:** All your files should end with a new line
* **Shebang:** The first line of all your files should be exactly `#!/usr/bin/python3`
* **README:** A `README.md` file, at the root of the folder of the project, is mandatory
* **Style:** Your code should use the **PEP 8** style (version 1.7)
* **Executable:** All your files must be executable
* **File Length:** The length of your files will be tested using `wc`
* **Documentation:** All modules, classes, and functions must have docstrings.

---

## 📂 Tasks

### 0. Square with size
Write a class `Square` that defines a square by:
* **Private instance attribute:** `size`
* **Instantiation:** `size` (no type/value verification)
* You are not allowed to import any module

> **Why? Why is size a private attribute?**
> The size of a square is crucial for a square, many things depend on it (area computation, etc.), so you, as a class builder, must control the type and value of this attribute. One way to have control is to keep it private. You will see in next tasks how to get, update, and validate the size value.

**File:** `0-square.py`

### 1. Size validation
Write a class `Square` that defines a square by: (based on `0-square.py`)
* **Private instance attribute:** `size`
* **Instantiation with optional size:** `def __init__(self, size=0):`
    * `size` must be an **integer**, otherwise raise a `TypeError` exception with the message `size must be an integer`
    * If `size` is less than **0**, raise a `ValueError` exception with the message `size must be >= 0`
* You are not allowed to import any module

**File:** `1-square.py`

### 2. Area of a square
Write a class `Square` that defines a square by: (based on `1-square.py`)
* **Private instance attribute:** `size`
* **Instantiation with optional size:** `def __init__(self, size=0):`
    * Same validation as Task 1.
* **Public instance method:** `def area(self):` that returns the current square area
* You are not allowed to import any module

**File:** `2-square.py`



### 3. Access and update private attribute
Write a class `Square` that defines a square by: (based on `2-square.py`)
* **Private instance attribute:** `size`:
    * **Property** `def size(self):` to retrieve it
    * **Property setter** `def size(self, value):` to set it:
        * `size` must be an **integer**, otherwise raise a `TypeError` exception with the message `size must be an integer`
        * If `size` is less than **0**, raise a `ValueError` exception with the message `size must be >= 0`
* **Instantiation with optional size:** `def __init__(self, size=0):`
* **Public instance method:** `def area(self):` that returns the current square area
* You are not allowed to import any module

> **Why a getter and setter?**
> Reminder: `size` is a private attribute. We did that to make sure we control the type and value. Getter and setter methods are not 100% Python, but more OOP. With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc. Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

**File:** `3-square.py`

### 4. Printing a square
Write a class `Square` that defines a square by: (based on `3-square.py`)
* **Private instance attribute:** `size`:
    * Property `def size(self):` to retrieve it
    * Property setter `def size(self, value):` to set it (with validation)
* **Instantiation with optional size:** `def __init__(self, size=0):`
* **Public instance method:** `def area(self):` that returns the current square area
* **Public instance method:** `def my_print(self):` that prints in stdout the square with the character `#`:
    * If `size` is equal to 0, print an empty line
* You are not allowed to import any module

**File:** `4-square.py`

---

## 📋 Repository Information
* **GitHub repository:** `holbertonschool-python-coding`
* **Directory:** `python-classes`