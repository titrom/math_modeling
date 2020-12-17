import matplotlib.pyplot as plt
import numpy as np
n=int(input())
def func1(R):
    t=np.arange(-2*np.pi,2*np.pi,0.01)
    x=R*(t-np.sin(t))
    y=R*(1-np.cos(t))
    plt.axis('equal')
    plt.plot(x,y)
    plt.show()
def func2(R):
    t=np.arange(-2*np.pi,2*np.pi,0.01)
    x=R*np.cos(t)**3
    y=R*np.sin(t)**3
    plt.axis('equal')
    plt.plot(x,y)
    plt.show()
if n==1:
    func1(10)
elif n==2:
    func2(2)
    
    
    
