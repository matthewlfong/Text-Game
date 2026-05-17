import random
import os

#helper function for status
def show_status(health, inventory):
    print("\n" + "-"*20)
    print("Health:", health)
    print("Inventory:", inventory)
    print("Weapon:", equipment["weapon"])
    print("Armor:", equipment["armor"])
    print("-"*20 + "\n")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

#dictionary of items
items = {
    # ===== POTIONS =====
    "small potion": {"type": "heal", "value": 15},
    "medium potion": {"type": "heal", "value": 30},
    "large potion": {"type": "heal", "value": 70},

    # ===== WEAPONS (basic) =====
    "stick": {"type": "weapon", "value": 5},
    "knife": {"type": "weapon", "value": 10},
    "club": {"type": "weapon", "value": 12},
    "sword": {"type": "weapon", "value": 20},
    "spear": {"type": "weapon", "value": 25},

    # ===== WEAPONS (advanced) =====
    "longsword": {"type": "weapon", "value": 35},
    "blazing sword": {"type": "weapon", "value": 50},
    "dragon blade": {"type": "weapon", "value": 80},

    # ===== ARMOR (light) =====
    "leather armor": {"type": "armor", "value": 5},
    "cloth robe": {"type": "armor", "value": 3},

    # ===== ARMOR (medium) =====
    "chain armor": {"type": "armor", "value": 10},
    "scale armor": {"type": "armor", "value": 15},

    # ===== ARMOR (heavy) =====
    "plate armor": {"type": "armor", "value": 20},
    "dragon armor": {"type": "armor", "value": 50},

    # ===== SPELLS (future-ready) =====
    "fireball": {"type": "spell", "value": 20},
    "lightning": {"type": "spell", "value": 20},
    "ice shard": {"type": "spell", "value": 18}
}

#dictionary of enemies
enemies = {
    "slime": {"hp": 30, "damage": 5},
    "goblin": {"hp": 50, "damage": 10},
    "orc": {"hp": 80, "damage": 15},
    "dragon": {"hp": 200, "damage": 40},
    "knight": {"hp": 120, "damage": 18},
    "bandit": {"hp": 60, "damage": 12}
}

enemies_list = ["slime", "goblin", "bandit", "orc"]
items_list = ["small potion", "medium potion", "stick", "knife", "club", "sword", "leather armor"]

while True:
    inventory = ["stick", "leather armor", "small potion"] #starting items and values
    health = 100
    game_over = False
    game_state = "exploration"
    
    equipment = {
    "weapon": "stick",
    "armor": "leather armor"
    }

    print("Welcome to your adventure!\n")

    print("You wake up in a dark forest. The trees block most of the sunlight.")
    print("You hear distant sounds... something is moving.\n")

    enemy = None

    while not game_over:
        #exploration mode
        if game_state == "exploration":
            print("\n\n\nYou are wandering...")

            print("1. Explore")
            print("2. Check status")
            print("3. Inventory / Equip")

            choice = input()

            if choice == "1":
                print("You move deeper into the forest...")

                event = random.choice(["enemy", "item", "nothing"])

                if event == "enemy":
                    enemy = random.choice(enemies_list)
                    enemy_hp = enemies[enemy]["hp"]
                    print(f"A hostile {enemy} appears!")

                    game_state = "combat"

                elif event == "item":
                    item = random.choice(items_list)
                    inventory.append(item)

                    print(f"You found a {item}!")

                else:
                    print("The forest is quiet... nothing happens.")

            elif choice == "2":
                show_status(health, inventory)
            
            elif choice == "3":
                print("\nInventory:")
                for i, item in enumerate(inventory):
                    print(i + 1, item)

                print("\n1. Equip weapon")
                print("2. Equip armor")
                print("3. Unequip weapon")
                print("4. Unequip armor")

                sub = input()

                if sub == "1":
                    weapons = [i for i in inventory if items[i]["type"] == "weapon"]

                    if not weapons:
                        print("No weapons available.")
                    else:
                        for i, w in enumerate(weapons):
                            print(i + 1, w)

                        pick = input()

                        if pick.isdigit():
                            pick = int(pick) - 1

                            if 0 <= pick < len(weapons):
                                equipment["weapon"] = weapons[pick]
                                print("Equipped", weapons[pick])
                            else:
                                print("Invalid choice.")
                        else:
                            print("Invalid input.")
                
                elif sub == "2":
                    armors = [i for i in inventory if items[i]["type"] == "armor"]

                    if not armors:
                        print("No armor available.")
                    else:
                        for i, a in enumerate(armors):
                            print(i + 1, a)

                        pick = input()

                        if pick.isdigit():
                            pick = int(pick) - 1

                            if 0 <= pick < len(armors):
                                equipment["armor"] = armors[pick]
                                print("Equipped", armors[pick])
                            else:
                                print("Invalid choice.")
                        else:
                            print("Invalid input.")
        
        #combat mode
        elif game_state == "combat":

            print(f"\nYou are fighting a {enemy}!")
            print("1. Attack")
            print("2. Run")
            print("3. Use potion")

            choice = input()

            armor_value = items[equipment["armor"]]["value"] if equipment["armor"] else 0
            weapon_damage = items[equipment["weapon"]]["value"] if equipment["weapon"] else 2

            if enemy is None:
                game_state = "exploration"
                continue

            # PLAYER TURN
            if choice == "1":
                print("You attack!")
                enemy_hp -= weapon_damage
                print("You deal", weapon_damage)

                if enemy_hp <= 0:
                    print("Enemy defeated!")
                    enemy = None
                    game_state = "exploration"
                    continue

            elif choice == "2":
                print("You ran away!")
                enemy = None
                enemy_hp = 0
                game_state = "exploration"
                continue

            elif choice == "3":
                potions = [i for i in inventory if items[i]["type"] == "heal"]

                if not potions:
                    print("No potions!")
                print("Choose potion:")

                for i, p in enumerate(potions):
                    print(i + 1, p)

                pick = input()

                if not pick.isdigit():
                    print("Invalid input.")

                else:
                    pick = int(pick) - 1
                    if 0 <= pick < len(potions):
                        potion = potions[pick]

                        heal_amount = items[potion]["value"]
                        health += heal_amount

                        inventory.remove(potion)

                        print("Healed", heal_amount)

                    else:
                        print("Invalid choice.")

            # ENEMY TURN (ONLY IF STILL IN COMBAT)
            if game_state == "combat" and enemy is not None:
                damage = max(0, enemies[enemy]["damage"] - armor_value)
                health -= damage
                print("Enemy hits you for", damage)


        if health <= 0: 
            print("You died!")
            game_over = True

    again = input("Play again? Enter yes or no.")
    if again != "yes":
        break
    
    
        
