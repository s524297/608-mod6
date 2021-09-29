#!/usr/bin/env python
# coding: utf-8

# In[18]:


get_ipython().system('pip install ipython-sql')


# In[19]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[20]:


get_ipython().run_line_magic('sql', 'sqlite://')


# In[21]:


import sqlite3


# In[22]:


connection = sqlite3.connect('books.db')


# In[23]:


# 5. import pandas 

import pandas as pd


# In[24]:


# 6. - use pd optioins.display to set max_columns to 10 

pd.options.display.max_columns = 10 


# In[25]:


# 7. - use pd read_sql function to select everything from the authors table 

pd.read_sql('Select * From authors', connection, index_col=['id'])


# In[26]:


pd.options.display.max_columns = 10


# In[27]:


# 8. - execute the more specific select cammands section 17.2.3 

pd.read_sql("""SELECT title, edition, copyright 
                FROM titles
                WHERE copyright > '2016'""", connection)


# In[31]:


# 9. - execute the commands using the ORDER BY clause to get results back that are sorted in a useful way 

pd.read_sql("""SELECT id, first, last 
               From authors 
               ORDER BY last, first""", 
               connection, index_col=['id'])


# In[32]:


pd.read_sql("""SELECT id, first, last
                    FROM authors
                    ORDER BY last DESC, first ASC""",
                    connection, index_col=['id'])


# In[33]:


pd.read_sql("""SELECT isbn, title, edition, copyright
                    FROM titles
                    WHERE title LIKE '%How to Program'
                    ORDER BY title""", connection)


# In[ ]:




