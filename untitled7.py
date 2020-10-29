import numpy as np
N = int(input())
M= int(input())

for i in range(N):
    for j in range(M):
        if i==1 or j==1:
           A=np.sin(N*i+M*j)
        elif i==0 or j==0:
            A=np.sin(N*(i+1)+M*(j+1))
        NxM=np.ndarray(shape=(N, M))

        

for i in range(N):
     for j in range(M):
         if NxM[i, j]<0:
             NxM[i, j]=0
print(NxM)
B= NxM[:,::-1]

print(B)
         