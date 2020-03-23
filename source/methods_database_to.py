from .methods_engine import (
    save_reference,
    load_reference,
    )

from .class_components import (
    Skill
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

def add_characterref(race, source, warband, category, ishero, skill, abilitylist, magiclist, itemlist, eventlist, experience, price, maxcount, description):
    
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
    skilldict = Skill.from_list(skill)

    datadict[race][source][warband][category]={
        'race': race,
        'source': source,
        'warband': warband,
        'category': category,
        'ishero': ishero,
        'skill': skilldict,
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'itemlist': itemlist,
        'eventlist': eventlist,
        'experience': experience,
        'price': price,
        'maxcount': maxcount,
        'description': description
    }

    print(f"Added character: {category}")
    save_reference(datadict, filename)

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

    skilldict = {}
    skilldict = Skill.from_list(skill)

    # Add data
    datadict[source][category][subcategory]={
        'source': source,
        'category': category,
        'subcategory': subcategory,
        'distance': distance,
        'skill': skilldict,
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'price': price,
        'description': description
    }
   
    print(f"Added item: {subcategory}")
    save_reference(datadict, filename)

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