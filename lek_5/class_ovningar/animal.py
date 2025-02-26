class Animal:
    def __init__(self, species, age):
        self.species = species
        self.age = age


#övning2: Jag har skapat en funktion för övning 2 och övning 3.
    def describe (self):
        return f"Djurens art : {self.species}, och {self.age} år gammal "  
    
#övning4: Jag har skapat en funktion för övning 4.    
    def __str__ (self):
        return f"Djuren : {self.species}, {self.age}"
    
