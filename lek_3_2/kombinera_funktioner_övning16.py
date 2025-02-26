def get_name ():
    name = input("Ange ditt namn : ")
    return name
def get_age():
    while True: 
        try:
            age = int(input("Ange din ålder : "))
            return age
        except ValueError:
            print("Fel! Vänligen ange en giltig ålder.")

def present():
    name = get_name()
    age = get_age()
    print(f"Hej! Jag heter {name} och är {age} år gammal")

present()
