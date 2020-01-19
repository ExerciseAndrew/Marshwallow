import os
import sys
import time

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

def clear():
    if os.name == 'nt': # windows
        _ = os.system('cls')
    else: # non windows
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


def split_first_word(s):
    return s.split(" ", 1)


