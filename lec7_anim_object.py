import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
fig,ax=plt.subplots()
ball,=plt.plot([],[],'o')

def circle_move(R,time):
    R=
    alpha=np.arange(0,2*np.pi)
    x=R*np.cos(alpha)
    y=R*np.sin(alpha)
    return x,y
edge=3
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)
def animate(i):
    ball.set_data(circle_move(R=1,time=i))
ani=FuncAnimation(fig,animate,frames=400,interval=100)
