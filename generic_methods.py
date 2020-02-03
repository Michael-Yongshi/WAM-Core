from database.json import *
from class_hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def cache_warband(datadict):
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Cache completed")


def save_warband(wbname):
       
    # Open data in cache
    datadict = open_json(jsonfile="database/saves/cache.json")

    # Determine filepath of new save
    filepath = "database/saves/" + wbname + ".json"

    # Save cache to JSON save file
    save_json(data=datadict, jsonfile=filepath)
    print("Save completed")


def load_warband(savename):
    # Determine filepath of existing save
    filepath = "database/saves/" + savename + ".json"
    datadict = open_json(filepath)

    # Push save to JSON cache
    # To do: write to global variable
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Loading completed")


    
if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    save_warband(wbname)
    load_warband(wbname)