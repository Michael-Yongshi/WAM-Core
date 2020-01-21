import json

#  Open Json file/ 
with open('references/warbands_ref.json', 'r') as infile:
    data = json.load(infile)

print(data)