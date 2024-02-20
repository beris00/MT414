#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Ex1
birthplace=input("Where were you born? ")
print("This person was born in", birthplace)


# In[2]:


#Ex2
list1=[]
i=10
while i>4:
    list1.append(i)
    i=i-1
print(list1)

for elt in list1:
    print(elt)
    


# In[3]:


#Ex3
prodDict={"Product A":[10.99,50],"Product B":[5.99,30],"Product C":[7.49,25]}
totRev=[]



# In[4]:


#Ex3 part 2
import pandas as pd
index_list=["Cost","Quantity"]
prodDf=pd.DataFrame(prodDict,index=index_list)
prodDf


# In[5]:


prodDf.iloc[2,"35"]


# In[ ]:





# In[ ]:


#Ex4 part 1
def MeanFun(x):
    if x ==0:
        print("This list is empty.")
    return(sum(x)/len(x))

list2=[12,15,6,13,12,18,2,15,8,9,16,14,16]
list3=[-12,-15,-6,-13,-12,-18,-2,-16,-8,-9,-16,-14,-16]
    
MeanFun(list2)


# In[ ]:


#Ex4 part 2
def Beta1Fun(lst1,lst2):
    if len(lst1) == len(lst2):
        topline=0
        for x in lst1:
            a=(x-MeanFun(lst1))
            for y in lst2:
                b=(y-MeanFun(lst2))
            sum_of_brackets=a*b
            topline=topline+sum_of_brackets

        bottomline=0
        for elt in lst1:
            brackets=(elt-MeanFun(lst1))**2
            bottomline=bottomline+brackets
            
    return(topline/bottomline)

list2=[12,15,6,13,12,18,2,15,8,9,16,14,16]
list3=[-12,-15,-6,-13,-12,-18,-2,-16,-8,-9,-16,-14,-16]

print(Beta1Fun(list2,list3))

import scipy.stats as sp

sp.linregress(list2,list3)


# In[10]:


#Ex5
import pandas as pd
inpDf=pd.read_csv(r"C:\Users\erisb\Downloads\Assignment_Input.csv")
inpDf


# In[7]:


beta1Val=Beta1Fun(inpDf["AdvBudg"],inpDf["Sales"])


# In[8]:


beta0Val=inpDf.mean("Sales")-(1.9*inpDf.mean("AdvBudg"))


# In[9]:


yPredVal=beta0Val+(beta1Val*15000)


# In[ ]:


#Ex6
import numpy as np
array1=np.array(range(105,191,5)).reshape(3,6)
array1

my_list=[3,4,5,6,7,8]
array2=np.array(my_list)

print("mean = " ,np.mean(array2))
print("median = " ,np.median(array2))
print("STD = " ,np.std(array2))


# In[ ]:


#Ex6 part 2
for elt in array2:
    z_score = (elt-np.mean(array2))/np.std(array2)
    print(z_score)


# In[ ]:





# In[ ]:




