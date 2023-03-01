import numpy
import matplotlib.pyplot as mpl

x_0, y_0, C, D = 0.1, 0.1, 0.3, 0.33

x_n, y_n = x_0, y_0
x,y = [],[]

def calc ():
    global x_n, y_n
    return x_n**2 - y_n**2 + C, 2 * x_n * y_n + D

n = int(input())
a = input()
if a != '':
    C, D = a.split()
    C, D = float(C), float(D)

for i in range(n):
    x_n, y_n = calc()
    x.append(x_n)
    y.append(y_n)

mpl.axis('equal')
mpl.plot(x,y)
mpl.savefig('7_4.png')
