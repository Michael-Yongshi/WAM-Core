import json

#  Open Json file/ 
def open_json(jsonfile):
    with open(jsonfile, 'r') as infile:
        data = json.load(infile)
    return data


# finding a specific record
def find_record(data, key):
    for record in data:
        if record[data] == key:
            return record[data]
            break

# dumping data to json
def save_json(data ,jsonfile):

    with open(jsonfile, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    # newpath = r(jsonfile) 
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)

# adding a record 
def append_json(data, datatype, jsonfile):
    with open(jsonfile, 'r') as infile:
        loaddata = json.load(infile)
    loaddata[datatype]=data
    save_json(loaddata, jsonfile)