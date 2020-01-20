from references.json import *
from stats import *
from warband import *
from inventory import *


def print_newline():
    print("\n")


def test_makeWarband():
    # Create data
    WarbandA = Warband(name="Uthluan Raiders", race="High Elves")
    WarbandA.inventory = Inventory(gold=500, itemlist=[
        "Mordheim Map", 
        "Elven Wine"
        ])
    WarbandA.herolist = [
        Character(name="Hero1", race="High Elves", type="Loremaster", skill=[5,4,4,3,3,1,6,1,9,0], abilitylist=[Ability("Excellent Sight"), Ability("Dispel")], inventory=Inventory(itemlist=["Mage staff", "Dagger"])), 
        Character(name="Hero2", race="High Elves", type="Swordwarden", skill=[5,4,4,3,3,1,6,1,9,0])
        ]
    WarbandA.squadlist = [
        Squad(name="Spearguard", type="Seaguard", henchmanlist=[
            Character(name="Spearguard1", race="High Elves", type="Seaguard", skill=[5,4,4,3,3,1,6,1,8,0], inventory=Inventory(itemlist=["Spear"])),
            Character("Spearguard2", "High Elves", "Seaguard", [5,4,4,3,3,1,6,1,8,0], Inventory(itemlist=["Spear"]))
        ]), 
        Squad(name="Bladeguard", type="Seaguard"), Squad(name="Cadet Archers", type="Cadet")
        ]
    
    # show data
    print(f"Warband testing")
    print(f"Name: {WarbandA.name}")
    print(f"Race: {WarbandA.race}")
    print(f"Gold: {WarbandA.inventory.gold}")
    print(f"Wyrdstones: {WarbandA.inventory.wyrd}")
    print(f"Inventory:")
    for item in WarbandA.inventory.itemlist:
        print(f"- {item}")

    print_newline()
    print("Heroes:")
    i = 1
    for hero in WarbandA.herolist:
        print(f"{i}.")
        print(f"Name: {hero.name}")
        print(f"Type: {hero.type}")
        print(f"Inventory:")
        for item in hero.inventory.itemlist:
            print(f"- {item}")
        i += 1
    print_newline()
    print("Squads:")
    i = 1
    for squad in WarbandA.squadlist:
        print(f"{i}.")
        print(f"Name: {squad.name}")
        print(f"Type: {squad.type}")
        print(f"(total: {squad.get_totalhenchman()})")
        i += 1

    # Save data (WIP)
    

if __name__ == "__main__":
    test_makeWarband()