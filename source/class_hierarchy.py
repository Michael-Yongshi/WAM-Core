import copy

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

from .class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    Event,
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

    def buy_item(self, wbid, item):
        """Basically adds the new item to every henchman in this squad in return for gold"""

        totalcost = item.price * self.get_totalhenchman()

        if totalcost > wbid.treasury.gold:
            message = "Lack of funds!"
        else:
            for henchman in self.henchmanlist:
                henchman.itemlist.append(item)
                wbid.treasury.gold -= item.price
            message = ""
        
        return message

    def sell_item(self, wbid, itemsubcategory):
        """Basically removes the item from every henchman in this squad in return for gold"""

        for henchman in self.henchmanlist:
            for i in henchman.itemlist:
                if i.subcategory == itemsubcategory:
                    index = henchman.itemlist.index(i)
                    item = henchman.itemlist.pop(index)
                    wbid.treasury.gold += item.price
                    break

    def add_experience(self, change_experience):
        
        for henchman in self.henchmanlist:
                
            # add the new experience
            henchman.experience += change_experience

            # If new advances has been reached, create empty advance events and add them to the characters event list
            henchman.eventlist += henchman.create_advance_events()

    def set_event_characteristic(self, roll1, roll2):

        for henchman in self.henchmanlist:
            event = henchman.get_tbd_advance_events()[0]
            message = henchman.set_event_characteristic(event, roll1, roll2)

        return message

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
        
        itemlist = []
        for itemdict in datadict["itemlist"]:
            itemref = Item.create_item(
                source = itemdict["source"], 
                category = itemdict["category"], 
                subcategory = itemdict["subcategory"], 
                )
            itemlist += [itemref]

        eventlist = []

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

        print(f"current advance is {dataobject.get_current_advance()}")
        print(f"new advance is {dataobject.get_new_advance()}")

        # Create advance level for this new character
        dataobject.eventlist += dataobject.create_advance_events()
        print(dataobject.eventlist)

        for event in dataobject.eventlist:
            if event.description[-3:] == "TBD":
                currentdesc = event.description[:-4]
                newdesc = " this character started with this advancement"
                event.description = f"{currentdesc}{newdesc}"
        
        return dataobject

    @staticmethod
    def create_template():
        dataobject = Character(
            name="",
            race="", 
            source="", 
            warband="",
            skill=Skill.create_skill_empty(), 
            category="", 
            ishero="",
        )
        return dataobject

    def buy_item(self, wbid, item):
        """Basically adds the new item to this hero in return for gold"""

        if item.price > wbid.treasury.gold:
            message = "Lack of funds!"
        else:
            self.itemlist.append(item)
            wbid.treasury.gold -= item.price
            message = ""
        
        return message

    def sell_item(self, wbid, itemsubcategory):
        """Basically removes the heroes item in return for gold"""

        for i in self.itemlist:
            if i.subcategory == itemsubcategory:
                index = self.itemlist.index(i)
                item = self.itemlist.pop(index)
                wbid.treasury.gold += item.price
                break

    def add_experience(self, change_experience):

        # add the new experience
        self.experience += change_experience

        # If new advances has been reached, create empty advance events and add them to the characters event list
        self.eventlist += self.create_advance_events()

    def create_advance_events(self):
        # Create empty new events based on new experience

        current_advance = self.get_current_advance()
        new_advance = self.get_new_advance()

        new_events = []
        while new_advance > current_advance:
            current_advance += 1
            newevent = Event.create_event(
                category="Advance " + str(current_advance), 
                description=f"Character reaches advance {current_advance}, TBD", 
                skill=Skill.create_skill_empty()
                )
            new_events += [newevent]

        # Return the new events
        return new_events

    def set_event_ability(self, event, new_ability):

        self.abilitylist.append(new_ability)
        result = f"The character gained the ability of {new_ability.name}"
        event.description = event.description[:-4] + result

        return result

    def set_event_magic(self, event, new_magic):
        
        self.magiclist.append(new_magic)
        result = f"The character is able to use new magic {new_magic.name}"
        
        event.description = event.description[:-4] + result

        return result

    def set_event_roll7(self, event, choice):
        
        if choice == "Weapon Skill":
            event.skill.weapon = 1
            result = f"Character gained +1 to their weapon skill characteristic!"

        if choice == "Ballistic Skill":
            event.skill.ballistic = 1
            result = f"Character gained +1 to their ballistic skill characteristic!"

        event.description = event.description[:-4] + result

        return result

    def set_event_characteristic(self, event, roll1, roll2):

        if roll1 == 6:
            if roll2 <= 3:
                event.skill.strength = 1
                result = f"Character gained +1 to their strength characteristic!"

            if roll2 >= 4:
                event.skill.actions = 1
                result = f"Character gained +1 to their attack characteristic!"

        if roll1 == 8:

            if roll2 <= 3:
                event.skill.initiative = 1
                result = f"Character gained +1 to their initiative characteristic!"

            if roll2 >= 4:
                event.skill.leadership = 1
                result = f"Character gained +1 to their leadership characteristic!"

        if roll1 == 9:

            if roll2 <= 3:
                event.skill.wounds = 1
                result = f"Character gained +1 to their wounds characteristic!"

            if roll2 >= 4:
                event.skill.toughness = 1
                result = f"Character gained +1 to their toughness characteristic!"

        event.description = event.description[:-4] + result

        return result

    def get_tbd_advance_events(self):
        eventlist = []

        for event in self.eventlist:
            if event.description[-3:] == "TBD":
                eventlist += [event]

        return eventlist

    def get_advance_events(self):
        eventlist = []
        for event in self.eventlist:
            if event.category[:8] == "Advance ":
                eventlist += [event]

        return eventlist

    def get_current_advance(self):
        """Get advance level of this character"""

        advance = 0
        current_advance = 0

        # For every event in eventlist, for every advance event check the number and compare with the previously highest advance number found
        for event in self.get_advance_events():
            advance = int(event.category[8:])
            if advance > current_advance:
                current_advance = advance
                    
        return current_advance

    def get_next_advance(self):

        next_advance = self.get_current_advance() + 1
        return next_advance

    def get_xp_ref(self):

        # load exp database
        datadict = load_reference("experience_table")
        if self.ishero == True:
            expdict = datadict["Hero"]
        else:
            expdict = datadict["Squad"]

        return expdict

    def get_xpneeded(self):
        """Get experience needed for next advance"""

        # load exp database
        expdict = self.get_xp_ref()

        # check when new advance is reached
        next_advance = self.get_next_advance()
        xpneeded = expdict["Advance " + str(next_advance)]

        return xpneeded

    def get_new_advance(self):
        """based on characters experience, check if new advance is warranted and return the new advance level"""

        # load exp database
        expdict = self.get_xp_ref()

        # check with reference what maximum advance is reached with this characters experience
        new_advance = 0
        for key in expdict:
            if self.experience >= expdict[key]:
                new_advance = int(key[8:])

        return new_advance

    def get_advance_process(self):

        processes = load_reference("processes")
        advance_processes = processes["Core Rules"]["Advancement"]

        if self.ishero == True:
            process = advance_processes["Heroes"]["description"]
        else:
            process = advance_processes["Squads"]["description"]

        return process

    def get_levelup_notification(self):
        if len(self.get_tbd_advance_events()) != 0:
            notification = f"Process new advances ({len(self.get_tbd_advance_events())})"
        else:
            notification = f""

        return notification

    def get_historydict(self):
        datadict = {}
        
        for event in self.eventlist:
            datadict[event.category] = event.to_dict()
        
        return datadict

    def get_historystring(self):
        datastring = "This is this characters history: </br>"
        
        for event in self.eventlist:
            datastring += "- " + event.to_string() + "<br/>"
        
        return datastring

    def get_price(self):
        charprice = self.price
        for item in self.itemlist:
            charprice += item.price

        return charprice

    def get_total_skilldict(self):

        datadict = {}

        selfdict = self.skill.to_dict()
        for key in selfdict:
            skilldict = {
                key: {'total': selfdict[key], 'children': {'base': selfdict[key]}}
                }
            datadict.update(skilldict)

        for event in self.eventlist:
            eventskills = event.skill.to_dict()
            for key in eventskills:
                if eventskills[key] != 0:
                    eventdict = {f"event: {event.datetime} - {event.category}": eventskills[key]}
                    datadict[key]['children'].update(eventdict)
                    datadict[key]['total'] += eventskills[key]
                    
        for item in self.itemlist:
            itemskills = item.skill.to_dict()
            for key in itemskills:
                if itemskills[key] != 0:
                    itemdict = {f"item: {item.subcategory}": itemskills[key]}
                    datadict[key]['children'].update(itemdict)
                    datadict[key]['total'] += itemskills[key]

        return datadict

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