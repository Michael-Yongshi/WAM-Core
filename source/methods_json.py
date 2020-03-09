import os
import json


def save_json(datadict, path, filename):
    """Dumps a dictionary to a json file in the documents folder"""

    print("save_json path:" + path)
    # check if directory already exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    filename = datadict["name"]
    print(path + filename)
    complete_path = os.path.join(path, filename + ".json")

    print(complete_path)

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
    """Load files to the documents folder"""

    # check if directory already exists, if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    complete_path = os.path.join(path, filename + ".json")

    # open save file and return the datadict
    with open(complete_path, 'r') as infile:
        datadict = json.load(infile)
    
    return datadict