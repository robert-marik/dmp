import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def kolonizace(N,b=1,beta=1,D=1):
    return b/(D*(N+beta))

def vymirani (N, S=1, a=1, k=1.4):
    return a*N**(k)/S

N = np.linspace(0,10,100)
plt.plot(N,kolonizace(N,b=10, D=1, beta=.5),"k-",label="kolonizace, blízký ostrov")
plt.plot(N,kolonizace(N,b=10, D=2, beta=.5),"k--",label="kolonizace, vzdálený ostrov")

plt.plot(N,vymirani(N, k=1.5, S = 10),"r-",label=r"vymírání, velký ostrov")
plt.plot(N,vymirani(N, k=1.5, S = 2),"r--",label=r"vymírání, malý ostrov")
plt.legend()
ax = plt.gca()
ax.set(
    ylim=(0,10), 
    xlim=(0,10),
    title="Dynamika vývoje počtu druhů na ostrově",
    xlabel="počet druhů",
    ylabel="rychlost kolonizace a vymírání",
    xticks=[],
    yticks=[]
    );


plt.savefig('ostrov1.pdf')

fig,ax = plt.subplots()

pocatecni_podminka = [0]
meze = [0,25]

t = np.linspace(*meze, 100) # časy ve kterých určíme hodnotu řešení
def rovnice(t, N, a=1, b=8, beta=0.2, D=0.5, k=1.3, S=20):
    return b/(D*(N+beta)) - a*N**k/S

reseni = solve_ivp(rovnice, 
                   meze, 
                   pocatecni_podminka, 
                   t_eval=t,
                   )

ax.plot(reseni.t, reseni.y.T)
ax = plt.gca()
ax.set(
    xlabel="čas",
    ylabel="počet druhů",
    title="Dynamika počtu druhů na ostrově"
)
ax.grid();

plt.savefig('ostrov2.pdf')


