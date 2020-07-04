from source.methods_engine import (
    save_warband,
    load_warband,
    show_warbands,
    load_reference,
    )

from source.class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from source.class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    Event,
    )

# test items

def test_all_items():

    # test warband
    wbid = Warband.create_warband(
        name = "Test Reikland",
        race = "Human",
        source = "Core Rules",
        warband =  "Reikland",
        )
   
    # test unit
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Mercenary Captain",
        )

    #load reference of all items
    datadict = load_reference("items")

    # loop over all items
    for category in datadict:
        for source in datadict[category]:
            for subcategory in datadict[category][source]:
                # get item data
                itemdict = datadict[category][source][subcategory]
                print(itemdict["subcategory"])
                # create python object
                dataobject = Item.from_refdict(datadict = itemdict)
                hero1.itemlist = [
                    dataobject
                    ]
                

if __name__ == "__main__":
    # test_all_warbands()
    test_all_items()
    # test_all_abilities()
    # test_all_magic()