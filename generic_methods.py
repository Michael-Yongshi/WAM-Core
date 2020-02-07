import os

from database.json import open_json
from database.json import save_json

from class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    )

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

    # Push to JSON cache
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Loading completed")

def show_saved_warbands():
    # Folderpath
    folderpath = "database/saves/"

    # Iterate over jsons in database/saves/
    savelist = []
    for filename in os.listdir(folderpath):
        if filename.endswith(".json") and not filename == "cache.json": 
            warbandname = os.path.splitext(filename)[0]
            # print(os.path.join(folderpath, filename))
            savelist.append(warbandname)

    return savelist

def get_current_warband():
    # Open data in cache
    datadict = open_json(jsonfile="database/saves/cache.json")

    # from dictionary to objects for manipulation
    wbid = Warband.from_dict(datadict)

    return wbid

if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    save_warband(wbname)
    load_warband(wbname)
    show_saved_warbands()