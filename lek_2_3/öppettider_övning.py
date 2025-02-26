
dagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag"]
helg = ["Lördag", "Söndag"]

userinput = input("Ange en dag : ")
userinput = userinput.capitalize()
userinput2 = int(input("Ange en tid : "))

if userinput in dagar and 9 <= userinput2 <18 :
    print("Butiken är öppen!")
elif userinput in helg and 10 <= userinput2 <16 :
    print("Butiken är öppen!")
else:
    print("Butiken är inte öppen!")