print("____________________________laba_3_osnov_3__________________________")
from astro_constants import acceleration_of_gravity_ears as g
y0 = 1
x0 = 2
v0 = 1
i = 0
t = 0
print("  t. x. y. ")
import numpy as np
A = np.zeros((500,3))
if  t  in range (0 , 5 , 0.01):
    x = x0 + v0 * t
    y = y0 + v0 * t - (g * t**2) / 2
    A = np.zeros((500,3))
    A [i , 1] = t
    A [i , 2] = x
    A [i , 3] = y
    i = i + 1
print(A)