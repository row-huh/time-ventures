
# day 3 of building rpg

import os
import rpgfunc
import play


# The mainest of main functions
def mainmenu():
    while True:
        
        os.system('cls')
        rpgfunc.header()
        #print("_"*40 + '\n')
        main_choice = input("Enter the corresponding number to:\n[1] Play\n[2] Credits\n[X] Exit\n\n-----> ").lower()
        
        if main_choice == '1':
            play.play_menu()
            continue
            
        elif main_choice == '2':
            rpgfunc.credits()
            continue
        
        elif main_choice == 'x':
            break
        
        else:
            os.system('cls')
            print("Invalid Input")
            continue
        
mainmenu()

