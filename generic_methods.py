import os

from database.json import open_json
from database.json import save_json

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
    savelist = {}
    i = 1
    for filename in os.listdir(folderpath):
        if filename.endswith(".json") and not filename == "cache.json": 
            # print(os.path.join(folderpath, filename))
            savedict = {'number': i, 'savefile': filename}
            savelist.update(savedict)
            i += 1
    
    print(savelist)
    return savelist


if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    save_warband(wbname)
    load_warband(wbname)
    show_saved_warbands()