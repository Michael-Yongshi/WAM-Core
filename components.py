

class Inventory(object):
    def __init__(self, gold=0, wyrd=0, itemlist=[]):
        self.gold = gold
        self.wyrd = wyrd
        self.itemlist = itemlist if itemlist else []

    def add_item(self, itemname):
        itemlis.append(itemname)

    def get_totalitems(self):
        itemlist = self.itemlist if self.itemlist else None
        return itemlist

    def get_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'gold': self.gold,
            'wyrd': self.wyrd,
            'itemlist': str(self.itemlist)
        }
        return data


class Item(object):
    def __init__(self, name, category, skill=None, abilitylist=[], desc=None, price=0):
        self.name = name
        self.category = category
        self.desc = desc
        self.skill = skill if skill else Skill(0,0,0,0,0,0,0,0,0,0)
        self.abilitylist = abilitylist if abilitylist else []
        self.price = price

    def get_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'name': self.name,
            'category': self.category,
            'desc': self.desc,
            'skill': str(self.skill),
            'abilitylist': str(self.abilitylist),
            'price': self.price     
        }
        return data


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