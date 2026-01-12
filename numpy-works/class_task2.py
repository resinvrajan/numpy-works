import numpy as np
arr=np.array([-1,2,3,-1,5,-6])
print(np.where(arr<0,"-ve","+ve"))