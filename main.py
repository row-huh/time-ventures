import os
import dialogues
import phase1
import time
import re


def main():
    while True:
        os.system('cls')
        dialogues.header()
        main_choice = input("Enter the corresponding number to:\n[1] Play\n[2] Credits\n[X] Exit\n\n-----> ").lower()
        
        if main_choice == '1':
            play_menu()
            continue
            
        elif main_choice == '2':
            dialogues.credits()
            continue
        
        elif main_choice == 'x':
            break
        
        else:
            os.system('cls')
            print("Invalid Input")
            continue

def play_menu():
    user_name = validate_username(input("Enter username: "))

    while not user_name:
        print("Username must start with 2 letters and contain atleast 4 characters")
        user_name = validate_username(input("Enter username: "))
        os.system('cls')
        dialogues.header()
    phase_1(user_name)
    print("-----> Thank You, " + user_name + " for Playing! ")
    input('\n\nPress Enter to continue...')
    dialogues.credits()


# validates username
def validate_username(name):
    if len(name) < 4:
        return False
    elif re.match(r"^[a-zA-Z]{2}.", name):
        return name
    else:
        return False
    


def phase_1(user_name):
    dialogues.start_dialogues()    
    while True:
        os.system('cls')
        dialogues.header()
        print("_" * 44)
        user_choice = input("What would you do\n[1] Scream for help\n[2] look in the room for clues\n[3] Grab your phone to try to call for help\n\n---> Enter: ")
        
        if user_choice == "1":
            dialogues.screamed_for_help()
            continue
        elif user_choice == "2":
            dialogues.looking_for_clues()
            continue
        elif user_choice == "3":
            if phase1.call(user_name) == False:
                continue
            # a = phase1.call(user_name)
            dialogues.big_guy_incoming()
            phase1.first_fight()
            dialogues.end()
            break
        else:
            print("Invalid input")
            continue


def credits():
    os.system('cls')
    dialogues.header()
    print("CREDITS:")
    print("_" * 40,"\n")
    print("Time Venturers")
    print("Text based adventure rpg")
    print("Written, Designed and Coded by Roha Pathan")
    print("Programmed on Python 3.10.9")
    for _ in range(5):
        print(".")
        time.sleep(0.5)
    input("\n\nPress Enter to continue.... ")


if __name__ == "__main__":        
    main()

