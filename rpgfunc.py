import os
import time



def header():
    print('-' * 88)
    print('>>>|  ' + ' '.join("TIME VENTURERS") + '  |<<< ')
    print('-' * 88 + '\n')
 


def credits():
    os.system('cls')
    header()
    print("CREDITS:")
    print("_" * 40,"\n")
    print("Time Venturers")
    print("Text based adventure rpg")
    print("Written, Designed and Coded by Roha Pathan")
    print("Programmed on Python 3.10.9")
    print("January 2023")
    for _ in range(5):
        print(".")
        time.sleep(0.5)
    input("\n\nPress Enter to continue.... ")
 
 
 
    
def loopdialogues(dialogues):
    for dialogue in dialogues:
        os.system('cls')
        header()
        print(dialogue)
        input("\n\nPress Enter to continue....")




def start_dialogues():
    dialogues = [
        "You wake up in a strange room with a big glass window...\n"
        "You glare outside the window to see a mega city with lots of big buildings,\nflying cars, people with mechanical implants and lots of big screens showing advertisements...",
        '"How did I end up in here", you wonder...\nYou try to leave the room but the door is locked...\n'
        "You check your pockets and you still have your cellphone..."
        ]
    
    loopdialogues(dialogues)



def grabbed_phone():
    dialogues = [
        "You grab your cellphone and proceed to call for help but you don't have any familiar contacts...\n",
        "There is only one contact named 'Alfred'\n'Who is that? And how did his contact just magically appear in my phone?', you wonder"    
    ]
    
    loopdialogues(dialogues)
    
    
        
def called_alf(user_name):
    dialogues = [
    ".....ringing......",
    ".....ringing......",
    "Alfred: Hello? This is Alfred speaking",
    user_name + ":  .....",
    "Alfred: Hello??",
    "Alfred: Look bro I don't have all day, if you've got nothing to say-",
    "Alfred: Wait...\nAlfred: Could it be...",
    ("Alfred: Are you "+ user_name + "?\nAlfred: This is " + user_name + ", right? You're from the year 2023?"),
    user_name + ": How do you know who I am?",
    "Alfred: ..So...It is you...\nAlfred: ..My experiment...It was a success!",
    user_name + ": What?",
    "Alfred: Look, I don\'t have time to explain everything\nAlfred: All I can tell you is that I summoned you from the past...This is year 2094",
    "Alfred: If I'm correct, you are in a room with the big window right now\nAlfred: This means that you have to get out of there immediately",
    "Alfred: Do you understand?'\nAlfred: G-get out of t-there im-m-\n*phone disconnects*",
    user_name + ": w-what? 2094?",
    ]
    
    loopdialogues(dialogues)
  
  
    
def big_guy_incoming():
    dialogues = [
        "....you hear footsteps....\n",
        "....someone is coming your way....\n",
        "....you grab a baseball bat from the bed at the far end of the room....\n",
        ".....*door opens*.....",
        "*A big guy wearing black stands before you*\n",
        "Unknown Big Guy: You must be the target....\n",
        "Unknown Big GUy: I apologize but You're going to have to die here\n",
    ]
    loopdialogues(dialogues)
 
 
 
    
def looking_for_clues():
    dialogues = [
        "You look around the room\nYou notice a bed on the far side of the room\nOn top of the bed lies a baseball bat and a piece of paper",
        "You grab the piece of paper\nIt says 'Cycle 78651'",
        "You notice an address is written on the bottom of the paper...\nAn adress you don't recognise..."
    ]        
    loopdialogues(dialogues)
 
 
        
def screamed_for_help():
    dialogues = [
        "You screamed for help...There was no reply...\nMaybe this building is empty?"
    ]
    loopdialogues(dialogues)


def phase1_conclusion(): 
    dialogues = [
    " You stand on the street...\n You can see tall imposing skyscrapers made of gleaming metal and glass covered in bright neon lights...",
    " The streeets are packed with people wearing cyberpunk-style clothing and a lot of vendors selling various goods.\n The people are using hoverbikes and drones as means of getting around the street",
    " You notice high tech transportation, cars are replaced by autonomous flying vehicles.\n Everywhere you look, you see holographic advertisements and displays, projected on buildings, streets, and even people's clothing",
    " You dont belong to this era,\n You dont know how you got here and why...\n All you know is that you need to find out the truth. ",
    " You remember there was a piece of paper in the room you were in, which you had already grabbed.\n You check it again, there is an adress written on it.",
    " Maybe this address will lead you to alfred and maybe he can tell you what is going on.",
    " You now know what you need to do...\n Your sole purpose right now is to demystify your situation...",
                ]
    loopdialogues(dialogues)
    



def end():
    os.system('cls')
    print('-' * 88)
    print('                  | ' + ' '.join("TIME VENTURERS") + '     |                      ')
    print('-' * 88)
    print('                  | ' + ' '.join("End of Phase One") + ' |                   ')
    print('-' * 88)
    
    for _ in range(5):
        print('.')
        time.sleep(0.5)