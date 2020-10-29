import numpy as np
N=int(input())
M=int(input())

NxM=[]
for i in range(N):
    a=[]
    for j in range(M):
        if i==0 or j==0:
            a.append(np.sin(N*(i+1)+M*(j+1)))
        elif i>0 and i>0:
            a.append(np.sin(N*i+M*j))
    NxM.append(a)
print(NxM[i][j])

