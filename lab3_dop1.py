import numpy as np
a=np.ndarray(shape=(4,3))
b=np.ndarray(shape=(4,3))
c=np.ndarray(shape=(4,3))
for i in range(4):
    for j in range(3):
        a[i,j]=input()
print(a)
for i in range(4):
    for j in range(3):
        b[i,j]=input()
print(b)
for i in range(4):
    for j in range(3):        
        if a[i,j]>b[i,j]:
            c[i,j]=a[i,j]
        else:
            c[i,j]=b[i,j]
print(c)