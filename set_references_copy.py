from wamcore.methods_database_from_copy import (
    get_warbandref,
    get_characterref,
    get_itemref,
    get_abilityref,
    get_magicref,
)

from wamcore.database.database import (
    Database,
    Table,
    Record,
)

database_path = """E:\\Git\\WAM-Core\\wamcore\\database"""
database_filename = "wam_core_database"

def magic_table(db):

    magicdict = get_magicref()
    # print(magicdict)

    table = db.create_table(
        name="magics", 
        column_names = ["source", "category", "name", "grouping", "difficulty", "description"], 
        column_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "INTEGER", "TEXT"],
    )

    for source in magicdict:
        for magictype in magicdict[source]:
            for magic in magicdict[source][magictype]:
                valuedict = magicdict[source][magictype][magic]
                values = []
                for key in valuedict:
                    values += [valuedict[key]]
                
                table.createRecord(values = values)
                # print(values)

    # return table

def ability_table(db):
    
    abilitydict = get_abilityref()
    # print(abilitydict)

    table = db.create_table(
        name="abilities",
        record_name="Ability",
        column_names = ["source", "maincategory", "category", "name", "description"], 
        column_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "TEXT"],
    )

    for maincategory in abilitydict:
        for category in abilitydict[maincategory]:
            for source in abilitydict[maincategory][category]:
                for name in abilitydict[maincategory][category][source]:
                    valuedict = abilitydict[maincategory][category][source][name]
                    values = []
                    for key in valuedict:
                        values += [valuedict[key]]
                    
                    table.createRecord(values = values)
                    # print(values)

    # return table

def item_table(db):

    magictable = db.get_table("magics")
    abilitytable = db.get_table("abilities")

    itemdict = get_itemref()
    # print(itemdict)

    table = db.create_table(
        name="items", 
        column_names = ["source", "category", "name", "distance", "movement", "weapon", "ballistic", "strength", "toughness", "wounds", "initiative", "actions", "leadership", "armoursave", "impact", "price", "description"], 
        column_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "TEXT"],
    )

    cr_ia_table = db.create_table(
        name="CROSSREF_items_abilities",
        column_names = ["item_id", "ability_id"],
        column_types = ["INTEGER REFERENCES items(id)", "INTEGER REFERENCES abilities(id)"],
    )

    cr_im_table = db.create_table(
        name="CROSSREF_items_magics",
        column_names = ["item_id", "magic_id"],
        column_types = ["INTEGER REFERENCES items(id)", "INTEGER REFERENCES magics(id)"],
    )

    
    for category in itemdict:
        for source in itemdict[category]:
            for subcategory in itemdict[category][source]:
                valuedict = itemdict[category][source][subcategory]
                values = []

                cr_ia_values = []
                cr_im_values = []
                for key in valuedict:
                    if key == "skill":
                        skilldict = valuedict[key]
                        for skill in skilldict:
                            values += [skilldict[skill]]

                    elif key == "abilitylist":
                        abilitylist = valuedict[key]
                        if abilitylist == []:
                            pass
                        else:
                            for ability in abilitylist:
                                where = [["name", [ability["name"]]]]
                                # print(where)
                                records = abilitytable.readRecords(where=where)
                                # print(records)
                                if records == []:
                                    pass
                                else:
                                    # print(records)
                                    cr_ia_values += [records[0].primarykey]

                    elif key == "magiclist":
                        magiclist = valuedict[key]
                        if magiclist == []:
                            pass
                        else:
                            for magic in magiclist:
                                where = [["name", [magic["name"]]]]
                                # print(where)
                                records = magictable.readRecords(where=where)
                                # print(records)
                                if records == []:
                                    pass
                                else:
                                    # print(records)
                                    cr_im_values += [records[0].primarykey]

                    else:
                        values += [valuedict[key]]
                
                # print(values)
                newrecord = table.createRecord(values = values)
                # print(newrecord)

                # create cross reference for abilities
                # print(cr_ia_values)
                for ia in cr_ia_values:
                    cr_ia_table.createRecord(
                        values=[
                            newrecord.primarykey, 
                            ia,
                            ]
                        )

                # print(cr_im_values)
                for im in cr_im_values:
                    cr_im_table.createRecord(
                        values=[
                            newrecord.primarykey, 
                            im,
                            ]
                        )

    # return table

def character_table(db):

    characterdict = get_characterref()

    magictable = db.get_table("magics")
    abilitytable = db.get_table("abilities")
    itemtable = db.get_table("items")
    
    characterdict = get_characterref()
    # print(characterdict)

    table = db.create_table(
        name="characters", 
        column_names = ["race", "source", "warband", "name", "ishero", "movement", "weapon", "ballistic", "strength", "impact", "toughness", "wounds", "initiative", "actions", "leadership", "armoursave", "experience", "price", "maxcount", "description"], 
        column_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "BOOL", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "INTEGER", "TEXT"],
    )

    cr_ca_table = db.create_table(
        name="CROSSREF_characters_abilities",
        column_names = ["character_id", "ability_id"],
        column_types = ["INTEGER REFERENCES characters(id)", "INTEGER REFERENCES abilities(id)"],
    )

    cr_cm_table = db.create_table(
        name="CROSSREF_characters_magics",
        column_names = ["character_id", "magic_id"],
        column_types = ["INTEGER REFERENCES characters(id)", "INTEGER REFERENCES magics(id)"],
    )

    cr_ci_table = db.create_table(
        name="CROSSREF_characters_items",
        column_names = ["character_id", "item_id"],
        column_types = ["INTEGER REFERENCES characters(id)", "INTEGER REFERENCES items(id)"],
    )

    for race in characterdict:
        for source in characterdict[race]:
            for warband in characterdict[race][source]:
                for name in characterdict[race][source][warband]:
                    valuedict = characterdict[race][source][warband][name]
                    # print(valuedict)

                    values = []

                    cr_ca_values = []
                    cr_cm_values = []
                    cr_ci_values = []
                    for key in valuedict:
                        if key == "skill":
                            skilldict = valuedict[key]
                            for skill in skilldict:
                                values += [skilldict[skill]]

                        elif key == "abilitylist":
                            abilitylist = valuedict[key]
                            if abilitylist == []:
                                pass
                            else:
                                for ability in abilitylist:
                                    where = [["name", [ability["name"]]]]
                                    # print(where)
                                    records = abilitytable.readRecords(where=where)
                                    # print(records)
                                    if records == []:
                                        pass
                                    else:
                                        # print(records)
                                        cr_ca_values += [records[0].primarykey]

                        elif key == "magiclist":
                            magiclist = valuedict[key]
                            if magiclist == []:
                                pass
                            else:
                                for magic in magiclist:
                                    where = [["name", [magic["name"]]]]
                                    # print(where)
                                    records = magictable.readRecords(where=where)
                                    # print(records)
                                    if records == []:
                                        pass
                                    else:
                                        # print(records)
                                        cr_cm_values += [records[0].primarykey]

                        elif key == "itemlist":
                            itemlist = valuedict[key]
                            if itemlist == []:
                                pass
                            else:
                                for item in itemlist:
                                    where = [["name", [item["subcategory"]]]]
                                    # print(where)
                                    records = itemtable.readRecords(where=where)
                                    # print(records)
                                    if records == []:
                                        pass
                                    else:
                                        # print(records)
                                        cr_ci_values += [records[0].primarykey]

                        elif key == "eventlist":
                            pass

                        else:
                            values += [valuedict[key]]
                    
                    # print(values)
                    newrecord = table.createRecord(values = values)
                    # print(newrecord)

                    # create cross reference for abilities
                    # print(cr_ca_values)
                    for ca in cr_ca_values:
                        cr_ca_table.createRecord(
                            values=[
                                newrecord.primarykey, 
                                ca,
                                ]
                            )

                    # print(cr_cm_values)
                    for cm in cr_cm_values:
                        cr_cm_table.createRecord(
                            values=[
                                newrecord.primarykey, 
                                cm,
                                ]
                            )
                    
                    # print(cr_ci_values)
                    for ci in cr_ci_values:
                        cr_ci_table.createRecord(
                            values=[
                                newrecord.primarykey, 
                                ci,
                                ]
                            )

    # return table

def warband_table(db):
    
    itemtable = db.get_table("items")
    
    warbanddict = get_warbandref()
    # print(warbanddict)

    table = db.create_table(
        name="warbands", 
        column_names = ["race", "source", "name", "rules", "startgold", "description"], 
        column_types = ["VARCHAR(255)", "VARCHAR(255)", "VARCHAR(255)", "TEXT", "INTEGER", "TEXT"],
    )

    cr_wi_table = db.create_table(
        name="CROSSREF_warbands_items",
        column_names = ["warband_id", "item_id"],
        column_types = ["INTEGER REFERENCES warbands(id)", "INTEGER REFERENCES items(id)"],
    )

    for race in warbanddict:
        for source in warbanddict[race]:
            for warband in warbanddict[race][source]:
                valuepairs = [warbanddict[race][source][warband]]
                # print(valuepairs)

                valuedict = warbanddict[race][source][warband]
                # print(valuedict)

                values = []

                cr_wi_values = []
                for key in valuedict:
                    if key == "skill":
                        skilldict = valuedict[key]
                        for skill in skilldict:
                            values += [skilldict[skill]]

                    elif key == "itemlist":
                        itemlist = valuedict[key]
                        if itemlist == []:
                            pass
                        else:
                            for item in itemlist:
                                where = [["name", [item["subcategory"]]]]
                                # print(where)
                                records = itemtable.readRecords(where=where)
                                # print(records)
                                if records == []:
                                    pass
                                else:
                                    # print(records)
                                    cr_ci_values += [records[0].primarykey]

                    elif key == "rulelist":
                        values += [f"{valuedict[key]}"]

                    # elif key == "description":
                        # value = valuedict[key].replace("""<i>""", '')
                        # value = value.replace("""</i>""", '')
                        # values += [value]

                    else:
                        values += [valuedict[key]]
                
                # print(values)
                newrecord = table.createRecord(values = values)
                # print(newrecord)

                # create cross reference for abilities
                # print(cr_wi_values)
                for wi in cr_wi_values:
                    cr_wi_table.createRecord(
                        values=[
                            newrecord.primarykey, 
                            wi,
                            ]
                        )

    # return table

def experience_table(db):

    datadict = {
        "Hero": {
            "Advance 0": 0,
            "Advance 1": 2,
            "Advance 2": 4,
            "Advance 3": 6,
            "Advance 4": 8,
            "Advance 5": 11,
            "Advance 6": 14,
            "Advance 7": 17,
            "Advance 8": 20,
            "Advance 9": 24,
            "Advance 10": 28,
            "Advance 11": 32,
            "Advance 12": 36,
            "Advance 13": 41,
            "Advance 14": 46,
            "Advance 15": 51,
            "Advance 16": 57,
            "Advance 17": 63,
            "Advance 18": 69,
            "Advance 19": 76,
            "Advance 20": 83,
            "Advance 21": 90
        },
        "Squad": {
            "Advance 0": 0,
            "Advance 1": 2,
            "Advance 2": 5,
            "Advance 3": 9,
            "Advance 4": 14
        }
    }

    table = db.create_table(
        name="advances",
        column_names = ["ishero", "number", "experience"], 
        column_types = ["BOOL", "INTEGER", "INTEGER"],
    )

    for ishero in datadict:
        for advance in datadict[ishero]:
            valuepairs = [datadict[ishero][advance]]
            # print(valuepairs)

            valuedict = datadict[ishero][advance]
            print(valuedict)

            values = []
            if ishero == "Hero":
                values += [True]
            else:
                values += [False]
            values += [advance]
            values += [valuedict]
            
            # print(values)
            newrecord = table.createRecord(values = values)
            # print(newrecord)

    # return table

if __name__ == "__main__":

    
    db = Database(path=database_path, filename=database_filename)
    
    magic_table(db)
    ability_table(db)
    item_table(db)
    character_table(db)
    warband_table(db)
    experience_table(db)





