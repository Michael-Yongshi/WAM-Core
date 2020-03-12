from source.methods_engine import (
    save_reference,
    load_reference,
    )


def create_ref_files():
    # Filename
    namelist = ["warbands", "characters", "items", "abilities", "magic"]
    for name in namelist:
        
        # create filename
        filename = name
        
        # Create empty dictionary file
        datadict = {}
        
        # call save reference function
        save_reference(datadict, filename)


def add_warbandref(race, source, warband, rulelist, itemlist, start_gold, description):

    filename = "warbands"
    # open ref json
    datadict = load_reference(filename)

    # First check if race already exists
    if race in datadict:
        pass
    else:
        datadict[race] = {}

    # Second check if source already exists
    if source in datadict[race]:
        pass
    else:
        datadict[race][source] = {}

    datadict[race][source][warband]={
        'race': race,
        'source': source,
        'warband': warband,
        'rulelist': rulelist,
        'itemlist': itemlist,
        'start_gold': start_gold,
        'description': description,
    }

    save_reference(datadict, filename)

def get_warbandref(race, source, warband):

    filename = "warbands"
    # open ref json
    datadict = load_reference(filename)

    # First check if race exists
    if race in datadict:
        # Second check if source exists
        if source in datadict[race]:
            
            warbanddict = datadict[race][source][warband]
            return warbanddict

        else:
            print(f"source {source} does not exist")
    else:
        print(f"Race {race} does not exist")

def add_characterref(race, source, warband, category, ishero, skill, abilitylist, magiclist, itemlist, experience, price, maxcount, description):
    
    filename = "characters"
    # open ref json
    datadict = load_reference(filename)

    # First check if race already exists
    if race in datadict:
        pass
    else:
        datadict[race] = {}

    # Second check if source already exists
    if source in datadict[race]:
        pass
    else:
        datadict[race][source] = {}

    # Second check if source already exists
    if warband in datadict[race][source]:
        pass
    else:
        datadict[race][source][warband] = {}

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

    datadict[race][source][warband][category]={
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
    save_reference(datadict, filename)

def get_characterref(race, source, warband, category):

    filename = "characters"
    # open ref json
    datadict = load_reference(filename)

    # First check if race exists
    if race in datadict:
        # Second check if source exists
        if source in datadict[race]:
            # Third check if warband exists
            if warband in datadict[race][source]: 
                # fourth check if character exists
                if category in datadict[race][source][warband]: 

                    characterdict = datadict[race][source][warband][category]
                    return characterdict
                    
                else:
                    print(f"Type:{category} does not exist")
            else:
                print(f"Type:{warband} does not exist")
        else:
            print(f"source {source} does not exist")
    else:
        print(f"Race {race} does not exist")

def add_itemref(source, category, subcategory, distance, skill, abilitylist, magiclist, price, description):

    filename = "items"
    # open ref json
    datadict = load_reference(filename)

    # First check if source already exists
    if source in datadict:
        pass
    else:
        datadict[source] = {}

    # Second check if category already exists
    if category in datadict[source]:
        pass
    else:
        datadict[source][category] = {}

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
    datadict[source][category][subcategory]={
        'source': source,
        'category': category,
        'subcategory': subcategory,
        'distance': distance,
        'skill': skilldict[0],
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'price': price,
        'description': description
    }
   
    print(f"Added item: {subcategory}")
    save_reference(datadict, filename)


def get_itemref(source, category, subcategory):
    
    filename = "items"
    # open ref json
    datadict = load_reference(filename)

    # First check if source exists
    if source in datadict:
        # Second check if category exists
        if category in datadict[source]:
            # Third check if item exists
            if subcategory in datadict[source][category]: 

                itemdict = datadict[source][category][subcategory]
                return itemdict

            else:
                print(f"Item:{subcategory} does not exist")
        else:
            print(f"Category {category} does not exist")
    else:
        print(f"Source {source} does not exist")

def add_abilityref(source, category, name, description):

    filename = "abilities"
    # open ref json
    datadict = load_reference(filename)

    # First check if source already exists
    if source in datadict:
        pass
    else:
        datadict[source] = {}

    # Second check if category already exists
    if category in datadict[source]:
        pass
    else:
        datadict[source][category] = {}

    # Add data
    datadict[source][category][name]={
        'source': source,
        'category': category,
        'name': name,
        'description': description,
    }
   
    print(f"Added ability: {name}")
    save_reference(datadict, filename)


def get_abilityref(source, category, name):
    
    filename = "abilities"
    # open ref json
    datadict = load_reference(filename)

    # First check if source exists
    if source in datadict:
        # second check if category exists
        if category in datadict[source]:
            # Third check if ability exists
            if name in datadict[source][category]: 

                abilitydict = datadict[source][category][name]
                return abilitydict

            else:
                print(f"ability:{name} does not exist")
        else:
            print(f"Category: {category} does not exist")
    else:
        print(f"Source {source} does not exist")


def add_magicref(source, category, name, group, difficulty, description):

    filename = "magic"
    # open ref json
    datadict = load_reference(filename)

    # First check if source already exists
    if source in datadict:
        pass
    else:
        datadict[source] = {}

    # Second check if category already exists
    if category in datadict[source]:
        pass
    else:
        datadict[source][category] = {}

    # Add data
    datadict[source][category][name]={
        'source': source,
        'category': category,
        'name': name,
        'group': group,
        'difficulty': difficulty,
        'description': description,
    }
   
    print(f"Added magic: {name}")
    save_reference(datadict, filename)


def get_magicref(source, category, name):

    filename = "magic"
    # open ref json
    datadict = load_reference(filename)

    # First check if source exists
    if source in datadict:
        if category in datadict[source]:
            # Third check if magic exists
            if name in datadict[source][category]: 

                magicdict = datadict[source][category][name]
                return magicdict

            else:
                print(f"magic:{name} does not exist")
        else:
            print(f"Category: {category} does not exist")
    else:
        print(f"Source {source} does not exist")

