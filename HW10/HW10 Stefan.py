#!/usr/bin/env python
# coding: utf-8

# # pandas Basics

# - In this homework assignment, you will practice selecting, sorting, and aggregating data in a DataFrame. 
# - Follow each *TODO* instruction to write a Python code snippet with pandas and Numpy. Include the output of each code cell.

# In[2]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame


# **TODO 1**
# Consider the following Python dictionary `adict`. 
# 
# ```python
# adict = {'state': ['New York', 'California', 'Maryland'], 
#          'pop2010': [19378, 37254, 5774],
#          'pop2018': [19542, 39557, 6043],
#          'rev2010': [71545, 112372, 17064],
#          'rev2018': [88541, 175017, 22427]}
# ```
# 
# Notation:
# 
# - `pop2010`: state's 2010 population (in thousand)
# - `pop2018`: state's 2018 population (in thousand)
# - `rev2010`: state's 2010 tax revenue (in million USD)
# - `rev2018`: state's 2018 tax revenue (in million USD)
# 
# Construct a DataFrame `frame` from dictionary `adict`. The row label (index) of each state is its abbreviation, i.e., `NY`, `CA` or `MD`. 

# In[3]:


#####TODO 1#####
pass
adict = {'state': ['New York', 'California', 'Maryland'], 
         'pop2010': [19378, 37254, 5774],
         'pop2018': [19542, 39557, 6043],
         'rev2010': [71545, 112372, 17064],
         'rev2018': [88541, 175017, 22427]}
states=["NY","CA","MD"]
frame = pd.DataFrame(adict,index=states)
frame


# **TODO 2**
# It is known that the areas of the three states are 54555, 163695 and 12406 square miles. Add a column `area` with appropriate data to DataFrame `frame`.

# In[4]:


#####TODO 2#####
pass
frame["area"] = [54555,163695,12406]
frame


# **TODO 3** 
# Select the first row and the last row of DataFrame `frame`.

# In[5]:


#####TODO 3#####
pass
frame[0:3:2]


# **TODO 4**
# Select just columns `state`, `pop2018` and `area` from DataFrame `frame`.

# In[6]:


#####TODO 4#####
pass

frame[['state','pop2018','area']]


# **TODO 5**
# Select the New York state's population data in 2010 and 2018.

# In[7]:


#####TODO 5#####
pass

frame.loc['NY',['pop2010','pop2018']]


# **TODO 6**
# Show the row labels of the second row and the third row.

# In[8]:


#####TODO 6#####
pass
frame.state[1:3]


# **TODO 7**
# Select just columns `state`, `rev2010` and `rev2018` of the second row and the third row from DataFrame `frame`.

# In[9]:


#####TODO 7#####
pass
frame.loc[['CA','MD'],['state','rev2010','rev2018']]


# **TODO 8** Select only the rows from DataFrame `frame` with an area greater than 50,000.

# In[ ]:


#####TODO 8#####
pass
frame.loc[frame.area > 50000]


# **TODO 9** 
# Add a column `popchange` to DataFrame `frame`. Assign the percentage change from 2010 to 2018 in each state's population to this new column.  

# In[10]:


#####TODO 9#####
pass
frame['popchange'] = frame.pop2018/frame.pop2010
frame


# **TODO 10** 
# Sort DataFrame `frame` by the index. 

# In[11]:


#####TODO 10#####
pass
frame.sort_values(by='state')


# **TODO 11**
# Sort DataFrame `frame` by the 2018 population in descending order.

# In[12]:


#####TODO 11#####
pass
frame.sort_values(by='pop2018',ascending=False)


# **TODO 12**
# Compute the total tax revenue across the three states in DataFrame `frame`.

# In[13]:


####TODO 12####
pass
sum(frame['rev2010']+frame['rev2018'])


# **TODO 13** In how many states did the tax reveue increase by at least 30%? 

# In[21]:


#####TODO 13#####
pass
frame.loc[(frame.rev2018/frame.rev2010) > 1.3]


# **TODO 14** 
# Return the index of the row with the highest `popchange` value. 

# In[20]:


#####TODO 14#####
pass
frame[['popchange']].idxmax()


# **TODO 15**
# Replace Maryland's `popchange` value by `np.NaN`. Then count the number of rows in the DataFrame with one or more missing values.
# 
# Hint: use methods `isnull()` and `any(axis = 1)`.

# In[17]:


#####TODO 15#####
pass

frame.loc['MD',['popchange']] = np.NaN
frame
frame.isnull().any(axis=1)


# In[ ]:




