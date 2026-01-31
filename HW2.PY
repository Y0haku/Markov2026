import numpy as np
import matplotlib.pyplot as plt

gamma = 4
x0 = 10
Ns = [100, 1000, 10000]

C = (gamma - 1) * x0**(gamma - 1)

def sample_powerlaw(N, gamma, x0):
    U = np.random.rand(N)
    return x0 * (1 - U)**(-1/(gamma - 1))

x = np.linspace(x0, 60, 1000)
pdf = C * x**(-gamma)

plt.figure()
for N in Ns:
    samples = sample_powerlaw(N, gamma, x0)
    plt.hist(samples, bins=50, density=True, alpha=0.4,
             label=f"N={N}", range=(0,60))

plt.plot(x, pdf, label="Theoretical PDF")
plt.xlim(0, 60)
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.show()
  
