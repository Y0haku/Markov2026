import numpy as np
import matplotlib.pyplot as plt

a = np.sqrt(3) - 1

def f(x):
    return (1/3) * x * (1+x) * np.exp(-x)

def g(x):
    return (a**2) * x * np.exp(-a*x)

c = np.exp(-a) / (3 * a**2 * (1-a))

x = np.linspace(0, 15, 1000)
plt.plot(x, f(x), label="f(x)")
plt.plot(x, c*g(x), label="c(a*) g_{a*}(x)")
plt.ylim(bottom=0)
plt.xlabel("x")
plt.ylabel("density")
plt.legend()
plt.show()
