from arenaGameFunction import *

print ("Welcome to the arena!" ,player.name, "Let the games begin!.")
if player.name == "anneopen":
    print ("GM çarı activated")
    player.hp = 99999
    player.atak = 99
    player.damage = 99
time.sleep(3)
print ("A", mob1.name, "appears!")


while True:
    print ("Your turn!")
    action = input ("What is your action? > ")

    if action.lower() == "attack":
        attack(player,mob1)

        if mob1.hp <= 0:
            print (mob1.name, "is dead! Cheers to", player.name ,"!" "Rest well, and get ready for the next round.")
            time.sleep(1)
            if player.hp < 26: player.hp = 26
            levelup()

            print ("Well done. The arena continues...")

            time.sleep(2)

            print ("Here comes the second opponent of the champion,", player.name, "!")
            time.sleep(1)
            print ("A", mob2.name ,"approaches!")
            time.sleep(1)

            while True:
                    healc = 1
                    print("Your turn!")
                    action = input("What is your action? > ")

                    if action.lower() == "attack":
                        attack(player,mob2)

                        if mob2.hp <= 0:
                            print(mob2.name, "is dead! Cheers to", player.name,
                                  "!" "Rest well, and get ready for the next round.")
                            time.sleep(1)
                            if player.hp < 36: player.hp = 36
                            levelup()

                            print ("You now have an action called 'heal' , if you type heal, you heal yourself for 10 hp."
                                   "Only available once per fight at the moment.")
                            input ("Press anything to continue...")
                            print("Well done. The arena continues...")

                            time.sleep(2)

                            print("Here comes the third opponent of the champion,", player.name, "!")
                            time.sleep(1)
                            print("A", mob3.name, "approaches!")
                            time.sleep(1)

                            while True:
                                print("Your turn!")
                                action = input("What is your action? > ")
                                if action.lower() == "attack":
                                    attack(player,mob3)

                                    if mob3.hp <= 0:
                                        print(mob3.name, "is dead! Cheers to", player.name,
                                              "!" "Rest well, and get ready for the next round.")
                                        time.sleep(1)
                                        if player.hp < 46: player.hp = 46
                                        levelup()
                                        healc = 2
                                        input("You can now use heal twice. Press anything to continue...")
                                        print("Well done. The arena continues...")

                                        time.sleep(2)

                                        print("Here comes the fourth opponent of the champion,", player.name, "!")
                                        time.sleep(1)
                                        print("A", mob4.name, "approaches!")
                                        time.sleep(1)

                                        while True:
                                            print("Your turn!")
                                            action = input("What is your action? > ")
                                            if action.lower() == "attack":
                                                attack(player,mob4)
                                                if mob4.hp <= 0:
                                                    print(mob4.name, "is dead! Cheers to", player.name,
                                                          "!" "Rest well, and get ready for the next round.")
                                                    time.sleep(1)
                                                    if player.hp < 56: player.hp = 56
                                                    levelup()
                                                    healc = 2
                                                    input("You can now use heal without consuming turns. Press anything to continue...")
                                                    print("Well done. The arena continues...")
                                                    time.sleep(2)

                                                    print("Here comes the fifth and final opponent of the champion,",
                                                          player.name, "!")
                                                    time.sleep(1)
                                                    print(mob5.name, "approaches!")
                                                    time.sleep(1)
                                                    while True:
                                                        print("Your turn!")
                                                        action = input("What is your action? > ")
                                                        if action.lower() == "attack":
                                                            attack(player,mob5)
                                                            if mob5.hp <= 0:
                                                                print(mob5.name, "is dead! Cheers to", player.name
                                                                      )
                                                                print ("YOU ARE THE CHAMPION, YOU WON!")
                                                                print ("WEEEEEEEEEEEEE ARE THE CHAMPIOOOONS")
                                                                time.sleep(1)
                                                                print ("MY FRIEEENDSSSS")
                                                                time.sleep(1)
                                                                print ("The game is over, thank you for playing!")
                                                                print(
                                                                    "The game will be closed automatically in 10 sec...")
                                                                time.sleep(10)
                                                                exit()


                                                            else:
                                                                attack(mob5,player)

                                                                if player.hp <= 0:
                                                                    print(player.name,
                                                                          "is dead! Game over! Your score : 4")
                                                                    print(
                                                                        "The game will be closed automatically in 10 sec...")
                                                                    time.sleep(10)
                                                                    exit()
                                                                else:
                                                                    continue

                                                            attack(mob5,player)
                                                            if player.hp <= 0:
                                                                print(player.name, "is dead! Game over! Your score : 3")
                                                                print(
                                                                    "The game will be closed automatically in 10 sec...")
                                                                time.sleep(10)
                                                                exit()
                                                            else:
                                                                continue

                                                        elif action.lower() == "heal" and healc > 0:
                                                            player.hp += 10
                                                            print("You healed for 10 hit points. Current hp:",
                                                                  player.hp)
                                                            healc -= 1
                                                        elif action.lower() == "heal" and not healc > 0:
                                                            print("You already used your heals for this round.")
                                                        elif action.lower() == "pass":
                                                            attack(mob5,player)
                                                            if player.hp <= 0:
                                                                print(player.name, "is dead! Game over! Your score : 3")
                                                                print(
                                                                    "The game will be closed automatically in 10 sec...")
                                                                time.sleep(10)
                                                                exit()
                                                            else:
                                                                continue

                                                        else:
                                                            print(
                                                                "Please enter an action. Available actions at the moment: 'pass,','attack' and 'heal' ")

                                                else:
                                                    attack(mob3,player)

                                                    if player.hp <= 0:
                                                        print(player.name, "is dead! Game over! Your score : 3")
                                                        print("The game will be closed automatically in 10 sec...")
                                                        time.sleep(10)
                                                        exit()
                                                    else:
                                                        continue

                                            elif action.lower() == "heal" and healc >0:
                                                player.hp += 10
                                                print("You healed for 10 hit points. Current hp:", player.hp)
                                                healc -= 1
                                                time.sleep(1)

                                                attack(mob4,player)
                                                if player.hp <= 0:
                                                    print(player.name, "is dead! Game over! Your score : 3")
                                                    print("The game will be closed automatically in 10 sec...")
                                                    time.sleep(10)
                                                    exit()
                                                else:
                                                    continue
                                            elif action.lower() == "heal" and not healc > 0:
                                                print("You already used your heals for this round.")
                                            elif action.lower() == "pass":
                                                 attack(mob4,player)
                                                 if player.hp <= 0:
                                                     print(player.name, "is dead! Game over! Your score : 3")
                                                     print("The game will be closed automatically in 10 sec...")
                                                     time.sleep(10)
                                                     exit()
                                                 else:
                                                    continue

                                            else:
                                                print(
                                                    "Please enter an action. Available actions at the moment: 'pass,','attack' and 'heal' ")


                                    else:
                                      attack(mob3,player)

                                      if player.hp <= 0:
                                         print(player.name, "is dead! Game over! Your score : 2")
                                         print("The game will be closed automatically in 10 sec...")
                                         time.sleep(10)
                                         exit()
                                      else:
                                        continue

                                elif action.lower() == "heal" and healc >0:
                                    player.hp += 10
                                    print ("You healed for 10 hit points. Current hp:", player.hp)
                                    healc -= 1
                                    time.sleep(1)

                                    attack(mob3,player)

                                    if player.hp <= 0:
                                        print(player.name, "is dead! Game over! Your score : 2")
                                        print("The game will be closed automatically in 10 sec...")
                                        time.sleep(10)
                                        exit()
                                    else:
                                        continue

                                elif action.lower() == "heal" and not healc >0:
                                    print ("You already used your heal for this round.")
                                elif action.lower() == "pass":
                                    attack(mob3,player)
                                    if player.hp <= 0:
                                        print(player.name, "is dead! Game over! Your score : 2")
                                        print("The game will be closed automatically in 10 sec...")
                                        time.sleep(10)
                                        exit()
                                    else:
                                        continue
                                else:
                                    print("Please enter an action. Available actions at the moment: 'pass,','attack' and 'heal' ")

                        else:
                         attack(mob2,player)
                         if player.hp <= 0:
                            print(player.name, "is dead! Game over! Your score : 1")
                            print("The game will be closed automatically in 10 sec...")
                            time.sleep(10)
                            exit()

                         else:
                            continue
                    elif action.lower() == "pass":
                        attack(mob2,player)
                    else:
                     print("Please enter an action. Available actions at the moment: 'attack' ")


        else:
            attack(mob1,player)
            if player.hp <= 0:
                player_dies()
            else:
                continue

    elif action.lower() == "pass":
        attack(mob1, player)
    else:
        print("Please enter an action. Available actions at the moment: 'pass','attack' ")
