import os

from source.methods_json import (
    save_json,
    show_json,
    load_json,
)

def get_localpath():
    """set the paths to the users documents folder"""

    local_path = os.path.join("~", "Documents", "WAM")
    path = os.path.expanduser(local_path)

    print("get_localpath: local path - " + local_path)

def save_warband(datadict):
    """Save warband to a save file"""

    # Folderpath
    path = get_localpath()
    print("save_warband: path - " + path)

    # set the filename to the warbands name
    filename = datadict["name"]

    # run the json command to save the file as a json file
    save_json(datadict, path, filename)

def show_warbands():
    """Show all the warband save files"""

    # Folderpath
    path = get_localpath()

    savelist = show_json(path)

    return savelist

def load_warband(wbname):
    """Load a specific warband save file"""

    # Folderpath
    path = get_localpath()

    # set the filename to the warbands name
    filename = wbname

    # run the load json command to open the respective json file
    datadict = load_json(path, filename)
    
    # return the warband dictionary
    return datadict

def save_reference(datadict, filename):
    """Save reference data to the fixed location within the application directory"""

    # set the paths to the applications database reference files
    path = "database/references/"

    # set the reference filename to be loaded
    filename = filename + "_ref"

    # run the json command to save the file as a json file
    save_json(datadict, path, filename)

def load_reference(reference):
    """Load reference data from the fixed location within the application directory"""

    # set the paths to the applications database reference files
    path = "database/references/"

    # set the reference filename to be loaded
    filename = reference + "_ref"

    # load the file
    datadict = load_json(path, filename)

    # return the reference dictionary
    return datadict
