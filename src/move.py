
from text_utilities import*

NORTH = 'north', 'n'
SOUTH = 'south', 's'
WEST = 'west', 'w'
EAST = 'east', 'e'
#FORWARD = 'forward', 'f'
#BACKWARD = 'back', 'backward', 'b', 

def player_move(myAction, zonemap, player):
    room = zonemap[player.location]
    while True:
        dest = input("What direction would you like to walk?\n")
        if dest in NORTH:
            destination = room['north']
            movement_handler(destination, zonemap, player)
            return
        elif dest in WEST:
            destination = room['west']
            movement_handler(destination, zonemap, player)
            return
        elif dest in EAST:
            destination = room['east']
            movement_handler(destination, zonemap, player)
            return
        elif dest in SOUTH:
           # destination = room['south']
            movement_handler(destination, zonemap, player)
            return
        else:
            print("Wait, go where?")

def movement_handler(destination, zonemap, player):
    if destination in zonemap:
        inp = urg_prompt("\n  You want to walk to the " + destination + "?")
        if inp in ('yes', 'Yes', 'y', 'Y'):
            print("\nYou walk to the " + destination + ".\n")
            player.location = destination
            player.print_location()
        elif inp == 'no':
            return
        elif destination == "":
            print("Well?")
        else:
            print("Did you say yes or no?")
    else:
        slow_print_ack("Maybe figure out where you're going before you just start yammering.\n", t = 0.03)
        