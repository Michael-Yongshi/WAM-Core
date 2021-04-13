import os

from .methods_json import (
    save_json,
    show_json,
    load_json,
)

from sqlitemanager.handler import SQLiteHandler

def get_localpath():
    """set the paths to the users documents folder"""

    local_path = os.path.join("~", "Documents", "WAM")
    path = os.path.expanduser(local_path)

    return path

def save_warband(datadict):
    """Save warband to a save file"""

    # Folderpath
    path = get_localpath()

    # set the filename to the warbands name
    filename = datadict["name"]

    # run the json command to save the file as a json file
    save_json(datadict, path, filename)

def show_warbands():
    """Show all the warband save files"""

    # Folderpath
    path = get_localpath()

    # get all the save files
    savelist = show_json(path)

    # return list of save files
    return savelist

def load_warband(wbname):
    """Load a specific warband save file"""

    # Folderpath
    path = get_localpath()

    # set the filename to the warbands name
    filename = wbname

    # open the respective save file
    datadict = load_json(path, filename)
    
    # return the warband dictionary
    return datadict

def save_reference(datadict, filename):
    """Save reference data to the fixed location within the application directory"""

    # set the paths to the applications database reference files
    path = os.path.join(os.path.dirname(__file__), "database")

    # set the reference filename to be loaded
    filename = filename + "_ref"

    # run the json command to save the file as a json file
    save_json(datadict, path, filename)

def load_reference(reference):
    """
    Load reference data from the database
    """

    # TODO: try / except if database is missing for some reason
    
    # set up database handler
    handler = SQLiteHandler()

    # set the path to the database
    current_dir = os.path.dirname(os.path.realpath(__file__))
    database_path = os.path.join(current_dir, "database")
    handler.database_open(filename="database", path=database_path)
    
    # set the reference to be loaded
    table = handler.database.tables["warbands"].records

    return table

def print_records(records):
    for record in records:
        print_record(record)

def print_record(record):
    print(f"primarykey: {record.primarykey}, recordpairs: {record.recordpairs}")
