import numpy as np
in_array = [1,3,4,5,2**8]
print("Input array :", in_array)
out_array = np.log(in_array)
print("Output array :" ,out_array)
print("\n np.log(4**4):", np.log(4**4))
print("np.log(2**4)", np.log(2**4))
print(np.expm1(in_array))

# calculate 2***p
print(np.exp2(in_array))

# log10
print(np.log10(in_array))

#log2
print(np.log2(in_array))

print(in_array(np.add(2,4)))