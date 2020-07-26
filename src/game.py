import cmd
import textwrap
import sys
import os
#import math
#import copy
#from pydub import AudioSegment
#from pydub.playback import play
#from text_utilities import *
from Player import*
from json_handler import*
from move import*
screen_width = 60

      
### Title Screen ###
def title_screen_selections():
    inp = prompt_select_from("", ["play", "help", "quit"], "Please enter a valid command.")
    if inp == "play":
        start_game()
    elif inp == "help":
        help_menu()
    else:
        sys.exit()

def title_screen():
    clear()
    print_intense("Marpshwallow!")
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
    print ("marshmallow your commands")
    print ("Use something like 'look' or\n'examine' to inspect something")
    print ("Figure it out! You're in a pop topping rock tipping hot topping talbo-dee-doo!")
    title_screen_selections()



def setup_game():
    slow = False
    if slow:
        myPlayer.name = slow_prompt("Howdy Doo! \nWho Are You?")
    else:
        myPlayer.name = "Fartmonster"

    
    myPlayer.reset_hp_mp()
    if slow:
        #ques_1()
        intro()
        clear()
        print("########################\n## IT BEGINS TO ITCH ###\n########################\n")
        main_game_loop()
        
    else:
        clear()
        print_intense("########################\n## IT BEGINS TO ITCH ###\n########################\n")
        myPlayer.print_location()
        main_game_loop()
    



def intro():
    slow_print_ack("Swim, " + myPlayer.name + "!\nSWiM!!", t = 0.02)
    inp = prompt_select_from("What are you doing?\n Swim!!!\n", ['drown', 'swim'], "You're gonna die!")
    if inp == "swim":
        slow_print_ack("The water is too shallow. . .\n", t = 0.03)
        slow_print_ack("No matter how hard you try, the swamp just isn't a good place\nfor exercise.")
        slow_print_ack("And if you slough around here too long you could\nwind up getting that weird rash again.", t = 0.03)
        time.sleep(0.5)
    elif inp == "drown":
        slow_print_ack("You lazily set yourself adrift atop the murky waters. . . \n", t = 0.03)
        slow_print_ack("Despite your best efforts, the swamp waters are too shallow to drown in.\n", t = 0.03)
    

###GAME INTERACTIVITY###

    
#def make_sound():
 #   alarm = AudioSegment.from_wav("Alarm01.wav")
  #  play(alarm)
    
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


def lookup_address_by_name(name):
    try:
        address = zonemap_lookup_address_by_name[name]
        address = special_lookup_address_by_name[name]
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

def player_examine(action):
    if zonemap[myPlayer.location][Solved]:
        print("Solved")
    else:
        print("Unsolved")
        ####Trigger event.
 
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

def prompt():
    print("\n" + "=====================")
    # I want to add: look, glance, read, climb, take, 'eat', 'drink', 'back', blah blah blah I want this to all be in a json file, daddy.
    acceptable_actions = ['sit', 'stand', 'sound', 'help', 'move', 'go', 'walk', 'quit', 'examine', 'scratch', 'glance', 'look', 'look at', 'onscreen', 'baswash', 'teleport', 'dev']
    action = prompt_select_from("What would you like to do?", acceptable_actions, "Unknown action, tryangle again.")

    if action.lower() == 'quit':
        input("ARE YOU SURE YOU WANT TO QUIT? y/n*\n>>>")
        if input == 'y' 'Y' 'yes' 'Yes':
            sys.exit()
        else:
            prompt()
    elif action.lower() in ['sound']:
        make_sound()
    elif action.lower() in ['help']:
        cry_for_help()
    elif action.lower() in ['move', 'go', 'walk']:
        player_move(action.lower(), zonemap, myPlayer)
    elif action.lower() in ['glance']:
        myPlayer.player_glance()
    elif action.lower() in ['look']:
        myPlayer.player_look()
    elif action.lower() in ['onscreen']:
        myPlayer.print_location()
    elif action.lower() in ['baswash']:
        god_mode()
    elif action.lower() in ['scratch']:
        slow_print_ack("You can't scratch this itch.\nI'm sorry.")
    elif action.lower() in ['sit']:
        slow_print_ack("You sit on the wet ground.\n", t = .08)
    elif action.lower in ['stand']:
        slow_print_ack("You feel the ground under your socks.\n", t = 0.05)
    elif action.lower() in ['dev']:
        if myPlayer.editrooms is True:
            room_edit_prompt()
        else:
            slow_print("You can't do that without permission.")
            prompt()
    elif action.lower() in ['teleport']:
        if myPlayer.can_teleport():
            player_teleport(action.lower())
        else:
            slow_print("You can't do that without permission.")
            prompt()

def cry_for_help():
    slow_print_ack("HELP!\n", t = 0.05)
    slow_print_ack("HEEEEEEELP!!!!\n", t = 0.03)
    slow_print_ack("... ... ...\n", t = 0.04)
    slow_print_ack("No answer, but you think you hear the sound of distant drums.\nBetter hunker down and lay low.", t = 0.03)


myPlayer = Player(zonemap)
#myRoom = Room()
title_screen()



##### def room_edit_prompt():
  #  inp = prompt_select_from("A)New Room\n B)Edit this room\n C)Exit", ['a', 'b', 'c'], "Try again.")
   # inp = inp.lower()
    #if inp == 'a':
     #   create_new_room(myRoom)
    # elif inp == 'b':
    #     edit_room()
    # elif inp == 'c':
    #     slow_print("Sam hands the ring back to Frodo")
    #     prompt()
