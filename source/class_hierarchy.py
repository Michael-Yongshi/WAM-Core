import copy

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

from source.class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    )


class Warband(object):
    def __init__(self, name, race, source, warband, description=None, treasury=None, rulelist=[], itemlist=[], herolist=[], squadlist=[]):
        self.name = name
        self.race = race
        self.source = source
        self.warband = warband
        self.description = description
        self.treasury = treasury if treasury else Treasury()
        self.rulelist = rulelist
        self.itemlist = itemlist
        self.herolist = herolist
        self.squadlist = squadlist

    def to_dict(self):
        """ Create a dictionary string of a Warband object, including all nested objects, that can be saved to a JSON file for storage."""

        treasury = self.treasury.to_dict()

        rulelist = []
        for rule in self.rulelist:
            rulelist += [rule.to_dict()] 

        itemlist = []
        for item in self.itemlist:
            itemlist += [item.to_dict()]

        herolist = []
        for hero in self.herolist:
            herolist += [hero.to_dict()]

        squadlist=[]
        for squad in self.squadlist:
            squadlist += [squad.to_dict()]

        data = {
            # 'key': str(self),
            'name': self.name,
            'race': self.race,
            'source': self.source,
            'warband': self.warband,
            'description': self.description,
            'treasury': treasury,
            'rulelist': rulelist,
            'itemlist': itemlist,
            'herolist': herolist, 
            'squadlist': squadlist,
        }

        return data
    
    @staticmethod
    def from_dict(datadict):
        """ Create an object, and all nested objects, out of a warband dictionary in order to enable updates to that data."""

        treasury = Treasury.from_dict(datadict["treasury"])

        rulelist = []
        for rule in datadict["rulelist"]:
            rulelist += [Rule.from_dict(rule)]

        itemlist = []
        for item in datadict["itemlist"]:
            itemlist += [Item.from_dict(item)]

        herolist = []
        for hero in datadict["herolist"]:
            herolist += [Character.from_dict(hero)]

        squadlist = []
        for squad in datadict["squadlist"]:
            squadlist += [Squad.from_dict(squad)]

        wbid = Warband(
            name = datadict["name"],
            race = datadict["race"],
            source = datadict["source"],
            warband = datadict["warband"],
            description = datadict["description"],
            treasury = treasury,
            rulelist = rulelist,
            itemlist = itemlist,
            herolist = herolist,
            squadlist = squadlist,
            )

        return wbid
    
    @staticmethod
    def create_warband(name, race, source, warband):
        """Create a new warband based on the given parameters"""
        
        # open reference data json file
        data = open_json("database/references/warbands_ref.json")

        rulelist = []
        for ruledict in data[race][source][warband]["rulelist"]:
            ruleobject = Rule.from_dict(ruledict)
            rulelist.append(ruleobject)

        itemlist = []
        for itemdict in data[race][source][warband]["itemlist"]:
            itemobject = Item.from_dict(itemdict)
            itemlist.append(itemobject)

        treasury=Treasury(
            gold = data[race][source][warband]["start_gold"],
        )
        
        # create new basic warband object
        new_warband = Warband(
            name = name, 
            race = race, 
            source = source, 
            warband = warband, 
            treasury = treasury,
            rulelist = rulelist,
            description = data[race][source][warband]["description"],  
        )      
                
        return new_warband

    def get_price(self):
        """ -- Can this be deleted? -- Get the worth of your warband"""
        
        wbinvprice = 0
        if self.itemlist:
            for item in self.itemlist:
                wbinvprice += item.price

        herolistprice = 0
        if self.herolist:
            for hero in self.herolist:
                herolistprice += hero.get_price()

        squadlistprice = 0
        if self.squadlist:
            for squad in self.squadlist:
                squadlistprice += squad.get_price()

        wbprice = wbinvprice + herolistprice + squadlistprice
        
        return wbprice


class Squad(object):
    def __init__(self, name, henchmanlist=[]):
        self.name = name
        self.henchmanlist = henchmanlist

    def to_dict(self):  
        henchmanlist=[] 
        for henchman in self.henchmanlist:
            henchmanlist += [henchman.to_dict()]
        
        data = {
            # 'key': str(self),
            'name': self.name,
            'henchmanlist': henchmanlist
        }
        
        return data

    @staticmethod
    def from_dict(datadict):
        henchmanlist = []
        for henchman in datadict["henchmanlist"]:
            henchmanlist += [Character.from_dict(henchman)]

        squad = Squad(
            name = datadict["name"],
            henchmanlist = henchmanlist,
            )

        return squad

    @staticmethod
    def create_squad(race, source, warband, category, name, number=1):
        """Create a new squad with the given parameters and creates the amount of henchman determined by the number parameter"""
        
        new_squad = Squad(
            name = name,
            henchmanlist = []
            )

        for i in range(0, number):
            newhenchman = Henchman.create_character(
                name = name + str(i),
                race = race,
                source = source,
                warband = warband,
                category = category,  
                )
            new_squad.henchmanlist.append(newhenchman)
                
        return new_squad

    def change_henchman_count(self, deltasize):
        if deltasize > 0:
            i = self.get_totalhenchman()
            
            for _ in range(0, deltasize):
                i += 1
                newhenchman = copy.deepcopy(self.henchmanlist[0])
                newhenchman.name = self.name + str(i)
                self.henchmanlist.append(newhenchman)

        if deltasize < 0:

            for _ in range(0, 0 - deltasize):
                self.henchmanlist.pop(-1)

    def equip_squad(self, source, category, subcategory):
        """Basically runs a create item method for every henchman in this squad"""

        for henchman in self.henchmanlist:
            newitem = Item.create_item(
                source = source,
                category = category,
                subcategory = subcategory,
                )
            henchman.itemlist.append(newitem)

    def get_totalhenchman(self):
        henchmanlist = self.henchmanlist if self.henchmanlist else []
        return len(henchmanlist)

    def get_price(self):

        squadsize = self.get_totalhenchman()
        henchmanprice = self.henchmanlist[0].get_price() # get price of a single character, including items

        squadprice = henchmanprice * squadsize # multiply the price for a henchman, with the number of henchman in the squad

        return squadprice

     
class Character(object):
    def __init__(self, name, race, source, warband, category, ishero, skill, abilitylist=[], magiclist=[], itemlist=[], experience=0, price=0, maxcount=0, description=None):
        self.name = name
        self.race = race
        self.source = source
        self.warband = warband
        self.category = category
        self.ishero = ishero
        self.skill = skill
        self.abilitylist = abilitylist
        self.magiclist = magiclist
        self.itemlist = itemlist
        self.experience = experience
        self.price = price
        self.maxcount = maxcount
        self.description = description
    
    def to_dict(self):  
        skill = self.skill.to_dict()
    
        abilitylist = []
        for ability in self.abilitylist:
            abilitylist += [ability.to_dict()]

        magiclist = []
        for magic in self.magiclist:
            magiclist += [magic.to_dict()]

        itemlist = []
        for item in self.itemlist:
            itemlist += [item.to_dict()]
        
        data = {
            # 'key': str(self),
            'name': self.name,
            'race': self.race,
            'source': self.source,
            'warband': self.warband,
            'category': self.category,
            'ishero': self.ishero,
            'skill': skill,
            'abilitylist': abilitylist,
            'magiclist': magiclist,
            'itemlist': itemlist,
            'experience': self.experience,
            'price': self.price,
            'maxcount': self.maxcount,
            'description': self.description
        }
        return data

    @staticmethod
    def from_dict(datadict, create = False):
        
        if create == True:
            name = ""
        
            abilitylist = []
            for abilitydict in datadict["abilitylist"]:
                abilityref = get_abilityref(
                    source = abilitydict["source"], 
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
            
            itemlist = []
            for itemdict in datadict["itemlist"]:
                itemref = Item.create_item(
                    source = itemdict["source"], 
                    category = itemdict["category"], 
                    subcategory = itemdict["subcategory"], 
                    )
                itemlist += [itemref]

            # events = ""

        else:
            name = datadict["name"]

            abilitylist = []
            for abilitydict in datadict["abilitylist"]:
                abilitylist += [Ability.from_dict(abilitydict)]

            magiclist = []
            for magicdict in datadict["magiclist"]:
                magiclist += [Magic.from_dict(magicdict)]

            itemlist = []
            for itemdict in datadict["itemlist"]:
                itemlist += [Item.from_dict(itemdict)]

            # events = datadict["events"]

        skilldict = datadict["skill"]
        skill = Skill.from_dict(skilldict)

        data = Character(
            name = name,
            race = datadict["race"],
            source = datadict["source"],
            warband = datadict["warband"],
            category = datadict["category"],
            ishero = datadict["ishero"],
            skill = skill,
            abilitylist = abilitylist,
            magiclist = magiclist,
            itemlist = itemlist,
            experience = datadict["experience"],
            price = datadict["price"],
            maxcount = datadict["maxcount"],
            description = datadict["description"]        
            )
        
        return data
    
    def get_total_skilldict(self):

        baseskill = self.skill.to_list()
        totalskills = baseskill

        for item in self.itemlist:
            totalskills = [sum(pair) for pair in zip(totalskills, item.skill.to_list())]
            
        skillobject = Skill.from_list(totalskills)
        skilldict = skillobject.to_dict()
            
        return skilldict

    def get_total_abilitylist(self):
        
        totalabilitylist = []

        for ability in self.abilitylist:
            totalabilitylist += [ability]

        for item in self.itemlist:
            for ability in item.abilitylist:
                ability.name = (ability.name + f"\n(source: {item.name})")
                totalabilitylist += [ability]
    
        return totalabilitylist
        
    def get_total_magiclist(self):
        
        totalmagiclist = []

        for magic in self.magiclist:
            totalmagiclist += [magic]

        for item in self.itemlist:
            for magic in item.magiclist:
                magic.name = (magic.name + f"\n(source: {item.name})")
                totalmagiclist += [magic]
        
        return totalmagiclist

    @staticmethod
    def create_character(name, race, source, warband, category):
        # open reference data json file
        data = open_json("database/references/characters_ref.json")
        datadict = data[race][source][warband][category]

        new_character = Character.from_dict(datadict = datadict, create = True)
        new_character.name = name

        return new_character

    def get_price(self):
        charprice = self.price
        for item in self.itemlist:
            charprice += item.price

        return charprice

class Hero(Character):
    @staticmethod
    def create_character(name, race, source, warband, category):
        # open reference data json file
        data = open_json("database/references/characters_ref.json")

        if data[race][source][warband][category]["ishero"] == False:
            print("Henchmen can't be added outside a squad")
        else:
            newhero = Character.create_character(name, race, source, warband, category)
            return newhero

class Henchman(Character):
    @staticmethod
    def create_character(name, race, source, warband, category):
        # open reference data json file
        data = open_json("database/references/characters_ref.json")

        if data[race][source][warband][category]["ishero"] == True:
            print("Heroes can't be added to a squad")
        else:
            newhenchman = Character.create_character(name, race, source, warband, category)
            return newhenchman