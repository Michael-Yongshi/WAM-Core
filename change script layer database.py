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

def move_core_rules():
    datadict = load_reference("abilities")
    newdatadict = {}

    for key1 in datadict:
        for key2 in datadict[key1]:
            if key2 in newdatadict:
                pass
            else:
                newdatadict[key2] = {}
            
            if key1 in newdatadict[key2]:
                pass
            else:
                newdatadict[key2][key1] = {}

            # print(f"added layers to : {newdatadict}")

            for key3 in datadict[key1][key2]:
                thisentry = datadict[key1][key2][key3]
                newdatadict[key2][key1].update({key3: thisentry})
                # print(f"The final dict looks like this: {newdatadict}")
                # print(f"")
        #         break
        #     break
        # break
    save_reference(newdatadict, "abilities")

if __name__ == '__main__':
    move_core_rules()
