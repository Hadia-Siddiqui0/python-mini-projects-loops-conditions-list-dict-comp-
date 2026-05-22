n=int(input("a number:"))
# square pattern
# for i in range (n):
#     for j in range(n):
#         print("*",end="")
#         # j=j+1
#     print()

# triangle pattern
for i in range (n):
    for j in range(n-i):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
        # j=n-j
    print()

