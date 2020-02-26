import os
import json


#  Open Json file/ 
def open_json(jsonfile):
    with open(jsonfile, 'r') as infile:
        data = json.load(infile)
    return data

def save_file(datadict, filename):
    """Dumps a save file to the documents folder"""

    # set the paths to the users documents folder
    local_path = r"~\WAM"
    user_path = os.path.expanduser(local_path)

    # check if file already exists, if not create it
    if not os.path.exists(user_path):
        os.makedirs(user_path)

    complete_path = os.path.join(user_path, filename + ".json")

    # open file and write json to it
    with open(complete_path, 'w') as savefile:
        # dump json data in the file
        json.dump(datadict, savefile, indent=4)

def load_file(filename):
    """Load files to the documents folder"""

    # set the paths to the users documents folder
    local_path = r"~\WAM"
    user_path = os.path.expanduser(local_path)

    # check if file already exists, if not create it
    if not os.path.exists(user_path):
        os.makedirs(user_path)

    complete_path = os.path.join(user_path, filename + ".json")

    # open save file and return the datadict
    with open(complete_path, 'r') as infile:
        datadict = json.load(infile)
    
    return datadict