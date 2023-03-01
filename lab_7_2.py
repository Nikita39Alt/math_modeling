import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.animation as animator

fig,ax = mpl.subplots()
circle, = mpl.plot([],[],'o')
def circle_extend(t):
    x, y = t*np.sin(np.arange(0,2*np.pi+0.1,0.1)), t*np.cos(np.arange(0,2*np.pi+0.1,0.1))
    return [x,y]

def animate(i):
    circle.set_data(circle_extend(i))

mpl.axis('equal')
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)

ani = animator.FuncAnimation(fig, animate, frames = 100, interval = 30)
ani.save('lab_7_2.gif')
