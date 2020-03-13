import copy

from source.methods_engine import (
    load_reference,
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

        # recursively set some nested objects to a dictionary
        treasury = self.treasury.to_dict()

        # recursively set a list of objects to a list of dictionaries
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

        # set the object values to a dictionary
        datadict = {
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

        return datadict
    
    @staticmethod
    def from_dict(datadict):
        """ Create an object, and all nested objects, out of a warband dictionary in order to enable updates to that data."""
        
        # recursively set a dictionary to some nested objects
        treasury = Treasury.from_dict(datadict["treasury"])

        # find the reference dictionaries of a set of values to a list of python objects
        # events = datadict["events"]
        
        herolist = []
        for herodict in datadict["herolist"]:
            herolist += [Character.from_dict(herodict)]

        squadlist = []
        for squaddict in datadict["squadlist"]:
            squadlist += [Squad.from_dict(squaddict)]

        itemlist = []
        for itemdict in datadict["itemlist"]:
            itemlist += [Item.from_dict(itemdict)]

        rulelist = []
        for ruledict in datadict["rulelist"]:
            rulelist += [Rule.from_dict(ruledict)]

        # set the dictionary values to a python object
        dataobject = Warband(
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
        
        return dataobject

    @staticmethod
    def from_refdict(datadict):
        """ Create an object, and all nested objects, out of a warband dictionary in order to enable updates to that data."""
        
        # recursively set a dictionary to some nested objects
        treasury=Treasury(
            gold = datadict["start_gold"],
        )

        # find the reference dictionaries of a set of values to a list of python objects
        # events = ""

        itemlist = []
        for itemdict in datadict["itemlist"]:
            itemref = Item.create_item(
                source = itemdict["source"], 
                category = itemdict["category"], 
                subcategory = itemdict["subcategory"], 
                )
            itemlist += [itemref]

        rulelist = []
        for ruledict in datadict["rulelist"]:
            rulelist += [Rule.from_dict(ruledict)]

        # set the dictionary values to a python object
        dataobject = Warband(
            name = "",
            race = datadict["race"],
            source = datadict["source"],
            warband = datadict["warband"],
            description = datadict["description"],
            treasury = treasury,
            rulelist = rulelist,
            itemlist = itemlist,
            herolist = [],
            squadlist = [],
            )
        
        return dataobject

    @staticmethod
    def create_warband(name, race, source, warband):
        """Create a new warband based on the given parameters"""
        
        # open reference data json file
        datadict = load_reference("warbands")
        wbdict = datadict[race][source][warband]

        dataobject = Warband.from_refdict(datadict = wbdict)
        dataobject.name = name

        return dataobject

    @staticmethod
    def create_template():

        template_wb = Warband(
            name="",
            race="", 
            source="", 
            warband="",
        )
        return template_wb

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

    def get_rulelist(self):
        rulelist = []
        
        for r in self.rulelist:
            rulelist += [r.name]
        
        return rulelist

class Squad(object):
    def __init__(self, name, henchmanlist=[]):
        self.name = name
        self.henchmanlist = henchmanlist

    def to_dict(self):  

        # recursively set a list of objects to a list of dictionaries
        henchmanlist=[] 
        for henchman in self.henchmanlist:
            henchmanlist += [henchman.to_dict()]
        
        # set the object values to a dictionary
        datadict = {
            'name': self.name,
            'henchmanlist': henchmanlist
        }
        
        return datadict

    @staticmethod
    def from_dict(datadict):

        # find the reference dictionaries of a set of values to a list of python objects
        henchmanlist = []
        for henchman in datadict["henchmanlist"]:
            henchmanlist += [Character.from_dict(henchman)]

        # set the dictionary values to a python object
        dataobject = Squad(
            name = datadict["name"],
            henchmanlist = henchmanlist,
            )

        return dataobject

    @staticmethod
    def create_squad(race, source, warband, category, name, number=1):
        """Create a new squad with the given parameters and creates the amount of henchman determined by the number parameter"""
        
        dataobject = Squad(
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
            dataobject.henchmanlist.append(newhenchman)
                
        return dataobject

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
    def __init__(self, name, race, source, warband, category, ishero, skill, abilitylist=[], magiclist=[], itemlist=[], eventlist=[], experience=0, price=0, maxcount=0, description=None):
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
        self.eventlist = eventlist
        self.experience = experience
        self.price = price
        self.maxcount = maxcount
        self.description = description
    
    def to_dict(self):  

        # recursively set some nested objects to a dictionary
        skill = self.skill.to_dict()

        # recursively set a list of objects to a list of dictionaries
        abilitylist = []
        for ability in self.abilitylist:
            abilitylist += [ability.to_dict()]

        magiclist = []
        for magic in self.magiclist:
            magiclist += [magic.to_dict()]

        itemlist = []
        for item in self.itemlist:
            itemlist += [item.to_dict()]
        
        eventlist = []
        for event in self.eventlist:
            eventlist += [event.to_dict()]

        # set the object values to a dictionary
        datadict = {
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
            'eventlist': eventlist,
            'experience': self.experience,
            'price': self.price,
            'maxcount': self.maxcount,
            'description': self.description
        }
        return datadict

    @staticmethod
    def from_dict(datadict):

        # recursively set a dictionary to some nested objects
        skill = Skill.from_dict(datadict["skill"])

        # find the reference dictionaries of a set of values to a list of python objects
        abilitylist = []
        for abilitydict in datadict["abilitylist"]:
            abilitylist += [Ability.from_dict(abilitydict)]

        magiclist = []
        for magicdict in datadict["magiclist"]:
            magiclist += [Magic.from_dict(magicdict)]

        itemlist = []
        for itemdict in datadict["itemlist"]:
            itemlist += [Item.from_dict(itemdict)]

        eventlist = []
        for eventdict in datadict["eventlist"]:
            eventlist += [Event.from_dict(eventdict)]

        # set the dictionary values to a python object
        dataobject = Character(
            name = datadict["name"],
            race = datadict["race"],
            source = datadict["source"],
            warband = datadict["warband"],
            category = datadict["category"],
            ishero = datadict["ishero"],
            skill = skill,
            abilitylist = abilitylist,
            magiclist = magiclist,
            itemlist = itemlist,
            eventlist = eventlist,
            experience = datadict["experience"],
            price = datadict["price"],
            maxcount = datadict["maxcount"],
            description = datadict["description"]        
            )
        
        return dataobject
    
    @staticmethod
    def from_refdict(datadict):
        
        # recursively set a dictionary to some nested objects
        skill = Skill.from_dict(datadict["skill"])

        # find the reference dictionaries of a set of values to a list of python objects
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

        eventlist = []
        for eventdict in datadict["eventlist"]:
            eventref = Event.create_event(
                source = eventdict["source"], 
                category = eventdict["category"], 
                subcategory = eventdict["subcategory"], 
                )
            eventlist += [eventref]

        # set the dictionary values to a python object
        dataobject = Character(
            name = "",
            race = datadict["race"],
            source = datadict["source"],
            warband = datadict["warband"],
            category = datadict["category"],
            ishero = datadict["ishero"],
            skill = skill,
            abilitylist = abilitylist,
            magiclist = magiclist,
            itemlist = itemlist,
            eventlist = eventlist,
            experience = datadict["experience"],
            price = datadict["price"],
            maxcount = datadict["maxcount"],
            description = datadict["description"]        
            )
        
        return dataobject

    @staticmethod
    def create_character(name, race, source, warband, category):
        # open reference data json file
        datadict = load_reference("characters")
        chardict = datadict[race][source][warband][category]

        dataobject = Character.from_refdict(datadict = chardict)
        dataobject.name = name

        return dataobject

    @staticmethod
    def create_template():
        dataobject = Character(
            name="",
            race="", 
            source="", 
            warband="",
            skill=Skill("","","","","","","","","","",), 
            category="", 
            ishero="",
        )
        return dataobject

    def get_price(self):
        charprice = self.price
        for item in self.itemlist:
            charprice += item.price

        return charprice

    def get_total_skilldict(self):

        skilldict = {
            'movement': {'total': self.skill.movement, 'children': {'base': self.skill.movement}},
            'weapon': {'total': self.skill.weapon, 'children': {'base': self.skill.weapon}},
            'ballistic': {'total': self.skill.ballistic, 'children': {'base': self.skill.ballistic}},
            'strength': {'total': self.skill.strength, 'children': {'base': self.skill.strength}},
            'toughness': {'total': self.skill.toughness, 'children': {'base': self.skill.toughness}},
            'wounds': {'total': self.skill.wounds, 'children': {'base': self.skill.wounds}},
            'initiative': {'total': self.skill.initiative, 'children': {'base': self.skill.initiative}},
            'actions': {'total': self.skill.actions, 'children': {'base': self.skill.actions}},
            'leadership': {'total': self.skill.leadership, 'children': {'base': self.skill.leadership}},
            'armoursave': {'total': self.skill.armoursave, 'children': {'base': self.skill.armoursave}},
        }

        # for event in self.eventlist:
        #     eventskills = event.skill.to_dict()
        #     for key in eventskills:
        #         if eventskills[key] != 0:
        #             eventskilldict = {f"event: {event.name}": eventskills[key]}
        #             skilldict[key]['children'].update(eventskilldict)
        #             skilldict[key]['total'] += eventskills[key]

        for item in self.itemlist:
            itemskills = item.skill.to_dict()
            for key in itemskills:
                if itemskills[key] != 0:
                    itemskilldict = {f"item: {item.subcategory}": itemskills[key]}
                    skilldict[key]['children'].update(itemskilldict)
                    skilldict[key]['total'] += itemskills[key]
                    print(skilldict[key])

        return skilldict

    def get_total_abilitylist(self):
        
        totalabilitylist = self.get_char_abilitylist() + self.get_item_abilitylist()

        return totalabilitylist

    def get_char_abilitylist(self):
        
        charabilitylist = []

        for ability in self.abilitylist:
            charabilitylist += [ability]
    
        return charabilitylist
        
    def get_item_abilitylist(self):
        
        itemabilitylist = []

        for item in self.itemlist:
            for ability in item.abilitylist:
                itemabilitylist += [ability]
    
        return itemabilitylist

    def get_magiclist(self):
        
        totalmagiclist = []

        for magic in self.magiclist:
            totalmagiclist += [magic]
        
        return totalmagiclist

class Hero(Character):
    @staticmethod
    def create_character(name, race, source, warband, category):
        # open reference data json file
        datadict = load_reference("characters")

        if datadict[race][source][warband][category]["ishero"] == False:
            print("Henchmen can't be added outside a squad")
        else:
            dataobject = Character.create_character(name, race, source, warband, category)
            return dataobject

class Henchman(Character):
    @staticmethod
    def create_character(name, race, source, warband, category):
        # open reference data json file
        datadict = load_reference("characters")

        if datadict[race][source][warband][category]["ishero"] == True:
            print("Heroes can't be added to a squad")
        else:
            dataobject = Character.create_character(name, race, source, warband, category)
            return dataobject