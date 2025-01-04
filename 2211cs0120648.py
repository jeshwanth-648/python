#!/usr/bin/env python
# coding: utf-8

# In[1]:


import scipy.stats as stats
import math
import numpy as np


# In[3]:


sample_data = np.array(
    [205, 198, 210, 190, 215, 205, 200, 192, 198, 205, 198, 202, 208, 200, 205, 198, 205, 210, 192, 205, 198, 205, 210, 192, 205])
population_std_dev = 5


# In[4]:


population_mean = 200


# In[5]:


sample_size = len(sample_data)


# In[6]:


alpha = 0.05  


# In[7]:


critical_value_left = stats.norm.ppf(alpha/2)


# In[8]:


critical_value_right = -critical_value_left


# In[9]:


sample_mean = sample_data.mean()


# In[10]:


z_score = (sample_mean - population_mean) /     (population_std_dev / math.sqrt(sample_size))


# In[11]:


if abs(z_score) > max(abs(critical_value_left), abs(critical_value_right)):
    print("Reject the null hypothesis.")
    print("There is statistically significant evidence that the average cholesterol level in the population is different from 200 mg/dL.")
else:
    print("Fail to reject the null hypothesis.")
    print("There is not enough evidence to conclude that the average cholesterol level in the population is different from 200 mg/dL.")


# In[22]:


from scipy.stats import ttest_1samp  
import numpy as np  


# In[23]:


ages = [45, 89, 23, 46, 12, 69, 45, 24, 34, 67]  
print(ages)  
  


# In[24]:


mean = np.mean(ages)  
print(mean)  


# In[25]:


sample_mean = sample_data.mean()
sample_mean


# In[26]:


z_score = (sample_mean - population_mean) /     (population_std_dev / math.sqrt(sample_size))
z_score


# In[27]:


t_test, p_val = ttest_1samp(ages, 30)  
print("P-value is: ", p_val)  


# In[28]:


if p_val < 0.05:      
    print(" We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis")  


# In[29]:


from scipy.stats import ttest_ind  
import numpy as np  


# In[34]:


data_group1 = np.array([12, 18, 12, 13, 15, 1, 7,  
                        20, 21, 25, 19, 31, 21, 17,  
                        17, 15, 19, 15, 12, 15])  
data_group1


# In[35]:


data_group2 = np.array([23, 22, 24, 25, 21, 26, 21,  
                       21, 25, 30, 24, 21, 23, 19,  
                        14, 18, 14, 12, 19, 15])  
data_group2


# In[36]:


mean1 = np.mean(data_group1)  
mean1


# In[37]:


mean2 = np.mean(data_group2)  
mean2


# In[38]:


std1 = np.std(data_group1)  
print("Data group 1 std value:", std1)  


# In[39]:


std2 = np.std(data_group2)  
print("Data group 2 std value:", std2)  


# In[40]:


t_test,p_val = ttest_ind(data_group1, data_group2)  
print("The P-value is: ", p_val)  


# In[42]:


if p_val < 0.05:      
    print("We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis")  


# In[50]:


from scipy.stats import ttest_ind  
import numpy as np   


# In[51]:


data_group1 = np.array([12, 18, 12, 13, 15, 1, 7,  
                        20, 21, 25, 19, 31, 21, 17,  
                       17, 15, 19, 15, 12, 15])  
data_group1


# In[52]:


data_group2 = np.array([23, 22, 24, 25, 21, 26, 21,  
                        21, 25, 30, 24, 21, 23, 19,  
                        14, 18, 14, 12, 19, 15]) 
data_group2                   


# In[53]:


mean1 = np.mean(data_group1) 
mean1 


# In[54]:


mean2 = np.mean(data_group2) 
mean2 


# In[55]:


std1 = np.std(data_group1)  
print("Data group 1 std value:", std1) 


# In[56]:


std2 = np.std(data_group2)
print("Data group 2 std value:", std2)


# In[62]:


t_test,p_val = ttest_ind(data_group1, data_group2)  
print("The P-value is: ", p_val)  


# In[63]:


if p_val < 0.05:      
    print("We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis") 


# In[75]:


import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp


# In[76]:


mydata=pd.read_csv("InternetMobileTime[1].csv")
mydata.head()


# In[77]:


len(mydata)


# In[78]:


mydata


# In[79]:


mean=np.mean(mydata)
print(mean)


# In[81]:


t_test,p_val = ttest_1samp(mydata,144)  
print("The P-value is: ", p_val)  


# In[82]:


print(t_test)


# In[83]:


if p_val < 0.05:      
    print("We can reject the null hypothesis")  
else:  
    print("We can accept the null hypothesis") 


# In[ ]:




