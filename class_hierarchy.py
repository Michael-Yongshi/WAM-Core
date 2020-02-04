from database.json import *
from class_components import * # reference to the script with all component classes


class Warband(object):
    def __init__(self, name, race, rulelist=[], inventory=None, herolist=[], squadlist=[]):
        self.name = name
        self.race = race
        self.rulelist = rulelist
        self.inventory = inventory if inventory else Inventory()
        self.herolist = herolist
        self.squadlist = squadlist

    def to_dict(self):
        """ Create a dictionary string of a Warband object, including all nested objects, that can be saved to a JSON file for storage."""
        # herolist = [hero.to_dict() for hero in self.herolist]      --- optional way of doing a simpler for loop

        rulelist = {} # change in a dict before setting dict values
        r = 1
        for rule in self.rulelist:
            ruleref = "Rule" + str(r) # to make sure it has a unique key
            rulelist.update(rule.to_dict(ref=ruleref)) # adding this one to the list
            r += 1 # iterate

        inventory = self.inventory.to_dict()

        herolist={} 
        h = 1
        for hero in self.herolist:
            heroref = "Hero" + str(h)
            herolist.update(hero.to_dict(ref=heroref))
            h += 1

        squadlist={} 
        s = 1
        for squad in self.squadlist:
            squadref = "squad" + str(s) 
            squadlist.update(squad.to_dict(ref=squadref))
            s += 1

        data = {
            # 'key': str(self),
            'name': self.name,
            'race': self.race,
            'rulelist': rulelist,
            'inventory': inventory,
            'herolist': herolist, 
            'squadlist': squadlist
        }

        return data
    
    @staticmethod
    def from_dict(datadict):
        """ Create an object, and all nested objects, out of a warband dictionary in order to enable updates to that data."""
        rulelist = []
        for rule in datadict["rulelist"].values():
            rulelist += [Rule.from_dict(rule)]

        inventory = Inventory.from_dict(datadict["inventory"])

        herolist = []
        for hero in datadict["herolist"].values():
            herolist += [Character.from_dict(hero)]

        squadlist = []
        for squad in datadict["squadlist"].values():
            squadlist += [Squad.from_dict(squad)]

        wbid = Warband(
            name=datadict["name"],
            race=datadict["race"],
            rulelist=rulelist,
            inventory=inventory,
            herolist=herolist,
            squadlist=squadlist
            )

        return wbid

    def add_squad(self, race, warband, category, name, number=1):
        """Creates a new squad and creates at least 1 henchman character within this squad"""
        # optional: check if squad already exists for input name
        # for squad in self.squadlist
        #     if "squad4" in squad.name:

        # create squad object
        newsquad = Squad(
            name=name, 
            category=category
            )
        
        # find reference of the squad category in the troops_ref.json
        datadict = open_json("database/references/troops_ref.json")

        if race in datadict:
            if warband in datadict[race]:
                if category in datadict[race][warband]:
                    troopdict = datadict[race][warband][category]
                else:
                    print(f" Category {category} not found")
            else:
                print(f"Warband {warband} not found")
        else:
            print(f"Race {race} not found")
   
        # fill squad object with the number of henchman desired (default = 1)
        for _ in range(number):
            henchmanref = category + str(number)
            newhenchman = Henchman(name=henchmanref, category=category, race=race, skill=skill)
            newsquad.henchmanlist += [newhenchman]
        
        # add created squad to the warbands squad list
        self.squadlist += [newsquad]
        
        return self

    
    def get_warbandprice(self):
        """ Temporary function, should be split in seperate functions to adjust gold baded on single events of buying equipment or getting loot"""
        wbinvprice = self.inventory.get_price()

        herolistprice = 0
        if self.herolist:
            for hero in self.herolist:
                heroprice = hero.price
                for item in hero.inventory.itemlist:
                    heroprice += item.price
                herolistprice += heroprice

        squadlistprice = 0
        if self.squadlist:
            for squad in self.squadlist:
                squadsize = squad.get_totalhenchman()
                
                henchmanprice = squad.henchmanlist[0].price # get price of a single henchman type
                for item in squad.henchmanlist[0].inventory.itemlist:
                    henchmanprice += item.price # get price of a single item of a henchman in this squad

                squadprice = henchmanprice * squadsize # multiply the price for a henchman and items with the number of henchman in the squad

                squadlistprice += squadprice # increment total squad cost with this squads prices

        price = wbinvprice + herolistprice + squadlistprice
        return price


class Squad(object):
    def __init__(self, name, henchmanlist=[]):
        self.name = name
        self.henchmanlist = henchmanlist

    def to_dict(self, ref):  
        henchmanlist={} 
        h = 1
        for henchman in self.henchmanlist:
            henchmanref = "Henchman" + str(h) 
            henchmanlist.update(henchman.to_dict(ref=henchmanref))
            h += 1
        
        data = {}
        data[str(ref)] = {
            # 'key': str(self),
            'name': self.name,
            'henchmanlist': henchmanlist
        }
        return data

    @staticmethod
    def from_dict(datadict):
        henchmanlist = []
        for henchman in datadict["henchmanlist"].values():
            henchmanlist += [Character.from_dict(henchman)]

        squad = Squad(
            name=datadict["name"],
            henchmanlist=henchmanlist,
            )

        return squad

    @staticmethod
    def create_squad(name, number, race, source, category):
        """Create a new squad with the given parameters and creates the amount of henchman determined by the number parameter"""
        
        newsquad = Squad(
            name = name,
            henchmanlist = []
            )

        for henchman in range(0, number):
            newhenchman = Character.create_character(
                name = name,
                race = race,
                source = source,
                category = category,
                callsquad = True    
                )
            newsquad.henchmanlist.append(newhenchman)
        
        return newsquad

    def equip_squad(self, name, source):
        """Basically runs a create item method for every henchman in this squad"""

        for henchman in self.henchmanlist:
            newitem = Item.create_item(
                name = name,  
                source = source
                )
            henchman.inventory.itemlist.append(newitem)

    def get_totalhenchman(ditobject):
        henchmanlist = ditobject.henchmanlist if ditobject.henchmanlist else []
        return len(henchmanlist)


    def add_henchman(self):
        """adds another henchman character to the squad
        for a new squad checks if character is a henchman sub-class"""
        # Create a character with the create character method based on the squads characteristics. 
        # Create a duplicate character if the squad is len(1>)

        NotImplemented

    def remove_henchman(self):
        """removes a specific henchman character in this squad, by default this is on FIFO basis"""
        NotImplemented

       
class Character(object):
    def __init__(self, name, race, source, category, ishero, skill, abilitylist=[], magiclist=[], inventory=None, experience=0, price=0, maxcount=0, description=None):
        self.name = name
        self.race = race
        self.source = source
        self.category = category
        self.ishero = ishero
        self.skill = skill
        self.abilitylist = abilitylist
        self.magiclist = magiclist
        self.inventory = inventory if inventory else Inventory()
        self.experience = experience
        self.price = price
        self.maxcount = maxcount
        self.description = description
    
    def to_dict(self, ref):  
        skill = self.skill.to_dict()
    
        abilitylist = []
        a = 1
        for ability in self.abilitylist:
            abilitylist.append(ability.to_dict())
            a += 1

        magiclist = []
        m = 1
        for magic in self.magiclist:
            magiclist.append(magic.to_dict())
            m += 1

        inventory = self.inventory.to_dict()

        data = {}
        data[str(ref)] = {
            # 'key': str(self),
            'name': self.name,
            'race': self.race,
            'source': self.source,
            'category': self.category,
            'ishero': self.ishero,
            'skill': skill,
            'abilitylist': abilitylist,
            'magiclist': magiclist,
            'inventory': inventory,
            'experience': self.experience,
            'price': self.price,
            'maxcount': self.maxcount,
            'description': self.description
        }
        return data

    @staticmethod
    def from_dict(datadict):
        skill = Skill.from_dict(datadict["skill"])
        
        abilitylist = []
        for ability in datadict["abilitylist"]:
            abilitylist += [Ability.from_dict(ability)]

        magiclist = []
        for magic in datadict["magiclist"]:
            magiclist += [Magic.from_dict(magic)]

        inventory = Inventory.from_dict(datadict["inventory"])

        data = Character(
            name=datadict["name"],
            race=datadict["race"],
            source=datadict["source"],
            category=datadict["category"],
            ishero=datadict["ishero"],
            skill=skill,
            abilitylist=abilitylist,
            magiclist=magiclist,
            inventory=inventory,
            experience=datadict["experience"],
            price=datadict["price"],
            maxcount=datadict["maxcount"],
            description=datadict["description"]
            )

        return data
    
    @staticmethod
    def create_character(name, race, source, category, callsquad=False):
        # open reference data json file
        data = open_json("database/references/characters_ref.json")

        if callsquad == data[race][source][category].get("ishero") == True:
            print("Heroes can't be added to a squad")
        else:
            skilllist = data[race][source][category].get("skill")
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
            for abilitydict in data[race][source][category].get("abilitylist"):
                abilityobject = Ability(name=abilitydict["name"], description=abilitydict["description"])
                abilitylist.append(abilityobject)

            magiclist = []
            for magicdict in data[race][source][category].get("magiclist"):
                magicobject = Magic(source=magicdict["source"], category=magicdict["category"], name=magicdict["name"], difficulty=magicdict["difficulty"], description=magicdict["description"])
                magiclist.append(magicobject)

            newcharacter = Character(
                name = name,
                race = race,
                source = source,
                category = category,
                ishero = data[race][source][category].get("ishero"),
                inventory = data[race][source][category].get("inventory"),
                skill = newskill,
                abilitylist = abilitylist,
                magiclist = magiclist,
                experience = data[race][source][category].get("experience"),
                price = data[race][source][category].get("price"),
                maxcount = data[race][source][category].get("maxcount"),
                description = data[race][source][category].get("description")        
                )
            
            return newcharacter
