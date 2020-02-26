import os
import json


#  Open Json file/ 
def open_json(jsonfile):
    with open(jsonfile, 'r') as infile:
        data = json.load(infile)
    return data

# dumping data to json
def save_json(data ,jsonfile):

    with open(jsonfile, 'w') as outfile:
        json.dump(data, outfile, indent=4)

# adding a record 
def append_json(data, datatype, jsonfile):
    with open(jsonfile, 'r') as infile:
        loaddata = json.load(infile)
    loaddata[datatype]=data
    save_json(loaddata, jsonfile)

def save_file(datadict, filename):
    """Dumps a save file to the documents folder"""

    # set the paths to the users documents folder
    path = "~\WAM"
    user_path = os.path.expanduser(path)
    completepath = os.path.join(user_path, filename + ".json")
    
    # check if file already exists, if not create it
    if not os.path.exists(completepath):
        os.makedirs(completepath)

    # open file
    savefile = open(completepath, 'w')

    # dump json data in the file
    json.dump(datadict, savefile, indent=4)