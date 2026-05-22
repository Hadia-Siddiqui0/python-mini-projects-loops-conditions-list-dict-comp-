num=(int(input("enter a number:")))

result=1
for i in range(1,num+1):
    result=result*i

print(f"factorial of {num} is {result}")