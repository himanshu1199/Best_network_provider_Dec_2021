#!/usr/bin/env python
# coding: utf-8

# # Who is the best network provider in Dec 2021
# ### ( parameters : speed more than average speed, strong signal strength, more 4G technology )

# ## Import required Libraries

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


# ## Load Dataset

# In[3]:


myspeed= pd.read_csv('December_MySpeed_2021.csv')


# ## Explore Dataset

# In[4]:


myspeed.head(10)


# In[5]:


myspeed.tail(10)


# In[6]:


myspeed.shape


# In[7]:


myspeed.columns


# In[8]:


myspeed.info()


# In[9]:


myspeed.isnull().sum()


# In[10]:


for i in myspeed.describe( include= object):
    print(i)
    print(myspeed[i].unique())
    print('.'*25)


# In[11]:


## value counts in signal strength column because of 'na' is in string type in this column

myspeed['signal_strength'].value_counts()


# ## Data Cleaning and Modification 

# In[12]:


''' Replace NaN value of lsa by Loc_na (location not available) because there are may NaN value 
and will not be good idea to drop them all as this column not required for our analysis '''

myspeed['lsa'].replace( to_replace= np.nan, value='Loc_na', inplace= True)


# In[13]:


## Replace 'na' with NaN in signal strength column 

myspeed['signal_strength'].replace(to_replace='na', value= np.nan, inplace=True)


# In[14]:


myspeed.head(10)


# In[15]:


## Remove null values from speed column

myspeed.dropna(inplace=True)


# In[16]:


## Change datatype of signal strength from object to float 

myspeed['signal_strength']= myspeed['signal_strength'].astype('float64')


# In[17]:


myspeed.dtypes


# In[18]:


myspeed.isnull().sum()


# In[19]:


myspeed.shape


# In[20]:


myspeed.head(10)


# ## Check for outliers 

# In[21]:


myspeed.describe()


# In[22]:


plt.figure(figsize=(6,6))
plt.boxplot(data=myspeed, x='speed')
plt.title('box plot of speed')


# In[23]:


## According to the Bharti Airtel expert 4G speed can go upto 100 mbps or 100000 kbps.
## Similarly according to wikipedia lowest speed of 3G is 144 kbps.
## So, anything outside this range will be outlier for us.

myspeed= myspeed[myspeed['speed']<100000]
myspeed= myspeed[myspeed['speed']>144]

myspeed


# ## Data Analysis and Visulaization 
# 

# In[24]:


myspeed.describe()


# In[25]:


## calculate average speed of network and plot a graph of operators who has network speed more than average.
avg_speed= round(myspeed['speed'].mean(),2)
print('Average speed', avg_speed)
print('-'*25)

plt.figure(figsize=(8,5))
sns.countplot(data=myspeed[myspeed['speed']>avg_speed], x='operator')
plt.title('Operators with more than average speed of network')


# ## Here JIO is clear winner in terms of network speed followed by Airtel

# In[26]:


## Average signal strength according to operators
mean_signal_strength= pd.DataFrame(round(myspeed.groupby(by= 'operator')[['signal_strength']].mean(), 2))
mean_signal_strength


# ## CELLONE give the best signal strength followed by JIO 

# In[27]:


## calculate percentage, operators with 4G technology
tech_4G = myspeed[myspeed['technology']== '4G']
print('percentage count of',round(tech_4G['operator'].value_counts(normalize=True),2))
print('-'*25)

plt.figure(figsize=(8,5))
sns.countplot(data=tech_4G, x='operator')
plt.title('Operator with 4G technology')


# ## JIO with highest 4G technology followed by Airtel

# # According to the given parameters JIO is clean winner, hence JIO is the best network provider in Dec 2021
