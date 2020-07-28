import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots()
anim_object, = plt.plot([],[],'o', ms=3 )
xdata, ydata = [],[]
ax.set_xlim(-0.4, 0.4)
ax.set_ylim(0, 0.8)

def fractal(n, C =0.3,D =0.33):
   """ по входным параметрам n,C,D строится фрактальное множество точек n"""
   if n==0:
       xdata.append(0.1)
       ydata.append(0.1)
   else:
    xdata.append(xdata[n-1]**2-ydata[n-1]**2 + C)
    ydata.append(2*xdata[n-1]*ydata[n-1]+D)
    anim_object.set_data(xdata,ydata)

   
    return anim_object,
ani = FuncAnimation(fig,fractal,frames = 100, interval= 100)
ani.save('fractal.gif')



