## Homework 5

## 1 def is_leap(year): """ Determines whether a given year is a leap year.

def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
        year (int): The year to be checked.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True

## 2. Conditional Statements Exercise

n = int(input())

if n % 2 == 1:
    print ("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print ("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    peint("Not Weird") 


## 3.Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.

a = 3
b = 10

# Ensure a is even (if not, add 1)
if a % 2 != 0:
    a += 1

even_numbers = list(range(a, b + 1, 2))
print(even_numbers)
