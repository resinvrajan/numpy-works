"""
np.where(condition,true_value,false_value)


"""
import numpy as np
arr=np.array([19,20,21,22,23,24,15])
print(np.where(arr>=20))
print(np.where(arr>=20,"adults","teen"))