import cmd
import textwrap
import sys
import os
import time
import random
import math
import json
import copy

screen_width = 100

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def slow_print(s, t = 0.05):
    s += "\n"
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(t)

def slow_prompt(s, t = 0.05):
    slow_print(s, t)
    return input(">>> ")

def slow_print_ack(s, t = 0.05):
    slow_print(s, t)
    input("")

def prompt_select_from(prompt, options, failure):
    inp = input(prompt + '\n').lower()
    while inp not in options:
        inp = input(failure + '\n').lower()
    return inp

def choose_triangle_type():
    # a = float(input("The length of side a = "))   
    # b = float(input("The length of side b = ")) 
    # c = float(input("The length of side c = "))  
    a = 1
    b = 1
    c = 1
    t = ''
    if a != b and b != c and a != c:
        t = 'scalene'
    elif a == b and b == c and a == c:
        t = 'equilateral'
    else:
        t = 'isosceles'
    print('You have chosen ' + t + '!\n')
    return t



solved_places: {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False,
                }


class Room:
    def __init__(self):
        self.name = ''
        self.address = float
        self.ingress_points = []
        self.objects = []
        self.editrooms = False
myRoom = Room()
### Player Setup ###
class Player:
    def __init__(self):
        self.name = ''
        self.triangle = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'c1' ## Also known as 'address' ##
        self.game_over = False
        self.teleport = False
        self.keys = False
        

    def reset_hp_mp(self):
        if self.triangle == 'scalene':
            self.hp = 120
            self.mp = 40
        elif self.triangle == 'equilateral':
            self.hp = 40
            self.mp = 120
        elif self.triangle == 'isosceles':
            self.hp = 80
            self.mp = 80
     
myPlayer = Player()

       
### Title Screen ###
def title_screen_selections():
    inp = prompt_select_from("", ["play", "help", "quit"], "Please enter a valid command.")
    if inp == "play":
        start_game()
    elif inp == "help":
        help_menu()
    else:
        sys.exit()
    # option = input(">")
    # while True:
    #     if option.lower() == ("play"):
    #         start_game() #placeholder until written
    #         break
    #     elif option.lower() == ("help"):
    #         help_menu()
    #         break
    #     elif option.lower() == ("quit"):
    #         sys.exit()
    #         break
    #     else:
    #         print("Please enter a valid command.")
    #         option = input(">")

def print_intense(txt, width = 3, spacing = 2):
    x = len(txt)
    padding = 0
    if 0 < width:
        padding = spacing + width 
        x = x + 2 * padding
    header = "#" * x
    print(header)
    if 0 < width:
        border = "#" * width
        s = (" " * spacing)
        print(border + s + txt + s + border)
    else:
        print(txt)
    print(header)

def title_screen():
    clear()
    print_intense("Maaaarshmalllooooowwwwwww Pizzaaaaa!!!!!!!")
    print ("            -Play-             ")
    print ("            -Help-             ")
    print ("            -Quit-             ")
    print (" --Copyright 2019 avaughan.me--")
    title_screen_selections()

def help_menu():
    print ("###############################")
    print ("Welcome to Marshmallow Recruitment Laboratories Inc.")
    print ("###############################")
    print ("Use up, down, left, pizza to move.")
    print ("triangle your commands")
    print ("Use 'look' to inspect something")
    print ("Figure it out! You're in a pizza! \n\nGo Go Marshmallow!")
    title_screen_selections()


###GAME INTERACTIVITY###
def print_location():
    address = myPlayer.location
    print ("\n" + ("#"*(4 + len(address))))
    print ("#" + address.upper() + "#")
    print ("#"+ zonemap[address][DESCRIPTION] +  "#")
    print ("\n" + "#"*(4 + len(address)) )



    

def split_first_word(s):
    return s.split(" ", 1)

def prompt():
    print("\n" + "=====================")

    acceptable_actions = ['move','go', 'walk', 'quit', 'examine', 'inspect', 'look at', 'interact', 'look', 'eat', 'drink' 'back', 'onscreen', 'baswash', 'teleport', 'dev']
    action = prompt_select_from("What would you like to do?", acceptable_actions, "Unknown action, tryangle again.")

    if action.lower() == 'quit':
        input("ARE YOU SURE YOU WANT TO QUIT? y/n*\n>>>")
        if input == 'y' 'Y':
            sys.exit()
        else:
            prompt()
    elif action.lower() in ['move', 'go', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'look at', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['onscreen']:
        print_location()
    elif action.lower() in ['baswash']:
        god_mode()
    elif action.lower() in ['dev']:
        if myPlayer.editrooms is True:
            room_edit_prompt(action.lower)
        else:
            slow_print("You can't do that without permission.")
            prompt()
    elif action.lower() in ['teleport']:
        if myPlayer.teleport is True:
            player_teleport(action.lower())
        else:
            slow_print("You can't do that without permission.")
            prompt()


def god_mode():
    inp = prompt_select_from("Sup?\n A) Room Editor\n B) Teleport\n C) Keys\n D) Restore Defaults\n E) Exit\n>>>", ['a', 'b', 'c', 'd', 'e', 'doughnut'], "Choose either A, B, C, D, OR E\n>>>") 
    if inp == 'a':
        myPlayer.editrooms = True
        print ("Room editor commands enabled")
        god_mode()
    elif inp == 'b':
        myPlayer.teleport = True
        print ("teleport commands enabled")
        god_mode()
    elif inp == 'c':
        myPlayer.keys = True
        print ("Room lock control enabled")
        god_mode()

    elif inp == 'd':
        slow_print("Everything is back to norbal !\n")
        myPlayer.editrooms = False
        myPlayer.teleport = False
        myPlayer.keys = False
        prompt()

    elif inp == 'e':
        slow_print("I hope you made a fucking difference.", t=0.05, )
        prompt()

    else:
        print_intense("AHHH!!\nDOUGHNUT!!\n")
        god_mode()

def room_edit_prompt():
    inp = prompt_select_from("A)New Room\n B)Edit this room\n C)Exit", ['a', 'b', 'c'], "Try again.")
    inp = inp.lower()
    if inp == 'a':
        create_new_room(myRoom)
    elif inp == 'b':
        edit_room()
    elif inp == 'c':
        slow_print("Sam hands the ring back to Frodo")
        prompt()

def lookup_address_by_name(name):
    try:
        address = zonemap_lookup_address_by_name[name]
        # room = zonemap[address]
        return address#, room
    except:
        return None, None

def player_teleport(myAction):
    while True:
        dest = input("Where would you like to teleport?\n")
        dest_address = lookup_address_by_name(dest)
        if dest_address == None:
            print("That is not a valid destination, try again")
        else:
            print("\n" + "you have teleported to " + dest + ".\n")
            myPlayer.location = dest_address
            print_location()
            prompt()

# def teleport_handler(destination):
#     if destination in zonemap:

def player_move(myAction):
    while True:
        dest = input("Where would you like to move?\n")
        if dest in UP:
            destination = zonemap[myPlayer.location]['up']
            movement_handler(destination)
            return
        elif dest in LEFT:
            destination = zonemap[myPlayer.location]['left']
            movement_handler(destination)
            return
        elif dest in RIGHT:
            destination = zonemap[myPlayer.location]['right']
            movement_handler(destination)
            return
        elif dest in DOWN:
            destination = zonemap[myPlayer.location]['down']
            movement_handler(destination)
            return
        else:
            print("Wait, go where?")

def movement_handler(destination):
    if destination in zonemap:
        print("\n" + "you have moved to " + destination + ".\n")
        myPlayer.location = destination
        print_location()
    else:
        if destination == "":
            print("There is no exit in that direction")
        else:
            print("Please let an admin know that this room exit is broken.")

def player_examine(action):
    if zonemap[myPlayer.location][SOLVED]:
        print("Solved")
    else:
        print("Unsolved")
        ####Trigger event.
  
#room set up#
### Map ###
# player starts at c1
###   __ __ __ __ __ 
###  |__|__|__|__|__|y5 a1,a2,a3...
###  |__|__|__|__|__|y4 b1,b2,b3...
###  |__|__|__|__|__|y3 c1,c2,c3...
###  |__|__|__|__|__|y2
###  |__|__|__|__|__|y1
###  x1 x2 x3 x4 x5
###



ZONENAME = 'zonename'
SOLVED = False
DESCRIPTION = 'description'
EXAMINATION = 'examine'
EXITS = 'UP', 'DOWN', 'LEFT', 'RIGHT'
UP = 'up', 'north', 'n'
DOWN = 'down', 'south', 's'
LEFT = 'left','west', 'w'
RIGHT = 'right', 'east', 'e'
def create_new_room(name, address, ingress):
        pass
def edit_room():
        pass

###GAME FUNCTIONALITY###
def start_game():
    clear()
    setup_game()
    main_game_loop()
    return

def main_game_loop():
    while myPlayer.game_over is False:
        prompt()
### here handle if game has been solved

# Do not uncomment this unless you are sure
# def update_zonemap():
#     directions = ["left", "right", "up", "down"]
#     zonemap2 = copy.deepcopy(zonemap)
#     for r in zonemap2:
#         room = zonemap2[r]
#         room["exits"] = {}
#         for key in room:
#             if key in directions:
#                 room["exits"][key] = room[key]

#         for d in directions:
#             room.pop(d, None)
#     to_json(zonemap2, "zonemap.json")
#


def to_json(zm, filename):
    # this replaces the original zonemap.json
    fp = open(filename, "w")
    string = json.dumps(zm, sort_keys = True, indent = 4)
    _ = fp.write( string )
    fp.close()

def setup_game():
    slow = False
    if slow:
        myPlayer.name = slow_prompt("Howdy Doo! \nWho Are You?")
    else:
        myPlayer.name = "Fartmonster"

    slow_print("What kind of triangle are you?")
    myPlayer.triangle = choose_triangle_type()
    myPlayer.reset_hp_mp()

    if slow:
        slow_print_ack("Welcome, " + myPlayer.name + " the " + myPlayer.triangle + ".", t = 0.04)
        slow_print_ack("You're just a dirty little " + myPlayer.triangle + ", aren't you?", t = 0.04)
        slow_print_ack("Look at yourself, " + myPlayer.name + ".\n\n You've gotten lost in the swamps.", t = 0.02)
        slow_print_ack("If you slough around here too long you could\nwind up getting that weird rash again.", t = 0.03)
        
        time.sleep(0.5)
        clear()
        print("########################\n## IT BEGINS TO ITCH ###\n########################\n")

    main_game_loop()

def load_json(p):
    with open(p, 'r') as file:
        data = file.read()
    return json.loads(data)

#actionfile = load_json("actions.json")
zonemap = load_json("zonemap.json")
zonemap_lookup_address_by_name = {}
for address, value in zonemap.items():
    zonemap_lookup_address_by_name[value['zonename']] = address
title_screen()