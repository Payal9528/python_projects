import numpy as np
import matplotlib.pyplot as plt
# csv data 
data = np.genfromtxt(
    "werther.csv",
    delimiter = ",",
    skip_header = 1
)
print("Data Shape :",data.shape)
print(data[:100]) # first 5 row 
day = data [:,0]
temp = data[:,1]
humidity = data[:,2]
wind = data[:,3]
temp = np.nan_to_num(temp, nan=np.nanmean(temp))
print("Avg temp :",np.mean(temp))
print("Max temp :",np.max(temp))
print("temp min :", np.min(temp))
print(" hum avg :",np.mean(humidity))
print("Wind Avg :",np.mean(data))
plt.figure()
plt.plot(day ,temp)
plt.xlabel("Day")
plt.ylabel("temperature (c)")
plt.title("Temperature Tend Over Days")
plt.show()
plt.figure()
plt.plot(day , temp)
plt.axhline(y=45)
plt.xlabel("Tempreture (C)")
plt.ylabel("Heatwave Detection")
plt.show()
# NaN safer
# creat a figer 
fig , ax1 = plt.subplots()
# temp plot (left y - axis)
ax1.plot( day ,temp)
ax1.set_xlabel(" Days")
ax1.set_ylabel(" Tempertuer (C)")
# secon y-axis for wind
ax2 = ax1.twinx()
ax2.plot( day , wind)
ax2.set_ylabel(" wind speed(km/h)")
plt.title("wheather anlysis : Temperature & wind vs days")
plt.show() 
ax3 = ax2.twinx()
ax3.plot(day , humidity )
ax3.set_ylabel("Humidity (C)")
plt.title("Wherther analysis : temperatire & huminity vs days")
plt.show()