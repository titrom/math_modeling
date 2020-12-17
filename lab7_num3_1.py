import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
fig,ax=plt.subplots()
anim_object,=plt.plot([],[],'-')
xdata,ydata=[],[]
edge=5
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge) 
def animate(t):
    xdata.append(np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    ydata.append(np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
    anim_object.set_data(xdata,ydata)
    return anim_object
ani=FuncAnimation(fig,animate,frames=np.arange(0,12*np.pi,0.1),interval=100)
