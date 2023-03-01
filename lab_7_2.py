import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.animation as animator

fig,ax = mpl.subplots()
circle, = mpl.plot([],[],'o',color='g')
def circle_extend(t):
    x, y = t*np.sin(np.arange(0,2*np.pi+0.1,0.05)), t*np.cos(np.arange(0,2*np.pi+0.1,0.05))
    return [x,y]

def animate(i):
    if i > 100:
        pass
    else:
        circle.set_data(circle_extend(i))

mpl.axis('equal')
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)

ani = animator.FuncAnimation(fig, animate, frames = 300, interval = 30)
ani.save('lab_7_2.gif')
