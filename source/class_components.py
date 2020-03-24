
from .methods_engine import (
    load_reference,
)

from .methods_database_from import(
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
# Events


class Rule(object):
    """Default object to assign special rules to a warband. Although should be race specific, for now it is saved in the warband for quick reference only"""
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def to_dict(self):  

        # set the object values to a dictionary
        datadict = {
            'name': self.name,
            'description': self.description
        }

        return datadict
    
    @staticmethod
    def from_dict(datadict):
        
        # set the dictionary values to a python object
        dataobject = Rule(
            name = datadict["name"],
            description = datadict["description"]
            )

        return dataobject

class Treasury(object):
    def __init__(self, gold=0, wyrd=0):
        self.gold = gold
        self.wyrd = wyrd

    def to_dict(self):  
        
        # set the object values to a dictionary
        datadict = {
            'gold': self.gold,
            'wyrd': self.wyrd
        }
        return datadict

    @staticmethod
    def from_dict(datadict):

        # set the dictionary values to a python object
        dataobject = Treasury(
            gold = datadict["gold"],
            wyrd = datadict["wyrd"]
            )
        
        return dataobject

class Item(object):
    def __init__(self, name, source, category, subcategory, distance=0, skill=None, abilitylist=[], magiclist=[], price=0, description=None):
        self.name = name
        self.source = source
        self.category = category
        self.subcategory = subcategory
        self.distance = distance
        self.skill = skill if skill else Skill()
        self.abilitylist = abilitylist
        self.magiclist = magiclist
        self.price = price
        self.description = description

    def to_dict(self):

        # recursively set some nested objects to a dictionary
        skill = self.skill.to_dict()
        
        # recursively set a list of objects to a list of dictionaries
        abilitylist=[]
        for ability in self.abilitylist:
            abilitylist += [ability.to_dict()]
              
        magiclist=[]
        for magic in self.magiclist:
            magiclist += [magic.to_dict()]

        # set the object values to a dictionary
        datadict = {
            # 'key': str(self),
            'name': self.name,
            'source': self.source,
            'category': self.category,
            'subcategory': self.subcategory,
            'distance': self.distance,
            'skill': skill,
            'abilitylist': abilitylist,
            'magiclist': magiclist,
            'price': self.price,
            'description': self.description
        }
        return datadict

    @staticmethod
    def from_dict(datadict):
        
        # recursively set some nested dictionaries to a python object
        skill = Skill.from_dict(datadict["skill"])

        # recursively set a list of dictionaries to a list of python objects
        # events = datadict["events"]
                
        abilitylist = []
        for abilitydict in datadict["abilitylist"]:
            abilitylist += [Ability.from_dict(abilitydict)]

        magiclist = []
        for magicdict in datadict["magiclist"]:
            magiclist += [Magic.from_dict(magicdict)]

        # set the dictionary values to a python object
        dataobject = Item(
            name = datadict["name"],
            subcategory = datadict["subcategory"],
            source = datadict["source"],
            category = datadict["category"],
            distance = datadict["distance"],
            skill = skill,
            abilitylist = abilitylist,
            magiclist = magiclist,
            price = datadict["price"],
            description = datadict["description"]
            )
        
        return dataobject

    @staticmethod
    def from_refdict(datadict):

        # recursively set a dictionary to some nested objects
        skill = Skill.from_dict(datadict["skill"])

        # find the reference dictionaries of a set of values to a list of python objects
        #  events = []

        abilitylist = []
        for abilitydict in datadict["abilitylist"]:
            abilityref = get_abilityref(
                source = abilitydict["source"], 
                main = abilitydict["main"],
                category = abilitydict["category"], 
                name = abilitydict["name"], 
            )
            abilitylist += [Ability.from_dict(abilityref)]

        magiclist = []
        for magicdict in datadict["magiclist"]:
            magicref = get_magicref(
                source = magicdict["source"], 
                category = magicdict["category"], 
                name = magicdict["name"], 
            )
            magiclist += [Magic.from_dict(magicref)]

        # set the dictionary values to a python object
        dataobject = Item(
            name = "",
            subcategory = datadict["subcategory"],
            source = datadict["source"],
            category = datadict["category"],
            distance = datadict["distance"],
            skill = skill,
            abilitylist = abilitylist,
            magiclist = magiclist,
            price = datadict["price"],
            description = datadict["description"]
            )
        
        return dataobject

    @staticmethod
    def create_item(source, category, subcategory):
        # open reference data json file
        datadict = load_reference("items")

        # get specific data
        itemdict = datadict[category][source][subcategory]

        # create object based on the reference data
        dataobject = Item.from_refdict(datadict = itemdict)

        return dataobject

class Skill(object):
    """Default object to assign skill values as a basis for character and item skill values"""
    def __init__(self, movement=0, weapon=0, ballistic=0, strength=0, impact=0, toughness=0, wounds=0, initiative=0, actions=0, leadership=0, armoursave=0):
        self.movement = movement
        self.weapon = weapon
        self.ballistic = ballistic
        self.strength = strength
        self.impact = impact
        self.toughness = toughness
        self.wounds = wounds
        self.initiative = initiative
        self.actions = actions
        self.leadership = leadership
        self.armoursave = armoursave
    
    def to_dict(self):  

        # set the object values to a dictionary
        datadict = {
            'movement': self.movement,
            'weapon': self.weapon,
            'ballistic': self.ballistic,
            'strength': self.strength,
            'impact': self.impact,
            'toughness': self.toughness,
            'wounds': self.wounds,
            'initiative': self.initiative,
            'actions': self.actions,
            'leadership': self.leadership,
            'armoursave': self.armoursave,
        }

        return datadict

    @staticmethod
    def from_dict(datadict):

        # set the dictionary values to a python object
        dataobject = Skill(
            movement = datadict["movement"],
            weapon = datadict["weapon"],
            ballistic = datadict["ballistic"],
            strength = datadict["strength"],
            impact = datadict["impact"],
            toughness = datadict["toughness"],
            wounds = datadict["wounds"],
            initiative = datadict["initiative"],
            actions = datadict["actions"],
            leadership = datadict["leadership"],
            armoursave = datadict["armoursave"],
            )

        return dataobject

    def to_list(self):

        # set the object values to a list
        datalist = []
        datalist.append(self.movement),
        datalist.append(self.weapon),
        datalist.append(self.ballistic),
        datalist.append(self.strength),
        datalist.append(self.impact),
        datalist.append(self.toughness),
        datalist.append(self.wounds),
        datalist.append(self.initiative),
        datalist.append(self.actions),
        datalist.append(self.leadership),
        datalist.append(self.armoursave),
        
        return datalist

    @staticmethod
    def from_list(datalist):

        # set the list values to a python object
        dataobject = Skill(
            movement = datalist[0],
            weapon = datalist[1],
            ballistic = datalist[2],
            strength = datalist[3],
            impact = datalist[4],
            toughness = datalist[5],
            wounds = datalist[6],
            initiative = datalist[7],
            actions = datalist[8],
            leadership = datalist[9],
            armoursave = datalist[10],
            )

        return dataobject

    def to_string(self):

        # convert the python object to a string of values
        datastring = f"mo: {self.movement}, we: {self.weapon}, ba: {self.ballistic}, st: {self.strength}, im: {self.impact}, to: {self.toughness}, wo: {self.wounds}, in: {self.initiative}, ac: {self.actions}, le: {self.leadership}, as: {self.armoursave}"
        
        return datastring
    
    @staticmethod
    def create_skill_empty():
        
        dataobject = Skill(0,0,0,0,0,0,0,0,0,0,0,)

        return dataobject

class Ability(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, source, category, name, description=""):
        self.source = source
        self.main = main
        self.category = category
        self.name = name
        self.description = description

    def to_dict(self):  
        
        # set the object values to a dictionary
        datadict = {
            'source': self.source,
            'main': self.main,
            'category': self.category,
            'name': self.name,
            'description': self.description
        }

        return datadict
    
    @staticmethod
    def from_dict(datadict):

        # set the dictionary values to a python object
        dataobject = Ability(
            source = datadict["source"],
            main = datadict["main"],
            category = datadict["category"],
            name = datadict["name"],
            description = datadict["description"],
            )

        return dataobject

    @staticmethod
    def create_ability(source, main, category, name):
        # open reference data json file
        datadict = load_reference("abilities")

        # get specific data
        abilitydict = datadict[main][category][source][name]

        # create object based on the data
        dataobject = Ability.from_dict(abilitydict)

        return dataobject

class Magic(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, source, category, name, group, difficulty, description=""):
        self.source = source
        self.category = category
        self.name = name
        self.group = group
        self.difficulty = difficulty
        self.description = description

    def to_dict(self):  

        # set the object values to a dictionary
        datadict = {
            'source': self.source,
            'category': self.category,
            'name': self.name,
            'group': self.group,
            'difficulty': self.difficulty,
            'description': self.description
        }

        return datadict

    @staticmethod
    def from_dict(datadict):
        
        # set the dictionary values to a python object
        dataobject = Magic(
            source = datadict["source"],
            category = datadict["category"],
            name = datadict["name"],
            group = datadict["group"],
            difficulty = datadict["difficulty"],
            description = datadict["description"],
            )

        return dataobject

    @staticmethod
    def create_magic(source, category, name):
        # open reference data json file
        datadict = load_reference("magic")

        # get specific data
        magicdict = datadict[source][category][name]

        # create object based on the data
        dataobject = Magic.from_dict(magicdict)

        return dataobject

class Event(object):
    """Default object to assign events as a basis for warband, character and item events"""
    def __init__(self, uniquehash, datetime, category, skill, description):
        self.uniquehash = uniquehash
        self.datetime = datetime
        self.category = category
        self.skill = skill
        self.description = description

    def to_dict(self):  

        # recursively set some nested objects to a dictionary
        skill = self.skill.to_dict()

        # set the object values to a dictionary
        datadict = {
            'uniquehash': self.uniquehash,
            'datetime': self.datetime,
            'category': self.category,
            'skill': skill,
            'description': self.description,
        }

        return datadict

    @staticmethod
    def from_dict(datadict):
        
        # recursively set some nested dictionaries to a python object
        skill = Skill.from_dict(datadict["skill"])

        # set the dictionary values to a python object
        dataobject = Event(
            uniquehash = datadict["uniquehash"],
            datetime = datadict["datetime"],
            category = datadict["category"],
            skill = skill,
            description = datadict["description"],
            )

        return dataobject

    def to_string(self):
        
        datastring = f"{self.uniquehash} - {self.datetime} - {self.category} - {self.description}"

        return datastring

    @staticmethod
    def create_event(datetime, category, skill, description):

        # create object based on the given parameters
        dataobject = Event(
            uniquehash = hash(str(datetime) + str(category) + str(description)),
            datetime = str(datetime),
            category = category,
            skill = skill,
            description = description,
            )

        return dataobject

    def set_advance_event(self, skill, ability=""):
        """Set a level up to new advance event. The specific event is given (advance with TBD at the end of the description) """
        
        currentdescription = self.description[:-4]
        self.description = currentdescription

        # check if skill increases or an ability happens
        if skill.to_string() != Skill.create_skill_empty().to_string():
            self.skill = skill

            # check which of the skills changed and add it to the description
            skilldict = skill.to_dict()
            for key in skilldict:
                if skilldict[key] != 0:
                    self.description = f"{self.description} \n - character achieved an increase in {key}"
        else:
            self.description = f"{self.description} character achieved the ability of {ability}"