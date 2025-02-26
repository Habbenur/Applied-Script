import random

def start_game():
    player_health = 100
    current_location = "start"
    monster_alive = True
    
    locations = {
        "start": {"description": "Du står vid en korsning.", "paths": {"norr": "skog", "öster": "grotta"}},
        "skog": {"description": "Du är i en tät skog.", "paths": {"söder": "start", "öster": "slott"}},
        "grotta": {"description": "En mörk och fuktig grotta.", "paths": {"väster": "start", "norr": "monster"}},
        "monster": {"description": "Här väntar ett skrämmande monster!", "paths": {"söder": "grotta"}},
        "slott": {"description": "Du ser ett vackert slott i fjärran.", "paths": {"väster": "skog"}},
    }
    
    while True:
        print(f"\n{locations[current_location]['description']}")
        if current_location == "monster" and monster_alive:
            print("Ett monster anfaller!")
            player_health = fight_monster(player_health)
            if player_health <= 0:
                print("Du dog! Spelet är över.")
                break
            else:
                print("Du besegrade monstret!")
                monster_alive = False
        
        if current_location == "slott" and not monster_alive:
            print("Grattis! Du har nått slottet och vunnit spelet!")
            break
        
        command = input("Vad vill du göra? (gå norr/söder/öster/väster): ").strip().lower()
        if command in locations[current_location]["paths"]:
            current_location = locations[current_location]["paths"][command]
        else:
            print("Du kan inte gå dit!")

def fight_monster(player_health):
    monster_health = 50
    while monster_health > 0 and player_health > 0:
        attack = random.randint(5, 20)
        monster_health -= attack
        print(f"Du slog monstret för {attack} skada. Monstrets hälsa: {max(monster_health, 0)}")
        
        if monster_health > 0:
            monster_attack = random.randint(5, 15)
            player_health -= monster_attack
            print(f"Monstret attackerar dig för {monster_attack} skada. Din hälsa: {max(player_health, 0)}")
    
    return player_health

if __name__ == "__main__":
    start_game()
