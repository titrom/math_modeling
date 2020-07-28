import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'o', ms=3 )
xdata, ydata = [],[]
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def heart(frame):
   
    
    xdata.append(16*np.sin(frame)**3)
    ydata.append(13*np.cos(frame)- 5*np.cos(2*frame)-2*np.cos(3*frame)-np.cos(4*frame))
    anim_object.set_data(xdata,ydata)

   
    return anim_object,

ani =FuncAnimation(fig,heart,frames = np.linspace(0,2*np.pi,1000),interval = 10)
ani.save('heart.gif')



