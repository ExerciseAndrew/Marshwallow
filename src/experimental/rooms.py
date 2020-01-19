# import cmd
# import textwrap
# import sys
# import os
# import time
# import random
# import math
# import json

# def clear():
#     if os.name == 'nt':
#         _ = os.system('cls')
#     else:
#         _ = os.system('clear')

# def slow_print(s, t = 0.05):
#     s += "\n"
#     for c in s:
#         sys.stdout.write(c)
#         sys.stdout.flush()
#         time.sleep(t)

# def slow_prompt(s, t = 0.05):
#     slow_print(s, t)
#     return input(">>> ")

# def slow_print_ack(s, t = 0.05):
#     slow_print(s, t)
#     input("")

# class Node:
# 	def __init__(self, name):
#         self.name = name
#         self.description = None

# class Edge:
#      def __init__(self, node_in, command, node_to, constraint = None):
#         self.node_in = node_in
#         self.command = command
#         self.node_to = node_to
#         self.constraint = constraint

# class Object:
#     def __init__(self, start_node, object_name, short_description, long_description, weight):
#         self.start_node = start_node
#         self.object_name = object_name
#         self.short_description = short_description
#         self.long_description = long_description
#         self.weight = weight

# class Room:
#     def __init__(self):
#         self.room_file = room_file
#         self.current = "start"
#         self.nodes = []
#         self.edges = []
#         self.objects = {}
#         self.name = ZONENAME
#         self.trigger = SOLVED
#         self.lock = False
#         self.key = False

#     def open_lock
#         if self.lock = False
#     def get_key(self)
#         if inp == "fullcockofsalami"
#             self.key = True

# def load_json(p):
#     with open(p, 'r') as file:
#         data = file.read()
#     return json.loads(data)

# zonemap = load_json("zonemap.json")