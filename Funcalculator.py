# # Addition
# numbers = float(input("enter the numbers"))
def add(*numbers)  :
    return sum(numbers)
# subtraction
def subtract(*numbers):
    result  = numbers[0]
    for n in numbers[1:] :
        result -= 1
        return result
#multiple
def multiple(*numbers):
    result  = 1
    for n in numbers:
        result *= n
        return result
#devision 
def devide(*numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result /= n
        return result 
    #       USER INPUT 
    while True:
        user_input = input("number with space")
        if user_input.strip() == "":
            print(" enter any number!")
        else:
            numbers = list(map(float, user_input.split()))
            break
    numbers = float(input("enter the number"))
    print("Additin = ",add(*numbers))
    print("Subtract = ",subtract(*numbers))
    print("Multiple = ",multiple(*numbers))
    print("Devision = ",devide(*numbers))