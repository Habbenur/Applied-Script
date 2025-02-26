# def trying ():
#     while True: 
#         try:
#             number = int(input("Ange ett heltal: \n"))
#             return number
#         except ValueError:
#             print("Fel! Vänligen ange ett giltigt tal!")


def heltal():
    a = input("Skriv ett heltal : ")
    try:
        int(a)
        print(f"Du skrev in {a}")
        return True
    except:
        print(f"Du skrev in o giltigt tal!")
        return False
while True:
    print(heltal())

        