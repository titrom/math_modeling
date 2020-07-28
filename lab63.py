import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'ro' )
anim_object1, = plt.plot([],[],'bo')
xdata, ydata = [],[]
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1, 1)

def sinus(frame, A=0.5,f=2,a=1,F=1):
   
    t= np.linspace(0,frame,100)
    xdata.append(f*t)
    ydata.append(A*np.sin(f*t))
    anim_object.set_data(xdata,ydata)

    xdata.append(F*t)
    ydata.append(a*np.sin(F*t))
    anim_object.set_data(xdata,ydata)
    return anim_object1,anim_object,

ani =FuncAnimation(fig,sinus,frames = np.linspace(0,2*np.pi,100),interval = 100)
ani.save('sinusruns.gif')