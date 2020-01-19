class Warband(object):
    def __init__(self, name, race, treasury=None, herolist=None, squadlist=None):
        self.name = name
        self.race = race
        self.treasury = treasury if treasury else None
        self.herolist = herolist if herolist else None
        self.squadlist = squadlist if squadlist else None


class Treasury(object):
    def __init__(self, gold=500):
        self.gold = gold


class Squad(object):
    def __init__(self, name, type, experience=0, henchmanlist=None):
        self.name = name
        self.type = type
        self.experience = experience
        self.henchmanlist = henchmanlist if henchmanlist else None

    def get_totalhenchman(ditobject):
        henchmanlist = ditobject.henchmanlist if ditobject.henchmanlist else []
        return len(henchmanlist)


class Character(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type
