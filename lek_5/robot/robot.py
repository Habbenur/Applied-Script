class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.started = False
        self.greating = f"Hello! I am {self.name}."

    def start(self):
        self.started = True

    def stop(self):
        self.started = False

#övning2:
    def charge(self):
        self.battery = 100

#övning3:
    def move(self, distance_in_meters):
        for i in range(distance_in_meters):
            self.battery -= 10
            if self.battery <= 0:
                break
    
#övning5:
    def introduce(self):
        return self.greating
    
#övning7:
    def move2(self, distance_in_meters):
        if distance_in_meters < 0:
            raise ValueError("Ett fel inträffade!")  # Kastar ValueError
        
        for _ in range(distance_in_meters):
            if self.battery <= 0:
                break
            self.battery -= 10
        
    def multiple_robots():
    #"""Kontrollerar att alla Robot-objekt i listan har batteri = 100."""
        robots = [Robot("Alpha", 100), Robot("Beta", 100), Robot("Gamma", 100)]
        for robot in robots:
            return robot