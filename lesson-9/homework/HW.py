## Homework 9
## Object-Oriented Programming (OOP) Exercises
# 1. Circle Class.Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter radius of the circle: "))
c = Circle(r)

print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())

# 2.  Person Class Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name, country, DOB):
        self.name = name
        self.country = country
        self.DOB = DOB  

    def calculate_age(self):
        birth_date = datetime.strptime(self.DOB, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def greet(self):
        age = self.calculate_age()
        print(f"Hello, my name is {self.name}. I'm {age} years old and I'm from {self.country}.")


p1 = Person("Sherzod", "USA", "1992-01-10")
p1.greet()

# 3. Calculator Class Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b

calc = Calculator()

print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))
print("Divide by zero test:", calc.divide(10, 0))

# 4. Shape and Subclasses Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 3

    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):  
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2 
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())

print("Square area:", square.area())
print("Square perimeter:", square.perimeter())

print("Triangle area:", triangle.area())
print("Triangle perimeter:", triangle.perimeter())

# 5. Binary Search Tree Class Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, value):
        current = self.root
        while current is not None:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False


tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))   
print(tree.search(20))  

# 6. Stack Data Structure Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None


stack = Stack()
stack.push(5)
stack.push(10)
print(stack.pop())  
print(stack.pop())
print(stack.pop())  

# 7. Linked List Data Structure Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None  

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node 
        else:
            current = self.head
            while current.next:
                current = current.next 
            current.next = new_node

    def delete(self, data):
        current = self.head
        previous = None

        while current:
            if current.data == data:
                if previous:  
                    previous.next = current.next
                else:  
                    self.head = current.next
                return True  
            previous = current
            current = current.next

        return False 

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()  

ll.delete(20)
ll.display()  

# 8. Shopping Cart Class Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name][1] += quantity  
        else:
            self.items[name] = [price, quantity] 

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
        else:
            print(f"{name} is not in the cart.")

    def get_total(self):
        total = 0
        for price, quantity in self.items.values():
            total += price * quantity
        return total

    def display_cart(self):
        if not self.items:
            print("Your shopping cart is empty.")
        else:
            print("Items in your cart:")
            for name, (price, quantity) in self.items.items():
                print(f"- {name}: ${price} x {quantity}")
            print(f"Total: ${self.get_total()}")

cart = ShoppingCart()
cart.add_item("Apple", 0.5, 4)
cart.add_item("Milk", 1.5, 2)
cart.display_cart()

cart.remove_item("Apple")
cart.display_cart()

# 9. Stack with Display Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Popped: {removed}")
            return removed
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def display(self):
        if not self.is_empty():
            print("Stack contents (top to bottom):")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.items) == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

stack.pop()
stack.display()

# 10. Queue Data Structure Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def display(self):
        if not self.is_empty():
            print("Queue contents (front to back):")
            for item in self.items:
                print(item)
        else:
            print("Queue is empty.")

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()

queue.dequeue()
queue.display()

# 11. Bank Class Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class CustomerAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposited ${amount}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}")
        else:
            print("Insufficient balance or invalid amount.")

    def show_balance(self):
        print(f"{self.name}'s balance: ${self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}  
    def create_account(self, name, initial_balance=0):
        if name not in self.accounts:
            self.accounts[name] = CustomerAccount(name, initial_balance)
            print(f"Account created for {name}")
        else:
            print("Account already exists.")

    def get_account(self, name):
        return self.accounts.get(name, None)
    
bank = Bank()
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)

alice = bank.get_account("Alice")
bob = bank.get_account("Bob")

if alice:
    alice.deposit(200)
    alice.withdraw(150)
    alice.show_balance()

if bob:
    bob.withdraw(1000)  
    bob.deposit(300)
    bob.show_balance()
