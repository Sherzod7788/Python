## Homework 17
# 1.Rename column names using function. "First Name" --> "first_name", "Age" --> "age

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)
print(df)



import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})
print(df)
# 2.Print the first 3 rows of the DataFrame

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df.iloc[0:3])
# 3. Find the mean age of the individuals

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print('mean age:', df['Age'].mean())
# 4.Select and print only the 'Name' and 'City' columns

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)

print(df.iloc[:, [0,2]]) 

# 5.Add a new column 'Salary' with random salary values

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

df['Salary'] = [2000,5000,7000,9000] 
print(df) 

# 6.Display summary statistics of the DataFrame

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
         'Age': [25, 30, 35, 40], 
         'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}

print(df.describe())
# Homework 2:

# 1.Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.

import pandas as pd

sales_and_expenses = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
                      'Sales': [5000,6000,7500,8000],
                      'Expenses': [3000,3500,4000,4500]}
df = pd.DataFrame(sales_and_expenses)
print(df)

# 2.Calculate and display the maximum sales and expenses.

sales_and_expenses = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
                      'Sales': [5000,6000,7500,8000],
                      'Expenses': [3000,3500,4000,4500]}
max_sales = df['Sales'].max()
max_expenses = df['Expenses'].max()

print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)
# 3.Calculate and display the minimum sales and expenses.

sales_and_expenses = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
                      'Sales': [5000,6000,7500,8000],
                      'Expenses': [3000,3500,4000,4500]}
min_sales = df['Sales'].min()
min_expenses = df['Expenses'].min()

print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

# 4.Calculate and display the average sales and expenses.

sales_and_expenses = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
                      'Sales': [5000,6000,7500,8000],
                      'Expenses': [3000,3500,4000,4500]}
avg_sales = df['Sales'].mean()
avg_expenses = df['Expenses'].mean()

print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)
# Homework 3:
# 1.Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.

import pandas as pd 

expenses = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
            'January': [1200,1300,1400,1500],
            'February': [200,220,240,250],
            'March': [300,320,330,350],
            'April': [150,160,170,180]}
df = pd.DataFrame(expenses)
print(df)
            
# 2.Calculate and display the maximum expense for each category.

expenses = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
            'January': [1200,1300,1400,1500],
            'February': [200,220,240,250],
            'March': [300,320,330,350],
            'April': [150,160,170,180]}

df = pd.DataFrame(expenses) 

df.set_index('Category', inplace=True)

max_rent = df.loc['Rent'].max()
max_utilities = df.loc['Utilities'].max()
max_groceries = df.loc['Groceries'].max()
max_entertainment = df.loc['Entertainment'].max()

print("Maximum Rent:", max_rent)
print("Maximum Utilities:", max_utilities)
print("Maximum Groceries:", max_groceries)
print("Maximum Entertainment:", max_entertainment)

# 3. Calculate and display the minimum expense for each category.

expenses = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
            'January': [1200,1300,1400,1500],
            'February': [200,220,240,250],
            'March': [300,320,330,350],
            'April': [150,160,170,180]}

df = pd.DataFrame(expenses) 

df.set_index('Category', inplace=True)

min_rent = df.loc['Rent'].min()
min_utilities = df.loc['Utilities'].min()
min_groceries = df.loc['Groceries'].min()
min_entertainment = df.loc['Entertainment'].min()

print("Minimum Rent:", min_rent)
print("Minimum Utilities:", min_utilities)
print("Minimum Groceries:", min_groceries)
print("Minimum Entertainment:", min_entertainment)
# 4.Calculate and display the average expense for each category.

expenses = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
            'January': [1200,1300,1400,1500],
            'February': [200,220,240,250],
            'March': [300,320,330,350],
            'April': [150,160,170,180]}

df = pd.DataFrame(expenses) 

df.set_index('Category', inplace=True)

avg_expenses = df.mean(axis=1)

print("Average Rent:", avg_expenses['Rent'])
print("Average Utilities:", avg_expenses['Utilities'])
print("Average Groceries:", avg_expenses['Groceries'])
print("Average Entertainment:", avg_expenses['Entertainment'])
