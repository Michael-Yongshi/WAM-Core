from references.json import *
from stats import *
from warband import *
from inventory import *


def print_newline():
    print(" ")


# test json calls
def test_json():
    data = {'key1': ['1','2'], 'key2': ['3', '4']}
    save_json(data, jsonfile='test.json')


# test warband classes
def test_makeWarband():
    # Create data
    WarbandA = Warband(name="Uthluan Raiders", race="High Elves")
    WarbandA.inventory = Inventory(gold=500, itemlist=[
        Item(name="Mordheim Map", category="Miscellaneous"),
        Item(name="Elven Wine", category="Miscellaneous")
        ])
    WarbandA.herolist = [
        Hero(name="Hero1", race="High Elves", category="Loremaster", skill=Skill(5,4,4,3,3,1,6,1,9,0), abilitylist=[Ability("Excellent Sight"), Ability("Dispel")], inventory=Inventory(itemlist=["Mage staff", "Dagger"])), 
        Hero(name="Hero2", race="High Elves", category="Swordwarden", skill=Skill(5,4,4,3,3,1,6,1,9,0), inventory=Inventory(itemlist=["Sword", "Dagger", "Shield", "Light Armour"]))
        ]
    WarbandA.squadlist = [
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
    print(f"Name: {WarbandA.name}")
    print(f"Race: {WarbandA.race}")
    print(f"Gold: {WarbandA.inventory.gold}")
    print(f"Wyrdstones: {WarbandA.inventory.wyrd}")
    print(f"Inventory:{WarbandA.inventory.itemlist}")
    totalheroes = len(WarbandA.herolist)
    totalhenchman = 0
    for s in WarbandA.squadlist:
        totalhenchman = totalhenchman + s.get_totalhenchman()
    totalchars = totalheroes+totalhenchman
    printtotal = "Number of units: " + str(totalchars)
    print(printtotal)
    print_newline()

    for hero in WarbandA.herolist:
        print(f"Name: {hero.name}")
        print(f" category: {hero.category}")
        print(f" skill: m:{hero.skill.movement}, w:{hero.skill.weapon}, b:{hero.skill.ballistic}, s:{hero.skill.strength}, t:{hero.skill.toughness}, a:{hero.skill.actions}, i:{hero.skill.initiative}, w:{hero.skill.wounds}, ld:{hero.skill.leadership}, as:{hero.skill.armoursave}")
        print(f" Items: {hero.inventory.itemlist}")
    print("Squads:")
    print_newline

    for squad in WarbandA.squadlist:
        print(f"Name: {squad.name}")
        print(f" category: {squad.category}")
        print(f" skill: m:{squad.henchmanlist[0].skill.movement}, w:{squad.henchmanlist[0].skill.weapon}, b:{squad.henchmanlist[0].skill.ballistic}, s:{squad.henchmanlist[0].skill.strength}, t:{squad.henchmanlist[0].skill.toughness}, a:{squad.henchmanlist[0].skill.actions}, i:{squad.henchmanlist[0].skill.initiative}, w:{squad.henchmanlist[0].skill.wounds}, ld:{squad.henchmanlist[0].skill.leadership}, as:{squad.henchmanlist[0].skill.armoursave}")
        print(f" items: {squad.henchmanlist[0].inventory.itemlist}")
        print(f" (total: {squad.get_totalhenchman()})")

    
    # Save data
    # Just the inventory of the warband
    print(WarbandA.inventory.get_dict())
    # save_json(objectref=WarbandA.inventory, jsonfile='savedwarbands.json')
    
    
if __name__ == "__main__":
    test_json()
    test_makeWarband()