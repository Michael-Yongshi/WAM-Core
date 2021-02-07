from .methods_engine import (
    load_reference,
    )

def get_warbandref():

    filename = "warbands"
    # open ref json
    datadict = load_reference(filename)

    return datadict


def get_characterref():

    filename = "characters"
    # open ref json
    datadict = load_reference(filename)

    return datadict

def get_itemref():
    
    filename = "items"
    # open ref json
    datadict = load_reference(filename)

    return datadict

def get_abilityref():
    
    filename = "abilities"
    # open ref json
    datadict = load_reference(filename)

    return datadict

def get_magicref():

    filename = "magic"
    # open ref json
    datadict = load_reference(filename)

    return datadict
