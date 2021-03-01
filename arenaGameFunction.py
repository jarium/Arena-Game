import random
import time

class Character():
    def __init__(self, hp, ac, atak, damage, name):
        self.hp = hp
        self.ac = ac
        self.atak = atak
        self.damage = damage
        self.name = name

player = Character(16,16,6, random.randint(1,8) + 4, input ("What's your name? >"))
mob1 = Character(9,14,5, random.randint(1,6) + 3, "Bandit")
mob2 = Character(18,16,6, random.randint(1,6) + 3, "Bandit Outlaw")
mob3 = Character(30,16,7, random.randint(1,8) + 5, "Bandit Chief")
mob4 = Character(43,16,8, random.randint(1,8) + 7, "Bandit Lord")
mob5 = Character(65,18,9, random.randint(1,10) + 10, "The King of Bandits")

zar = random.randint(1,20)

def attack(x,y):
    zar = random.randint(1,20)
    attack_roll = zar + x.atak
    print ("Attack action by",x.name,"rolled", zar)
    time.sleep (1)
    if zar == 20:
        print ("CRITICAL HIT! Dealt", x.damage * 2, "points of damage")
        y.hp -= x.damage * 2
        print (y.name,"remaining hp:", y.hp)
        time.sleep(1)
        if y.hp <= 0:
            print(y.name,"dies.")
    elif attack_roll >= y.ac:
        print ("Hit! Dealt", x.damage ,"points of damage")
        y.hp -= x.damage
        print(y.name,"remaining hp:", y.hp)
        time.sleep(1)
        if y.hp <= 0:
            print (y.name,"dies.")
    else:
        print ("The attack by", x.name,"is missed.")

def levelup():
    print("""Congratulations",You grew stronger and gained +10 hp. You may choose one attribute to 
                  improve, before the next fight. Read carefully and choose wisely.
                  
                  Type 1 for +1 Armor
                  Type 2 for +2 Hit chance
                  Type 3 for +3 damage
                  """)

def player_dies(x):
    print(player.name, "is dead! Game over! Your score :", x)
    print("The game will be closed automatically in 10 sec...")
    time.sleep(10)
    exit()

def mob_dies(x):


    while True:
        skillup = input("Which attribute would you like to improve? >")
        if skillup == "1":
            player.ac += 1
            return False
        elif skillup == "2":
            player.atak += 2
            return False
        elif skillup == "3":
            player.damage += 3
            return False
        else: print ("Please enter a valid number")












