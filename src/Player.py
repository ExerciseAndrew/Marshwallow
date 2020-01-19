### Player Setup ###
class Player:
    def __init__(self, zonemap):
        self.name = ''
        self.triangle = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'c1' ## Also known as 'address' ##
        self.game_over = False
        self._teleport = False
        self.keys = False
        self._zm = zonemap

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

    def print_location(self):
            address = self.location
            room = self._zm[address]
            print ("")
            print ("#"*(4 + len(address)))
            print ("# " + address.upper() + " #")
            print ("# "+ room['description'].replace('\n', '') +  " #")
            print ("#"*(4 + len(address)) )

    def can_teleport(self):
        return self._teleport


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