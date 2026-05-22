import math
x=4

def is_prime(y):
    if (y<=1):
        return False
    elif (y==2):
        return True
    elif (y%2==0):
        return False

    limit=int(math.sqrt(y))+1

    for i in range (3,limit,2):
          if (y%i==0):
            return False
    return True


if(x%2==0):
    print("x is even")
else:
    print("x is odd")

if(x%3/5==0):
    print("x is divisble by 3/5")


if(is_prime(x)):
    print("number is prime")
else:
    print("number is not prime")
