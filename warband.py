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


if __name__ == "__main__":
    def print_newline():
        print("\n")
    currentwarband = Warband("Mike's Mercenaries", race="High Elves")
    currentwarband.treasury = Treasury(gold=456)
    currentwarband.herolist = [Character(name="Hero1", type="Loremaster"), Character(name="Hero2", type="Swordwarden")]
    currentwarband.squadlist = [Squad(name="Spearguard", type="Seaguard", experience=1), Squad(name="Bladeguard", type="Seaguard", experience=2), Squad(name="Cadet Archers", type="Cadet", experience=0)]
    

    print(f"Name: {currentwarband.name}")
    print(f"Race: {currentwarband.race}")
    print(f"Treasury: {currentwarband.treasury}")
    print(f"Gold: {currentwarband.treasury.gold}")
    print_newline()
    print("Heroes:")
    i = 1
    for hero in currentwarband.herolist:
        print(f"{i}.")
        print(f"Name: {hero.name}")
        print(f"Type: {hero.type}")
        i += 1
    print_newline()
    print("Squads:")
    i = 1
    for squad in currentwarband.squadlist:
        print(f"{i}.")
        print(f"Name: {squad.name}")
        print(f"Type: {squad.type}")
        print(f"(total: {squad.get_totalhenchman()}, exp: {squad.experience})")
        i += 1