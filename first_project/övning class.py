class Person:
    def __init__(self, förnamn, efternamn, ålder, kön) :
        self.firstname = förnamn
        self.secondname = efternamn
        self.age = ålder
        self.gender = kön

    def print_info(self):
        print(self.firstname, + " ", self.secondname, + ", ", str(self.age), + ", ", self.gender)

    def get_info(self):
        all_info = [self.firstname, self.secondname, self.age, self.gender]
        return all_info



person_1 = Person("Habbenur", "Özen", 35, "Kvinna")
person_2 = Person("Sauda", "Haque", 27, "Kvinna")
person_3 = Person("Carl", "Stael von Holstein", 27, "Man")
person_4 = Person("Ali Reza", "Hezareh", 25, "Man" )



