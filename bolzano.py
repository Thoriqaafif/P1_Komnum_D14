from pickle import TRUE
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

def f(x):
    return x**3-3*x+1

def bolzano(a,b,n):
    x1 = a
    x2 = b
    for i in range(n):
        x3 = (x1+x2)/2
        fx1=f(x1)
        fx2=f(x2)
        fx3=f(x3)
        if(fx1*fx3>0):
            x1=x3
        elif(fx1*fx3<0):
            x2=x3
        else:
            return x3
        print(x1, x2)
    return x1, x2

x1, x2 = 1, 2
i=10

yrange = f(x1), f(x2)
y1, y2 = min(yrange), max(yrange)
vf = np.vectorize(f)
x = np.linspace(x1,x2)
y = vf(x)
epsilon = 0.1

fig = plt.figure()
ax = plt.axes(xlim=(x1-epsilon, x2+epsilon), ylim=(y1,y2))
curve, = ax.plot([],[],color='green')
left, = ax.plot([],[],color='black')
right, = ax.plot([],[],color='black')

def init():
    left.set_data([],[])
    right.set_data([],[])
    curve.set_data([],[])
    return left, right, curve

def animate(i):
    a, b = bolzano(x1, x2, i)
    left.set_data([a,a],[y1,y2])
    right.set_data([b,b],[y1,y2])
    curve.set_data(x,y)
    return left, right, curve

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=i, interval=600, blit=True)

plt.grid()
plt.show()