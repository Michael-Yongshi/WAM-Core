import json

# creating an items-ref json file
data = {}
data['items_ref'] = []
data['items_ref'].append({
    'name': 'Dagger',
    'type': 'Melee Weapon',
    'price': '2',
    'desc': 'A basic dagger where any character starts with'
})
data['items_ref'].append({
    'name': 'Bow',
    'type': 'Missile weapon',
    'price': '10',
    'desc': 'A simple bow with a range of 16 inch'
})
data['items_ref'].append({
    'name': 'Light Armour',
    'type': 'Armour',
    'price': '20',
    'desc': 'Lightweight armour that provides a single armour save'
})

with open('references\items_ref.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
