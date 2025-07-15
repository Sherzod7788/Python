## Lesson 8
## Python Exception Handling: Exercises, Solutions, and Practice
# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

try:
    num = int(input("Enter a number: "))
    result = num / 0  # This will cause a ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

# 2.Write a Python program that prompts the user to input an integer and raises a ValueError exception 
# if the input is not a valid integer.

try:
    numerator = int(input('Enter a number to divide:'))
    denomerator = int(input('Enter a number to divide by:'))
    res = numerator / denomerator
    print(res)
except ValueError:
    print('You can not enter string to the integer part') 
# 3.Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

try:
    file_name = input("Enter the filename to open: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")

# 4.Write a Python program that prompts the user to input two numbers and raises a TypeError exception if 
# the inputs are not numerical.


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)
except ValueError:
    print("Error: Please enter only numeric values.")

# 5.Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    file_name = input("Enter the file name: ")
    with open(file_name, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except PermissionError:
    print("Error: You don't have permission to open this file.")

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception 
# if the index is out of range.

try:
    my_list = [10, 20, 30, 40, 50]
    index = int(input("Enter an index (0 to 4): "))
    print("Element at index", index, "is:", my_list[index])
except IndexError:
    print("Error: Index is out of range. Please enter a number between 0 and 4.")
except ValueError:
    print("Error: Please enter a valid integer.")

# 7.Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the 
# user cancels the input.

try:
    number = int(input("Enter a number:"))
    print("Your entered number", number)
except KeyboardInterrupt:
    print("\n Enterence stopped (Ctrl+C pushed). system stopped")

# 8.Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = a / b
    print("Result:", result)
except ArithmeticError:
    print("Error: An arithmetic error occurred (possibly division by zero).")

# 9.Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

filename = input("Enter the file name: ")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print("File content:\n", content)

except UnicodeDecodeError:
    print("UnicodeDecodeError: Trying with different encoding...")

    try:
        with open(filename, 'r', encoding='latin-1') as f:
            content = f.read()
            print("File content (fallback):\n", content)

    except Exception as e:
        print("Still couldn't read the file:", e)

except FileNotFoundError:
    print("File not found. Please check the file name.")

except Exception as e:
    print("Unexpected error:", e)

# 10.Write a Python program that executes a list operation and handles an AttributeError exception if the 
# attribute does not exist.

try:
    list[1,2,3,4,5,6,7]
    list.upper()
except AttributeError:
    print("Error there is not such kind of element or attribute")
## Python File Input Output: Exercises, Practice, Solution
## File Input/Output Exercises
# 1.Write a Python program to read an entire text file.

filename = input("Enter the file name ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\n📄 File content:\n")
        print(content)
except FileNotFoundError:
    print("❌ Error: File not found.")
except Exception as e:
    print("❗An error occurred:", e)

# 2.Write a Python program to read first n lines of a file.

filename = input("Enter the file name: ")
n = int(input("Enter how many lines to read: "))

try:
    with open(filename, 'r') as file:
        print(f"\n First {n} lines of the file:\n")
        for i in range(n):
            line = file.readline()
            if not line:  
                break
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
# 3. Write a Python program to append text to a file and display the text.

with open("example.txt", "a") as file:
    file.write("\n Hello World.")

with open('example.txt', 'r')as file:
    content = file.read()
    print('\n File content after appending \n')
    print(content)
# 4. Write a Python program to read last n lines of a file.

filename = input("Enter the file name: ")
n = int(input("Enter last line to read: "))

try:
    with open(filename, 'r') as file:
        lines = file.readlines() 
        print(f"\n Last {n} lines of the file:\n")
        for line in lines[-n:]:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
# 5.Write a Python program to read a file line by line and store it into a list.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]  
        print("\n Lines stored in a list:\n")
        print(lines)
except FileNotFoundError:
    print(" Error: File not found.")
except Exception as e:
    print("An error occurred:", e)


# 6.Write a Python program to read a file line by line and store it into a variable.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        content = ""
        for line in file:
            content += line  
        print("\n File content stored in variable:\n")
        print(content)
except FileNotFoundError:
    print(" Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 7.Write a Python program to read a file line by line and store it into an array.

filename = input("Enter file name ")

try:
    with open(filename, "r") as file:
        lines = [line.strip() for line in file]  
        print("\n File content stored into an array:")
        print(lines)

except FileNotFoundError:
    print(" Error: File not found")
except Exception as e:
    print(" Unknown error:", e)

# 8.Write a Python program to find the longest words.

with open("example.txt", "r") as file:
    content = file.read()
    words = content.split()
    max_len = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_len]

print("📏 Longest word(s) from file:", longest_words)

# 9.Write a Python program to count the number of lines in a text file.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        line_count = sum(1 for line in file)
        print(f"\n Total number of lines: {line_count}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)
# 10. Write a Python program to count the frequency of words in a file.

file = open("example.txt", "r")
words = file.read().split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(word, ":", count)
file.close()

# 11. Write a Python program to get the file size of a plain file.

import os

filename = input("Enter the file name: ")

try:
    size = os.path.getsize(filename)
    print(f"\n File size of '{filename}' is {size} bytes")
except FileNotFoundError:
    print(" Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 12.Write a Python program to write a list to a file.

file = open('example.txt', 'w')
file.write('Hello Sherzod whats up')
file.close()


file = open('example.txt', 'r')
content = file.read()
print(content)
file.close() 
# 13. Write a Python program to copy the contents of a file to another file.

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, "r") as src:
        content = src.read()

    with open(destination_file, "w") as dest:
        dest.write(content)

    print(f"\nContent copied from '{source_file}' to '{destination_file}' successfully!")

except FileNotFoundError:
    print(" Error: Source file not found.")
except Exception as e:
    print("An error occurred:", e)
# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.

file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")

try:
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        print("\n Combined lines:")
        for l1, l2 in zip(lines1, lines2):
            combined = l1.strip() + " " + l2.strip()
            print(combined)

except FileNotFoundError:
    print(" Error: One of the files was not found.")
except Exception as e:
    print(" An error occurred:", e)

# 15.Write a Python program to read a random line from a file.

import random

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()  

        if lines:
            random_line = random.choice(lines)
            print("\n Random line from file:")
            print(random_line.strip())
        else:
            print("⚠️ The file is empty.")

except FileNotFoundError:
    print(" Error: File not found.")
except Exception as e:
    print(" An error occurred:", e)

# 16.Write a Python program to assess if a file is closed or not.

file = open("example.txt", "r")
print("Is the file closed?", file.closed) 
file.close()

print("Is the file closed now?", file.closed) 

# 17.Write a Python program to remove newline characters from a file.

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()  
    
    cleaned_text = ' '.join(line.strip() for line in lines)

    print("\n Cleaned content (no newline characters):\n")
    print(cleaned_text)

except FileNotFoundError:
    print(" Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.

# Ask for the file name
filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        text = file.read()            
        words = text.split()            
        word_count = len(words)        

        print(f"\n Total number of words in '{filename}': {word_count}")

except FileNotFoundError:
    print(" Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 19. Write a Python program to extract characters from various text files and put them into a list.

import os

file_list = ["example.txt", "example2.txt"]

char_list = []

for file_name in file_list:
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()
            char_list.extend(list(content)) 
    else:
        print(f" File '{file_name}' not found.")

char_list = [char for char in char_list if char != '\n']

print("\n Characters extracted from files:")
print(char_list)

# 20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w") as file:
        file.write(f"This is file {filename}\n")

print(" 26 text files (A.txt to Z.txt) have been created.")

# 21.Write a Python program to create a file where all letters of the English alphabet are listed with a 
# specified number of letters on each line.

import string

n = int(input("Enter number of letters per line: "))

alphabet = string.ascii_lowercase 

with open("alphabet_output.txt", "w") as file:
    for i in range(0, len(alphabet), n):
        line = alphabet[i:i+n]  
        file.write(' '.join(line) + "\n") 

print("File 'alphabet_output.txt' created successfully.")
