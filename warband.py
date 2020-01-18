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
    def __init__(self, type, experience=0, henchmanlist=None):
        self.experience = experience
        self.type = type
        self.henchmanlist = henchmanlist if henchmanlist else None

    def get_totalhenchman(ditobject):
        henchmanlist = ditobject.henchmanlist if ditobject.henchmanlist else []
        return len(henchmanlist)


class Character(object):
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    def print_newline():
        print("\n")
    currentwarband = Warband("Mike's Mercenaries", race="High Elves")
    currentwarband.treasury = Treasury(gold=456)
    currentwarband.squadlist = [Squad("Archer", experience=100), Squad("Spearman")]
    currentwarband.herolist = [Character(name="Essale"), Character(name="Homo")]


    print(f"Name: {currentwarband.name}")
    print(f"Race: {currentwarband.race}")
    print_newline()
    print(f"Treasury: {currentwarband.treasury}")
    print(f"Gold: {currentwarband.treasury.gold}")
    print_newline()
    print("Squads:")
    i = 1
    for squad in currentwarband.squadlist:
        print(f"{i}. Type {squad.type} (total: {squad.get_totalhenchman()}, exp: {squad.experience})")
        i += 1
    print_newline
    print("Heroes:")
    for hero in currentwarband.herolist:
        print(f"- {hero.name}")
