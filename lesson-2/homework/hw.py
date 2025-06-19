## 1. Age Calculator
## Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

name = input('enter your name')
year_of_birth = int(input('enter your year of birth'))
current_year = 2025
age = current_year - year_of_birth
print(f'Hello, {name}! Your are {age} years old.')





## 2. Extract Car Names
## Extract car names from the following text:


txt = 'LMaasleitbtui'

txt [::2]
txt [1::2]



## 3. Extract Car Names
## Extract car names from the following text:

txt = 'MsaatmiazD'

txt[::2]




## 4. Extract Residence Area
## Extract the residence area from the following text:

txt = "I'am John. I am from London"

name = input('enter his name')
city = input('enter where does he from')
print(f" I'm {name}. I am from {city}")  


## 5. Reverse String
## Write a Python program that takes a user input string and prints it in reverse order.

txt = input('enter any text')
reversed_txt = txt[::-1]
print('Reversed text', reversed_txt)




## 6. Count Vowels
## Write a Python program that counts the number of vowels in a given string.

txt = input('enter a string')
vowels = 'aeiouAEIOU'
count = 0
for char in txt:
    if char in vowels:
        count += 1
print('number of vowels', count) 




## 7. Find Maximum Value
## Write a Python program that takes a list of numbers as input and prints the maximum value.

number_list = int(input('enter number'))
number_list2 = int(input('enter number'))

txt = f'The product of {number_list} and {number_list2} is equal {number_list * number_list2}'
txt 
 




## 8. Check Palindrome
## Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).


word = input("Enter a word: ")

if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")



## 9. Extract Email Domain
## Write a Python program that extracts and prints the domain from an email address provided by the user.

email = input('enter email')
domain = email.split('@')[1]
print('email domain is', domain) 


## 10. Generate Random Password
## Write a Python program to generate a random password containing letters, digits, and special characters.

import random
letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*"
all_characters = letters + letters.upper() + digits + symbols
length = int(input("Enter password length: "))
password = ""
for i in range(length):
    password += random.choice(all_characters)
print("Your password is:", password)







