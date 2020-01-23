from references.json import *
from stats import *
from warband import *
from inventory import *


def print_newline():
    print("\n")


# test json calls
def test_json():
    data = {'key1': ['1','2'], 'key2': ['3', '4']}
    save_json(data, jsonfile='test.json')


# test warband classes
def test_makeWarband():
    # Create data
    WarbandA = Warband(name="Uthluan Raiders", race="High Elves")
    WarbandA.inventory = Inventory(gold=500, itemlist=[
        "Mordheim Map", 
        "Elven Wine"
        ])
    WarbandA.herolist = [
        Character(name="Hero1", race="High Elves", category="Loremaster", skill=[5,4,4,3,3,1,6,1,9,0], abilitylist=[Ability("Excellent Sight"), Ability("Dispel")], inventory=Inventory(itemlist=["Mage staff", "Dagger"])), 
        Character(name="Hero2", race="High Elves", category="Swordwarden", skill=[5,4,4,3,3,1,6,1,9,0], abilitylist=[Ability("Excellent Sight")], inventory=Inventory(itemlist=["Sword", "Dagger", "Shield", "Light Armour"]))
        ]
    WarbandA.squadlist = [
        Squad(name="Spearguard", category="Seaguard", henchmanlist=[
            Character(name="Spearguard1", race="High Elves", category="Seaguard", skill=[5,4,4,3,3,1,6,1,8,0], inventory=Inventory(itemlist=["Spear"])),
            Character("Spearguard2", "High Elves", "Seaguard", [5,4,4,3,3,1,6,1,8,0], Inventory(itemlist=["Spear"]))
        ]), 
        Squad(name="Bladeguard", category="Seaguard", henchmanlist=[
            Character(name="Bladeguard1", race="High Elves", category="Seaguard", skill=[5,4,4,3,3,1,6,1,8,0], inventory=Inventory(itemlist=["Sword"]))
        ]), 
        Squad(name="Cadet Archers", category="Cadet", henchmanlist=[
            Character(name="Cadet1", race="High Elves", category="Cadet", skill=[5,3,3,3,3,1,6,1,7,0], inventory=Inventory(itemlist=["Longbow"]))
        ])
        ]
    
    # Load warband data
    
    # show data
    print(f"Warband testing")
    print(f"Name: {WarbandA.name}")
    print(f"Race: {WarbandA.race}")
    print(f"Gold: {WarbandA.inventory.gold}")
    print(f"Wyrdstones: {WarbandA.inventory.wyrd}")
    print(f"Inventory:")
    for item in WarbandA.inventory.itemlist:
        print(f"- {item}")

    print("Heroes:")
    i = 1
    for hero in WarbandA.herolist:
        print(f"{i}.")
        print(f"Name: {hero.name}")
        print(f"category: {hero.category}")
        print(f"skill: {hero.skill}")
        print(f"Items: {hero.inventory.itemlist}")
        i += 1

    print("Squads:")
    i = 1
    for squad in WarbandA.squadlist:
        print(f"{i}.")
        print(f"Name: {squad.name}")
        print(f"category: {squad.category}")
        print(f"items: {squad.henchmanlist[0].inventory.itemlist}")
        print(f"(total: {squad.get_totalhenchman()})")
        i += 1

    

    # Save data
    # save_json(dict(data=WarbandA.inventory), jsonfile='savedwarbands.json')
    # save_json(dict(data=WarbandA.herolist), jsonfile='savedwarbands.json')
    # save_json(dict(data=WarbandA.squadlist), jsonfile='savedwarbands.json')
    # save_json(data=WarbandA.__dict__, jsonfile='savedwarbands.json')
    # werkt niet , Object of type Squad is not JSON serializable
    
if __name__ == "__main__":
    test_json()
    test_makeWarband()