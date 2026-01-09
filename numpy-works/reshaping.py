"""
reshaping
=========
np.reshape(arr1,shap=(size))
"""
import numpy as np
arr1=np.array([1,2,3,4,5,6])
new_arr=np.reshape(arr1,shape=(2,3))
print(new_arr)