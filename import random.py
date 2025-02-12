import random
a = random.randint(1, 10)
print(int(a))
def userguess(): 
    userguess = int(input("Gissa ett nummer"))
    return userguess

print(userguess())
while True:
    guess = userguess()
    if guess == a:
        print("Congratulations! You guessed it!")
        break
    else:
        print("try again")