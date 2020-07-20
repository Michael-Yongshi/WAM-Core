from .methods_engine import (
    load_reference,
    )

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

def get_itemref(source, category, subcategory):
    
    filename = "items"
    # open ref json
    datadict = load_reference(filename)

    # First check if category exists
    if category in datadict:
        # Second check if source exists
        if source in datadict[category]:
            # Third check if item exists
            if subcategory in datadict[category][source]: 

                itemdict = datadict[category][source][subcategory]
                return itemdict

            else:
                print(f"Item:{subcategory} does not exist")
        else:
            print(f"Source {source} does not exist")
    else:
        print(f"Category {category} does not exist")

def get_abilityref(source, main, category, name):
    
    filename = "abilities"
    # open ref json
    datadict = load_reference(filename)

    # Check if main exists
    if main in datadict:
        # First check if category exists
        if category in datadict[main]:
            # Second check if source exists
            if source in datadict[main][category]:
                # Third check if ability exists
                if name in datadict[main][category][source]: 

                    abilitydict = datadict[main][category][source][name]
                    return abilitydict

                else:
                    print(f"ability:{name} does not exist")
            else:
                print(f"Source {source} does not exist")
        else:
            print(f"Category: {category} does not exist")
    else:
        print(f"Main: {main} does not exist")

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