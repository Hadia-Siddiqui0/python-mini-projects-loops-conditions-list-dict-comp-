to_do=[]

while True:
    menu=int(input("1. add item in list\n"
                   "2. want to remove an item from list\n" 
                   "3. want to view your list\n" 
                   "4. you want to exit the programe\n"))
    
    if(menu==1):
        task=input("enter a item: ")
        to_do.append(task)
        print("ALHAMDULILAH! added")
    elif(menu==2):
        rem=input("enter a item you want to remove: ")
        if rem in to_do:
            to_do.remove(rem)
            print("ALHAMDULILAH! task removed")
        else:
            print("there is not task with this name")
    elif(menu==3):
        if not to_do:
            print("no task exist")
        else:
            print(f"here is your list: {to_do}")
    elif(menu==4):
        print("ALAH HAFIZ! have a best life")
        break
    else:
        print("choose any number from the list")
    

