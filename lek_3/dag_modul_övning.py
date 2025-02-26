import datetime

def day_now ():
    day = datetime.datetime.now()
    print(day.strftime("%B"))

print(day_now())