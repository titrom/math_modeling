import numpy as np
from lab3_task import acceleration_of_gravity as g
x0=float(input('Введите начало координат по x: '))
y0=float(input('Введите начало координат по y: '))
V0x=float(input('Введите начальную скорость по x: '))
V0y=float(input('Введите начальную скорость по y: '))

for t in range(0,6,1):
    if t<=5:
        x=x0+V0x*t
        y=y0+V0y*t+g*t**2/2
        q=np.array([t,x,y])
        print(q)
        



