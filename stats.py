class Skill(object):
    """Default object to assign skill values as a basis for character and item skill values"""
    def __init__(self, movement=0, weapon=0, ballistic=0, strength=0, toughness=0, wounds=0, initiative=0, actions=0, leadership=0, armoursave=0):
        self.movement = movement
        self.weapon = weapon
        self.ballistic = ballistic
        self.strength = strength
        self.toughness = toughness
        self.wounds = wounds
        self.initiative = initiative
        self.actions = actions
        self.leadership = leadership
        self.armoursave = armoursave
    
    def get_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'movement': self.movement,
            'weapon': self.weapon,
            'ballistic': self.ballistic,
            'strength': self.strength,
            'toughness': self.toughness,
            'wounds': self.wounds,
            'initiative': self.initiative,
            'actions': self.actions,
            'leadership': self.leadership,
            'armoursave': self.armoursave
        }
        return data

class Ability(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def get_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'name': self.name,
            'description': self.description
        }
        return data