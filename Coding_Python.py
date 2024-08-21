#!/usr/bin/env python
# coding: utf-8

# In[24]:


#Stair Case problem : 1

def create_staircase_1(nums):
  while len(nums) != 0:
    step = 1
    subsets = []
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False

  return subsets


# In[25]:


create_staircase_1([1,2,3])


# In[27]:


#Stair Case problem : 2

def create_staircase_2(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets


# In[28]:


create_staircase_2([1,2,3])


# In[ ]:




