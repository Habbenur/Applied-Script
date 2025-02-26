# def log_operator (a, b, c):
#    a = bool(input("Är det sant? True/False"))
#    b = bool(input("Är det sant? True/False"))
#    c = bool(input("Är det sant? True/False"))
#    if a == True or b == True or c == True:
#       return True

# x = log_operator(True, True, False)
# print(x)

def log_operator (a, b, c):
    counter = 0
    if a:
        counter += 1
    if b:
        counter += 1
    if c:
        counter += 1
    if counter > 1:
        return True
    else:
        return False
    
print(log_operator(True,True,False))
print(log_operator(True, False, True))
