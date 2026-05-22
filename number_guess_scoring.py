import random

user_score={}
while True:
    question=int(input("1. you want to play more:\n"
                       "2. no i am now tired! exit the game"))
    if (question==1):
        name=input("enter your name: ")
        rnd_no=random.randint(1,10)
        score=1
        while True:
            x=int(input("guess the number: "))
            if(x==rnd_no):
                print("ALHAMDULILAH! you guess right")
                break
            elif(x<rnd_no):
                print("please increase it")
            else:
                print("please decrease it")

            score=score+1
            
            user_score[name]=score
    elif(question==2):
        print("okay")
        break
    else:
        print("you pressed the wrong number")
for i in user_score.values():
    first_value=next(iter(user_score.values()))
    if (i<first_value):
        i=first_value
         
print(user_score)
print(f"the highest score is {name,first_value}")

