import random
import time

def tarning ():
    tarning1 = random.randint(1,6)
    tarning2 = random.randint(1,6)
    tarning3 = random.randint(1,6)
    tarning4 = random.randint(1,6)
    return tarning1, tarning2, tarning3, tarning4
    

player1 = input("Ange första spelare: \n")
player2 = input("Ange andra spelare: \n")


tarning1, tarning2, tarning3, tarning4 = tarning()
counter = 5
print("Start!")
while counter > -1:
    time.sleep(1)
    print(counter)
    counter -= 1
print("Time is out!")
print(f"{player1} : {tarning1}")
counter = 5
print("Start!")
while counter > -1:
    time.sleep(1)
    print(counter)
    counter -= 1
print("Time is out!")
print(f"{player2} : {tarning2}")
counter = 5
print("Start!")
while counter > -1:
    time.sleep(1)
    print(counter)
    counter -= 1
print("Time is out!")
print(f"{player1} : {tarning3}")
counter = 5
print("Start!")
while counter > -1:
    time.sleep(1)
    print(counter)
    counter -= 1
print("Time is out!")
print(f"{player2} : {tarning4}")

if tarning1+tarning3 > tarning2+tarning4:
    print(f"Vinnaren är : {player1}")
elif tarning1+tarning3 == tarning2+tarning4:
    print("Oavgjort!")
else:
    print(f"Vinnaren är {player2}")


