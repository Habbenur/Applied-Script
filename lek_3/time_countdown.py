import time

counter = 5
print("Start!")
while counter > -1:
    time.sleep(1)
    print(counter)
    counter -= 1
print("Time is out!")