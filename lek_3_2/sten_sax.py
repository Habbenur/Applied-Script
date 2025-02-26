



# if user_choice == "påse":
#     print(f"Du vann och valde {user_choice}")
# elif user_choice == "sax":
#     print("Du förlorade, datorn valde", computer)
# else:
#     print("Oavgjort")




computer = "sten"


while True:

        user_choice = input("sten, sax eller påse?")
        if user_choice == "sax":
            print("Du förlorade!")
        elif user_choice == computer:
            print("Oavgjort!")
        elif user_choice == "påse":
           print("Du vann!")
           break
        else:
             print("Ange bara 'sten, sax eller påse'")
    

