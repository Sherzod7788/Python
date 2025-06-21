## Homework 3


## 1. Create and Access List Elements
## Create a list containing five different fruits and print the third fruit.

fruits = ['apple', 'cherry', 'banana', 'coconut', 'mellon'] 
fruits[2] 


## 2. Concatenate Two Lists
## Create two lists of numbers and concatenate them into a single list.

l1=[1, 2, 3, 4]
l2=[5, 6, 7, 8]
l1.extend(l2)
l1


## 3. Extract Elements from a List
## Given a list of numbers, extract the first, middle, and last elements and store them in a new list.

numbers = [1, 2, 3, 4, 5]
first = numbers.pop(0) 
last = numbers.pop(-1) 
middle_index = len(numbers) // 2
middle = numbers.pop(middle_index) 

result = []
result.append(first)
result.append(middle)
result.append(last)

print("Extracted elements:", result)



## 4. Convert List to Tuple
## Create a list of your five favorite movies and convert it into a tuple.

movie = ['Avangers', 'Terminator', 'Titanic', 'Wolf of wall street', 'Mechanic'] 
movie = tuple(movie) 

print(movie)
print(type(movie)) 


## 5. Check Element in a List
## Given a list of cities, check if "Paris" is in the list and print the result.

city = ['New York', 'London', 'Paris', 'Tokyo']
city[2]


## 6. Duplicate a List Without Using Loops
## Create a list of numbers and duplicate it without using loops.

original = [1, 2, 3, 4]
duplicate = original.copy()
print(duplicate)  # [1, 2, 3, 4]

## 7. Swap First and Last Elements of a List
## Given a list of numbers, swap the first and last elements.

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print('After swapping', numbers) 

## 8. Slice a Tuple
## Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
numbers 

print(numbers[3:7])


## 9. Count Occurrences in a List
## Create a list of colors and count how many times "blue" appears in the list.

color = ['black', 'white', 'blue', 'red', 'blue', 'yellow', 'blue']
color.count('blue')


## 10. Find the Index of an Element in a Tuple
## Given a tuple of animals, find the index of "lion".

animals = ('snake', 'tiger', 'lion', 'monkey', 'elephant')
animals.index('lion')


## 11. Merge Two Tuples
## Create two tuples of numbers and merge them into a single tuple.

num1 = (10, 20, 30, 40)
num2 = (50, 60, 70, 80, 90)

merged = num1 + num2

print(merged)


## 12. Find the Length of a List and Tuple
## Given a list and a tuple, find and print their lengths.

numlist = [1, 2, 3, 4, 5, 6, 7]
fruits = ('apple', 'strawberry', 'grape', 'banana')

print('length for list', len(numlist))
print('length for tuple', len(fruits)) 


## 13. Convert Tuple to List
## Create a tuple of five numbers and convert it into a list.

numtuple = (77, 88, 99, 55, 44)
numlist = list(numtuple)

print(numlist)
print(type(numlist))  


## 14. Find Maximum and Minimum in a Tuple
## Given a tuple of numbers, find and print the maximum and minimum values.

numbers = (12, 56, 83, 4, 97, 36)

maximum = max(numbers) 
minimum = min(numbers) 

print('Maximum valued number', maximum)
print('Minimum valued number', minimum) 


## 15. Reverse a Tuple
## Create a tuple of words and print it in reverse order.

words = ('technology', 'probability', 'possibility', 'ability')

reversedwords = words [::-1]

print('true tuple', words)
print('reversed tuple', reversedwords)
