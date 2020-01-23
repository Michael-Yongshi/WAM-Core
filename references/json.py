import json

# purpose of these functions are to have a general way to load, work and dump stuff with json files

# 'jsonfile' is the referenced files to open / type of data to get
# 'data' is the complete data table / json content
# 'record' is the specific record to add
# 'jsonfile' is the reference to the actual json file / type of data to store

#  Open Json file/ 
def open_json(jsonfile):
    with open(jsonfile, 'r') as infile:
        data = json.load(infile)
    
    return data
    print(data)

# show all records of a json dataset
def show_records(data):
    
    return data
    print(data)

# finding a specific record
def find_record(data, key):
    for record in data:
        if record[data] == key:
            return record[data]
            print(record[data])
            break

# adding a record 
def add_record(data ,datatype, record):
    data[datatype].append({record})

# dumping data to json
def save_json(data ,jsonfile):
    with open(jsonfile, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print(data)
