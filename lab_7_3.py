import numpy as np
import matplotlib.pyplot as mpl

e = 2.71

t = np.arange(0,np.pi*12,0.1)

x = np.sin(t) * (e ** (np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5 )
y = np.cos(t) * (e ** (np.cos(t)) - 2 * np.cos(4*t) + np.sin(t/12)**5 )
mpl.plot(x,y,color='r')
mpl.axis('equal')


t = np.arange(0,np.pi*2,0.1)

x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
mpl.plot(x,y,color='g')

mpl.savefig('7_3.png')
