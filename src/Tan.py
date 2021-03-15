import matplotlib.pyplot as plt
import numpy as np


plt.plot(np.linspace(0,2*np.pi,100),np.tan(np.linspace(0,2*np.pi,100)))
plt.xlabel("X")
plt.ylabel("Sin(x)")
plt.grid()
plt.title("A sin Graph")
plt.show()
