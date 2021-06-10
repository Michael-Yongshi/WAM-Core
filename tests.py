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
    )

from wamcore.class_components import (
    Skill,
    Item,
    Ability,
    Magic,
    )

# test items

def test_all_warbands():

    try:
        wbtable = load_reference("warbands")
        
        for wb_record in wbtable:

            wb_id = wb_record.primarykey
            warband = Warband.from_database(primarykey=wb_id)

            character_list = warband.get_characters()

            for char_id in character_list:
                newchar = Character.from_database(char_id)

                if newchar.ishero == 1:
                    newhero = Hero.from_database(primarykey=char_id)
                    warband.herolist.append(newhero)

                else:
                    newsquad = Squad.from_database(primarykey=char_id)
                    warband.squadlist.append(newsquad)

            pass

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

def test_add_character(name,race,source,warband,ishero,skilldict,experience,price,maxcount,description, starting_dagger):

    skill = Skill.from_dict(skilldict)

    # set the values to a python object first
    dataobject = Character(
        name = "My Character",
        race = race,
        source = source,
        warband = warband,
        category = name,
        ishero = ishero,
        skill = skill,
        abilitylist=[],
        magiclist=[],
        itemlist=[],
        eventlist=[],
        experience=experience,
        price=price,
        maxcount=maxcount,
        description=description,
        )
    
    if starting_dagger == True:
        dataobject.itemlist.append(Item.from_database(primarykey=1))

    return

if __name__ == "__main__":

    # # get from database
    # test_all_warbands()
    # test_all_items()
    # test_all_abilities()
    # test_all_magics()

    # add to database
    test_add_character(
        race = "Brawlers",
        source = "Pijani",
        warband = "Cavewalkers",
        name = "King of the Hill",
        ishero = 1,
        skilldict = {
            "movement": 3,
            "weapon": 4,
            "ballistic": 4,
            "strength": 5,
            "impact": 0,
            "toughness": 3,
            "wounds": 1,
            "initiative": 3,
            "actions": 1,
            "leadership": 8,
            "armoursave": 0,
        },
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "Leader of a cavewalker warband",
        starting_dagger = True,
        )