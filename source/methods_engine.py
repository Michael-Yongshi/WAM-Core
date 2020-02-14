import os

from source.methods_json import (
    open_json,
    save_json,
)

from source.class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from source.class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    )

# specific methods for application
def cache_warband(wbid):
    
    datadict = wbid.to_dict()
    save_json(data=datadict, jsonfile="database/saves/cache.json")

def save_warband(warband):

    wbdict = warband.to_dict()
    filepath = "database/saves/" + warband.name + ".json"
    save_json(wbdict, filepath)

def save_warband_from_cache(wbname):
       
    # Open data in cache
    datadict = open_json(jsonfile="database/saves/cache.json")

    # Determine filepath of new save
    filepath = "database/saves/" + wbname + ".json"

    # Save cache to JSON save file
    save_json(data=datadict, jsonfile=filepath)
    print("Save completed")

def load_warband(savename):
    filepath = "database/saves/" + savename + ".json"
    datadict = open_json(filepath)
    wbid = Warband.from_dict(datadict)
    return wbid

def load_warband_to_cache(savename):
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
