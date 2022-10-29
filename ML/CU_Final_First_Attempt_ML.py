#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from google.colab import files
import io
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

from pathlib import Path
from collections import Counter


# In[2]:


from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced


# In[6]:


#data = files.upload()


# In[3]:


animalData_df = pd.read_csv('Animal_Data.csv')
animalData_df.head()


# In[4]:


animalData_df.columns


# In[22]:


cleaned_df1 = animalData_df.drop(['Animal_ID', 'Name', 'State', 'Sex', 'Animal_type', 'Breed_Class', 'Color'], axis=1)
print(cleaned_df1.shape[0])
cleaned_df1.head()


# In[45]:


age_df = cleaned_df1[['Age']].copy()
age_df.head()


# In[44]:


#age_df = pd.DataFrame


# In[46]:


#Разделили цифры от слов в разные колонки
age_df1= age_df["Age"].str.split(" ", n = 1, expand = True)
age_df1.head()


# In[47]:


age_df1.replace({"months": 1,
"month": 1, 
"years": 12,
"year":12,
"day":0,
"days":0,
"week":0,
"weeks":0}, inplace=True)
age_df1.head()


# In[31]:



#age_df1['A'] = age_df1['A'].astype(int)


# In[48]:


age_df1.columns = ['A', 'B']
age_df1['A'] = age_df1['A'].astype(int)
age_df1['B'] = age_df1['B'].astype(int)
age_df1['Age'] = age_df1['A'] * age_df1['B']
age_df1.head()


# In[56]:


age_df2 = age_df1.drop(columns=['A', 'B'])
age_df2.head()


# In[60]:


new_age_df = cleaned_df1.join(age_df2, how = 'left', rsuffix= ' month')
new_age_df.tail()


# *Try to change the index after join*

# In[ ]:





# In[10]:


# Remove the `Not Tested` 4Dx status
noTest_mask = cleaned_df1['4Dx_tested'] != 'Not Tested'
tested_df = cleaned_df1.loc[noTest_mask]

tested_df.shape[0]


# In[11]:


tested_df.columns


# In[14]:


tested_df['4Dx_tested'].value_counts()


# In[16]:


tick_joined_df = pd.read_csv('../Data/completed_joined_tick_data.csv')
tick_joined_df.head()


# In[18]:


tick_joined_df.ixodes_scapularis_county_status_2016	.value_counts()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


from tables.tests.test_suite import test
# Splitting the age column to separate numbers from words
tested_df[['Age_num', 'age_str']] = tested_df['Age'].apply(lambda x: pd.Series(str(x).split(" ")))
tested_df['Age'] = tested_df['Age_num']
tested_df['Age'] = tested_df['Age'].astype('float')

print(tested_df["age_str"].unique())

# Changing the ages to all be in years
tested_df.loc[tested_df.age_str == 'days', ['Age']] = tested_df['Age'] / 365
tested_df.loc[tested_df.age_str == 'day', ['Age']] = tested_df['Age'] / 365
tested_df.loc[tested_df.age_str == 'months', ['Age']] = tested_df['Age'] / 12
tested_df.loc[tested_df.age_str == 'month', ['Age']] = tested_df['Age'] / 12
tested_df.loc[tested_df.age_str == 'weeks', ['Age']] = tested_df['Age'] / 52
tested_df.loc[tested_df.age_str == 'week', ['Age']] = tested_df['Age'] / 52

tested_df.head()


# In[ ]:


tester = tested_df.drop(['age_str', 'Age_num'], axis=1)
tester.columns


# In[ ]:


tester.head()


# In[ ]:


tester.dtypes


# ### Split data into training and testing groups

# In[ ]:


# Creating features
X = tester.drop(columns='4Dx_tested')
X = pd.get_dummies(X)

y = tester['4Dx_tested']

X.head()


# In[ ]:


X.describe()


# In[ ]:


# Check the balance of the target variable
y.value_counts()


# In[ ]:


# Splitting data into testing and training sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(Counter(y_train))
print(Counter(y_test))


# In[ ]:


from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=1)
X_resampled, y_resampled = ros.fit_resample(X_train, y_train)

Counter(y_resampled)


# In[ ]:


from sklearn.linear_model import LogisticRegression

LG_model = LogisticRegression(solver='lbfgs', random_state=1)
LG_model.fit(X_resampled, y_resampled)


# In[ ]:


from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix

y_pred = LG_model.predict(X_test)
print(balanced_accuracy_score(y_test, y_pred))

Confusion_matrix = confusion_matrix(y_test, y_pred)
Confusion_matrix


# In[ ]:


Confusion_matrix_df = pd.DataFrame(Confusion_matrix, index=["Actual Positive", "Actual Negative"], columns=["Predicted Positive", "Predicted Negative"])
Confusion_matrix_df


# In[ ]:


from imblearn.metrics import classification_report_imbalanced

print(classification_report_imbalanced(y_test, y_pred))


# In[ ]:




