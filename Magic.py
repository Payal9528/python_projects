import pdb  
x = int(input("enter first number:"))
y = int(input("enter second number:"))
sum = x + y
print("Sum = ",sum)
def even_sum(num):
    total = 0
    for n in num:
        if n %2 == 0:
            total += n
    return total
nums = [ 10 , 20 , 30 , 25]
#dubugging start
pdb.set_trace()
result = even_sum(nums)
print(" sum of even number", result)
