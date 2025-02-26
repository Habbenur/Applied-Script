def result (a):
    
    if 90 <= a <= 100:
        print("Du fick 'A")
    elif 80 <= a <= 89:
        print("Du fick 'B")
    elif 70 <= a <= 79:
        print("Du fick 'C")
    elif 60 <= a <= 69:
        print("Du fick 'D")
    elif 0 <= a < 60:
        print("Du fick 'F")
    else:
        print("Du skrev in ogiltigt poäng!")

user_input = int(input("Ange ett poäng : \n"))
result(user_input)