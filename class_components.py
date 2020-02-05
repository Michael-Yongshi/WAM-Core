from database.json import open_json

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

    def to_dict(self, ref):  
        skill = self.skill.to_dict()
        
        abilitylist={}
        a = 1
        for ability in self.abilitylist:
            abilityref = "Ability" + str(a)
            abilitylist.update(ability.to_dict(ref=abilityref))
            a += 1        
        
        magiclist={}
        m = 1
        for magic in self.magiclist:
            magicref = "Magic" + str(m)
            magiclist.update(magic.to_dict(ref=magicref))
            m += 1

        data = {}
        data[str(ref)] = {
            # 'key': str(self),
            'name': self.name,
            'source': self.source,
            'category': self.category,
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
        skill = Skill.from_dict(datadict["skill"])
        
        abilitylist = []
        for ability in datadict["abilitylist"].values():
            abilitylist += [Ability.from_dict(ability)]
            
        magiclist = []
        for magic in datadict["magiclist"].values():
            magiclist += [Magic.from_dict(magic)]

        item = Item(
            name=datadict["name"],
            source=datadict["source"],
            category=datadict["category"],
            skill=skill,
            abilitylist=abilitylist,
            magiclist=magiclist,
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

        magiclist = []
        for magicdict in data[source][name].get("magiclist"):
            magicobject = Magic(source=magicdict["source"], category=magicdict["category"], name=magicdict["name"], difficulty=magicdict["difficulty"], description=magicdict["description"])
            magiclist.append(magicobject)

        newitem = Item(
            name = name,
            source = source,
            category = data[source][name].get("category"),
            distance = data[source][name].get("distance"),
            skill = newskill,
            abilitylist = abilitylist,
            magiclist = magiclist,
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
        data = Ability(
            name=datadict["name"],
            description=datadict["description"]
            )

        return data

class Magic(object):
    """Default object to assign ablities as a basis for character and item abilities"""
    def __init__(self, source, category, name, difficulty, description=None):
        self.source = source
        self.category = category
        self.name = name
        self.difficulty = difficulty
        self.description = description

    def to_dict(self, ref):  
        data = {}
        data[str(ref)] = {
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