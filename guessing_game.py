import random

n=None
num=random.randint(1,100)

while n!=num:
    n=int(input("enter a number:"))
    if (n==num):
        print("you guessed it right")
        break
    elif (n<num):
        print("you guessed it wrong! increase the number")    
    else:
        print("you guessed it wrong! decrease the number")
