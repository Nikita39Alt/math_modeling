import numpy as np
import matplotlib.pyplot as mpl
import matplotlib.animation as animator

colors = ['r','orange','yellow','g','cyan','b','purple']

fig,ax = mpl.subplots()
circle, = mpl.plot([],[],'o')
def circle_extend(t):
    x, y = t*np.sin(np.arange(0,2*np.pi,0.1)), t*np.cos(np.arange(0,2*np.pi,0.1))
    return [x,y]

def animate(i):
    circle = mpl.plot(circle_extend(i)[0],circle_extend(i)[1],color=colors[i%7])

mpl.axis('equal')

ani = animator.FuncAnimation(fig, animate, frames = 50, interval = 100)
ani.save('lab_7_2_a.gif')
