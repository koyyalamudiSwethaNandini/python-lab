import random
a=random.randrange(1,10)
print(a)
b=int(input("Guess a number between 1 and 10 until you get it right:"))
while a!=b:
    b=int(input("Guess a number between 1 and 10 until you get it right:"))
print("Well Guessed")  

    
