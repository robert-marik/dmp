#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(suppress=True);


L = np.matrix([
    0, 1.26, 2.0,
    0.614, 0, 0,
    0, 0.808, 0.808
]).reshape(3,3)


N = 10
X = np.zeros((3,N+1))
X[:,0] = [10,5,12]
for i in range(N):
    X[:,i+1] = L@X[:,i]

    
    
    
fig, ax = plt.subplots(1)
cas = np.linspace(0,N,N+1) * 4
ax.plot(cas,X.T)     
ax.legend(
    ["mláďata","mladí tuleni","staří tuleni"],
    title="Věková kategorie"
    )
ax.set(
    ylim=(0,None),
    title="Počet jedinců podle věkových kategorií",
    ylabel="Počet jedinců",
    xlabel="Čas/rok"
    )
ax.grid();


# In[ ]:


import pandas as pd
df = pd.DataFrame(data=X.T, 
                  columns=["mláďata","mladí tuleni","staří tuleni"], 
                  index=4*np.arange(0,X.shape[1])
                 )
df.index.name = "čas/rok"
df.columns.name = "věková kategorie"
df


# In[ ]:


df.plot(grid=True, title="Vývoj počtu tuleňů", ylabel="počet jedinců")
plt.savefig("tuleni.pdf")


# In[ ]:


styly = ["-","--","-."]
fig, ax = plt.subplots(1,2, figsize=(10,5))
df.plot(grid=True, title="Vývoj počtu tuleňů",  
        ylabel="počet jedinců", 
        #logy=True, 
        ax =ax[0],
        style = styly
        )
df.div(df.sum(axis=1), axis=0).mul(100).plot(
        title="Procentuální zastoupení kategorií", 
        ylabel="procento z celkového počtu", 
        ax=ax[1], grid=True, legend=False, style=styly)
# plt.suptitle("Vývoj počtu tuleňů")
plt.tight_layout()
plt.savefig("tuleni2.pdf")


# In[ ]:


df.plot(grid=True, title="Vývoj počtu tuleňů", ylabel="počet jedinců", logy=True)


# In[ ]:


df.plot(grid=True, title="Vývoj počtu tuleňů", ylabel="počet jedinců", logy=True)


# In[ ]:


df.sum(axis=1)


# In[ ]:


df.div(df.sum(axis=1), axis=0).mul(100).plot(
        title="Procentuální zastoupení věkových tříd", 
        ylabel="procento z celkového počtu")


# In[ ]:




