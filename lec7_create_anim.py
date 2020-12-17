import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
fig,ax=plt.subplots()
anim_object,=plt.plot([],[],'o')
xdata,ydata=[],[]
ax.set_xlim(0,2*np.pi)
ax.set_ylim(-1,1)
def upate(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    anim_object.set_data(xdata,ydata)
    return anim_object
ani=FuncAnimation(fig,upate,frames=np.arange(0,2*np.pi,0.1),interval=100)
