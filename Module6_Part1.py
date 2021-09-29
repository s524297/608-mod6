#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1. - read in the Titanic Disaster dataset

import pandas as pd

titanic = pd.read_csv('https://vincentarelbundock.github.io/' +
        'Rdatasets/csv/carData/TitanicSurvival.csv')
   


# In[3]:


# 2. - Set the precision to 2 decimal places 

pd.set_option('precision', 2) # format for float's 


# In[4]:


# 3. View the head and tail of the file

titanic.head()


# In[5]:


titanic.tail()


# In[6]:


# 4. - customize the column headings 

titanic.columns = ['name', 'survived', 'sex', 'age', 'class']


# In[7]:


titanic.head()


# In[8]:


# 5. - use describe function to calculate basic descriptive statistics 

titanic.describe()


# In[9]:


# 6. - describe statistics for those who survived 

(titanic.survived == 'yes').describe()


# In[10]:


# 8. - enable matplotlib

get_ipython().run_line_magic('matplotlib', '')


# In[11]:


# 9. - showing histogram 

histogram = titanic.hist()


# In[ ]:




