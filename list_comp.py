x=[4,3,6,7,8]
print("squared list")
sq=[i**2 for i in x]
print(sq)

print("odd filtered list")
odd=[i for i in x if i%2!=0]
print(odd)

print("flatten list")
list_2=[[1,2,33],[2,5,4]]
flatten_list=[item for innerlist in list_2 for item in innerlist]
print(flatten_list)