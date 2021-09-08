import os
import datetime

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

def save_warband(warband, filename="", filepath="", add_timestamp=False):
    """
    Save warband to a save file
    if filename is empty the warband name is used
    if filepath is empty the default wam location is used under the users documents
    a timestamp can be given to the file
    """

    # Folderpath
    filepath = get_localpath() if filepath == "" else filepath

    # transform warband object to dict for saving to json
    datadict = warband.to_dict()

    # set the filename to the warbands name unless a specific name is given
    if filename == "":
        filename = datadict["name"]
    else:
        filename

    # add a timestamp if deemed necessary
    if add_timestamp==True:

        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")	
        filename += f"-{timestamp}"
    print(f"filename: {filename}")

    # run the json command to save the file as a json file
    save_json(datadict, filepath, filename)

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

def get_database_handler():
    # TODO: try / except if database is missing for some reason
    
    # set up database handler
    handler = SQLiteHandler()

    # set the path to the database
    current_dir = os.path.dirname(os.path.realpath(__file__))
    database_path = os.path.join(current_dir, "database")
    handler.database_open(filename="database", path=database_path)

    return handler

def load_crossreference(source_table, target_table, key):

    # get handler
    handler = get_database_handler()

    # reading crossreferences
    records = handler.crossref_read_record(
        tablename1=source_table,
        tablename2=target_table,
        primarykey=key,
    )
    # print(f"Looking up records of {target_table} based on key {key} of {source_table}")
    # print_records(records)

    return records

def print_records(records):
    for record in records:
        print_record(record)

def print_record(record):
    print(f"primarykey: {record.primarykey}, recordpairs: {record.recordpairs}")


# def save_reference(datadict, filename):
#     """Save reference data to the fixed location within the application directory"""

#     # set the paths to the applications database reference files
#     path = os.path.join(os.path.dirname(__file__), "database")

#     # set the reference filename to be loaded
#     filename = filename + "_ref"

#     # run the json command to save the file as a json file
#     save_json(datadict, path, filename)


def load_strings():
    """Load reference data from the fixed location within the application directory"""

    # # set the paths to the applications database reference files
    # path = path = os.path.join(os.path.dirname(__file__), "database")

    # # set the reference filename to be loaded
    # filename = reference + "_ref"

    # # load the file
    # datadict = load_json(path, filename)

    # # return the reference dictionary
    # return datadict

    current_dir = os.path.dirname(os.path.realpath(__file__))
    strings_path = os.path.join(current_dir, "database")

    datadict = load_json(path=strings_path, filename="strings.json")

    return datadict

def load_reference(table):
    """
    Load table data from the database
    """

    # get handler
    handler = get_database_handler()
    
    # set the table to be loaded
    table = handler.database.tables[table].records

    return table
