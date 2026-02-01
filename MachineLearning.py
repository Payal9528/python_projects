import numpy as np 
data = np.array([160,170,165,180,175])
mean = np.mean(data)
standard_deviation = np.std(data)
print("Z score normalization",(data - mean)/standard_deviation)
print("reshape",np.reshape(1,-1))
