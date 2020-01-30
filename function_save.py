from database.json import *
from hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def test_saveWarband(wbname):
       
    # Open data in cache
    datadict = open_json(jsonfile="database/saves/cache.json")

    # Determine filepath of new save
    filepath = "database/saves/" + wbname + ".json"

    # Save cache to JSON save file
    save_json(data=datadict, jsonfile=filepath)
    print("save completed")


if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    test_saveWarband(wbname)