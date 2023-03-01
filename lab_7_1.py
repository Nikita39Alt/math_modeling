import numpy as np
import matplotlib.pyplot as mpl
from scipy.integrate import odeint


R = 10
t = np.arange(-20,20,0.1)

x = R * (t - np.sin(t))
y = R * (1 - np.cos(t))

mpl.plot(x,y,color='r')
mpl.axis('equal')

x = R * np.cos(t)**3
y = R * np.sin(t)**3
mpl.plot(x,y,color='g')

mpl.savefig('god_bless_me.png')
