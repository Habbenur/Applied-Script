try:
    användaren = int(input("Skriv ett heltal : "))
    print(f"Du skrev in : {användaren}")
except ValueError:
    print("Du måste skriva ett heltal!")

