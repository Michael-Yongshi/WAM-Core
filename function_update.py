from database.json import *
from class_hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def test_updateWarband():
    # Open cached warband
    filepath = "database/saves/cache.json"
    datadict = open_json(filepath)

    # from dictionary to objects for manipulation
    wbid = Warband.from_dict(datadict)



    # add new henchman group of 'test' henchmen
    wbid.add_squad(name="Bowguard", race="High Elf", warband="High Elves", category="Seaguard")



    # from objects to dictionary for placing back in cache
    datadict = wbid.to_dict()

    # Push save to JSON cache
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Update completed")


if __name__ == "__main__":
    test_updateWarband()