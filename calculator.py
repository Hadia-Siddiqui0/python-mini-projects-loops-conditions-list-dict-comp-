x=int(input("enter a number:"))
y=int(input("enter another number:"))
op=input("enter a operand:")

if (op=="+"):
    a=x+y
    print(a)
elif (op=="-"):
    a=x-y
    print(a)
elif (op=="*"):
    a=x*y
    print(a)
elif (op=="/"):
    a=x/y
    print(a)
else:
    print("not an acceptable operator")
