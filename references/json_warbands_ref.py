import json

#  Open Json file/ 
with open('references/warbands_ref.json', 'r') as infile:
    data = json.load(infile)

# finding a record
# adding a record
data['warbands_ref'].append({
    'race': 'Human',
    'name': 'Humantest',
    'source': 'test',
})

with open('references/warbands_ref.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print(data)