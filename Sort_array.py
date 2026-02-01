nums = [ 5 , 2 , 9 , 1 , 3 ]
nums.sort()
print(nums)

def f( x = []):
    x.append(1)
    return x
print(f(),f())


a = [ 1,2,3]
b = a 
c = a[:]
b += [4]
c.append(5)
print( a, b ,c)


# a,b,c,d= list(map(int,input().split()))
# avg = ( a + b + c + d)/4
# print(avg)
