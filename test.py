from references.json import *
from stats import *
from warband import *
from inventory import *


def print_newline():
    print(" ")


# test warband classes
def test_makeWarband():
    # Create data
    wbid = Warband(name="Uthluan Raiders", race="High Elves")
    wbid.inventory = Inventory(gold=500, itemlist=[
        Item(name="Mordheim Map", category="Miscellaneous"),
        Item(name="Elven Wine", category="Miscellaneous")
        ])
    wbid.herolist = [
        Hero(name="Hero1", race="High Elves", category="Loremaster", skill=Skill(5,4,4,3,3,1,6,1,9,0), abilitylist=[Ability("Excellent Sight"), Ability("Dispel")], inventory=Inventory(itemlist=["Mage staff", "Dagger"])), 
        Hero(name="Hero2", race="High Elves", category="Swordwarden", skill=Skill(5,4,4,3,3,1,6,1,9,0), inventory=Inventory(itemlist=["Sword", "Dagger", "Shield", "Light Armour"]))
        ]
    wbid.squadlist = [
        Squad(name="Spearguard", category="Seaguard", henchmanlist=[
            Henchman(name="Spearguard1", race="High Elves", category="Seaguard", skill=Skill(5,4,4,3,3,1,6,1,8,0), inventory=Inventory(itemlist=["Spear"])),
            Henchman("Spearguard2", "High Elves", "Seaguard", Skill(5,4,4,3,3,1,6,1,8,0), Inventory(itemlist=["Spear"]))
        ]), 
        Squad(name="Bladeguard", category="Seaguard", henchmanlist=[
            Character(name="Bladeguard1", race="High Elves", category="Seaguard", skill=Skill(5,4,4,3,3,1,6,1,8,0), inventory=Inventory(itemlist=["Sword"]))
        ]), 
        Squad(name="Cadet Archers", category="Cadet", henchmanlist=[
            Character(name="Cadet1", race="High Elves", category="Cadet", skill=Skill(5,3,3,3,3,1,6,1,7,0), inventory=Inventory(itemlist=["Longbow"]))
        ])
        ]
    
    # Load warband data
    
    # show data
    print(f"Warband testing")
    print(f"Name: {wbid.name}")
    print(f"Race: {wbid.race}")
    print(f"Gold: {wbid.inventory.gold}")
    print(f"Wyrdstones: {wbid.inventory.wyrd}")
    print(f"Inventory:{wbid.inventory.itemlist}")
    totalheroes = len(wbid.herolist)
    totalhenchman = 0
    for s in wbid.squadlist:
        totalhenchman = totalhenchman + s.get_totalhenchman()
    totalchars = totalheroes+totalhenchman
    printtotal = "Number of units: " + str(totalchars)
    print(printtotal)
    print_newline()

    for hero in wbid.herolist:
        print(f"Name: {hero.name}")
        print(f" category: {hero.category}")
        print(f" skill: m:{hero.skill.movement}, w:{hero.skill.weapon}, b:{hero.skill.ballistic}, s:{hero.skill.strength}, t:{hero.skill.toughness}, a:{hero.skill.actions}, i:{hero.skill.initiative}, w:{hero.skill.wounds}, ld:{hero.skill.leadership}, as:{hero.skill.armoursave}")
        print(f" Items: {hero.inventory.itemlist}")
    print("Squads:")
    print_newline

    for squad in wbid.squadlist:
        print(f"Name: {squad.name}")
        print(f" category: {squad.category}")
        print(f" skill: m:{squad.henchmanlist[0].skill.movement}, w:{squad.henchmanlist[0].skill.weapon}, b:{squad.henchmanlist[0].skill.ballistic}, s:{squad.henchmanlist[0].skill.strength}, t:{squad.henchmanlist[0].skill.toughness}, a:{squad.henchmanlist[0].skill.actions}, i:{squad.henchmanlist[0].skill.initiative}, w:{squad.henchmanlist[0].skill.wounds}, ld:{squad.henchmanlist[0].skill.leadership}, as:{squad.henchmanlist[0].skill.armoursave}")
        print(f" items: {squad.henchmanlist[0].inventory.itemlist}")
        print(f" (total: {squad.get_totalhenchman()})")

    
    # Save data
    filepath = "saves/" + wbid.name + ".json"

    datadict = wbid.get_dict()
    save_json(data=datadict, jsonfile=filepath)

    for hero in wbid.herolist:
        datadict = hero.get_dict()
        append_json(data=datadict, datatype=hero.name, jsonfile=filepath)
    
    datadict = wbid.inventory.get_dict()
    print(datadict)
    print_newline

    for item in wbid.inventory.itemlist:
        datadict = item.get_dict()
        print(datadict)
        print_newline


    
    
if __name__ == "__main__":
    test_makeWarband()