import numpy as np
# creat 5x5 image 
image = np.random.randint(0,226,size =(5,5))
print("Original Image\n", image)
bright_image = image+100
# cap value at 225
bright_image = np.clip(bright_image,0,225)
print("Increase brightness",bright_image)
print(image.shape)