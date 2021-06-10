from wamcore.methods_engine import (
    print_record,
    print_records,
    save_warband,
    load_warband,
    show_warbands,
    load_reference,
    load_crossreference,
    )

from wamcore.class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from wamcore.class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    Event,
    )

# test items

def test_all_warbands():

    try:
        wbtable = load_reference("warbands")
        chartable = load_reference("characters")
        wb_chartable = load_reference("CROSSREF_warbands_characters")
        
        for wb_record in wbtable:

            wb_id = wb_record.primarykey
            print(wb_record.recorddict["base"])

            warband = Warband.from_database(primarykey=wb_id)

            print(warband.race)
            print(warband.source)
            print(warband.warband)
            # print(warband.description)
            print(warband.treasury.gold)
            print(warband.rulelist)
            print(warband.itemlist)
            print("done")

            # Create list of characters
            wb_char_records = load_crossreference(
                source_table="warbands",
                target_table="characters",
                key=wb_id,
                )
            print_records(wb_char_records)

            for wb_char_record in wb_char_records:
                char_id = wb_char_record.recorddict["characters_id"]
                newchar = Character.from_database(char_id)

                if newchar.ishero == 1:
                    newhero = Hero.from_database(primarykey=char_id)
                    warband.herolist.append(newhero)

                else:
                    newsquad = Squad.from_database(primarykey=char_id)
                    warband.squadlist.append(newsquad)

            print(warband.herolist)
            print(warband.squadlist)
    
    except:
        print("Testing all warbands failed")

def test_all_items():

    try:
        #load reference of all items
        table = load_reference("items")

        # loop over all items
        items = []
        for record in table:

            dataobject = Item.from_database(record.primarykey)
            items.append(dataobject)

        print(items)

    except:
        print("Testing all items failed")

def test_all_abilities():

    try:
        # load reference of all abilities
        table = load_reference("abilities")

        # loop over all abilities
        abilities = []
        for record in table:

            dataobject = Ability.from_database(record.primarykey)
            abilities.append(dataobject)

        print(abilities)

    except:
        print("Testing all abilities failed")

def test_all_magics():

    try:

        # load reference of all magics
        table = load_reference("magics")

        # loop over all magics
        magics = []
        for record in table:

            dataobject = Magic.from_database(record.primarykey)
            magics.append(dataobject)

        print(magics)

    except:
        print("Testing all magics failed")

if __name__ == "__main__":

    test_all_warbands()
    test_all_items()
    test_all_abilities()
    test_all_magics()