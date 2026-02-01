import random
print(" WELCONE TO NUMBER GEUSSING GAME: ")
print("I am thinking of a number betwwen 1 to 10:")
secret_number = random.randint(1 , 10)
chances = 7
score = 0
while chances > 0:
    print("\nRemaing chances :",chances)
    guess = int(input("enter your guess :"))
    if guess == secret_number:
        score = chances*10
        print("Comgratulation ! you guessed it right")
        print(" Your Score :",score)
        break
    elif guess < secret_number:
        print("Too High ! ")
    else:
        print("Too Low !")
    chances -= 1
    if chances == 0:
        print("/n Game Over ")
        print(" The correct number was :")