print("____________________________laba_3_osnov_3__________________________")
from astro_constants import acceleration_of_gravity_ears as g
import numpy as np

N = 10
A = np.zeros((N, 3))
t = np.arange(0, 5, 0.1)
t = np.linspace(0, 5, N)
y0 = 1
x0 = 2
v0 = 10


for i in range(N):
    x = x0 + v0 * t[i]
    y = y0 + v0 * t[i] - (g * t[i]**2) / 2
    
    A[i, 0] = t[i]
    A[i, 1] = x
    A[i, 2] = y

print(A)
