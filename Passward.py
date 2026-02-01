import re
pwd = input(" EMNTER YOUR PASSWARD:")
if (len(pwd) >= 12 and
    re.search("[A-Z]",pwd) and
    re.search("[a-z]",pwd) and
    re.search("[0-9]",pwd) and
    re.search("[!@#$%^&*_-]",pwd)):
    print(" very strong passward")
elif (len(pwd)>=10 and
      re.search("[A-z]",pwd) and
      re.search("[a-z]",pwd) and
      re.search("[0-9]",pwd)):
    print("you normal passward")
    
else:
    print(" weak passward")
print(type(re))
a= 10
b = 3
print(a//b)