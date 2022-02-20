#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[38]:


train_df=pd.read_excel(r"C:\Users\Aatif\Downloads\Data_Train.xlsx")
train_df.head()


# In[39]:


test_df=pd.read_excel(r"C:\Users\Aatif\Downloads\Test_set.xlsx")
test_df.head()


# In[40]:


df= train_df.append(test_df)


# In[41]:


df.head()


# In[42]:


df.info()


# In[43]:


# Here we can see that the date time colum dtype is object we need to convert it into Integer.
# feature engineering
df['Date']=df['Date_of_Journey'].str.split('/').str[0]
df['month']=df['Date_of_Journey'].str.split('/').str[1]
df['year']=df['Date_of_Journey'].str.split('/').str[2]


# In[44]:


df.head()


# In[45]:


df['Date']=df['Date'].astype(int)
df['month']=df['month'].astype(int)
df['year']=df['year'].astype(int)


# In[46]:


df.info()


# In[47]:


df.drop('Date_of_Journey' , axis=1 , inplace=True)


# In[48]:


df.head()


# In[49]:


df['Arrival_Time']=df['Arrival_Time'].str.split(' ').str[0]


# In[50]:


df.isnull().sum()


# In[51]:


df['Arrival_Hour']=df['Arrival_Time'].str.split(':').str[0]
df['Arrival_min']=df['Arrival_Time'].str.split(':').str[1]


# In[52]:


df.head()


# In[53]:


df['Arrival_Hour']=df['Arrival_Hour'].astype(int)
df['Arrival_min']=df['Arrival_min'].astype(int)
df.drop('Arrival_Time' ,axis=1 , inplace = True)


# In[54]:


df.info()


# In[55]:


df['Dept_hour']=df['Dep_Time'].str.split(':').str[0]
df['Dept_min']=df['Dep_Time'].str.split(':').str[1]
df['Dept_hour']=df['Dept_hour'].astype(int)
df['Dept_min']=df['Dept_min'].astype(int)
df.drop('Dep_Time',axis=1,inplace=True)


# In[60]:


df['Total_Stops'].unique()


# In[61]:


df['Total_Stops']=df['Total_Stops'].map({'non-stop': 0 ,'1 stop':1 ,   '2 stops': 2 , '3 stops':  3  ,  '4 stops': 4 , 'nan' : 1 })


# In[ ]:


df.drop('Route' , axis=1 , inplace = True)


# In[66]:


df.head()


# In[69]:


df['duration_hour']=df['Duration'].str.split(' ').str[0].str.split('h').str[0]


# In[72]:


df[df['duration_hour']=='5m']


# In[73]:


df.drop(6474,axis=0,inplace=True)
df.drop(2660,axis=0,inplace=True)


# In[75]:


df['duration_hour']=df['duration_hour'].astype('int')


# In[76]:


df.drop('Duration',axis=1,inplace=True)


# In[77]:


df['Airline'].unique()


# In[78]:


from sklearn.preprocessing import LabelEncoder


# In[79]:


Lb=LabelEncoder()


# In[82]:


df['Airline']=Lb.fit_transform(df['Airline'])
df['Source']=Lb.fit_transform(df['Source'])
df['Destination']=Lb.fit_transform(df['Destination'])
df['Additional_Info']=Lb.fit_transform(df['Additional_Info'])


# In[83]:


df.head(2)


# In[84]:


from sklearn.preprocessing import OneHotEncoder


# In[85]:


Ohe=OneHotEncoder()


# In[ ]:


df['Airline']=Ohe.fit_transform(df['Airline'])
df['Source']=OheOhe.fit_transform(df['Source'])
df['Destination']=Ohe.fit_transform(df['Destination'])
df['Additional_Info']=Ohe.fit_transform(df['Additional_Info'])


# In[87]:


pd.get_dummies(df,columns=["Airline", "Source", "Destination" , 'Additional_Info'] ,drop_first = True)


# In[ ]:





# In[ ]:




