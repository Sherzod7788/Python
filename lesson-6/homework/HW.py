## Homework Lesson 6
## 1. Modify String with Underscores
# Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an
# underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

# Examples
# Input: hello Output: hel_lo
# Input: assalom Output: ass_alom
# Input: abcabcabcdeabcdefabcdefg Output: abc_abc_abcd_abcd_abcdef


def insert_underscores(txt):
    vowels = 'aeiouAEIOU'
    result = ''
    i = 0

    while i < len(txt):
        # Get the next 3 characters
        group = txt[i:i+3]
        result += group

        # If group is less than 3 or end of text, stop
        if len(group) < 3 or i + len(group) >= len(txt):
            break

        next_char = txt[i + 3] if i + 3 < len(txt) else ''
        
        # If 3rd char is vowel or next char is underscore → shift
        if group[-1] in vowels or next_char == '_':
            if i + 3 < len(txt) - 1:
                result += txt[i + 3]
                result += '_'
                i += 4  # move past group + shifted char
            else:
                i += 3
        else:
            result += '_'
            i += 3

    return result.rstrip('_')  # Remove underscore at end if added


txt = "abcabcabcdeabcdefabcdefg"
print(insert_underscores(txt))

# 2. Integer Squares Exercise
# Task
# The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

n = int(input())  

for i in range(n):  
    print(i ** 2)   
## 3. Loop-Based Exercises
## Exercise 1: Print first 10 natural numbers using a while loop

i = 1 
while i <= 10:
    print(i)
    i += 1
# Exercise 2: Print the following pattern: 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
# Exercise 3: Calculate sum of all numbers from 1 to a given number
#Example:
# Enter number 10
# Sum is: 55

n = 10 
total = 0

for i in range(1, n + 1):
    total += i

print('Sum is:', total)
# Exercise 4: Print multiplication table of a given number
# Example:

number = int(input('Enter a number: '))


for i in range(1, 11):
    print(number* i)

# Exercise 5: Display numbers from a list using a loop
# Given: 
 
numbers = [12, 75, 150, 180, 145, 525, 50]

for numbers in numbers:
    if numbers >= 75 and numbers <= 150:
        print(numbers)


# Exercise 6: Count the total number of digits in a number
# Example: 75869 Output: 5

number = int(input("Enter a number: "))
digit_count = len(str(abs(number)))  
print("Total digits:", digit_count)

# Exercise 7: Print reverse number pattern 

for i in range(5, 0, -1):           
    for j in range(i, 0, -1):      
        print(j, end=' ')
    print()  

# Exercise 8: Print list in reverse order using a loop
# Given: list1 = [10, 20, 30, 40, 50]

list1 = [10, 20, 30, 40, 50]

for item in reversed(list1):
    print(item)

# Exercise 9: Display numbers from -10 to -1 using a for loop

num = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]

for item in reversed(num):
    print(item)
# Exercise 10: Display message “Done” after successful loop execution

if i in range(5):
    print(i)
print('Done!')
# Exercise 11: Print all prime numbers within a range

start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  
        for i in range(2, int(num ** 0.5) + 1): 
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12: Display Fibonacci series up to 10 terms

n = 10
a, b = 0, 1

print("Fibonacci sequence:")

for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b  

# Exercise 13: Find the factorial of a given number

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "is", factorial)

# 4. Return Uncommon Elements of Lists
# Task
# Return the elements that are not common between two lists. The order of elements does not matter.



from collections import Counter

def uncommon_elements(list1, list2):
    # Count frequency of elements in both lists
    c1 = Counter(list1)
    c2 = Counter(list2)

    result = []

    # Elements from list1 that are not in list2 or appear more times
    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
        elif c1[elem] > c2[elem]:
            result.extend([elem] * (c1[elem] - c2[elem]))

    # Elements from list2 that are not in list1 or appear more times
    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
        elif c2[elem] > c1[elem]:
            result.extend([elem] * (c2[elem] - c1[elem]))

    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))      

print(uncommon_elements([1, 2, 3], [4, 5, 6]))      

print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  







