class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.started = False

    def start(self):
        self.started = True
    def stop(self):
        self.started = False

