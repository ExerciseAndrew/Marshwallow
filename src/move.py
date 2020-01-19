import json

UP = 'up', 'north', 'n'
DOWN = 'down', 'south', 's'
LEFT = 'left','west', 'w'
RIGHT = 'right', 'east', 'e'

def player_move(myAction, zonemap, player):
    room = zonemap[player.location]
    while True:
        dest = input("Where would you like to move?\n")
        if dest in UP:
            destination = room['up']
            movement_handler(destination, zonemap, player)
            return
        elif dest in LEFT:
            destination = room['left']
            movement_handler(destination, zonemap, player)
            return
        elif dest in RIGHT:
            destination = room['right']
            movement_handler(destination, zonemap, player)
            return
        elif dest in DOWN:
            destination = room['down']
            movement_handler(destination, zonemap, player)
            return
        else:
            print("Wait, go where?")

def movement_handler(destination, zonemap, player):
    if destination in zonemap:
        print("\n" + "you have moved to " + destination + ".\n")
        player.location = destination
        player.print_location()
    else:
        if destination == "":
            print("There is no exit in that direction")
        else:
            print("Please let an admin know that this room exit is broken.")
