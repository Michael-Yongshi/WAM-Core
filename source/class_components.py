from source.methods_json import (
    open_json,
)

from source.methods_database import(
    get_abilityref,
    get_characterref,
    get_itemref,
    get_magicref,
    get_warbandref,
)

# Contains several component classes that are used in different places:
# Inventory
# Items
# Skills
# Abilities


class Rule(object):
    """Default object to assign special rules to a warband. Although should be race specific, for now it is saved in the warband for quick reference only"""
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def to_dict(self):  

        data = {
            # 'key': str(self),
            'name': self.name,
            'description': self.description
        }

        return data
    
    @staticmethod
    def from_dict(datadict):
        
        data = Rule(
            name=datadict["name"],
            description=datadict["description"]
            )

        return data

class Treasury(object):
    def __init__(self, gold=0, wyrd=0):
        self.gold = gold
        self.wyrd = wyrd

    def to_dict(self):  
        data = {
            # 'key': str(self),
            'gold': self.gold,
            'wyrd': self.wyrd
        }
        return data

    @staticmethod
    def from_dict(datadict):
        data = Treasury(
            gold=datadict["gold"],
            wyrd=datadict["wyrd"]
            )
        
        return data

class Item(object):
    def __init__(self, name, source, category, distance=0, skill=None, abilitylist=[], magiclist=[], price=0, description=None):
        self.name = name
        self.source = source
        self.category = category
        self.distance = distance
        self.skill = skill if skill else Skill()
        self.abilitylist = abilitylist
        self.magiclist = magiclist
        self.price = price
        self.description = description

    def to_dict(self):  
        skill = self.skill.to_dict()
        
        abilitylist=[]
        for ability in self.abilitylist:
            abilitylist += [ability.to_dict()]
              
        magiclist=[]
        for magic in self.magiclist:
            magiclist += [magic.to_dict()]

        data = {
            # 'key': str(self),
            'source': self.source,
            'category': self.category,
            'name': self.name,
            'distance': self.distance,
            'skill': skill,
            'abilitylist': abilitylist,
            'magiclist': magiclist,
            'price': self.price,
            'description': self.description
        }
        return data

    @staticmethod
    def from_dict(datadict):
        skilldict = datadict["skill"]
        skill = Skill.from_dict(skilldict)

        abilitylist = []
        for abilitydict in datadict["abilitylist"]:
            abilityref = get_abilityref(
                source=abilitydict["source"], 
                category=abilitydict["category"], 
                name=abilitydict["name"], 
            )
            abilitylist += [Ability.from_dict(abilityref)]

        magiclist = []
        for magicdict in datadict["magiclist"]:
            magicref = get_magicref(
                source=magicdict["source"], 
                category=magicdict["category"], 
                name=magicdict["name"], 
            )
            magiclist += [Magic.from_dict(magicref)]

        data = Item(
            name=datadict["name"],
            source=datadict["source"],
            category=datadict["category"],
            skill=skill,
            abilitylist=abilitylist,
            magiclist=magiclist,
            price=datadict["price"],
            description=datadict["description"]
            )
        
        return data

    @staticmethod
    def create_item(source, category, name):
        # open reference data json file
        data = open_json("database/references/items_ref.json")
        datadict = data[source][category][name]

        new_item = Item.from_dict(datadict)

        return new_item


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
    
    def to_dict(self):  

        data = {
            # 'key': str(self),
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

    @staticmethod
    def from_dict(datadict):

        skill = Skill(
            movement=datadict["movement"],
            weapon=datadict["weapon"],
            ballistic=datadict["ballistic"],
            strength=datadict["strength"],
            toughness=datadict["toughness"],
            wounds=datadict["wounds"],
            initiative=datadict["initiative"],
            actions=datadict["actions"],
            leadership=datadict["leadership"],
            armoursave=datadict["armoursave"]
            )

        return skill

    def to_list(self):

        data = []
        data.append(self.movement),
        data.append(self.weapon),
        data.append(self.ballistic),
        data.append(self.strength),
        data.append(self.toughness),
        data.append(self.wounds),
        data.append(self.initiative),
        data.append(self.actions),
        data.append(self.leadership),
        data.append(self.armoursave),
        
        return data

    @staticmethod
    def from_list(datalist):

        skill = Skill(
            movement=datalist[0],
            weapon=datalist[1],
            ballistic=datalist[2],
            strength=datalist[3],
            toughness=datalist[4],
            wounds=datalist[5],
            initiative=datalist[6],
            actions=datalist[7],
            leadership=datalist[8],
            armoursave=datalist[9],
            )

        return skill

    def to_string(self):
        data = f"mo: {self.movement}, we: {self.weapon}, ba: {self.ballistic}, st: {self.strength}, to: {self.toughness}, wo: {self.wounds}, in: {self.initiative}, ac: {self.actions}, le: {self.leadership}, as: {self.armoursave}"
        
        return data

class Ability(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, source, category, name, description=""):
        self.source = source
        self.category = category
        self.name = name
        self.description = description

    def to_dict(self):  
        
        data = {
            # 'key': str(self),
            'source': self.source,
            'category': self.category,
            'name': self.name,
            'description': self.description
        }

        return data
    
    @staticmethod
    def from_dict(datadict):

        data = Ability(
            source=datadict["source"],
            category=datadict["category"],
            name=datadict["name"],
            description=datadict["description"]
            )

        return data

    @staticmethod
    def create_ability(source, category, name):
        # open reference data json file
        data = open_json("database/references/abilities_ref.json")
        datadict = data[source][category][name]

        new_ability = Ability.from_dict(datadict)

        return new_ability

class Magic(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, source, category, name, difficulty, description=""):
        self.source = source
        self.category = category
        self.name = name
        self.difficulty = difficulty
        self.description = description

    def to_dict(self):  

        data = {

            # 'key': str(self),
            'source': self.source,
            'category': self.category,
            'name': self.name,
            'difficulty': self.difficulty,
            'description': self.description
        }

        return data

    @staticmethod
    def from_dict(datadict):
        
        data = Magic(
            source = datadict["source"],
            category=datadict["category"],
            name=datadict["name"],
            difficulty=datadict["difficulty"],
            description=datadict["description"]
            )

        return data

    @staticmethod
    def create_magic(source, category, name):
        # open reference data json file
        data = open_json("database/references/magic_ref.json")
        datadict = data[source][category][name]

        new_magic = Magic.from_dict(datadict)

        return new_magic