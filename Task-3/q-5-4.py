import numpy as np
a=np.array([1,2,3,4,5,6,7])
print("Before changing:","\n The data type is",a.dtype,"\n The array is ")
print(a)
a=a.astype(np.float16)
print("After changing:","\n The data type is",a.dtype,"\n The array is ")
print(a)
