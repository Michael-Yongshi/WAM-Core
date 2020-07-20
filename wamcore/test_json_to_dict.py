import os
import json


# set the paths to the  reference file
path = os.path.join(os.path.dirname(__file__), 'database') # the same folder as caller
# filename = "abilities_ref"
# filename = "characters_ref"
# filename = "experience_table_ref"
# filename = "items_ref"
# filename = "magic_ref"
# filename = "processes_ref"
filename = "warbands_ref"
complete_path = os.path.join(path, filename + ".json")

# open file and return the dictionary
with open(complete_path, 'r') as infile:
    datadict = json.load(infile)

print(datadict)
