import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp

### Příprava funkcí a parametrů
pocatecni_podminka = np.array([0.1])  # počáteční podmínka
meze = np.array([0,10]) # interval, na kterém hledáme řešení
parametry = [.2,.5,.8] # seznam parametrů

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
df.columns.name = 'parametr'  # název sloupců tabulky
df.plot()
#%%