import numpy as np
#weekly sales data :sales of 5 week 
sales = np.array([100,120,130,90,150])
# calculate persentage
growth_persentage = ((sales[1:] - sales[:1])/sales[:1]*100)
#Display result 
for i , growth in enumerate(growth_persentage ,start=2):
  print(f"Week {i} growth compare to week {i -1}:{growth :2f} %")
  max_sales = np.max(sales)
# find  weekly 
week_high = np.argmax(sales)+1
print("high sales", max_sales)
print("weekly high sales",week_high)
