#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np # linear algebra
import pandas as pd # data processing
import seaborn as sns # Plots
import matplotlib.pyplot as plt # Plots


# In[2]:


pwd


# In[3]:


data = pd.read_csv(r'C:\Users\vanes\OneDrive\Dokumente\1. Semester\Data Science\Projekt\master.csv')


# In[4]:


display(data)


# In[5]:


data.shape 


# In[6]:


print(data.columns)


# In[7]:


a = data[' gdp_for_year ($) ']
a.info()


# In[8]:


dataclean = data.drop(columns = [' gdp_for_year ($) '])


# In[9]:


sns.heatmap(dataclean.isnull(),yticklabels=False, cbar = False, cmap = 'viridis')


# In[10]:


print(dataclean.isnull().sum())


# In[11]:


dataclean = dataclean.drop(columns = ['HDI for year'])


# In[12]:


dataclean.info()


# In[13]:


dataclean.describe()


# In[14]:


datanummeric = dataclean.select_dtypes(include=['number'])
corr = datanummeric.corr()
corr.style.background_gradient(cmap='coolwarm')


# In[15]:


print(dataclean.year.min())
print(dataclean.year.max())
print(type(dataclean.year.min()))


# In[16]:


np.unique(dataclean['age'])


# In[17]:


sum(dataclean.age == '15-24 years')


# In[55]:


print(dataclean(row = ['2']).age == '15-24 years')


# In[49]:


summe = 0
i = 0
for i in range (0, 31756, 1):
    if (dataclean[i].age == '15-24 years'):
        summe = summe + dataclean[i].suicides_no
print(summe)


# In[ ]:




