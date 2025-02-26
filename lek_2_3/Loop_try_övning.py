

while True: 
    try:
        userinput = int(input("Skriv ett heltal : "))
        
        print(f"Du skrev in {userinput}")
        break
        
    except ValueError:
        print("Ange ett giltigt heltal!")
