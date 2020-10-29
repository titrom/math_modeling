import numpy as np
N=int(input())
M=int(input())
a=np.ndarray(shape=(N,M))

for i in range(N):
    for j in range(M):
        a[i,j]=input()
print(a)


for i in range(N):
    c=a[:,i]
    mami=c[0]
    for j in range(M):
        if mami<c[i]:
            mami=c[i]
print(i)
        