from warband import *
from references import *


def print_newline():
    print("\n")


def test_makeWarband():
    WarbandA = Warband("Mike's Mercenaries", race="High Elves")
    WarbandA.treasury = Treasury(gold=456)
    WarbandA.herolist = [Character(name="Hero1", type="Loremaster"), Character(name="Hero2", type="Swordwarden")]
    WarbandA.squadlist = [Squad(name="Spearguard", type="Seaguard", experience=1), Squad(name="Bladeguard", type="Seaguard", experience=2), Squad(name="Cadet Archers", type="Cadet", experience=0)]
    
    print(f"Warband testing")
    print(f"Name: {WarbandA.name}")
    print(f"Race: {WarbandA.race}")
    print(f"Treasury: {WarbandA.treasury}")
    print(f"Gold: {WarbandA.treasury.gold}")
    print_newline()
    print("Heroes:")
    i = 1
    for hero in WarbandA.herolist:
        print(f"{i}.")
        print(f"Name: {hero.name}")
        print(f"Type: {hero.type}")
        i += 1
    print_newline()
    print("Squads:")
    i = 1
    for squad in WarbandA.squadlist:
        print(f"{i}.")
        print(f"Name: {squad.name}")
        print(f"Type: {squad.type}")
        print(f"(total: {squad.get_totalhenchman()}, exp: {squad.experience})")
        i += 1
    
def test_makeEquipment():
    equipmentlist = []
    equipmententry1 = Equipment(name="Dagger", type="Weapon", desc="Free default weapon for most units, but giving disadvantage in penetrating armour")
    print(f"References testing")
    print(f"Name: {equipmententry1.name}")
    print(f"Type: {equipmententry1.type}")
    print(f"Description: {equipmententry1.desc}")

if __name__ == "__main__":
    test_makeWarband()
    test_makeEquipment()