## Homework 4
Python Dictionary and Set Exercises



## 1. Sort a Dictionary by Value
## Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict = {'c': 3, 'a': 1, 'b': 2}


ascending = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", ascending)

descending = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", descending)


## 2. Add a Key to a Dictionary
## Write a Python script to add a key to a dictionary.
my_dict1 = {0: 10, 1: 20}

my_dict1[2] = 30
my_dict1


## 3. Concatenate Multiple Dictionaries
## Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged = dic1 | dic2 | dic3
print(merged)



## 4. Generate a Dictionary with Squares
## Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n= int(input('Enter a number'))

squares_dict = {x: x*x for x in range(1, n+1)}
print(squares_dict)


## 5. Dictionary of Squares (1 to 15)
## Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) 
# and the values are the square of the keys.
p = int(input('Enter a number'))

squares_dict = {x: x*x for x in range(1, p+1)}
print(squares_dict)


## Set exercises
## 1. Create a Set
## Write a Python program to create a set.
set_1 = {1, 2, 3, 4, 5}
set_1



## 2. Iterate Over a Set
## Write a Python program to iterate over sets.
my_set = {'Mercedes', 'BMW', 'Audi'}

for item in my_set:
    print(item)


## 3. Add Member(s) to a Set
## Write a Python program to add member(s) to a set.
my_set = {'Mercedes', 'BMW', 'Audi'}
my_set.add('Volvo')
my_set

## 4. Remove Item(s) from a Set
## Write a Python program to remove item(s) from a given set.
my_set = {'Mercedes', 'BMW', 'Audi', 'Volvo'}
my_set.remove('BMW')
my_set 


## 5. Remove an Item if Present in the Set
## Write a Python program to remove an item from a set if it is present in the set.
my_set = {'Mercedes', 'BMW', 'Audi', 'Volvo'}
my_set.discard('BMW')
my_set 
