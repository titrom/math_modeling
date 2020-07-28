import matplotlib.pyplot as plt
import numpy as np
from math import e
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'-', ms=3 )
xdata, ydata = [],[]
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def butterfly(frame):
   
    
    xdata.append(np.sin(frame)*(e**(np.cos(frame))-2*np.cos(4*frame)+np.sin(frame/12)**5))
    ydata.append(np.cos(frame)*(e**(np.cos(frame))-2*np.cos(4*frame)+np.sin(frame/12)**5))
    anim_object.set_data(xdata,ydata)

   
    return anim_object,

ani =FuncAnimation(fig,butterfly,frames = np.linspace(0,12*np.pi,1000),interval = 10)
ani.save('butterfly.gif')


