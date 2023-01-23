
import os
import random
import rpgfunc


stats = {
    "Health" : 100,
    "Weapon" : 'Baseball bat',
    "Skills" : "None"
        }

enemy_stats = {
    "Health" : 150,
    "Weapon" : "Melee Attacks",
    "Skills" : "None"
              }



def print_user_stats():
    os.system('cls')
    rpgfunc.header()
    print(' '.join('STATS'))
    print("*" * 44)
    print('Player')
    for item in stats:
        print(item + ' : ' + str(stats[item]))
    print("*" * 44 + '\n')
    
    
    
def print_stats():
    os.system('cls')
    rpgfunc.header()
    print(' '.join('STATS'))
    print("*" * 88)
    
    print('Player' + ' ' * 28 + 'Unknown_Big_Guy')
    print()
    for item in stats:
        print(item + ' : ' + str(stats[item]) + ' ' * (22 - len(str(stats[item]))) + '|', end='')
        print(item + ' : ' + str(enemy_stats[item]), end='\n')
    print("*" * 88 + '\n')
    
    

def hits_taken(hit):

    stats["Health"] -= hit
    print_stats()
    
    
    
def enemy_hit():
    if int(enemy_stats["Health"]) <= 0:
        return
    dmg = random.choice([0, 5, 10 , 20])
    stats["Health"] -= dmg
    os.system('cls')
    print_stats()
    if dmg > 0:
        print(">>> The enemy attacked you in return.\n>>> You lost {} hp...".format(dmg))
        input("\n\nPress Enter to continue...")


    
def dmg_dealt():
    dmg = random.choice([25, 50, 75, 0])
    os.system('cls')
    rpgfunc.header()
    enemy_stats["Health"] -= int(dmg)
    print_stats()

    if int(dmg) >= 75:
        print(">>> This was a CRIT HIT!")
    elif int(dmg) <= 0:
        print(">>> The enemy wasn't fazed by your attack")
    print(">>> You dealt {} damage to the enemy".format(dmg))
    _ = input("\n\nPress Enter to continue...")

        
        
def dodge():
    
    os.system('cls')
    rpgfunc.header()
    print_stats()
    rand = random.choice([1, 2]) #One for succesfuly dodging, two for getting hit anyway
    
    if rand == 1:
        hits_taken(5)
        print_stats()
        print(">>> You tried to dodge but failed\nYou got hit and lost 5 hp...")
        input("\n\nPress Enter to continue...")
        return True
    elif rand == 2:
        print_stats()
        print(">>> You successfully dodged the attack")
        input("\n\nPress Enter to continue...")



def win_or_no():
    if stats["Health"] > enemy_stats["Health"]:
        bool_value = True
    elif stats["Health"] < enemy_stats["Health"]:
        bool_value = False
    
    os.system('cls')
    rpgfunc.header()
    print_stats()
    if bool_value == True: # true means you defeated enemy
        print("You succesfuly defeated the enemy")
        input("\n\nPress Enter to continue...")
        rng_drops()
    elif bool_value == False:
        print(' ' . join("GAME OVER"))
        print(">>> You died (╥﹏╥)")
        print(">>> But you can always try again! ")
        while True:
            user_choice = input("\n\nEnter number corresponding to\n[1] Try again\n[2] Exit\n\nEnter: ")
            if user_choice == '2':
                return False
            elif user_choice == '1':
                return True
            else:
                continue
            
            
            
def rng_drops():
    rand = random.choice(['Food', 'Nothing'])
    os.system('cls')
    rpgfunc.header()
    print_user_stats()
    print("The enemy dropped:", rand)
    input("\n\nPress Enter to continue...")
def skill():
    os.system('cls')
    rpgfunc.header()
    print_stats()
    if stats["Skills"] == "None":
        print(">>> You do not have any skills unlocked right now")
        input("\n\nPress Enter to continue...")
    # more skills coming soon
    
    
    
def heal(hp, stats):
    stats["Health"] += hp
    
    

def fight():
    stats["Health"] , enemy_stats["Health"] = 100, 150
    a = True
    while True:
        os.system('cls')
        rpgfunc.header()
        print_stats()
        print(">>| What would you do\n[1] Attack\n[2] Dodge\n[3] Use skill")
        user_choice = input("\n\nEnter: ")
        
        if user_choice == '1':
            dmg_dealt()
            enemy_hit()

        elif user_choice == '2':
            dodge()
        
        elif user_choice == '3':
            skill()

        if int(stats["Health"]) <= 0 or int(enemy_stats["Health"]) <= 0:
            return win_or_no(), stats
        
