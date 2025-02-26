numbers = [1,2,3,4,5]
for number in numbers:
    print(f"Nummer : {numbers[2]}")


for i in range (5):
    print(i)


try:
    number = int(input("Ange ett heltal: "))
    print(f"Du skrev in : {number}")
except ValueError:
    print("Fel: Du måste ange ett heltal!")