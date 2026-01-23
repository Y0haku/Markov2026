import numpy as np
import matplotlib.pyplot as plt

def f(u):
    return (u**4) / (1 + u**6)

xs = np.arange(1.0, 5.0 + 1e-12, 0.1)
Ns = np.floor(10**xs).astype(int)

# Reference value (from high-accuracy numerical integration)
I_ref = 0.1434257774478257

E = []

rng = np.random.default_rng(0)  # seed for reproducibility

for N in Ns:
    U = rng.random(N)
    V = rng.random(N)
    hits = (V <= f(U)).mean()
    E.append(hits)

E = np.array(E)

plt.figure()
plt.plot(Ns, E, marker='o', linewidth=1)
plt.xscale('log')
plt.xlabel('N (log scale)')
plt.ylabel('E(N) estimate')
plt.show()
