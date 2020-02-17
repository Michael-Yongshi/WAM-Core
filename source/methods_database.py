from source.methods_json import (
    open_json,
    save_json,
)


def create_warbandref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "warbands_ref.json"

    # Create data file
    data = {}

    print(f"Created warbandfile")
    save_json(data, filepath)

def add_warbandref(race, source, name, rulelist, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "warbands_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if race already exists
    if race in data:
        pass
    else:
        data[race] = {}

    # Second check if source already exists
    if source in data[race]:
        pass
    else:
        data[race][source] = {}

    data[race][source][name]={
        'race': race,
        'source': source,
        'name': name,
        'rulelist': rulelist,
        'description': description,
    }

    print(f"Added warband: {name}")
    save_json(data, filepath)

def get_warbandref(race, source, name):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "warbands_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if race exists
    if race in data:
        # Second check if source exists
        if source in data[race]:
            
            warbanddict = data[race][source][name]
            return warbanddict

        else:
            print(f"source {source} does not exist")
    else:
        print(f"Race {race} does not exist")


def create_characterref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # Create data file
    data = {}

    print(f"Created characterfile")
    save_json(data, filepath)

def add_characterref(race, source, warband, category, ishero, skill, abilitylist, magiclist, itemlist, experience, price, maxcount, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if race already exists
    if race in data:
        pass
    else:
        data[race] = {}

    # Second check if source already exists
    if source in data[race]:
        pass
    else:
        data[race][source] = {}

    # Second check if source already exists
    if warband in data[race][source]:
        pass
    else:
        data[race][source][warband] = {}

    skilldict = {}
    skilldict = {
        "movement": skill[0],
        "weapon": skill[1],
        "ballistic": skill[2],
        "strength": skill[3],
        "toughness": skill[4],
        "wounds": skill[5],
        "initiative": skill[6],
        "actions": skill[7],
        "leadership": skill[8],
        "armoursave": skill[9]
        },

    data[race][source][warband][category]={
        'race': race,
        'source': source,
        'warband': warband,
        'category': category,
        'ishero': ishero,
        'skill': skilldict[0],
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'itemlist': itemlist,
        'experience': experience,
        'price': price,
        'maxcount': maxcount,
        'description': description
    }

    print(f"Added character: {category}")
    save_json(data, filepath)


def get_characterref(race, source, warband, category):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if race exists
    if race in data:
        # Second check if source exists
        if source in data[race]:
            # Third check if warband exists
            if warband in data[race][source]: 
                # fourth check if character exists
                if category in data[race][source][warband]: 

                    characterdict = data[race][source][warband][category]
                    return characterdict
                    
                else:
                    print(f"Type:{category} does not exist")
            else:
                print(f"Type:{warband} does not exist")
        else:
            print(f"source {source} does not exist")
    else:
        print(f"Race {race} does not exist")


def create_itemref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "items_ref.json"

    # Create data file
    data = {}
    data["Core Rules"] = {}

    print(f"Created itemfile")
    save_json(data, filepath)


def add_itemref(source, category, name, distance, skill, abilitylist, magiclist, price, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "items_ref.json"
    
    # open items_ref.json
    data = open_json(filepath)

    # First check if source already exists
    if source in data:
        pass
    else:
        data[source] = {}

    # Second check if category already exists
    if category in data[source]:
        pass
    else:
        data[source][category] = {}

    skilldict = {
        "movement": skill[0],
        "weapon": skill[1],
        "ballistic": skill[2],
        "strength": skill[3],
        "toughness": skill[4],
        "wounds": skill[5],
        "initiative": skill[6],
        "actions": skill[7],
        "leadership": skill[8],
        "armoursave": skill[9]
        },

    # Add data
    data[source][category][name]={
        'source': source,
        'category': category,
        'name': name,
        'distance': distance,
        'skill': skilldict[0],
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'price': price,
        'description': description
    }
   
    print(f"Added item: {name}")
    save_json(data, filepath)


def get_itemref(source, category, name):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "items_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if source exists
    if source in data:
        # Second check if category exists
        if category in data[source]:
            # Third check if item exists
            if name in data[source][category]: 

                itemdict = data[source][category][name]
                return itemdict

            else:
                print(f"Item:{name} does not exist")
        else:
            print(f"Category {category} does not exist")
    else:
        print(f"Source {source} does not exist")


def create_abilityref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "abilities_ref.json"

    # Create data file
    data = {}
    data["Core Rules"] = {}

    print(f"Created abilityfile")
    save_json(data, filepath)


def add_abilityref(source, category, name, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "abilities_ref.json"
    
    # open abilitys_ref.json
    data = open_json(filepath)

    # First check if source already exists
    if source in data:
        pass
    else:
        data[source] = {}

    # Second check if category already exists
    if category in data[source]:
        pass
    else:
        data[source][category] = {}

    # Add data
    data[source][category][name]={
        'source': source,
        'category': category,
        'name': name,
        'description': description,
    }
   
    print(f"Added ability: {name}")
    save_json(data, filepath)


def get_abilityref(source, category, name):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "abilities_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if source exists
    if source in data:
        if category in data[source]:
            # Third check if ability exists
            if name in data[source][category]: 

                abilitydict = data[source][category][name]
                return abilitydict

            else:
                print(f"ability:{name} does not exist")
        else:
            print(f"Category: {category} does not exist")
    else:
        print(f"Source {source} does not exist")


def create_magicref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "magic_ref.json"

    # Create data file
    data = {}
    data["Core Rules"] = {}

    print(f"Created magicfile")
    save_json(data, filepath)


def add_magicref(source, category, name, difficulty, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "magic_ref.json"
    
    # open magics_ref.json
    data = open_json(filepath)

    # First check if source already exists
    if source in data:
        pass
    else:
        data[source] = {}

    # Second check if category already exists
    if category in data[source]:
        pass
    else:
        data[source][category] = {}

    # Add data
    data[source][category][name]={
        'source': source,
        'category': category,
        'name': name,
        'difficulty': difficulty,
        'description': description
    }
   
    print(f"Added magic: {name}")
    save_json(data, filepath)


def get_magicref(source, category, name):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "magic_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if source exists
    if source in data:
        if category in data[source]:
            # Third check if magic exists
            if name in data[source][category]: 

                magicdict = data[source][category][name]
                return magicdict

            else:
                print(f"magic:{name} does not exist")
        else:
            print(f"Category: {category} does not exist")
    else:
        print(f"Source {source} does not exist")

