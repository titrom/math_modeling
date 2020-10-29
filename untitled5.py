from math import sin
N = int(input())

M = int(input())
NxM = []
for i in range(N):
    a = []
    for j in range(M):
        a.append(sin(N*(i+1) + M*(j+1)))
    NxM.append(a)
 
for i in range(N):
    for j in range(M):
        if NxM[i][j] < 0:
            NxM[i][j] = 0
            print(NxM[i][j], end=' ')
        else:
            print(NxM[i][j], end=' ')
    print()