
import datetime

from .methods_engine import (
    load_reference,
    load_crossreference,
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
        """
        Create a dictionary string of an existing Rule object that can be saved to a JSON file for storage.
        """

        # set the object values to a dictionary
        datadict = {
            'name': self.name,
            'description': self.description
        }

        return datadict
    
    @staticmethod
    def from_dict(datadict):
        """
        create a Rule object from a an existing warband saved as a dict in a json file
        """

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
        """
        Create a dictionary string of an existing Treasury object that can be saved to a JSON file for storage.
        """

        # set the object values to a dictionary
        datadict = {
            'gold': self.gold,
            'wyrd': self.wyrd
        }
        return datadict

    @staticmethod
    def from_dict(datadict):
        """
        create a Treasury object from a an existing warband saved as a dict in a json file
        """

        # set the dictionary values to a python object
        dataobject = Treasury(
            gold = datadict["gold"],
            wyrd = datadict["wyrd"]
            )
        
        return dataobject

class Item(object):
    def __init__(self, name, source, category, subcategory, database_id= None, distance=0, skill=None, abilitylist=[], magiclist=[], price=0, description=None):
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

    @staticmethod
    def from_database(primarykey):
        """
        create a new Item object from a record in the database
        """

        table = load_reference("items")
        for record in table:
            if record.primarykey == primarykey:
                item_record = record
                break

        skill = Skill.from_database_record(item_record)

        # find the reference dictionaries of a set of values to a list of python objects
        # Create list of abilities
        item_ability_records = load_crossreference(
            source_table="items",
            target_table="abilities",
            key=primarykey,
            )

        abilitylist = []
        for item_ability_record in item_ability_records:
            abilitylist += [Ability.from_database(item_ability_record.recorddict["abilities_id"])]

        # Create list of magics
        item_magic_records = load_crossreference(
            source_table="items",
            target_table="magics",
            key=primarykey,
            )

        magiclist = []
        for item_magic_record in item_magic_records:
            magiclist += [Magic.from_database(item_magic_record.recorddict["magics_id"])]

        # set the database values to a python object
        dataobject = Item(
            name = "My Item",
            subcategory = item_record.recorddict["subcategory"],
            source = item_record.recorddict["source"],
            category = item_record.recorddict["category"],
            distance = item_record.recorddict["distance"],
            skill = skill,
            abilitylist = abilitylist,
            magiclist = magiclist,
            price = item_record.recorddict["price"],
            description = item_record.recorddict["description"],
            )
        
        return dataobject

    def to_dict(self):
        """
        Create a dictionary string of an existing Item object that can be saved to a JSON file for storage.
        """

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
        """
        create an Item object from a an existing warband saved as a dict in a json file
        """

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
        """
        depreciated
        """

        return

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
        """
        depreciated
        """

        return

        try:

            # open reference data json file
            datadict = load_reference("items")

            # get specific data
            itemdict = datadict[category][source][subcategory]

            # create object based on the reference data
            dataobject = Item.from_refdict(datadict = itemdict)

        except:
            dataobject = None
            print(f"Couldn't add item")

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

    @staticmethod
    def from_database_record(record):
        """
        create a new Skill object from a record in the database
        """

        try:
            # set the record values to a python object
            dataobject = Skill(
                movement = record.recorddict["movement"],
                weapon = record.recorddict["weapon"],
                ballistic = record.recorddict["ballistic"],
                strength = record.recorddict["strength"],
                impact = record.recorddict["impact"],
                toughness = record.recorddict["toughness"],
                wounds = record.recorddict["wounds"],
                initiative = record.recorddict["initiative"],
                actions = record.recorddict["actions"],
                leadership = record.recorddict["leadership"],
                armoursave = record.recorddict["armoursave"],
                )
        except:
            print(f"Record {record} doesnt contain all needed skills!")

        return dataobject

    def to_dict(self):  
        """
        Create a dictionary string of an existing Skill object that can be saved to a JSON file for storage.
        """

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
        """
        create a Skill object from a an existing warband saved as a dict in a json file
        """

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
    def __init__(self, source, main, category, name, database_id=None, description=""):
        self.source = source
        self.main = main
        self.category = category
        self.name = name
        self.description = description

    @staticmethod
    def from_database(primarykey):
        """
        create a new Ability object from a record in the database
        """

        table = load_reference("abilities")
        for record in table:
            if record.primarykey == primarykey:
                ability_record = record
                break

        # set the record to a python object
        dataobject = Ability(
            source = ability_record.recorddict["source"],
            main = ability_record.recorddict["maincategory"],
            category = ability_record.recorddict["category"],
            name = ability_record.recorddict["name"],
            description = ability_record.recorddict["description"],
            )

        return dataobject

    def to_dict(self):  
        """
        Create a dictionary string of an existing Ability object that can be saved to a JSON file for storage.
        """

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
        """
        create an Ability object from a an existing warband saved as a dict in a json file
        """

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
        """
        depreciated
        """

        return

        # open reference data json file
        datadict = load_reference("abilities")

        # get specific data
        abilitydict = datadict[main][category][source][name]

        # create object based on the data
        dataobject = Ability.from_dict(abilitydict)

        return dataobject

class Magic(object):
    """Default object to assign magic as a basis for character and item abilities"""
    def __init__(self, source, category, name, group, difficulty, database_id=None, description=""):
        self.source = source
        self.category = category
        self.name = name
        self.group = group
        self.difficulty = difficulty
        self.description = description

    @staticmethod
    def from_database(primarykey):
        """
        create a new Ability object from a record in the database
        """

        table = load_reference("magics")
        for record in table:
            if record.primarykey == primarykey:
                magic_record = record
                break

        # set the record to a python object
        dataobject = Magic(
            source = magic_record.recorddict["source"],
            category = magic_record.recorddict["category"],
            name = magic_record.recorddict["name"],
            group = magic_record.recorddict["grouping"],
            difficulty = magic_record.recorddict["difficulty"],
            description = magic_record.recorddict["description"],
            )

        return dataobject

    def to_dict(self):  
        """
        Create a dictionary string of an existing Magic object that can be saved to a JSON file for storage.
        """

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
        """
        create a Magic object from a an existing warband saved as a dict in a json file
        """

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

class Event(object):
    """Default object to assign events as a basis for warband, character and item events"""
    def __init__(self, uniquehash, datetime, category, skill, description):
        self.uniquehash = uniquehash
        self.datetime = datetime
        self.category = category
        self.skill = skill
        self.description = description

    def to_dict(self):  
        """
        Create a dictionary string of an existing Event object that can be saved to a JSON file for storage.
        """

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
        """
        create an Event object from a an existing warband saved as a dict in a json file
        """

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
    def create_event(category, skill, description):

        # create object based on the given parameters
        dataobject = Event(
            uniquehash = hash(str(datetime) + str(category) + str(description)),
            datetime = str(datetime.datetime.now()),
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