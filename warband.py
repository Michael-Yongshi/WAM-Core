from inventory import *
from stats import *

class Warband(object):
    def __init__(self, name, race, inventory=None, herolist=None, squadlist=None):
        self.name = name
        self.race = race
        self.inventory = inventory if inventory else Inventory()
        self.herolist = herolist if herolist else None
        self.squadlist = squadlist if squadlist else None


class Character(object):
    def __init__(self, name, race, type, skill, abilitylist=None, inventory=None, experience=0):
        self.name = name
        self.race = race
        self.type = type
        self.skill = skill if skill else Skill()
        self.abilitylist = abilitylist if abilitylist else None
        self.inventory = inventory if inventory else Inventory()
        self.experience = experience


class Hero(Character):
    def __init__(self):
        super().__init__()

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
    def __init__(self):
        super().__init__()

class Squad(object):
    def __init__(self, name, type, experience=0, henchmanlist=None):
        self.name = name
        self.type = type
        self.henchmanlist = henchmanlist if henchmanlist else None

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