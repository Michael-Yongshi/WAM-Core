from database.json import *
from hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def test_loadWarband(savename):
    # Choosing a save file
    name = "Uthluan Wyrdbreakers"

    # Determine filepath of existing save
    filepath = "database/saves/" + name + ".json"
    datadict = open_json(filepath)

    # Push save to JSON cache
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Loading completed")

if __name__ == "__main__":
    test_loadWarband(savename="Uthluan Wyrdbreakers")