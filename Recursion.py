# import math 
# lower = int(input("enter the lower range :"))
# upper = int(input("enter the upper range:"))
# print(" PRIME NUMBER :")
# for num in range(lower, upper+1):
#     if (num>1):
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)
#             print(math.comb(num))


start = int(input("Range ka start number daalein: "))
end = int(input("Range ka end number daalein: "))

prime_numbers = []  # Prime numbers ko store karne ke liye list

# Loop har number ke liye
for num in range(start, end + 1):
    if num > 1:  # 1 se bada number hi prime ho sakta hai
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # sqrt(num) tak check karna kaafi hai
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

# Output
print(f"Prime numbers in range {start} to {end}:")
print(prime_numbers)
print(f"Total prime numbers: {len(prime_numbers)}")