import numpy as np
from scipy.integate import odeint
import mathplotlib.pyplot as mpl

import math

x = np.arange(-10,10)
w0 = 0

def func(w,t):
  y,z = w
  dydt = z
  dzdt = math.sqrt(1-z**2)
  return dydt, dzdt

graph = odeint(func, w0, x)
plt.plot(x, graph[:0])
plt.plot(x, graph[:1])
plt.savefig('pic.png')
