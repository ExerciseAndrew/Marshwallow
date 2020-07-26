import json

#
def edit_rm_json(rm, filename):
    fp = open(filename, "w")
    string = json.dumps(rm, sort_keys = True, indent = 4)
    _ = fp.write( string )
    fp.close()
    
def edit_zm_json(zm, filename):
    # this replaces the original zonemap.json
    fp = open(filename, "w")
    string = json.dumps(zm, sort_keys = True, indent = 4)
    _ = fp.write( string )
    fp.close()

def load_json(p):
    p = "data/" + p
    with open(p, 'r') as file:
        data = file.read()
    return json.loads(data)

#actionfile = load_json("actions.json")
#special = load_json("special_cases.json")
zonemap = load_json("zonemap_original.json")
zonemap_lookup_address_by_name = {}
for address, value in zonemap.items():
    zonemap_lookup_address_by_name[value['zonename']] = address
special_lookup_address_by_name = {}
#for address, value in special.items():
 #   special_lookup_address_by_name[value['cases']] = address


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
