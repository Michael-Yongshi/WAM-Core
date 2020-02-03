from database.json import *

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

    def to_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            # 'key': str(self),
            'name': self.name,
            'description': self.description
        }
        return data
    
    @staticmethod
    def from_dict(datadict):
        rule = Rule(
            name=datadict["name"],
            description=datadict["description"]
            )

        return rule

class Inventory(object):
    def __init__(self, gold=0, wyrd=0, itemlist=[]):
        self.gold = gold
        self.wyrd = wyrd
        self.itemlist = itemlist if itemlist else []

    def to_dict(self):  
        itemlist = {}        
        i = 1
        for item in self.itemlist:
            itemref = "Item" + str(i) # to make sure it has a unique key
            itemlist.update(item.to_dict(ref=itemref))
            i += 1

        data = {
            # 'key': str(self),
            'gold': self.gold,
            'wyrd': self.wyrd,
            'itemlist': itemlist
        }
        return data

    @staticmethod
    def from_dict(datadict):
        itemlist = []
        for item in datadict["itemlist"].values():
            itemlist += [Item.from_dict(item)]

        inventory = Inventory(
            gold=datadict["gold"],
            wyrd=datadict["wyrd"],
            itemlist=itemlist
            )
        
        return inventory

    def get_price(self):
        invprice = 0
        for item in self.itemlist:
            itemprice = item.price
            invprice += itemprice
        return invprice
        
    def add_item(self, itemname):
        itemlist.append(itemname)

    def get_totalitems(self):
        itemlist = self.itemlist if self.itemlist else None
        return itemlist


class Item(object):
    def __init__(self, name, source, category, distance=0, skill=None, abilitylist=[], price=0, description=None):
        self.name = name
        self.source = source
        self.category = category
        self.distance = distance
        self.skill = skill if skill else Skill()
        self.abilitylist = abilitylist
        self.price = price
        self.description = description

    def to_dict(self, ref):  
        skill = self.skill.to_dict()
        
        abilitylist={}
        a = 1
        for ability in self.abilitylist:
            abilityref = "Ability" + str(a) # to make sure it has a unique key
            abilitylist.update(ability.to_dict(ref=abilityref))
            a += 1        
        
        data = {}
        data[str(ref)] = {
            # 'key': str(self),
            'name': self.name,
            'source': self.source,
            'category': self.category,
            'distance': self.distance,
            'skill': skill,
            'abilitylist': abilitylist,
            'price': self.price,
            'description': self.description
        }
        return data

    @staticmethod
    def from_dict(datadict):
        skill = Skill.from_dict(datadict["skill"])
        
        abilitylist = []
        for ability in datadict["abilitylist"].values():
            abilitylist += [Ability.from_dict(ability)]

        item = Item(
            name=datadict["name"],
            source=datadict["source"],
            category=datadict["category"],
            skill=skill,
            abilitylist=abilitylist,
            price=datadict["price"],
            description=datadict["description"]
            )
        
        return item
    @staticmethod
    def create_item(name, source):
        # open reference data json file
        data = open_json("database/references/items_ref.json")

        skilllist = data[source][name].get("skill")
        skilldict = skilllist[0]
        newskill = Skill(
            movement = skilldict["movement"],
            weapon = skilldict["weapon"],
            ballistic = skilldict["ballistic"],
            strength=skilldict["strength"],
            toughness=skilldict["toughness"],
            wounds=skilldict["wounds"],
            initiative=skilldict["initiative"],
            actions=skilldict["actions"],
            leadership=skilldict["leadership"],
            armoursave=skilldict["armoursave"]
            )

        abilitylist = []
        for abilitydict in data[source][name].get("abilitylist"):
            abilityobject = Ability(name=abilitydict["name"], description=abilitydict["description"])
            abilitylist.append(abilityobject)

        newitem = Item(
            name = name,
            source = source,
            category = data[source][name].get("category"),
            distance = data[source][name].get("distance"),
            skill = newskill,
            abilitylist = abilitylist,
            price = data[source][name].get("price"),
            description = data[source][name].get("description")        
        )
        
        return newitem


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

class Ability(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def to_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            # 'key': str(self),
            'name': self.name,
            'description': self.description
        }
        return data

    @staticmethod
    def from_dict(datadict):
        ability = Ability(
            name=datadict["name"],
            description=datadict["description"]
            )

        return ability