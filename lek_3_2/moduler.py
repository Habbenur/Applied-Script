with open ("exempel.txt", "w") as file:
    file.write("Hej från Python!")

with open ("exempel.txt", "r") as file:
    print(file.read())

import minmodul

print(minmodul.hej("Habbe"))