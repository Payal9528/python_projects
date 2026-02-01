import random as rn
n = int(input("enter the andom number"))
numbers = []
for i in range(n):
  numbers.append(rn.randint(1,20))
  print("Random numbers:" ,numbers)
  # sum 
  add = sum(numbers)
  # sub
  sub = numbers[0]
  for num in numbers[1:]:
    sub -= num
    #mult
    mult = 1
    for num in numbers:
      mult *= num
      #div
      div = numbers[0]
      for num in numbers[1:]:
        div /= num
        print("add = ",add)
        print("sub = " ,sub)
        print("mult = ",mult)
        print("div = " ,div)
#show opration 
# print("choose opreation:")
# print("1. addition(+):")
# print("2.Subtraction(-):")
# print("3. Multiple(*): ")
# print("4. Divide(/): ")
# choice = input("enter your choice(1/2/3/4): ")
# #perform calculation
# if choice == "1" :
#   print("Result = ", num1+num2)
# elif choice == "2" :
#   print("Result = ", num1-num2)
# elif choice == "3" :
#   print("Result = ", num1*num2)
# else :
#   print("Invalid choice") 