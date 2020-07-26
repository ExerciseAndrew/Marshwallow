
def prompt():
    print("\n" + "=====================")
    # I want to add: look, glance, read, climb, take, 'eat', 'drink', 'back', 
    acceptable_actions = ['move','go', 'walk', 'quit', 'examine', 'scratch', 'glance', 'look', 'look at', 'onscreen', 'baswash', 'teleport', 'dev', 'help']
    action = prompt_select_from("What would you like to do?", acceptable_actions, "Unknown action, tryangle again.")

    if action.lower() == 'quit':
        input("ARE YOU SURE YOU WANT TO QUIT? y/n*\n>>>")
        if input == 'y' 'Y' 'yes' 'Yes':
            sys.exit()
        else:
            prompt()
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
    elif action.lower() in ["scratch"]:
        slow_print_ack("You can't scratch this itch.\nI'm sorry.")
        prompt()
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
        slow_print_ack("HELP!\n", t = 0.01)
        slow_print_ack("HEEEEEEELP!!!!\n", t = 0.01)
        slow-print_ack("... ... ...\n", t = 0.01)
        slow_print_ack("No answer, but you think you hear the sound of distant drums.\nBetter hunker down and lay low.", t = 0.01)