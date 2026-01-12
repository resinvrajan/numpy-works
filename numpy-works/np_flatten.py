"""
flatening
=========
np.ravel -> is used to flatten array
arr.flatten -> also used to flat array

"""
import numpy as np
arr=np.array([[10,20],[30,40],[50,60]])
new_arr=np.ravel(arr)
print(new_arr)
new_arr1=arr.flatten()
print(new_arr1)