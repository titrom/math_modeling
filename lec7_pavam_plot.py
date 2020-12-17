import matplotlib.pyplot as plt
import numpy as np
alpha =np.arange(-2*np.pi,2*np.pi,0.1)
R=6
x=R*np.cos(alpha)
y=R*np.sin(alpha)
plt.axis('equal')
plt.plot(x,y,ls='--',lw=1)
plt.show()