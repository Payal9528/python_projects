number = list(map(int ,input("number input karo:").split()))
operator = ("Operator(+ - * / // % **):")
result = number[0]

for n in number[:1]:
    if operator == "+" :
        result += n
    elif operator =="-" :
        result -=n
    elif operator == "*" :
        result *= n
    elif operator == "/" :
        result /= n
    elif operator == "//" :
        result //= n 
    elif operator == "%" :
        result %= n
    elif operator == "**" :
        result **= n
print("Result: ",result)
