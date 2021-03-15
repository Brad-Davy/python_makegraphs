import matplotlib.pyplot as plt
import numpy as np


plt.plot(np.linspace(0,2*np.pi,100),np.cos(np.linspace(0,2*np.pi,100)))
plt.xlabel("X")
plt.ylabel("Cos(x)")
plt.grid()
plt.title("A cos Graph")
plt.show()
