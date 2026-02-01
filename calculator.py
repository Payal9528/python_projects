num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))
print("1. Addition :")
print("2. Subtraction :")
print("3. Multipy :")
print("4. Division :")
print("5. Exponetial :")
print("6. FloatDivision :")
print("7. moduls :")
print("8. Queue :")
choice = int(input("enter your choice : (1-8)"))
if choice == 1:
    print("Result :",num1 + num2)
elif choice == 2:
    print("Result :",num1 -num2)
elif choice == 3:
    print("Result :",num1 * num2)
elif choice == 4:
    print("Result :",num1 /num2)
elif choice == 5:
    print("Result :",num1 ** num2)
elif choice == 6:
    print("Result :",num1 // num2)
elif choice == 7:
    print("Result :",num1 % num2)
elif choice == 8:
    print("Result :",num1*num1*num1)
else :
    print("Invalid choice:")