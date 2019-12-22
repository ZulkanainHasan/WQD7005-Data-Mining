#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[2]:


import numpy as np
import pandas as pd
import pandas_datareader.data as web


# In[3]:


start = '2019-06-01'
end = '2019-09-25'


# In[4]:


stocks_query = pd.read_csv('klse-main-market-stocks-rhbtradesmart-topvolume-code.csv', index_col=[0])


# In[5]:


stocks = web.DataReader(stocks_query, data_source='yahoo')


# In[6]:


stocks.head()


# In[7]:


stocks.tail()


# In[8]:


type(stocks)


# In[9]:


stocks.info()


# In[20]:


stocks.to_csv('klse-main-market-stock-rhbtradesmart-topvolume-data.csv')

