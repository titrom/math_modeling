import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'o', ms=3 )
xdata, ydata = [],[]
ax.set_xlim(0, 20)
ax.set_ylim(0, 10)
plt.grid()
plt.axis('equal')
R=2
t=np.linspace(0,4*np.pi,1000)
x=R*(t-np.sin(t))
y=R*(1-np.cos(t))
plt.plot(x,y,label ='cycloid')
plt.legend()
plt.show()
def sycloid(R,t):
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))

    return x,y

def acyc(frame):
    anim_object.set_data(sycloid(2,frame))
    return anim_object,
ani =FuncAnimation(fig,acyc,frames = np.linspace(0,4*np.pi,1000),interval = 10)
ani.save('sinusoid.gif')



