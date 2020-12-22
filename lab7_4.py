import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
x0=0.1
y0=0.1
C=0.3
D=0.33
fig,ax=plt.subplots()
anim_object,=plt.plot([],[],'o')
xdata,ydata=[],[]
edge=5
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge) 
def animate(t):
    xdata.append((x0**2+y0**2*t+C)*t)
    ydata.append((2*x0*y0+D)*t)
    anim_object.set_data(xdata,ydata)
    return anim_object
ani=FuncAnimation(fig,animate,frames=100,interval=100)


