cont_book={}
while True:
    ques=int(input("1.add contact\n" 
                   "2.remove contact\n"
                   "3.search contact\n"
                   "4.see all contacts\n" 
                   "5.exit:"))
    if (ques==1):
        name=input("enter name: ")
        number=input("enter number: ")
        cont_book[name]=number
    elif ques == 2:
        rem_con = input("Enter the contact you want to remove: ")
        if not cont_book:  
            print("Your contact book is empty")
        elif rem_con in cont_book:  
            cont_book.pop(rem_con)
            print(f"ALHAMDULILAH! {rem_con} deleted")
        else:
            print(f"There is no contact named {rem_con}")
    elif(ques==3):
        sea_name=input("enter the name of the person you want to search: ")
        
        if not cont_book:
                print("no contacts in your list")
        elif sea_name in cont_book:
                contact=cont_book.get(sea_name)
                print(f"the contact of {sea_name} is {contact}")
        else:
                print(f"no entry with {sea_name}")               
    elif(ques==4):
        print(cont_book)
    elif(ques==5):
        print("ALHAMDULILAH! ALLAH HAFIZZZ")
        break
    else:
        print("please press correct options")
