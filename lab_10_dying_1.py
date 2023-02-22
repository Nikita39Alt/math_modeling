import numpy as np
from scipy.integate import odeint
import mathplotlib.pyplot as mpl

x = np.arange(-10,10)
w0 = 0

graph = odeint(func, w0, x)
plt.plot(x, graph[:0])
plt.plot(x, graph[:1])
plt.savefig('pic.png')
