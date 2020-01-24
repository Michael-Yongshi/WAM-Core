from inventory import *
from stats import *

class Warband(object):
    def __init__(self, name, race, inventory=None, herolist=None, squadlist=None):
        self.name = name
        self.race = race
        self.inventory = inventory if inventory else Inventory()
        self.herolist = herolist if herolist else None
        self.squadlist = squadlist if squadlist else None

    def get_dict(self):  
        data = {}
        data[self] = {
            'name': self.name,
            'race': self.race,
            'inventory': self.inventory,
            'herolist': self.herolist, 
            'squadlist': self.squadlist
        }
        return data

    def save_warband(self):
        NotImplemented

class Character(object):
    def __init__(self, name, race, category, skill, abilitylist=None, inventory=None, experience=0):
        self.name = name
        self.race = race
        self.category = category
        self.skill = skill
        self.abilitylist = abilitylist if abilitylist else None
        self.inventory = inventory if inventory else None
        self.experience = experience

# Although __dict__ of the object could be used, it doesnt automatically give the object id from self, I would like to 
# use the key of the subobjects to link them to the result of the arrays in their superobjects.
    def get_dict(self):  
        data = {}
        data[self] = {
            'name': self.name,
            'race': self.race,
            'category': self.category,
            'skill': self.skill,
            'abilitylist': self.abilitylist,
            'inventory': self.inventory
        }
        return data


class Hero(Character):
    def __init__(self, name, race, category, skill, abilitylist=None, inventory=None, experience=0):
        super().__init__(name, race, category, skill, abilitylist, inventory, experience)

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
    """Henchman is a class with no methods as these are 
    invoked using the Squad class to prevent henchmen 
    to deviate from their peers"""
    def __init__(self, name, race, category, skill, abilitylist=None, inventory=None, experience=0):
        super().__init__(name, race, category, skill, abilitylist, inventory, experience)


class Squad(object):
    def __init__(self, name, category, experience=0, henchmanlist=None):
        self.name = name
        self.category = category
        self.henchmanlist = henchmanlist if henchmanlist else None

    def get_dict(self):  
        data = {}
        data[self] = {
            'name': self.name,
            'category': self.category,
            'henchmanlist': self.henchmanlist
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