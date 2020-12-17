import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation  import FuncAnimation
fig,ax=plt.subplots()
ball,=plt.plot([],[],'o',color='r')
def cirle_move(R):

    alpha=np.arange(0,2*np.pi,0.1)
    x=R*np.cos(alpha)
    y=R*np.sin(alpha)
    return x,y
edge=15
plt.axis('equal')
ax.set_xlim(-edge,edge)
ax.set_ylim(-edge,edge)    
def animate(i):
    ball.set_data(cirle_move(R=i))
ani=FuncAnimation(fig,
                  animate,
                  frames=100,
                  interval=100)
