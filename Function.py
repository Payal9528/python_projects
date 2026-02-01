def Calc_sum( a,b,c):
    sum = a+b+c
    return sum  
# taking input from user
num1 = int(input("enter the first number "))   
num2 = int(input("enter the second number "))
num3 = int(input("enter the third number "))    
#caling the function
total = Calc_sum(num1,num2,num3)
#printing the total sum
print("the total sum of three number is ", total)
#angain function call
total = Calc_sum(10,20,30)      
print("the total sum of three number is ", total)
