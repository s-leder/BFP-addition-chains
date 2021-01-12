
# coding: utf-8

# Problem 2: Addition Chains

# In[1]:

import matplotlib.pyplot as plt
from math import floor, ceil, log2 as log
from numpy import linspace
import time


# In[2]:

#auxiliary function that adds the sum of any two elements to the list
def aux(lst: list):
    
    result = []
    for k in lst:
        for l in lst:
            if k+l > lst[-1] and lst+[k+l] not in result:
                result.append(lst+[k+l])
    
    return result


# In[3]:

#function that makes all ACs up to length n (still very slow and inefficient)
def add_chain(n: int):
    
    lst = [[[1]]]
    for i in range(1, n+1):
        lst.append([])
        for j in range(len(lst[i-1])):
            for k in aux(lst[i-1][j]):
                if k not in lst[i]:
                    lst[i].append(k)
    
    return lst


# In[4]:

#searches through all ACs to find the first occurence of n
def search(n: int):
    
    for i in range(len(ac_list)):
        for j in ac_list[i]:
            if n in j:
                return i
    
    return -1


# In[5]:

#computes the hamming weight
def hw(n: int):
    
    c = 0
    while n:
        c += 1
        n &= n - 1
    
    return c


# In[6]:

#time to compute all ACs up to length 7 (up to 8 already takes ~80 seconds)
t = time.clock()
ac_list = add_chain(7)
print(time.clock() - t)


# In[7]:

#number of ACs per length
for i in range(len(ac_list)):
    print(i, len(ac_list[i]))


# In[8]:

search(47) #so there is no AC for 47 with length 7 or less


# Below is a plot with the computed lengths of the ACs and a theoretical lower and upper bound (L and U):
# - L = floor(log(n)) + ind(n is not a power of 2), where ind denotes the indicator of that event and all logarithms are base 2. This is because in k steps you can reach at most $2^k$ and if n is not a power of 2 you will always need at least one more step.
# - U = floor(log(n)) + hw(n) - 1, where hw denotes the Hamming weight. This is because you can always reach $2^k$ in k steps and then add the lower powers of two corresponding to the 1s in the binary representation (e.g. to reach 25=11001, we go 1-2-4-8-16-24-25)

# In[9]:

ind = list(range(1, 51))
lst = [search(i) for i in ind]
lst[46] = 8 #manual adjustment


# In[10]:

x = linspace(1, 50, 981)
plt.figure(figsize=(20,10));
plt.plot(x, [floor(log(i))+1 for i in x]); #lb
plt.plot(ind, [floor(log(i))+hw(i)-1 for i in ind]); #ub
plt.scatter(ind, lst, c='k', s=50);
plt.grid();

plt.show()

