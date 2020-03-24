from source.methods_database_to import (
    create_ref_files,
    add_warbandref,
    add_characterref,
    add_itemref,
    add_abilityref,
    add_magicref,
)

from source.methods_database_from import (
    get_warbandref,
    get_characterref,
    get_itemref,
    get_abilityref,
    get_magicref,
)

from source.methods_engine import (
    save_reference,
    load_reference,
)

def add_impact_character():
    # for every character in character-ref add impact: 0 skill
    datadict = load_reference("characters")
    for key1 in datadict:
        for key2 in datadict[key1]:
            for key3 in datadict[key1][key2]:
                for key4 in datadict[key1][key2][key3]:
                    characterdict = datadict[key1][key2][key3][key4]
                    # print(characterdict) # check for correct dict
                    impactdict = {'impact': 0}
                    characterdict['skill'].update(impactdict)
                    # print(characterdict) # check if change is processed ok
        #             break # breaks so we only get the first result for debugging
        #         break
        #     break
        # break
    # save_reference(datadict, "characters")

def add_impact_item():
    # for every item in items-ref add impact: 0 skill except for missile items
    datadict = load_reference("items")
    for key1 in datadict:
        for key2 in datadict[key1]:
            for key3 in datadict[key1][key2]:
                itemdict = datadict[key1][key2][key3]
                # print(itemdict) # check for correct dict
                if key2 == "Missile Weapon":
                    impact = itemdict['skill']['strength']
                    impactdict = {'impact': impact}
                    strengthdict = {'strength': 0}
                    itemdict['skill'].update(strengthdict)
                    itemdict['skill'].update(impactdict)
                    # print(itemdict) # check if change is processed ok
                else:
                    impactdict = {'impact': 0}
                    itemdict['skill'].update(impactdict)
                # print(itemdict) # check if change is processed ok
        #         break # breaks so we only get the first result for debugging
        #     break
        # break
    save_reference(datadict, "items")


if __name__ == '__main__':
    # add_impact_character()
    # add_impact_item()
