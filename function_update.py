from database.json import *
from class_hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def test_updateWarband():
    # Open cached warband
    filepath = "database/saves/cache.json"
    datadict = open_json(filepath)

    # from dictionary to objects for manipulation
    wbid = Warband.from_dict(datadict)



    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Cadet",
        race = "High Elf",
        source = 'High Elves',
        category = "Cadet",
        number = 1
        )
    
    # Adding items to the squads
    squad1.equip_squad(name = "Dagger", source = "Core Rules")
    squad1.equip_squad(name = "Long Bow", source = "Core Rules")

    # adding the squads to the squadlist
    wbid.squadlist.append(squad1)



    # from objects to dictionary for placing back in cache
    datadict = wbid.to_dict()

    # Push save to JSON cache
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Update completed")


if __name__ == "__main__":
    test_updateWarband()