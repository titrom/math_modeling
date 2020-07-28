import matplotlib.pyplot as plt
import numpy as np
from math import pi
def cycloid(R=1):
    t = np.linspace(0, 4*pi,1000)
    x= R*(t-np.sin(t))
    y= R*(1-np.cos(t))
    plt.axis('equal')
    plt.plot(x,y,label ='cycloid')
    plt.legend()
    plt.show()
cycloid ()  
   
def astroid(R=1):
    t = np.linspace(0, 4*pi,1000)
    x= R*np.cos(t)**3
    y= R*np.sin(t)**3
    plt.axis('equal')
    plt.plot(x,y, label = 'astroid')
    plt.legend()
    plt.show()
astroid ()

