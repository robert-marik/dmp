#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp

### Příprava funkcí a parametrů
pocatecni_podminka = np.array([0.1])  # počáteční podmínka
meze = np.array([0,10]) # interval, na kterém hledáme řešení
parametry = [.2,.5,.8] # seznam parametrů
styles = ['-', '--', '-.'] # styly pro grafy

def rovnice(t, P, k=1, m=0.5):
    return k*P*(1-P) - m*P

### Řešení modelu
t=np.linspace(*meze)  # definiční obor, v těchto bodech budeme hledat řešení
df = pd.DataFrame()      # tabulka pro výstup
df.index = t              # sloupec s časem

for parametr in parametry:
    reseni = solve_ivp(
                       lambda t,x:rovnice(t,x,m=parametr),
                       meze,
                       pocatecni_podminka,
                       t_eval=t
                       )
    df[parametr] = reseni.y.T # další sloupec tabulky
    # lambda funkce viz https://www.w3schools.com/python/python_lambda.asp
    # (dočasná nepojmenovaná funkce)
df.index.name = 'čas'  # název řádků tabulky
df.columns.name = r'parametr $m$'  # název sloupců tabulky
ax = df.plot(style=styles)
ax.set(
    title = r"Vývoj populace v čase pro různé hodnoty parametru $m$",
    ylim=(0,None))
ax.grid()
plt.savefig("metapopulace.pdf")
#%%

P = np.linspace(0,1)
df2 = pd.DataFrame(index=P)
df2.index.name = r"$P$"
for m in parametry:
    df2[rf"extinkce $m={m}$"] = -rovnice(0, P, k=0, m=m)
df2["kolonizace"] = rovnice(0, P, k=1, m=0)
ax = df2.plot(style=styles)
ax.set(ylim=(0,0.3), title="Rychlosti kolonizace a extinkce")
ax.grid()
plt.savefig("metapopulace2.pdf")
# %%
