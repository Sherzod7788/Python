## Homework Projects: 
## Homework 1. ToDo List Application
# 1.Define Task Class: Create a Task class with attributes such as task title, description, due date, and status.

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date  
        self.status = status     

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}")


task1 = Task(
    title="Finish Python Project",
    description="Complete the final module of the Python course",
    due_date=datetime(2025, 7, 25),
    status="In Progress"
)
print(task1)

# 2.Define ToDoList Class: 
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date  
        self.status = status     

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}\n")

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for task in self.tasks:
            print(task)

    def display_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status != "Completed"]
        if not incomplete:
            print("All tasks are completed!")
            return
        for task in incomplete:
            print(task)

todo = ToDoList()

task1 = Task("Study Python", "Complete OOP section", datetime(2025, 7, 22))
task2 = Task("Buy groceries", "Milk, eggs, bread", datetime(2025, 7, 21))

todo.add_task(task1)
todo.add_task(task2)

print("\nAll Tasks:")
todo.list_all_tasks()

print("\nIncomplete Tasks:")
todo.display_incomplete_tasks()

todo.mark_task_complete("Buy groceries")

print("\nIncomplete Tasks After Completion:")
todo.display_incomplete_tasks()

# 3.Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.

from datetime import datetime

class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return (f"\nTitle: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date.strftime('%Y-%m-%d')}\n"
                f"Status: {self.status}\n")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            print(task)

    def display_incomplete_tasks(self):
        found = False
        for task in self.tasks:
            if task.status != "Completed":
                print(task)
                found = True
        if not found:
            print("No incomplete tasks!")

def main():
    todo_list = ToDoList()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD): ")
            try:
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                task = Task(title, description, due_date)
                todo_list.add_task(task)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        elif choice == "2":
            title = input("Enter the title of the task to mark as complete: ")
            todo_list.mark_task_complete(title)
        elif choice == "3":
            print("\nAll Tasks:")
            todo_list.list_all_tasks()
        elif choice == "4":
            print("\nIncomplete Tasks:")
            todo_list.display_incomplete_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()

# 4.Test the Application: Create instances of tasks and test the functionality of your ToDoList.

from datetime import datetime

todo = ToDoList()


task1 = Task("Buy groceries", "Buy milk, bread, eggs", datetime(2025, 7, 21))
task2 = Task("Finish homework", "Complete Python OOP assignment", datetime(2025, 7, 22))
task3 = Task("Workout", "Go for a 30-minute run", datetime(2025, 7, 23))

print("Adding Tasks:")
todo.add_task(task1)
todo.add_task(task2)
todo.add_task(task3)

print("\nListing All Tasks:")
todo.list_all_tasks()

print("\nIncomplete Tasks:")
todo.display_incomplete_tasks()

print("\nMarking 'Workout' as completed:")
todo.mark_task_complete("Workout")

print("\nIncomplete Tasks (After Completion):")
todo.display_incomplete_tasks()

print("\nTrying to complete a non-existent task:")
todo.mark_task_complete("Call Mom")

## Homework 2. Simple Blog System
# 1.Define Post Class: Create a Post class with attributes like title, content, and author.

class Post:
    def __init__(self, title, content, author):
        self.title = title        
        self.content = content    
        self.author = author      

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}")


post1 = Post("Welcome Post", "Hello everyone! This is our first post.", "Admin")

print(post1)

# 2.Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
class Blog:
    def __init__(self):
        self.posts = []  

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post titled '{post.title}' added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for post in self.posts:
            print(post)
            print("-" * 40)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print(post)
                print("-" * 40)
                found = True
        if not found:
            print(f"No posts found by author: {author_name}")

post1 = Post("Python Tips", "Use list comprehensions for cleaner code.", "Toshmat")
post2 = Post("Django Intro", "Django is a powerful web framework.", "Bob")
post3 = Post("Advanced Python", "Let's dive into decorators!", "Toshmat")

my_blog = Blog()
my_blog.add_post(post1)
my_blog.add_post(post2)
my_blog.add_post(post3)

print("\nAll Blog Posts:")
my_blog.list_all_posts()

print("\nPosts by Toshmat:")
my_blog.display_posts_by_author("Toshmat")

# 3. Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Content:\n{self.content}")

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for post in self.posts:
            print("\n" + str(post))
            print("-" * 40)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print("\n" + str(post))
                print("-" * 40)
                found = True
        if not found:
            print(f"No posts found by author: {author_name}")

def main():
    blog = Blog()

    while True:
        print("\n===== BLOG MENU =====")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Exit")

        choice = input("Enter your choice (1–4): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author's name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            print("\nAll Blog Posts:")
            blog.list_all_posts()

        elif choice == "3":
            author_name = input("Enter the author's name to filter posts: ")
            blog.display_posts_by_author(author_name)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

# 4. Enhance Blog System: Add functionality to delete a post, edit a post, and display the latest posts.

from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def edit(self, new_title=None, new_content=None, new_author=None):
        if new_title:
            self.title = new_title
        if new_content:
            self.content = new_content
        if new_author:
            self.author = new_author
        self.timestamp = datetime.now()

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Posted: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Content:\n{self.content}")

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
            return
        for post in self.posts:
            print("\n" + str(post))
            print("-" * 40)

    def display_posts_by_author(self, author_name):
        found = False
        for post in self.posts:
            if post.author.lower() == author_name.lower():
                print("\n" + str(post))
                print("-" * 40)
                found = True
        if not found:
            print(f"No posts found by author: {author_name}")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' has been deleted.")
                return
        print(f"No post found with the title '{title}'.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                print("Leave blank to keep current value.")
                new_title = input("New title: ")
                new_content = input("New content: ")
                new_author = input("New author: ")
                post.edit(
                    new_title if new_title.strip() else None,
                    new_content if new_content.strip() else None,
                    new_author if new_author.strip() else None,
                )
                print(f"Post '{title}' updated successfully.")
                return
        print(f"No post found with the title '{title}'.")

    def display_latest_posts(self, count=5):
        if not self.posts:
            print("No posts available.")
            return
        sorted_posts = sorted(self.posts, key=lambda p: p.timestamp, reverse=True)
        print(f"\nShowing latest {min(count, len(sorted_posts))} post(s):")
        for post in sorted_posts[:count]:
            print("\n" + str(post))
            print("-" * 40)

def main():
    blog = Blog()

    while True:
        print("\n===== BLOG MENU =====")
        print("1. Add a Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author's name: ")
            post = Post(title, content, author)
            blog.add_post(post)

        elif choice == "2":
            blog.list_all_posts()

        elif choice == "3":
            author_name = input("Enter the author's name to filter posts: ")
            blog.display_posts_by_author(author_name)

        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.delete_post(title)

        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            blog.edit_post(title)

        elif choice == "6":
            try:
                count = int(input("How many latest posts do you want to see? (default 5): ") or 5)
                blog.display_latest_posts(count)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


# 5.Test the Application: Create instances of posts and test the functionality of your Blog system.

from datetime import datetime, timedelta
import time

def test_blog_system():
    blog = Blog()

    
    print("\n Adding posts:")
    post1 = Post("Welcome", "Welcome to our new blog!", "Admin")
    time.sleep(1)  
    post2 = Post("Python Tips", "Use list comprehensions for clean code.", "Alice")
    time.sleep(1)
    post3 = Post("Django Intro", "Learn Django for web development.", "Bob")
    time.sleep(1)
    post4 = Post("Advanced Python", "Explore decorators and generators.", "Alice")
    time.sleep(1)
    post5 = Post("Goodbye", "Thanks for visiting!", "Admin")

    for post in [post1, post2, post3, post4, post5]:
        blog.add_post(post)

    
    print("\n Listing all posts:")
    blog.list_all_posts()

   
    print("\n Posts by Alice:")
    blog.display_posts_by_author("Alice")

    print("\n Editing 'Django Intro' post:")
    post_to_edit = "Django Intro"
    for post in blog.posts:
        if post.title == post_to_edit:
            post.edit(new_content="Django is a high-level Python web framework.")
            print(f"Edited post:\n{post}")
            break

    
    print("\n Deleting 'Goodbye' post:")
    blog.delete_post("Goodbye")

    
    print("\n Deleting non-existent post:")
    blog.delete_post("NonExistent")

   
    print("\n Displaying latest 3 posts:")
    blog.display_latest_posts(3)

test_blog_system()

## Homework 3. Simple Banking System
# 1.Define Account Class: Create an Account class with attributes like account number, account holder name, and balance.

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.holder_name}\n"
                f"Balance: ${self.balance:.2f}")

acc1 = Account("123456789", "John Doe", 700.0)

print(acc1)

# 2.Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited to account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn from account {self.account_number}.")
        else:
            print("Insufficient balance or invalid amount.")

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.holder_name}\n"
                f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} created for {account.holder_name}.")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balance for {account.holder_name}: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")


my_bank = Bank()

acc1 = Account("001", "Sanjar", 1000)
acc2 = Account("002", "Bobur", 500)

my_bank.add_account(acc1)
my_bank.add_account(acc2)

my_bank.check_balance("001")

my_bank.deposit("001", 200)

my_bank.withdraw("002", 300)

my_bank.check_balance("002")

# 3.Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited to account {self.account_number}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn from account {self.account_number}.")
        else:
            print("Insufficient balance or invalid amount.")

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.holder_name}\n"
                f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f" Account '{account.account_number}' created for {account.holder_name}.")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f" Balance: ${account.balance:.2f}")
        else:
            print(" Account not found.")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(" Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print(" Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n====== BANK MENU ======")
        print("1. Add New Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            try:
                initial_balance = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid balance input.")
                continue
            account = Account(acc_num, name, initial_balance)
            bank.add_account(account)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.deposit(acc_num, amount)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
            except ValueError:
                print("Invalid amount.")
                continue
            bank.withdraw(acc_num, amount)

        elif choice == "5":
            print(" Exiting. Thank you for using our bank system!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()

# 4.Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.

class Account:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" ${amount:.2f} deposited to account {self.account_number}.")
        else:
            print(" Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print(" Amount must be greater than zero.")
        elif amount > self.balance:
            print(" Insufficient balance. Overdraft not allowed.")
        else:
            self.balance -= amount
            print(f" {amount:.2f} withdrawn from account {self.account_number}.")

    def __str__(self):
        return (f"\n Account Details:\n"
                f"Account Number: {self.account_number}\n"
                f"Holder Name: {self.holder_name}\n"
                f"Balance: ${self.balance:.2f}")
    
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f" Account '{account.account_number}' created for {account.holder_name}.")

    def find_account(self, account_number):
        for acc in self.accounts:
            if acc.account_number == account_number:
                return acc
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f" Balance: ${account.balance:.2f}")
        else:
            print(" Account not found.")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.deposit(amount)
        else:
            print(" Account not found.")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)

        if not from_acc:
            print(f" Sender account '{from_acc_num}' not found.")
            return
        if not to_acc:
            print(f" Receiver account '{to_acc_num}' not found.")
            return
        if amount <= 0:
            print("Invalid transfer amount.")
            return
        if from_acc.balance < amount:
            print(" Transfer failed. Insufficient funds.")
            return

        from_acc.withdraw(amount)
        to_acc.deposit(amount)
        print(f"{amount:.2f} transferred from {from_acc_num} to {to_acc_num}.")

    def show_account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(account)
        else:
            print(" Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n====== BANK MENU ======")
        print("1. Add New Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Show Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            try:
                initial_balance = float(input("Enter initial balance: "))
            except ValueError:
                print(" Invalid balance input.")
                continue
            account = Account(acc_num, name, initial_balance)
            bank.add_account(account)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            bank.check_balance(acc_num)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to deposit: "))
                bank.deposit(acc_num, amount)
            except ValueError:
                print(" Invalid amount.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            try:
                amount = float(input("Enter amount to withdraw: "))
                bank.withdraw(acc_num, amount)
            except ValueError:
                print(" Invalid amount.")

        elif choice == "5":
            from_acc = input("Enter sender account number: ")
            to_acc = input("Enter receiver account number: ")
            try:
                amount = float(input("Enter amount to transfer: "))
                bank.transfer(from_acc, to_acc, amount)
            except ValueError:
                print(" Invalid amount.")

        elif choice == "6":
            acc_num = input("Enter account number: ")
            bank.show_account_details(acc_num)

        elif choice == "7":
            print(" Exiting. Thank you for using our bank system!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")


# 5.Test the Application:
# Create instances of accounts and test the functionality of your Banking system.

bank = Bank()


acc1 = Account("A001", "Toshmat", 1000.0)
acc2 = Account("A002", "Bobur", 500.0)
acc3 = Account("A003", "Sanjar", 300.0)

bank.add_account(acc1)
bank.add_account(acc2)
bank.add_account(acc3)

bank.show_account_details("A001")
bank.show_account_details("A002")
bank.show_account_details("A003")

bank.deposit("A001", 200.0)   
bank.deposit("A002", 100.0)   

bank.withdraw("A003", 50.0)   
bank.withdraw("A003", 500.0)  


bank.transfer("A001", "A002", 300.0)  
bank.transfer("A002", "A003", 700.0)  

bank.check_balance("A001")
bank.check_balance("A002")
bank.check_balance("A003")
