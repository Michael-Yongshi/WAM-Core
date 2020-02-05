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


    
if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    save_warband(wbname)
    load_warband(wbname)