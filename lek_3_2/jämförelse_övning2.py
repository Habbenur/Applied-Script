def comparison(a,b):
    if a < b :
        print (f"{a}, mindre än {b}")
    elif a > b :
        print (f"{a}, större än {b}")
    else:
        print (f"{a} och {b} är likamed.")

x = input("Ange ett heltal : \n")
y = input("Ange ett andra heltal : \n")
comparison(x,y)    

