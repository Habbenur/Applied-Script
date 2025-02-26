import datetime
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


    def car_age (self):
        now = datetime.datetime.now()
        now_year = now.year
        return  now_year - self.year 

