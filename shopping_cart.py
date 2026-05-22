cart=[]
total=0
while True:
    menu=int(input("1.want to shop?\n"
                   "2.want to remove item from cart?\n"
                   "3.calculate total?\n"
                   "4.want to exit"))
    if(menu==1):
        while True:
            item=int(input("1.bannana for rs 50\n"
                           "2.mango for rs 200\n"
                           "3.water bottle for rs 50\n"
                           "4.salad for rs 70\n"
                           "5.back to main menu"))
            if(item==1):
                cart.append("bannana")
                total = total + 50
                print("ALHAMDULILAH! bannana added")
            elif(item==2):
                cart.append("mango")
                total=total+200
                print("ALHAMDULILAH! mango added")
            elif(item==3):
                cart.append("water bottle")
                total=total+50
                print("ALHAMDULILAH! water bottle added")
            elif(item==4):
                cart.append("salad")
                total=total+70
                print("ALHAMDULILAH! salad added")
            elif(item==5):
                print("ALHAMDULILAH!done")
                break
            else:
                print("no such item, you want to go out then press 5")
    elif(menu == 2):
        rem=input("enter item you want to remove from cart? ")
        if rem in cart:
            cart.remove(rem)
            print("ALHAMDULILAH! item removed")
        elif rem not in cart:
            print("this item is not in cart")
        else:
            print("cart is empty")
    elif(menu==3):
        for item in cart:
            print(f"your items are: {item}")
        print(f" and your total is {total}")
    elif(menu==4):
        print("ALLAH HAFIZ")
        break
            