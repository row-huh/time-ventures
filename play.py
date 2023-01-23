import phase1_choices
import os
import rpgfunc



def play_menu():
    while True:
        os.system('cls')
        rpgfunc.header()
        global user_name
        user_name = input("Enter your name: ").title()

        if len(user_name) >= 2:
            break
        else:
            input("Username must contain atleast 2 characters\n\nPress Enter to continue....")
    phase_1(user_name)



def phase_1(user_name):
    rpgfunc.start_dialogues()    
    while True:
        os.system('cls')
        rpgfunc.header()
        print("_" * 44)
        user_choice = input("What would you do\n[1] Scream for help\n[2] look in the room for clues\n[3] Grab your phone to try to call for help\n\n---> Enter: ")
        
        if user_choice == "1":
            rpgfunc.screamed_for_help()
            continue
        elif user_choice == "2":
            rpgfunc.looking_for_clues()
            continue
        elif user_choice == "3":
            if phase1_choices.call(user_name) == False:
                continue
            # a = phase1_choices.call(user_name)
            rpgfunc.big_guy_incoming()
            phase1_choices.first_fight()
            rpgfunc.end()
            print("-----> Thank You, " + user_name + " for Playing! ")
            input('\n\nPress Enter to continue...')
            rpgfunc.credits()
            break
        else:
            print("Invalid input")
            continue
