
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1000)
y_binomial = np.random.binomial(100, 0.8, len(x))

plt.plot(x,y_binomial)
plt.show()

