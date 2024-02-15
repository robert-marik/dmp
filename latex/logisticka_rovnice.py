import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

x = np.linspace(0,10,100)
a = 3
df = pd.DataFrame(index=x)

df["Holling I"] = x/15
df["Holling II"] = x/(x+a)
df["Holling III"] = x**2/(x**2+a**2)

df.plot()
plt.grid();
plt.gca().set(title="Trofické funkce", xlabel="Populace kořisti", ylabel="Množství zkonzumované kořisti")
plt.savefig('holling.pdf')

pocatecni_podminka = np.arange(0.1,1.5,0.1)
meze = [0,10]

def rovnice(t, x, h=0):
    r = 1
    K = 1
    return r*x*(1-x/K) - h

t=np.linspace(*meze, 100)  # graf reseni
reseni = solve_ivp(
                   rovnice,
                   meze,
                   pocatecni_podminka,
                   t_eval=t, ## zde je možné zadat pole hodnot, kde se mají určit řešení
                   )
reseni

fig,ax = plt.subplots(1)
ax.plot(t,reseni.y.T, color='C0')


ax.set(title="Řešení logistické rovnice pro různé počáteční podmínky", ylabel="velikost populace", xlabel="čas")

plt.savefig('logisticka.pdf')
