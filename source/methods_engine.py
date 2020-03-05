import os

from source.methods_json import (
    save_file,
    show_files,
    load_file,
)

def get_localpath():
    """set the paths to the users documents folder"""
    local_path = os.path.join("~", "Documents", "WAM")
    path = os.path.expanduser(local_path)
    print("get_localpath: local path - " + local_path)

def save_warband(datadict):
    """Save warband to a save file"""
    path = get_localpath()
    print("save_warband: path - " + path)

    # set the filename to the warbands name
    filename = datadict["name"]

    # run the json command to save the file as a json file
    save_file(datadict, path, filename)

def show_warbands():
    # Folderpath
    path = get_localpath()
    savelist = show_files(path)

    return savelist

def load_warband(wbname):
    path = get_localpath()

    # set the filename to the warbands name
    filename = wbname

    # run the load json command to open the respective json file
    datadict = load_file(path, filename)
    
    # return the warband dictionary
    return datadict

def save_reference(datadict, filename):
    # set the paths to the applications database reference files
    path = "database/references/"

    # run the json command to save the file as a json file
    save_file(datadict, path, filename)

def load_reference(reference):
    # set the paths to the applications database reference files
    path = "database/references/"

    # set the reference filename to be loaded
    filename = reference + "_ref"

    # load the file
    datadict = load_file(path, filename)

    # return the reference dictionary
    return datadict
