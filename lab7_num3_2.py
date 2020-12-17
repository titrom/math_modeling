import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
fig,ax=plt.subplots()
anim_object,=plt.plot([],[],'-')
xdata,ydata=[],[]
edge=20
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(t):
    xdata.append(16*np.sin(t)**3)
    ydata.append(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))
    anim_object.set_data(xdata,ydata)
    return anim_object
ani=FuncAnimation(fig,animate,frames=np.arange(0,2*np.pi,0.1),interval=100) 