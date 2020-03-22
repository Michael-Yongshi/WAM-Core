from source.methods_engine import (
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