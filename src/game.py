import cmd
import textwrap
import sys
import os
import time
import random
import math
import json
import copy

from text_utilities import *
from Player import *
from Rooms import *
from move import *
screen_width = 100

      
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

    

def prompt():
    print("\n" + "=====================")

    acceptable_actions = ['move','go', 'walk', 'quit', 'examine', 'inspect', 'look at', 'interact', 'look', 'eat', 'drink', 'back', 'onscreen', 'baswash', 'teleport', 'dev']
    action = prompt_select_from("What would you like to do?", acceptable_actions, "Unknown action, tryangle again.")

    if action.lower() == 'quit':
        input("ARE YOU SURE YOU WANT TO QUIT? y/n*\n>>>")
        if input == 'y' 'Y':
            sys.exit()
        else:
            prompt()
    elif action.lower() in ['move', 'go', 'walk']:
        player_move(action.lower(), zonemap, myPlayer)
    elif action.lower() in ['examine', 'inspect', 'look at', 'look']:
        player_examine(action.lower())
    elif action.lower() in ['onscreen']:
        myPlayer.print_location()
    elif action.lower() in ['baswash']:
        god_mode()
    elif action.lower() in ['dev']:
        if myPlayer.editrooms is True:
            room_edit_prompt(action.lower)
        else:
            slow_print("You can't do that without permission.")
            prompt()
    elif action.lower() in ['teleport']:
        if myPlayer.can_teleport():
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
        myPlayer._teleport = True
        print ("teleport commands enabled")
        god_mode()
    elif inp == 'c':
        myPlayer.keys = True
        print ("Room lock control enabled")
        god_mode()

    elif inp == 'd':
        slow_print("Everything is back to norbal !\n")
        myPlayer.editrooms = False
        myPlayer._teleport = False
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
            myPlayer.print_location()
            prompt()

# def teleport_handler(destination):
#     if destination in zonemap:


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
# DESCRIPTION = 'description'
EXAMINATION = 'examine'
EXITS = 'UP', 'DOWN', 'LEFT', 'RIGHT'


solved_places: {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False,
                'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False,
                }

def create_new_room(name, address=None, ingress=None):
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
    p = "data/" + p
    with open(p, 'r') as file:
        data = file.read()
    return json.loads(data)

#actionfile = load_json("actions.json")
zonemap = load_json("zonemap.json")
zonemap_lookup_address_by_name = {}
for address, value in zonemap.items():
    zonemap_lookup_address_by_name[value['zonename']] = address
myPlayer = Player(zonemap)
myRoom = Room()
title_screen()
