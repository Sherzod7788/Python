## Homework 19 
# Homework Assignment 1: Analyzing Sales Data

You are given a dataset containing sales data for an e-commerce website. The dataset (task\sales_data.csv) has the following columns:

Date: Date of the sale.
Product: Name of the product sold.
Category: Category to which the product belongs.
Quantity: Number of units sold.
Price: Price per unit.
# 1.Group the data by the Category column and calculate the following aggregate statistics for each category:
# Total quantity sold.
# Average price per unit.
# Maximum quantity sold in a single transaction.

import pandas as pd 

sales = pd.read_csv('sales_data.csv')
sales.head(10)
sales.groupby("Category").agg({"Quantity": ["sum", "max"], "Price": "mean"}) 
sales.groupby("Date").agg(
    highest_total_sale=("Quantity", "sum"),
    highest_total_sale=("Price", "max") )

sales.groupby("Category").agg(
    total_quantity_sold=("Quantity", "sum"),
    max_quantity_sold=("Quantity", "max"),
    avg_price_per_unit=("Price", "mean")
)

# 2.Identify the top-selling product in each category based on the total quantity sold.

grouped = sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()

top_selling = grouped.loc[grouped.groupby('Category')['Quantity'].idxmax()]
print(grouped)
print(top_selling) 
# 3.Find the date on which the highest total sales (quantity * price) occurred.

sales['TotalSale'] = sales['Quantity'] * sales['Price']

daily_sales = sales.groupby('Date')['TotalSale'].sum().reset_index()

max_sales_date = daily_sales.loc[daily_sales['TotalSale'].idxmax()]

max_sales_date
# Homework Assignment 2: Examining Customer Orders

You have a dataset (task\customer_orders.csv) containing information about customer orders. The dataset has the following columns:

OrderID: Unique identifier for each order.
CustomerID: Unique identifier for each customer.
Product: Name of the product ordered.
Quantity: Number of units ordered.
Price: Price per unit.
# 1.Group the data by CustomerID and filter out customers who have made less than 20 orders.

import pandas as pd 

customer = pd.read_csv('customer_orders.csv') 
customer 
sales = customer.groupby("CustomerID").filter(lambda x: len(x) >= 20)  
sales 
# 2.Identify customers who have ordered products with an average price per unit greater than $120.

avg_price = customer.groupby(['CustomerID', 'Product'])['Price'].mean().reset_index()

high_value_orders = avg_price[avg_price['Price'] > 120]

customers = high_value_orders['CustomerID'].unique()
high_value_orders

# 3.Find the total quantity and total price for each product ordered, and filter out products that have a total quantity less than 5 units.

product_totals = customer.groupby("Product")[["Quantity", "Price"]].sum()

filtered_products = product_totals[product_totals["Quantity"] >= 5]
filtered_products

# Homework Assignment 3: Population Salary Analysis
# 1."task\population.db" sqlite database has population table.

import sqlite3
import pandas as pd 
conn = sqlite3.connect("task/population.db")  # use forward slash or raw string for Windows

# 2. "task\population salary analysis.xlsx" file defines Salary Band categories.
# Read the data from population table and calculate following measures:
# Percentage of population for each salary category;
# Average salary in each salary category;
# Median salary in each salary category;
# Number of population in each salary category;

population = pd.read_excel('population_salary_analysis.xlsx')
population.head(7)

import pandas as pd
import sqlite3
import numpy as np

# 1. Load salary band ranges from Excel
salary_bands = pd.read_excel("task/population salary analysis.xlsx")

# 2. Connect to the SQLite database and read the population table
conn = sqlite3.connect("task/population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

def extract_min_max(val):
    val = val.replace('$', '').replace(',', '').lower()
    if 'till' in val:
        return pd.Series([0, int(val.split()[-1])])
    elif 'over' in val:
        return pd.Series([int(val.split()[0]), np.inf])
    else:
        parts = val.split('-')
        return pd.Series([int(parts[0].strip()), int(parts[1].strip())])

salary_bands[['Min', 'Max']] = salary_bands['Salary Band'].apply(extract_min_max)


def assign_band(salary):
    for i, row in salary_bands.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Salary Band']
    return None

population_df['Salary Band'] = population_df['salary'].apply(assign_band)


# Group by assigned salary band
result = population_df.groupby('Salary Band')['salary'].agg(
    Number_of_population='count',
    Average_Salary='mean',
    Median_Salary='median'
).reset_index()

# Calculate total population for percentage
total_pop = result['Number_of_population'].sum()
result['Percentage'] = (result['Number_of_population'] / total_pop) * 100


final = salary_bands[['Salary Band']].merge(result, on='Salary Band', how='left')

print(final)

# Optional: Save to Excel
final.to_excel("output_salary_analysis.xlsx", index=False)


# 3.Calculate the same measures in each State

import pandas as pd
import sqlite3
import numpy as np

# Load salary band definitions
salary_bands = pd.read_excel("task/population salary analysis.xlsx")

# Connect to SQLite and load population table
conn = sqlite3.connect("task/population.db")
population_df = pd.read_sql_query("SELECT * FROM population", conn)
conn.close()

def extract_min_max(val):
    val = val.replace('$', '').replace(',', '').lower()
    if 'till' in val:
        return pd.Series([0, int(val.split()[-1])])
    elif 'over' in val:
        return pd.Series([int(val.split()[0]), np.inf])
    else:
        parts = val.split('-')
        return pd.Series([int(parts[0].strip()), int(parts[1].strip())])

salary_bands[['Min', 'Max']] = salary_bands['Salary Band'].apply(extract_min_max)


def assign_band(salary):
    for _, row in salary_bands.iterrows():
        if row['Min'] <= salary <= row['Max']:
            return row['Salary Band']
    return None

population_df['Salary Band'] = population_df['salary'].apply(assign_band)


# Group by both State and Salary Band
grouped = population_df.groupby(['state', 'Salary Band'])['salary'].agg(
    Number_of_population='count',
    Average_Salary='mean',
    Median_Salary='median'
).reset_index()


# Total population per state
state_totals = grouped.groupby('state')['Number_of_population'].sum().reset_index()
state_totals.columns = ['state', 'Total']

# Merge to get totals into main table
grouped = grouped.merge(state_totals, on='state')
grouped['Percentage'] = (grouped['Number_of_population'] / grouped['Total']) * 100

# Drop helper column
grouped.drop(columns='Total', inplace=True)


# Sort for readability
grouped = grouped.sort_values(['state', 'Salary Band'])

# View results
print(grouped)

# Optional: Save to Excel
grouped.to_excel("statewise_salary_analysis.xlsx", index=False)
