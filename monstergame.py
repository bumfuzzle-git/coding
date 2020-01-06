def monstergame():
    player = {"name":"", "attack": 10, "heal": 16, "health": 100}
    monster = {"name": "Dragon", "attack_min": 12, "attack_max": 20, "health": 100}
    game_running = True

    while game_running == True:
        new_round = True
        player = {"attack": 10, "heal": 16, "health": 100}
        monster = {"name": "Dragon", "attack": 12, "health": 100}

        print("--Fight_the_monster--")
        print("Enter Player name: ")
        player["name"] = input()

        print(player["name"] + " has " + str(player["health"]) +  " health")
        print(monster["name"] + " has " + str(monster["health"]) +  " health")
        print("---" * 9)
        while new_round == True:

            player_won = False
            monster_won = False

            print("Please select an action")
            print("1) Attack")
            print("2) Heal")

            player_choice = input()

            if player_choice == "1":
                monster["health"] = monster["health"] - player["attack"]
                if monster["health"] <= 0:
                    player_won = True
                else:
                    player["health"] = player["health"] - monster["attack"]
                    if player["health"] <= 0:
                        monster_won = True

            elif player_choice == "2":
                print("Heal player")
                player["health"] = player["health"] + player["heal"]

                player["health"] = player["health"] - monster["attack"]
                if player["health"] <= 0:
                        monster_won = True

            elif player_choice == "3":
                new_round = False
                game_running = False

            elif player_choice == "4":
                print("new game")
                monstergame()

            else:
                print ("""
    HELP
    Press 1 - to attack
    Press 2 - to heal
    Press 3 - to exit the game
    Press 4 - for a new game
                    """)

            if player_won == False and monster_won == False:
                print(player["name"] + " has " + str(player["health"]) + " left")
                print(monster["name"] + " has " + str(monster["health"]) + " left")
            
            elif player_won:
                print(player["name"] + " won")
                new_round = False

            elif monster_won:
                print("The Monster won")
                new_round = False

monstergame()