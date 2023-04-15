import os
import dialogues
import phase1

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
    while True:
        os.system('cls')
        dialogues.header()
        global user_name
        user_name = input("Enter your name: ").title()

        if len(user_name) >= 2:
            break
        else:
            input("Username must contain atleast 2 characters\n\nPress Enter to continue....")
    phase_1(user_name)



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
            print("-----> Thank You, " + user_name + " for Playing! ")
            input('\n\nPress Enter to continue...')
            dialogues.credits()
            break
        else:
            print("Invalid input")
            continue


if __name__ == "__main__":        
    main()

