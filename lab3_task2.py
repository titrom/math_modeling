import numpy as np
from lab3_task import acceleration_of_gravity as g
a=np.pi/3
b=np.pi/6
h=100
v1=np.sqrt((g*h*(np.tan(b)**2))/((2*np.cos(a)**2)*(1-np.tan(b)*np.tan(a))))
print(v1)

from lab3_task import boltzmann_constant as k
from lab3_task import planck_constant as h
T=200
E=300
N=(2/np.sqrt(np.pi))*(h/(k*T)**1.5)*(np.e**(-np.e/(k*T)))*np.e**(T/2)
print(N)