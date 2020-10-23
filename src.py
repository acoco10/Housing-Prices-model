#!/usr/bin/env python
# coding: utf-8

# In[2]:

def remove_outliers(x):
    std = x.std()
    two_std = x.mean() + 2*std
    return np.where(x < two_std, x, two_std)


# In[ ]:




