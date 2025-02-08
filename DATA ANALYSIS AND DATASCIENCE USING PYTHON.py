#!/usr/bin/env python
# coding: utf-8

# # A. Data Loading

# Load the dataset using **pandas**

# In[1]:


import pandas as pd


# In[12]:


df = pd.read_csv("student-mat.csv", delimiter=";")


# Display the first few rows using .head().

# In[22]:


df.head()


# # B. Data Exploration

# In[23]:


df.columns


# In[24]:


df.describe()


# In[28]:


df.shape


# In[25]:


df.isnull().sum()


# # C. Data Cleaning

# In[20]:


df['sex'].unique()


# In[21]:


df['school'].unique()


# In[26]:


df.dtypes


# In[28]:


df.shape


# In[29]:


df.drop_duplicates()


# # D. Data Analysis Questions

# ### 1. What is the average score in math (G3)?

# In[36]:


round(df['G3'].mean(),2)


# Avg of score in Math G3 is 10.42

# ### 2. How many students scored above 15 in their final grade (G3)?

# In[56]:


df[df['G3'] > 15].shape[0]


# In[57]:


df[df['G3'] > 15]['G3'].count()


# ### 3.  Is there a correlation btw study time (study time) and the final grade (G3)?

# In[58]:


correlation = df['studytime'].corr(df['G3'])
print(correlation)


# Interpretation:
# - If correlation > 0, there is a positive relationship (more study time leads to higher grades).
# - If correlation < 0, there is a negative relationship (more study time leads to lower grades).
# - If correlation ≈ 0, there is no strong relationship between study time and final grades.
# 
# Our answer is >0, So positive correlation

# In[61]:


import matplotlib.pyplot as plt

plt.scatter(df['studytime'], df['G3'])
plt.xlabel('Study_Time')
plt.ylabel('Final Grade (G3)')
plt.title('Study Time vs Final Grade')
plt.show()


# ### 4.  Which gender has a higher average final grade (G3) ?

# In[64]:


df.groupby('sex')['G3'].mean()


# From the results, **males (M)** have a higher average final grade (`G3`) than **females (F)`**:  
# 
# - **Females (F):** 9.97  
# - **Males (M):** 10.91  
# 
# This means, on average, male students scored higher in their final grade (`G3`) compared to female students.

# # E. Data Visualization

# In[67]:


import matplotlib.pyplot as plt

plt.hist(df['G3'], bins=10, edgecolor='black')
plt.xlabel('Final Grade (G3)')
plt.ylabel('Number of Students')
plt.title('Distribution of Final Grades (G3)')
plt.show()


# ### 2. Scatter plot between study time (study time) and final grade (G3)

# In[69]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(x='studytime', y='G3', data=df, color='blue')
plt.xlabel('Study Time')
plt.ylabel('Final Grade (G3)')
plt.title('Scatter Plot: Study Time vs Final Grade')
plt.show()


# ### 3. Bar chart comparing the average scores of male and female students

# In[70]:


import seaborn as sns
import matplotlib.pyplot as plt

avg_scores = df.groupby('sex')['G3'].mean().reset_index()
sns.barplot(x='sex', y='G3', data=avg_scores, palette='Set2')
plt.xlabel('Gender')
plt.ylabel('Average Final Grade (G3)')
plt.title('Average Final Grades by Gender')
plt.show()


# In[ ]:




