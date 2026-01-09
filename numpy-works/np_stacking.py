"""
stacking
========
a)vertical stacking
    np.vstack((arr1,arr2))
b)horizondal stacking
    np.hstack((arr1,arr2))

"""
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])
v_stack_arr=np.vstack((arr1,arr2))
print(v_stack_arr)
h_stack_arr=np.hstack((arr1,arr2))
print(h_stack_arr)