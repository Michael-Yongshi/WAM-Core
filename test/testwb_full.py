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

def test_createWarband(wbname, wbrace, wbsource):
   
    # create_warband
    wbid = Warband(
        name=wbname,
        race=wbrace,
        source=wbsource,
        description="No description"
        )

    # Manually adding rules of warband
    wbid.rulelist=[
            Rule(name="Test rule", description="Test rule description."),
            ]

    # Manually adding an item
    wbid.itemlist=[
        Item(name="Test item", source = "manual", category="Other")
        ]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name="A", 
        race="High Elf", 
        source="Broheim - High Elves",
        category="Loremaster",
        )
    
    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(name = "Mage Staff (Two Handed)", source = "Broheim - High Elves")
        ]

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    
    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Spearguard",
        race = "High Elf",
        source = 'Broheim - High Elves',
        category = "Seaguard",
        number = 2
        )
    
    squad2 = Squad.create_squad(
        name = "Bladeguard",
        race = "High Elf",
        source = 'Broheim - High Elves',
        category = "Seaguard",
        number = 1
        )

    # Adding items to the squads
    squad1.equip_squad(name = "Spear", source = "Core Rules")

    squad2.equip_squad(name = "Greatsword", source = "Core Rules")

    # adding the squads to the squadlist
    wbid.squadlist = [
        squad1,
        squad2
        ]

    # Current gold minus cost of the warband
    startgold = 500
    wbid.treasury.gold = startgold - wbid.get_price()
    
    # Push new warband to JSON cache
    # To do: write to global variable
    cache_warband(wbid)
    print("Create Completed")

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
        source="Broheim - High Elves",
        category="Sword Warden"
        )
    newhero2 = Hero.create_character(
        name="Crypton", 
        race="High Elf", 
        source="Broheim - High Elves",
        category="Sword Warden"
        )
    newhero3 = Hero.create_character(
        name="Danan", 
        race="High Elf", 
        source="Broheim - High Elves",
        category="Ranger"
        )
    newhero4 = Hero.create_character(
        name="Everia", 
        race="High Elf", 
        source="Broheim - High Elves",
        category="Ranger"
        )
    newhero5 = Hero.create_character(
        name="Crytonia", 
        race="High Elf", 
        source="Broheim - High Elves",
        category="Ranger"
        )
    
    # Add items for new hero
    newhero.itemlist = [
        Item.create_item(name = "Sword", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        Item.create_item(name = "Shield", source = "Core Rules")
        ]
    newhero2.itemlist = [
        Item.create_item(name = "Sword", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        Item.create_item(name = "Shield", source = "Core Rules")
        ]
    newhero3.itemlist = [
        Item.create_item(name = "Long Bow", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        ]
    newhero4.itemlist = [
        Item.create_item(name = "Long Bow", source = "Core Rules"),
        Item.create_item(name = "Light Armour", source = "Core Rules"),
        ]
    newhero5.itemlist = [
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
        source = "Broheim - High Elves",
        category = "Cadet",
        number = 1
        )
    newsquad2 = Squad.create_squad(
        name = "Cadet2",
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Cadet",
        number = 1
        )
    newsquad3 = Squad.create_squad(
        name = "Cadet3",
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Cadet",
        number = 1
        )
    newsquad4 = Squad.create_squad(
        name = "Cadet4",
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Cadet",
        number = 1
        )

    
    # Adding items to the squads
    newsquad.equip_squad(name = "Long Bow", source = "Core Rules")
    newsquad2.equip_squad(name = "Long Bow", source = "Core Rules")
    newsquad3.equip_squad(name = "Long Bow", source = "Core Rules")
    newsquad4.equip_squad(name = "Long Bow", source = "Core Rules")

    # adding the squads to the squadlist
    wbid.squadlist.append(newsquad)
    wbid.squadlist.append(newsquad2)
    wbid.squadlist.append(newsquad3)
    wbid.squadlist.append(newsquad4)

    cache_warband(wbid)
    save_warband(wbid)
    print("Update completed")

if __name__ == "__main__":
    wbname = "Full WB test"
    wbrace = "High Elf"
    wbsource = "Broheim - High Elves"
    test_createWarband(wbname, wbrace, wbsource)

    test_updateWarband()