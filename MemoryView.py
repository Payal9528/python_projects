import numpy as np
a = np.arange(20).reshape(4,5)
b = a[:,::2]
print(b)
x= np.array([1,2,3,4,5])
A = np.random.rand(3,2,1)
B = np.random.rand(2,3)
x = np.array([ 1,-2,3,-4,5])
marks = x < 0
print(marks)
print(A+B)
print(np.vectorize())