# typle demonstration program 
# creat tuple
t = ( 10 , 20 , 30 , 40 , 50 , 60 , 70)
print("Oreginal tuple:",t)
# lenth of tuple 
print("Length :",len(t))

#count of tuple 

print(" count of 20:",t.count(20))

#imndex function
print("Index of 30 :" ,t.index(30))
# access using index 
print("first element:",t[0])
print("Last element :", t[-1])
# loop 
print("element uding loop :")
for i in t:
    print(i)
# slicing
print("slicing  [1:4]",t[1:4])
# membership test 
print("Is 40 in tuple: ",40 in t)
print("Is 100 in tuple :",100 in t)
# built in function 
print("Maximum:", max(t))
print("minumum :" ,min(t))
print(" sum of element :",sum(t))

# short tuple 
sorted_t = sorted(t)
print("shorted tuple:" ,sorted_t)
# tuple packing 
packed =  1, 2, 3
print("packed tuple:",packed)
#unpacked 
a , b , c = packed
print("unpacked tuple :", a , b, c)
# nested tuple
nested = (1 , (2 , 3), 4)
print("Nested tuple:",nested)
print("Aeccess nested value:",nested[1][0])

# tuple concatenation
t2 = ( 50 , 60)
new_tuple = t + t2
print("Repeated tuple :",new_tuple)
# tuple repetition
repeat_tuple = t2 * 3
print("Repeated tuple:",repeat_tuple)
#any() and all()
print("Any true ",any(t))
print("all true :", all(t))
# enumerate()
print("Using enumerate :")
for index , value in enumerate(t):
    print(index, value)
    # zip 
names = (" ram" , "payal" ,"khushi")
marks = (80 , 85 , 90 )
zipped = tuple(zip(names , marks))
print("Zipped tuple :",zipped)
# convert list to tuple
lst = [1 , 2 , 3]
tuple_from_list = tuple(lst)
print("List to tuple :",tuple_from_list)
# conver tuple to list 
list_from_tuple = list(t)
print("Tuple to list :", list_from_tuple)
# tuple immutability  demonstraction
print(" Tuple is immutable , cannot modify element")