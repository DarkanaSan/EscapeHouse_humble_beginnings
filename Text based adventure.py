#RPG
import cmd
import textwrap
import os
import time
import random
import sys

screen_width = 100

#Player Setup class - store carachter
class player:
    def __init__ (self):
        self.name = ""
        #self.hp = 0
        #self.mp = 0
        #self.status_effects = []
        self.location = "Cellar"
        self.game_Over = False
        self.solved = 0
myPlayer = player()

# Title Screen
def title_screen_selections():
    while True:
        option = input("> ").lower().strip()
        if option.lower() in ["play", "paly", "start"]:
            setup_game()
            break
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "exit":
            sys.exit()
        else:
            print("Please enter a valid command: 'play', 'help', 'quit'")


def title_screen():
    os.system("cls")
    print("#######################################")
    print("# Welcome to my little text Adventure # ")
    print("#######################################")
    print("             -Play-              ")
    print("             -Help-              ")
    print("             -Quit-              ")
    print("                                 ")
    print("                                 ")
    print("Copyright Darkana                ")    
    title_screen_selections()

def help_menu():
    print("#######################################")
    print("#        Navigation / Help            # ")
    print("#######################################")
    print("movement commands: up, down, left, right \nnote: not every movement if possible everywhere")
    print("type your commands and make sure there are no spelling mistakes")
    print("use 'look' or 'examine' to inspect something\n")
    print("Good luck, have fun!")
    print("Feedback appreciated\n") 
    ask1 = "Back to title screen?\n"
    for character in ask1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    answer1 = input("> ")
    if answer1.lower() == "yes":
        title_screen()
    else:
        help_menu()


#MAP
"""Player starts at cellar
Pleayer needs to get out of house

Celler -> Entrance hall
Entrance Hall -> Living room & kitchen (and out)
Living room -> Entrance Hall & Kitchen & Secret room
Kitchen -> Living Room & Entrance Hall
Secret Room -> Living room"""

ZONENAME = "name" #these strings are what ppl need to type for triggering it
DESCRIPTION = "description"
EXAMINATION = "examine"
PUZZLE = "riddle"
SOLVED = False
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
HINT = "hint"

solved_places ={"Living room": False, "Secret room": False, "Kitchen": False, "Cellar": False, "Entrance hall":False, 
} #its a key value dictionary. living romm = key, false = value


#dictionary of rooms/zone/whatever
housemap = { 
    "Cellar": {
        ZONENAME: "Cellar",
        DESCRIPTION: "Dark, nasty, moldy cellar",
        EXAMINATION: "Your starting point, there seems nothing interesting to be here. \nA blank room with some stairs, leading up",
		PUZZLE: "\nI fly without wings. I see without eyes. I move without legs.\nI conjure more love than any lover and more fear than any beast.\nI am cunning, ruthless, and tall; in the end, I rule all.'\n'What am I?'",
		SOLVED: "imagination",
        UP: "Entrance hall",
        DOWN: "",
        LEFT: "",
        RIGHT: "",
        HINT: "Below the wodden stairs you find something carved in the wall: \nHouse locked. \nRiddles everywhere. \nSolve them all - FREEDOM!", 
    },
    "Entrance hall": {
        ZONENAME: "Entrance hall",
        DESCRIPTION: "The central room of this strange house. It's dirty and old looking.",
        EXAMINATION: "A quick count reveals four doors. One of them the cellar door you came from. \nOne to your left, and one to our right. \nAnd one big exit door - without handle or lock\n",
        PUZZLE: "",
        SOLVED: False,
        UP: "",
        DOWN: "Cellar",
        LEFT: "Living room",
        RIGHT: "Kitchen",
        HINT: "Not many things to do here. Just go out - if you figgure out how to open the god damn exit door! \nOr go to another room"
    },
    "Living room": {
        ZONENAME: "Living room",
        DESCRIPTION: "A dusty room with blind windows, destroyed furniture and two doors, one of them leading back to the entrance hall",
        EXAMINATION: "You see a suprisingsly good looking bookshelf on the wall. \nIt has only two books left:\nOne about sound and one about riddles",
        PUZZLE: "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
        SOLVED: "echo",
        DOWN: "Secret room",
        LEFT: "",
        RIGHT: "Entrance hall",
        UP: "",
        HINT: "I love the Bookshelf. Can we have a closer look? There must be something down behind"
    },
    "Kitchen": {
        ZONENAME: "Kitchen",
        DESCRIPTION: "A completely destroyed kitchen. Nearly no furniture, cracked flooring and cobwebs on the ceiling.",
        EXAMINATION: "Some drawers have closed doors, as well as the fridge",
        PUZZLE: "What have I got in my pocket?",
        SOLVED: "ring",
        LEFT: "Entrance hall",
        RIGHT: "",
        UP: "",
        DOWN: "",
        HINT: "Bilbo, is that you?",

    },
    "Secret room": {
        ZONENAME: "Secret Room",
        DESCRIPTION: "A tiny room you found behind a livingroom painting",
        EXAMINATION: "A grey book on this dusty table catches your eye",
        PUZZLE: "I have a spine but no bones, pages but no words. \nI can take you on magical journeys. \nWhat am I?",        
        SOLVED: "book",
        UP: "Living room",
        DOWN: "",
        LEFT: "",
        RIGHT: "",
        HINT: "",
    },
}
# Game interactivity
          
def print_location():
    print("\n" + ("#" * (4 +len(myPlayer.location)))) #len = length of the string for the location
    print("\n" + "# " + housemap[myPlayer.location][ZONENAME] + " #")
    print("\n" + "# " + housemap[myPlayer.location][DESCRIPTION] + " #") #<-- needed if player should get description directy when asking for location
    print("\n" + ("#" * (4 +len(myPlayer.location))))


def riddle():
	if solved_places[myPlayer.location] == False:
		print(housemap[myPlayer.location][PUZZLE])
		puzzle_answer = input("> ")
		player_puzzle(puzzle_answer)
	else:
		print("Riddle already solved for "), housemap[myPlayer.location]
          

def player_puzzle(puzzle_answer):
    if myPlayer.location == 'Cellar':
        if puzzle_answer == housemap[myPlayer.location][SOLVED]:
            solved_places[myPlayer.location] = True
            myPlayer.solved += 1
            print("You have solved the riddle. Onwards!")
            print("\nRiddles solved: " + str(myPlayer.solved))
        else:
            print("Wrong answer! Try again or go on.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif myPlayer.location == 'Living room':
        if puzzle_answer == housemap[myPlayer.location][SOLVED]:
            solved_places[myPlayer.location] = True
            myPlayer.solved += 1
            print("You have solved the riddle. Onwards!")
            print("\nRiddles solved: " + str(myPlayer.solved))
        else:
            print("Wrong answer! Try again or go on.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif myPlayer.location == "Kitchen":
        if puzzle_answer == housemap[myPlayer.location][SOLVED]:
            solved_places[myPlayer.location] = True
            myPlayer.solved += 1
            print("You have solved the riddle. Onwards!")
            print("\nRiddles solved: " + str(myPlayer.solved))
        elif puzzle_answer == housemap[myPlayer.location] is "hands" or "handses":
            print("Wrong answer! See, hands are out.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
        else:
            print("Wrong answer! Try again or go on.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    elif myPlayer.location == 'Secret room':
        if puzzle_answer == housemap[myPlayer.location][SOLVED]:
            solved_places[myPlayer.location] = True
            myPlayer.solved += 1
            print("You have solved the riddle. Onwards!")
            print("\nRiddles solved: " + str(myPlayer.solved))
        else:
            print("Wrong answer! Try again or go on.\n~~~~~~~~~~~~~~~~~~~~~~~~~~")


def player_move(myAction):
    ask = f"Where would you like to {myAction} to? (up, down, left, right)\n> "
    destination = input(ask).lower().strip()

    if myPlayer.location not in housemap:
        print("Invalid location.")
        return

    current_room = housemap[myPlayer.location]

    directions = ["up", "down", "left", "right"]

    if destination in directions:
        if destination in current_room and current_room[destination]:
            movement_handler(current_room[destination])
        else:
            print(f"There is no path to '{destination}' from here.")
    else:
        print("Invalid direction. Please choose from: up, down, left, right.")


def movement_handler(destination):
   print(f"\nYou have moved to the {destination}.")
   myPlayer.location = destination #moves player to chosen location
   print_location()



def prompt():
    if myPlayer.solved == 4: #Cellar, Living room, kitchen, secret room, entrance hall
        print("Something in the house seems to have changed. Hmm...\n\n\n")
        if myPlayer.location is not housemap["Entrance hall"] and myPlayer.solved >=4:
            myPlayer.location = housemap["Entrance hall"]
            endspeech = ("""One final time you entered the Entrance hall.
One final time you have to look at the closed exit door.
All of a sudden the door begins to glow.
Light begins to shine through the cracks in it.
A blinding flash of light hits you.
You have escaped!
FREEDOM at last""")
            for character in endspeech:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.1)
            print("\nCONGRATULATIONS!\n")
            play_again()
    print("\nWhat would you like to do?\n")
    action = input("> ")
    accpetable_actions = ["move", "go", "travel", "walk", "movement commands can be used in second step with left/right/up/down", "quit", "examine", "inspect", "interact", "look",
"help", "location", "hint", "riddle", "puzzle", "secret", "how to play", "display housemap",
]
    while action.lower() not in accpetable_actions:
        print("Unknown action, try again!\nTo get a list with valid actions, please use 'help'")
        action = input("> ")

    if action.lower() == "quit":
        print("\nThank you for playing. Goodbye!\n")
        sys.exit()
    elif action.lower() in ["move", "go", "travel", "walk"]:
        player_move(action) #action because action = input?
    elif action.lower() in ["examine", "inspect", "interact", "look"]:
        player_examine()
    elif action.lower() == "location":
        print_location()
    elif action.lower() == "hint":
        print(housemap[myPlayer.location][HINT])
    elif action.lower() in ["riddle", "puzzle", "secret"]:
        riddle()
    elif action.lower() == "help":
        print("What you could do: "); print(accpetable_actions)
    elif action.lower() == "how to play":
        how_to_play()
    elif action.lower() == "display housemap":
        display_housemap()


def how_to_play():
    ask1 = "As said before, you're trapped in a very small house with only 5 rooms\n"
    ask2 = "To escape the house you need to solve 4 riddles\nOne in every room, the Entrance hall has none for now\n"
    ask3 = "'location' will tell you where you are\n"
    ask4 = "'help' will display every action you can do'\n"
    ask5 = "To move you first have to say something like 'move/walk/etc' \nafter this you will be asked where you want to move. \nonly (left/right/up/down)are valid\n"
    ask6 = """For now, 'back' is not a valid movement option\nIf you want to go where you came frome, you have to go back the opposite direction.
This means: if you entered a room with 'move' 'left' \nyou will get back to previous location with 'move' right'\n"""
    for character in ask1, ask2, ask3, ask4, ask5, ask6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    ask7 = "The action 'display housemap' will give you an overall overview.\n(Written only for now)"
    for character in ask7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)

def display_housemap():
    print("""
Cellar -> below the Entrance hall
Entrance hall -> Has the cellar below. Living room to the left, kitchen to the right.
Secret room -> below another room. Figure it out
""")

def player_examine():
    if housemap[myPlayer.location][SOLVED] == True: 
        print("Everything that could be done here, has been done")
    else:
        print (housemap[myPlayer.location][EXAMINATION]) #can add more functions for actually doing stuff


# Game functionality
def main_game_loop():     #here handle if puzzles have been solved, boss defeted, etc
    while not myPlayer.game_Over:
        prompt()


def play_again():
    answer_play = input("Wanna play again? (yes/no): ")
    if answer_play.lower().strip() in ["y", "yes", "jupp", "okay", "sure", "ja"]:
        title_screen_selections()
    else:
        print("\nThank you for playing. Goodbye!\n")
        sys.exit()


def setup_game():
    os.system("cls")
#name collection question
    question1 = "Hello, what's your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    
#more questions about whatever you want the player to be (and what is defined in "class player")    
    #question2 = ""

#Introduction
    speech0 = (f"Welcome {player_name}, to my little escape house game. \nAgain.\n")
    speech1 = "Your goal is still to escape the house.\n"
    speech2 = "What else?\n"
    speech3 = "This time you actually have free movement\n"
    speech4 = "As well as some hints to find\n"
    for character in speech0:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    
    speech5 ="Start? (yes/no)\n"
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    getstarted = input("> ")
    if getstarted.lower() in ["yes", "ja", "jupp", "okay", "go", "los", "Jah"]:
        os.system("cls") #clears the screen
        print("#########################")
        print("# Let's find a way out! #")
        print("#########################")

#enter explenation how to move and a map, somehow
        starter_hint1 = "If this is your first time playing, type 'how to play'\n"
        starter_hint2 = "This will give you a short explenation for what you can do right now"
        for character in starter_hint1, starter_hint2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)


        main_game_loop()

    else:
        title_screen()







title_screen()













###########################
""" possible future content
vlcht nachdem man riddle eingegeben hat und nicht drauf kommt, 
dann eben nochmal hint und einen zweites, leichteres riddle bekommt

movement in one word - move up instead of 1. move, 2. up
inspect - what to inspect. like bookshelf, fridge, etc

display possible actions in each room (if asked for)
-> helper function? like "what to do"and it lists what is not solved yet?



"""
###########################

