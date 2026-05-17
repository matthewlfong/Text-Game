import random

#helper function for status
def show_status(health, inventory):
    print("\n" + "-"*20)
    print("Health:", health)
    print("Inventory:", inventory)
    print("-"*20 + "\n")

#dictionary of items
items = {
    "small potion": {"type": "heal", "value": 15},
    "medium potion": {"type": "heal", "value": 30},
    "large potion": {"type": "heal", "value": 70},
    "blazing sword": {"type": "weapon", "value": 50},
    "sword": {"type": "weapon", "value": 20},
    "spear": {"type": "weapon", "value": 25},
    "club": {"type": "weapon", "value": 10},
    "stick": {"type": "weapon", "value": 5},
    "knife": {"type": "weapon", "value": 15},
    "fireball": {"type": "spell", "value": 20},
    "lightning": {"type": "spell", "value": 20},
    "leather armor": {"type": "armor", "value": 5},
    "chain armor": {"type": "armor", "value": 10},
    "plate armor": {"type": "armor", "value": 20},
    "dragon armor": {"type": "armor", "value": 50}
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

enemies_list = ["slime", "goblin", "bandit"]
items_list = ["small potion", "sword", "stick"]

while True:
    inventory = ["stick", "leather armor", "small potion"] #starting items and values
    health = 100
    game_over = False
    game_state = "exploration"

    print("Welcome to your adventure!\n")

    print("You wake up in a dark forest. The trees block most of the sunlight.")
    print("You hear distant sounds... something is moving.\n")

    enemy = None

    while not game_over:
        #exploration mode
        if game_state == "exploration":
            print("\nYou are wandering...")

            print("1. Explore")
            print("2. Check status")

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
        
        #combat mode
        elif game_state == "combat":

            print(f"\nYou are fighting a {enemy}!")
            print("1. Attack")
            print("2. Run")
            print("3. Use potion")

            choice = input()

            #ARMOR CALC 
            armor_value = 0
            for item in inventory:
                if items[item]["type"] == "armor":
                    armor_value = max(armor_value, items[item]["value"])

            #WEAPON CALC
            weapon_damage = 5
            for item in inventory:
                if items[item]["type"] == "weapon":
                    weapon_damage = max(weapon_damage, items[item]["value"])

            if choice == "1":
                print("You attack!")

                enemy_hp -= weapon_damage
                print("You deal", weapon_damage, "damage.")

                if enemy_hp <= 0:
                    print("You defeated the enemy!")
                    game_state = "exploration"

                else:
                    damage = max(0, enemies[enemy]["damage"] - armor_value)
                    health -= damage
                    print("Enemy hits you for", damage)

            elif choice == "2":
                print("You ran away!")
                game_state = "exploration"

            elif choice == "3":
                potions = [i for i in inventory if items[i]["type"] == "heal"]

                if len(potions) == 0:
                    print("No potions!")
                else:
                    potion = potions[0]
                    heal_amount = items[potion]["value"]

                    health += heal_amount
                    inventory.remove(potion)

                    print("You used", potion, "and healed", heal_amount)


        if health <= 0: 
            print("You died!")
            game_over = True

    again = input("Play again? Enter yes or no.")
    if again != "yes":
        break
    
    
        


