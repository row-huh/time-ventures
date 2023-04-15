import os
import dialogues
import combat


def call(user_name):
    os.system('cls')
    dialogues.header
    print("_" * 44)
    dialogues.grabbed_phone()
    
    while True:
        os.system('cls')
        dialogues.header()
        print("_" * 44)
        user_input = input("What would you do?\n[1] Call Alfred\n[2] Look for another way\n\n---> Enter: ")
        
        if user_input == '1':
            dialogues.called_alf(user_name)
            break

        elif user_input == '2':
            return False
        
        else:
            print("Invalid Input")
            continue


def first_fight():
    while True:
        os.system('cls')
        dialogues.header()
        user_choice = input("What would you do?\n[1] Fight him\n[2] Try to escape\n\n---> Enter: ")
        if user_choice == '1':
            flag = True
            while flag == True:
                flag, stats = combat.fight()
                go_out(stats)
            break
        elif user_choice == '2':
            os.system('cls')
            dialogues.header()
            print("You tried to run, but the big guy stepped in your way")
            input("\n\nPress Enter to conitnue...")
            continue
        else:
            print("Invalid Input")



def go_out(stats):
    x = 1
    while True:
        os.system('cls')
        dialogues.header()
        combat.print_user_stats()
        
        user_input = input("What would you do:\n[1] Move\n[2] Rest\n\nEnter: ")
        if user_input == '1':
            if x == 1:
                os.system('cls')
                dialogues.header()
                combat.print_user_stats()
                print('You walked through the corridor, nothing happened...')
                input("\n\nPress Enter to continue...")
                x += 1
            elif x == 2:
                os.system('cls')
                dialogues.header()
                combat.print_user_stats()
                print("You walked through the corridor, and reached an exit")
                input("\n\nPress Enter to continue...")
                reached_exit(stats)
                break
        elif user_input == '2':
            resting(stats)
        else:
            print("Invalid Input")
            continue



def reached_exit(stats):
    while True:
        os.system('cls')
        dialogues.header()
        combat.print_user_stats()
        user_input = input("What would you do?\n[1] Exit Building\n[2] Rest\n\nEnter: ")
        if user_input == '1':
            dialogues.phase1_conclusion()
            break
        elif user_input == '2':
            resting(stats)
            
            


def resting(stats):
    os.system('cls')
    dialogues.header()
    y = stats["Health"] + 10
    if y < 100:
        stats["Health"] = y
        combat.print_user_stats()
        print("You rested for a while\n{} hp was recovered".format(10))
        input("\n\nPress Enter to continue...")

    elif stats["Health"] >= 100:
        stats["Health"] = 100
        combat.print_user_stats()
        print("--> You already have max hp...")
        input("\n\nPress Enter to continue...")

    elif y >= 100 and stats["Health"] < 100:
        stats["Health"] = 100
        combat.print_user_stats()
        print("You rested a little\nYour hp is max now")
        input("\n\nPress Enter to continue...")