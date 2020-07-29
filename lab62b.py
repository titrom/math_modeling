import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'o', ms=5 )
xdata, ydata = [],[]
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
plt.grid()
plt.axis('equal')
R=2
t=np.linspace(0,4*np.pi,1000)
x=R*np.sin(t)**3
y=R*np.cos(t)**3
plt.plot(x,y,label ='astroid')
plt.legend()
plt.show()
def astroid(R,t):
    x=R*np.sin(t)**3
    y=R*np.cos(t)**3

    return x,y

def astr(frame):
    anim_object.set_data(astroid(2,frame))
    return anim_object,
ani =FuncAnimation(fig,astr,frames = np.linspace(0,4*np.pi,1000),interval = 10)
ani.save('astroid.gif')


