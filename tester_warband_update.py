from database.json import (
    open_json,
    save_json,
    )

from generic_methods import (
    save_warband,
    load_warband,
    cache_warband,
    )

from class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from class_components import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    )

def test_updateWarband():
    # Open cached warband
    filepath = "database/saves/cache.json"
    datadict = open_json(filepath)

    # from dictionary to objects for manipulation
    wbid = Warband.from_dict(datadict)

    # Add another hero
    newhero = Hero.create_character(
        name="Bearand", 
        race="High Elf", 
        source="High Elves",
        category="Sword Warden"
        )
    newhero2 = Hero.create_character(
        name="Crypton", 
        race="High Elf", 
        source="High Elves",
        category="Sword Warden"
        )
    newhero3 = Hero.create_character(
        name="Danan", 
        race="High Elf", 
        source="High Elves",
        category="Ranger"
        )
    newhero4 = Hero.create_character(
        name="Everia", 
        race="High Elf", 
        source="High Elves",
        category="Ranger"
        )
    newhero5 = Hero.create_character(
        name="Crytonia", 
        race="High Elf", 
        source="High Elves",
        category="Ranger"
        )
    
    # Add items for new hero
    newhero.itemlist = [
        Item.create_item(name = "Dagger", source = "Core Rules"),
        Item.create_item(name = "Sword", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        Item.create_item(name = "Shield", source = "Core Rules")
        ]
    newhero2.itemlist = [
        Item.create_item(name = "Dagger", source = "Core Rules"),
        Item.create_item(name = "Sword", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        Item.create_item(name = "Shield", source = "Core Rules")
        ]
    newhero3.itemlist = [
        Item.create_item(name = "Dagger", source = "Core Rules"),
        Item.create_item(name = "Long Bow", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        ]
    newhero4.itemlist = [
        Item.create_item(name = "Dagger", source = "Core Rules"),
        Item.create_item(name = "Long Bow", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        ]
    newhero5.itemlist = [
        Item.create_item(name = "Dagger", source = "Core Rules"),
        Item.create_item(name = "Long Bow", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        ]

    # adding the heroes to the warband hero list
    wbid.herolist.append(newhero)
    wbid.herolist.append(newhero2)
    wbid.herolist.append(newhero3)
    wbid.herolist.append(newhero4)
    wbid.herolist.append(newhero5)

    # Create Squads and the henchmen within
    newsquad = Squad.create_squad(
        name = "Cadet",
        race = "High Elf",
        source = 'High Elves',
        category = "Cadet",
        number = 1
        )
    newsquad2 = Squad.create_squad(
        name = "Cadet2",
        race = "High Elf",
        source = 'High Elves',
        category = "Cadet",
        number = 1
        )
    newsquad3 = Squad.create_squad(
        name = "Cadet3",
        race = "High Elf",
        source = 'High Elves',
        category = "Cadet",
        number = 1
        )
    newsquad4 = Squad.create_squad(
        name = "Cadet4",
        race = "High Elf",
        source = 'High Elves',
        category = "Cadet",
        number = 1
        )

    
    # Adding items to the squads
    newsquad.equip_squad(name = "Dagger", source = "Core Rules")
    newsquad.equip_squad(name = "Long Bow", source = "Core Rules")
    newsquad2.equip_squad(name = "Dagger", source = "Core Rules")
    newsquad2.equip_squad(name = "Long Bow", source = "Core Rules")
    newsquad3.equip_squad(name = "Dagger", source = "Core Rules")
    newsquad3.equip_squad(name = "Long Bow", source = "Core Rules")
    newsquad4.equip_squad(name = "Dagger", source = "Core Rules")
    newsquad4.equip_squad(name = "Long Bow", source = "Core Rules")

    # adding the squads to the squadlist
    wbid.squadlist.append(newsquad)
    wbid.squadlist.append(newsquad2)
    wbid.squadlist.append(newsquad3)
    wbid.squadlist.append(newsquad4)



    # from objects to dictionary for placing back in cache
    datadict = wbid.to_dict()

    # Push save to JSON cache
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Update completed")


if __name__ == "__main__":
    test_updateWarband()