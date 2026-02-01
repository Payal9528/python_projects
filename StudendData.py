import numpy as np
marks = np.array([45,67,89,76,56])
print("Average",np.mean(marks))
print( "Total sum",np.sum(marks)) #sum 
mediam_marks = np.median(marks) # median
print("Median" ,mediam_marks)
print("Standerd diviation",np.std(marks)) # standard divation
narmilize_marks = (marks - np.min(marks)/(np.max(marks) - np.min(marks)))
print("Narmilize marks",narmilize_marks)