import os
import json


def save_json(datadict, path, filename):
    """Dumps a dictionary to a json file in the documents folder"""

    # check if directory already exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    filename = filename

    complete_path = os.path.join(path, filename + ".json")

    # open file and write json to it
    with open(complete_path, 'w') as savefile:
        # dump json data in the file
        json.dump(datadict, savefile, indent=4)

def show_json(path):
    """Show all json files in a folder"""

    # check if directory already exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)
        
    # Iterate over json files
    filelist = []
    for filename in os.listdir(path):
        if filename.endswith(".json"): 
            warbandname = os.path.splitext(filename)[0]
            filelist.append(warbandname)

    return filelist

def load_json(path, filename):
    """Load json files and return a dictionary"""

    # check if directory already exists, if not create it
    if not os.path.exists(path):
        print(f"cant find path {path}")

    else:
        complete_path = os.path.join(path, filename + ".json")

        # open save file and return the datadict
        with open(complete_path, 'r') as infile:
            datadict = json.load(infile)
    
        return datadict
