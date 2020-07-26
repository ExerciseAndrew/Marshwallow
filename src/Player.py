

### Player Setup ###
class Player:
    def __init__(self, zonemap):
        self.name = ''
        self.triangle = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'Swamp Swimming Hole' ## Also known as 'address' ##
        self.facing = ''
        self.game_over = False 
        self._teleport = False 
        self._keys = False
        self._zm = zonemap
        #self._rm = "roommap"
        
   
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

    def player_look(self):
            address = self.location
            room = self._zm[address]
            print ("")
            print ("#"*(4 + len(address)))
            print ("# " + address.upper() + " #")
            print ("# "+ room['look'].replace('\n', '') +  " #")
            print ("#"*(4 + len(address)) )

    def player_glance(self):
            address = self.location
            room = self._zm[address]
            print ("")
            print ("#"*(4 + len(address)))
            print ("# " + address.upper() + " #")
            print ("# "+ room['glance'].replace('\n', '') +  " #")
            print ("#"*(4 + len(address)) )

            

    def can_teleport(self):
        return self._teleport

    def has_keys(self):
        return self._keys