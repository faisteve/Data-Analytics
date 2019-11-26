#!/usr/bin/env python
# coding: utf-8

# # Titanic: Data Preparation and Analysis

# - In this homework assignment, you will practice data loading, preparation, transformation and analysis.
# - Follow each *TODO* instruction to write a Python code snippet with pandas. 
# - After you finish coding and debugging, click the `Cell` tab, select `Run All`, and then save the notebook that includes the output of each code cell.

# In[4]:


import pandas as pd
from pandas import Series, DataFrame


# **TODO 1**
# Load data from files `train.csv` and `test.csv` into two DataFrames `train` and `test`, respectively. Display the first six rows of the two DataFrames, respectively.

# In[34]:


#####TODO 1#####
pass
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print(train.head(6))
test.head(6)


# **TODO 2**
# Find the number of columns in the `train` and `test` DataFrames, respectively. 

# In[35]:


#####TODO 2#####
pass
print(train.shape[1])
test.shape[1]


# **TODO 3** 
# Show the names of all columns in the `train` DataFrame with an `object` data type.

# In[36]:


#####TODO 3#####
pass
train.columns[train.dtypes == 'object']


# **TODO 4**
# Show the names of all columns in the `train` DataFrame with missing values.

# In[37]:


#####TODO 4#####
pass
train.columns[train.isnull().any()]


# **TODO 5**
# Find the ticket class with the highest number of passengers in the `train` DataFrame.

# In[40]:


#####TODO 5#####
pass
train.groupby('Pclass').Survived.mean().sort_values().index[-1]


# **TODO 6**
# Find the ticket class with the highest survival rate in the `train` DataFrame.
# 
# *Hint*: use `train.groupby()`.

# In[13]:


#####TODO 6#####
pass
train[['Pclass', 'Survived']].groupby(['Pclass']).mean().idxmax()


# **TODO 7**
# Column `Embarked`stores the port of embarkation for each passenger. Find the number of missing values in this column of both DataFrames separately. Then fill in any missing value in this column with the port of the highest frequency in the `train` DataFrame. Finally, re-calculate the number of missing values in this column to verify your operations.

# In[41]:


#####TODO 7#####
pass
print(train.Embarked.isnull().sum())
print(test.Embarked.isnull().sum())
train.Embarked = train.Embarked.fillna(train.Embarked.value_counts().index[0])
print(train.Embarked.isnull().sum())
print(test.Embarked.isnull().sum())


# **TODO 8** Output the number of rows in the `train` DataFrame with field `Embarked` equal to 'S'.

# In[22]:


#####TODO 8#####
pass
train.Embarked.value_counts().S


# **TODO 9** Column `Fare` stores the  the tickt fare each passenger paid. Find the number of missing values in this column of both DataFrames separately. If a DataFrame has missing values in this column, then fill in any missing value with the mean ticket fare of the same ticket class in the `train` DataFrame. Finally, re-calculate the number of missing values in this column to verify your operations.

# In[42]:


#####TODO 9#####
pass
print(train.Fare.isnull().sum())
print(test.Fare.isnull().sum())
if test.Fare.isnull().any():
    pclass = test.Pclass[test.Fare.isnull()].values[0]
    test.Fare = test.Fare.fillna(train[train.Pclass == pclass].Fare.mean())
print(train.Fare.isnull().sum())
print(test.Fare.isnull().sum())


# **TODO 10** 
# Output the ticket fare of the passenger in the `test` DataFrame with field `PassengerId` equal to 1044.   

# In[43]:


#####TODO 10#####
pass
test[test.PassengerId == 1044].Fare


# **TODO 11**
# Compute the survival rate under each distinct level of field `Parch` in the `train` DataFrame.

# In[25]:


#####TODO 11#####
pass
train[['Parch', 'Survived']].groupby(['Parch']).mean()


# **TODO 12**
# Convert the data in column 'Sex' to 1 for 'male' and 0 for 'female' in both DataFrames. Then find the number of zeros in this column of the `train` DataFrame.

# In[26]:


####TODO 12####
pass
train.Sex.replace({'male' : 1, 'female' : 0}, inplace = True)
test.Sex.replace({'male' : 1, 'female' : 0}, inplace = True)
sum(train.Sex == 0)


# **TODO 13** 
# Fill in the missing values in column `Age` with the mean age in the `train` DataFrame. Then compute the mean age in the `test` DataFrame.

# In[46]:


#####TODO 13#####
pass
test.Age = test.Age.fillna(train.Age.mean())
train.Age = test.Age.fillna(train.Age.mean())


# **TODO 14** Add a column `IsChild` to both DataFrames. Assign 1 to this column if a passenger's age is below 16 years old, or 0 otherwise. Then compute the column total. 
# 
# *Hint*: use `DataFrame.apply()`. You may define a function.

# In[44]:


#####TODO 14#####
pass
def comp(x, y):
    if x < y:
        return 1
    return 0
train['IsChild'] = train.Age.apply(comp, args = (16,))
print(train.IsChild.sum())
test['IsChild'] = test.Age.apply(comp, args = (16,))
print(test.IsChild.sum())


# **TODO 15** 
# Compute the survival rates of children and adults in the `train` DataFrame.

# In[45]:


#####TODO 15#####
pass
print(train.groupby('IsChild').Survived.mean())


# In[ ]:




