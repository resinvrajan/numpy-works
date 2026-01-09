import numpy as np
two_d_arr1=np.array([[1,2],
                     [3,4]])
two_d_arr2=np.array([[10,20],
                     [30,40]])
v_stack_arr=np.vstack((two_d_arr1,two_d_arr2))
print(v_stack_arr)
h_stack_arr=np.hstack((two_d_arr1,two_d_arr2))
print(h_stack_arr)
