## Homework 13 
# 1.Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.


from datetime import datetime

birth_input = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.strptime(birth_input, "%Y-%m-%d")
today = datetime.today()

years = today.year - birthdate.year
months = today.month - birthdate.month
days = today.day - birthdate.day

if days < 0:
    months -= 1
    days += 30 

if months < 0:
    years -= 1
    months += 12

print(f"You are {years} years, {months} months, and {days} days old.")

# 2.Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import datetime

birth_input = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birth_input, "%Y-%m-%d")
today = datetime.today()

next_birthday = birthdate.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days

print(f"There are {days_left} days left until your next birthday!")

# 3. Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

current_input = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
current_datetime = datetime.strptime(current_input, "%Y-%m-%d %H:%M")

hours = int(input("Enter the meeting duration (hours): "))
minutes = int(input("Enter the meeting duration (minutes): "))

duration = timedelta(hours=hours, minutes=minutes)

end_time = current_datetime + duration

print("The meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))

# 4.Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
import pytz

input_datetime = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
from_timezone = input("Enter your current timezone (e.g. Asia/Tashkent): ")
to_timezone = input("Enter the timezone you want to convert to (e.g. US/Eastern): ")


naive_dt = datetime.strptime(input_datetime, "%Y-%m-%d %H:%M")


from_tz = pytz.timezone(from_timezone)
localized_dt = from_tz.localize(naive_dt)


to_tz = pytz.timezone(to_timezone)
converted_dt = localized_dt.astimezone(to_tz)


print("Converted date and time:", converted_dt.strftime("%Y-%m-%d %H:%M %Z%z"))

# 5.Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

target_input = input("Enter the future date and time (YYYY-MM-DD HH:MM:SS): ")
target_time = datetime.strptime(target_input, "%Y-%m-%d %H:%M:%S")

while True:
    now = datetime.now()
    remaining = target_time - now

    if remaining.total_seconds() <= 0:
        print("⏰ Time's up!")
        break

    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    
    print(f"\rTime remaining: {days}d {hours}h {minutes}m {seconds}s", end="")

    time.sleep(1)  

# 6.Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

email = input("Enter your email address: ")


if re.match(pattern, email):
    print(" This is a valid email address.")
else:
    print(" Invalid email format.")

# 7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

phone = input("Enter a 10-digit phone number: ")


phone = ''.join(filter(str.isdigit, phone))

if len(phone) == 10:
    formatted = f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"
    print("Formatted phone number:", formatted)
else:
    print(" Please enter exactly 10 digits.")

# 8.Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

# Ask user to input a password
password = input("Enter a password: ")

# Initialize a list to collect error messages
errors = []

# Check password length
if len(password) < 8:
    errors.append(" Password must be at least 8 characters long.")

# Check for lowercase letter
if not re.search(r"[a-z]", password):
    errors.append(" Password must contain at least one lowercase letter.")

# Check for uppercase letter
if not re.search(r"[A-Z]", password):
    errors.append(" Password must contain at least one uppercase letter.")

# Check for a digit
if not re.search(r"[0-9]", password):
    errors.append(" Password must contain at least one digit.")

# Show results
if errors:
    print("Password is **weak**. Please fix the following:")
    for error in errors:
        print(error)
else:
    print(" Password is strong!")

# 9.Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.


sample_text = """
Python is a powerful programming language. Python is popular for data science, web development, automation, and more.
Learning Python is fun and useful. Many developers enjoy coding in Python.
"""


search_word = input("Enter the word you want to find: ").lower()


words = sample_text.lower().split()


matches = [word for word in words if word.strip(".,") == search_word]


if matches:
    print(f"\n The word '{search_word}' was found {len(matches)} times:")
    for i, word in enumerate(matches, 1):
        print(f"{i}. {word}")
else:
    print(f"\n The word '{search_word}' was not found in the text.")



# 10.Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re


text = input("Enter some text that may contain dates: ")


date_pattern = r'\b(?:\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b'


dates = re.findall(date_pattern, text)


if dates:
    print("\n Dates found in the text:")
    for date in dates:
        print("-", date)
else:
    print("\n No dates found in the text.")
