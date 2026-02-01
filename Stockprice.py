import numpy as np
price = np.array([100,102,98,97,105,110,108,107,111,115])
daily_retern = ((price[1:] -price[-1:] /price[-1])*100)
print("Daily return persentage", daily_retern)
window_size = 3
moving_avg = np.convolve(price,np.ones(window_size)/window_size,mode='valid')
print("Moving avg  windows size 3",moving_avg)
