## Lesson 18
Homework 2 
# 1.Find all questions that were created before 2014

import pandas as pd 

df = pd.read_csv("tackoverflow_qa.csv", parse_dates=["creationdate"])

questions_before_2014 = df[df["creationdate"] < "2014-01-01"]

print(questions_before_2014)

## 2.Find all questions with a score more than 50

import pandas as pd 


df = pd.read_csv('tackoverflow_qa.csv')

filt1 = df['score'] > 50 
filtered_df = df[filt1]

print(filtered_df)


# 3.Find all questions with a score between 50 and 100

df = pd.read_csv('tackoverflow_qa.csv')

filt1 = df['score'].between (50, 100)  
filtered_df = df[filt1]

print(filtered_df)
# 4. Find all questions answered by Scott Boston

df = pd.read_csv('tackoverflow_qa.csv')

filt1 = df['ans_name'] == "Scott Boston" 
filtered_df = df[filt1]

print(filtered_df)


# 5.Find all questions answered by the following 5 users

df = pd.read_csv("tackoverflow_qa.csv")

target_users = ["Scott Boston", "Joe", "Anurag Dabas", "jezrael", "coldspeed"]

filtered_df = df[df['ans_name'].isin(target_users)]

filtered_df
# 6. Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.

df = pd.read_csv("tackoverflow_qa.csv")

df['creationdate'] = pd.to_datetime(df['creationdate'])


filt1 = df["creationdate"].between("2014-03-01", "2014-10-31")
filt2 = df["ans_name"] == "Unutbu"
filt3 = df["score"] < 5

final_filter = filt1 & filt2 & filt3

result = df[final_filter]
print(result)
# 7.Find all questions that have score between 5 and 10 or have a view count of greater than 10,000

df = pd.read_csv("tackoverflow_qa.csv")

filt1 = df["score"].between (5, 10)
filt2 = df["viewcount"] > 10000
final_filter = filt1 | filt2

result = df[final_filter]

print(result)

# 8.Find all questions that are not answered by Scott Boston

df = pd.read_csv("tackoverflow_qa.csv")

filt1 = df["ans_name"] != "Scott Boston"

filtered_df = df[filt1]

print(filtered_df)
df = pd.read_csv('tackoverflow_qa.csv')
df.head()
Homework 3
# 1.Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.

import pandas as pd 
import numpy as np

df = pd.read_csv('titanic.csv') 

filt1 = df["Sex"] == "female"
filt2 = df["Pclass"] == 1
filt3 = df["Age"].between (20, 30) 
final_filt = filt1 & filt2 & filt3 

res = df[final_filt]
print(res)


# 2.Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.

df = pd.read_csv('titanic.csv') 
 
filt = df["Fare"] > 100  

res = df[filt][["Name", "Pclass", "Fare"]] 

print(res)
# 3.Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).

import pandas as pd

df = pd.read_csv('titanic.csv')

filt1 = df["Survived"] == 1
filt2 = df["SibSp"] == 0
filt3 = df["Parch"] == 0
final_filter = filt1 & filt2 & filt3

res = df[final_filter]
res 

# 4.Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.

df = pd.read_csv('titanic.csv')

filt1 = df["Embarked"] == "C"
filt2 = df["Fare"] > 50
final_filter = filt1 & filt2 

res = df[final_filter] 
res 
# 5.Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.

df = pd.read_csv('titanic.csv')

filt1 = df['SibSp'] == 1
filt2 = df['Parch'] == 1
final_filter = filt1 & filt2 

res = df[final_filter] 
res 
# 6.Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.

df = pd.read_csv('titanic.csv')

filt1 = df['Age'] <= 15
filt2 = df['Survived'] == 0
final_filter = filt1 & filt2

res = df[final_filter]
res 
# 7.Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.

df = pd.read_csv('titanic.csv')

filt1 = df['Cabin'].notna()
filt2 = df['Fare'] > 200

final_filter = filt1 & filt2 

res = df[final_filter]
res 
# 8.Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.

df = pd.read_csv('titanic.csv')

filt = df['PassengerId'] % 2 == 1
odd_passangers = df[filt]
 
odd_passangers 
# 9.Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers. 

df = pd.read_csv('titanic.csv')

unique_tickets = df['Ticket'].unique()

print("Total unique tickets:", df['Ticket'].nunique())
print(unique_tickets)
# 10.Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.

df = pd.read_csv('titanic.csv')

filt1 = df['Sex'] == 'female'
filt2 = df['Name'].str.contains("Miss", case=False, na=False) 
filt3 = df['Pclass'] == 1
final_filter = filt1 & filt2 & filt3 

res = df[final_filter]
res 
