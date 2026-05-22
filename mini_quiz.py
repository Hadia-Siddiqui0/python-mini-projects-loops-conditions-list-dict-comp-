score=0

a=input("Who is our Lord?")
b=input("Who is our Prophet?")
c=input("Which is the last revelation?")
d=int(input("how many main revleations are there"))

if (a=="ALLAH TALA"):
    score=score+1

if (b=="Muhammad SAW"):
    score=score+1

if (c=="Quran"):
    score=score+1

if (d==4):
    score=score+1

total_score=score
print(score)