from components import * # reference to the script with all component classes


class Warband(object):
    def __init__(self, name, race, rulelist=[], inventory=None, herolist=[], squadlist=[]):
        self.name = name
        self.race = race
        self.rulelist = rulelist
        self.inventory = inventory if inventory else Inventory()
        self.herolist = herolist
        self.squadlist = squadlist

    def to_dict(self, ref="Warband"):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'name': self.name,
            'race': self.race,
            'rulelist': str(self.rulelist),
            'inventory': str(self.inventory),
            'herolist': str(self.herolist), 
            'squadlist': str(self.squadlist)
        }
        return data

    def get_warbandprice(self):
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

    def save_warband(self):
        NotImplemented


class Squad(object):
    def __init__(self, name, category, experience=0, henchmanlist=[]):
        self.name = name
        self.category = category
        self.henchmanlist = henchmanlist

    def to_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'name': self.name,
            'category': self.category,
            'henchmanlist': str(self.henchmanlist)
        }
        return data

    def get_totalhenchman(ditobject):
        henchmanlist = ditobject.henchmanlist if ditobject.henchmanlist else []
        return len(henchmanlist)

    def add_henchman(self):
        """adds another henchman character to the squad
        for a new squad checks if character is a henchman sub-class"""
        NotImplemented

    def remove_henchman(self):
        """removes a specific henchman character in this squad, by default this is on FIFO basis"""
        NotImplemented

# The following functions are changes to the henchman character, but invoked from the squad in order to maintain sync between the members of a squad

    def add_experience(self):
        """adds experience to every henchman in the squad"""
        NotImplemented

    def remove_experience(self):
        """removes experience from every henchmen in the squad"""
        NotImplemented

    def add_item(self):
        """adds an item to every henchman in the squad
        increases replacecost for the squad by the cost of the item added"""
        NotImplemented

    def remove_item(self):
        """removes an item from all henchmen in this squad
        decreases replacecost for the squad by the cost of the item removed"""
        NotImplemented

    def add_skill(self):
        """adds a skill to every henchman in the squad"""
        NotImplemented

    def remove_skill(self):
        """removes a skill from every henchmen in the squad"""
        NotImplemented
        

class Character(object):
    def __init__(self, name, race, category, skill, abilitylist=[], inventory=None, experience=0, price=0):
        self.name = name
        self.race = race
        self.category = category
        self.skill = skill
        self.abilitylist = abilitylist
        self.inventory = inventory
        self.experience = experience
        self.price = price


class Hero(Character):
    def __init__(self, name, race, category, skill, abilitylist=[], inventory=None, experience=0, price=0):
        super().__init__(name, race, category, skill, abilitylist, inventory, experience, price)

    def to_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'name': self.name,
            'race': self.race,
            'category': self.category,
            'skill': str(self.skill),
            'abilitylist': str(self.abilitylist),
            'inventory': str(self.inventory),
            'experience': self.experience,
            'price': self.price
        }
        return data

    def add_experience(self):
        """adds experience to this hero character"""
        NotImplemented

    def remove_experience(self):
        """removes experience from this hero"""
        NotImplemented

    def add_item(self):
        """adds an item to this hero character"""
        NotImplemented

    def remove_item(self):
        """removes an item from this hero"""
        NotImplemented

    def add_skill(self):
        """adds a skill to this hero character"""
        NotImplemented

    def remove_skill(self):
        """removes a skill from this hero"""
        NotImplemented


class Henchman(Character):
    """Henchman is a class with no mutation methods as these are 
    invoked using the Squad class to prevent henchmen 
    to deviate from their peers"""
    def __init__(self, name, race, category, skill, abilitylist=[], inventory=None, experience=0, price=0):
        super().__init__(name, race, category, skill, abilitylist, inventory, experience, price)

    def to_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'name': self.name,
            'race': self.race,
            'category': self.category,
            'skill': str(self.skill),
            'abilitylist': str(self.abilitylist),
            'inventory': str(self.inventory),
            'experience': str(self.experience),
            'price': self.price
        }
        return data


