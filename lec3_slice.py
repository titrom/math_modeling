#[start:stop:ste[p] 
#по умолчанию
#start = 0
#stop=len(строка или столбец)
#step= 1
import numpy as np
A=np.array([[1,2,3] ,[4,5,6]])
print(A)
print(A[1,:])
print(A[:,1])
B=A[:,::-1] 
print(B)
