# %%

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# %%
x = np.linspace(0, 3, 100)
k = [0.5, 1, 2, 3]

for ki in k:
    y = ki * x
    plt.plot(x, y, label=f'k={ki}')

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Grafy funkcí $y = kx$')
plt.legend()
plt.grid()
plt.savefig('prima_umernost.pdf', transparent=True)

# %%

x = np.linspace(0, 3, 100)
K = [0.5, 1, 2, 3]
r = 1
for ki in K:
    y = r * x * (1 - x / ki)
    plt.plot(x, y, label=f'r={r}, K={ki}')

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Grafy funkcí $y = rx\left(1-\frac{x}{K}\right)$')
plt.ylim(0, 1)
plt.legend()
plt.grid()
plt.savefig('kvadraticka_funkce.pdf', transparent=True)

# %%

# %%
x = np.linspace(0, 3, 100)
k = [0.5, 1, 2, 3]

for ki in k:
    y = x**ki
    plt.plot(x, y, label=f'k={ki}')

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Grafy funkcí $y = x^k$')
plt.legend()
plt.grid()
plt.ylim(0, 2)
plt.savefig('mocnina.pdf', transparent=True)
# %%
x = np.linspace(0, 8, 100)
k = [1,1,1,3]
a = [0.5,1,2,1]

for ki, ai in zip(k,a):
    y = x**ki/(x**ki + ai**ki)
    plt.plot(x, y, label=f'k={ki}, a={ai}')

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Grafy funkcí $y = \frac{x}{x+a}$ a $y=\frac{x^k}{x^k+a^k}$')
plt.legend()
plt.grid()
plt.ylim(0, 1.2)
plt.savefig('lomena.pdf', transparent=True)

# %%
