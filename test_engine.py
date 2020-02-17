from source.methods_json import (
    open_json,
    save_json,
    )
    
from source.methods_engine import (
    save_warband,
    load_warband,
    cache_warband,
    show_saved_warbands,
    get_current_warband,
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
    )

def test_createWarband(name, race, source, warband):
   
    # create_warband
    wbid = Warband.create_warband(
        name=name,
        race=race,
        source=source,
        warband=warband,
        )

    # Manually adding an item
    wbid.itemlist=[
        Item(source = "Broheim", category="Other", name="Wyrdbreaker")
        ]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name="A", 
        race="High Elf", 
        source="Broheim",
        warband="High Elves",
        category="Loremaster",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(name = "Mage Quarter Staff", category = "Melee Weapon", source = "Broheim")
        ]
    print("hero1 item succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Spearguard",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Seaguard",
        number = 2
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Bladeguard",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Seaguard",
        number = 1
        )
    print("squad2 create succesfull")

    # Adding items to the squads
    squad1.equip_squad(name = "Spear", category = "Melee Weapon", source = "Core Rules")
    print("squad1 item succesfull")

    squad2.equip_squad(name = "Great Sword", category = "Melee Weapon", source = "Core Rules")
    print("squad1 item succesfull")

    # adding the squads to the squadlist
    wbid.squadlist = [
        squad1,
        squad2
        ]

    print("squad 12 assign succesfull")
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
        source = "Broheim",
        warband = "High Elves",
        category="Sword Warden"
        )
    newhero2 = Hero.create_character(
        name="Crypton", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Sword Warden"
        )
    newhero3 = Hero.create_character(
        name="Danan", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Ranger"
        )
    newhero4 = Hero.create_character(
        name="Everia", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Ranger"
        )
    newhero5 = Hero.create_character(
        name="Felicia", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Ranger"
        )
    
    # Add items for new hero
    newhero.itemlist = [
        Item.create_item(name = "Sword", category = "Melee Weapon", source = "Core Rules"),
        Item.create_item(name = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        Item.create_item(name = "Shield", category = "Armour & Protection", source = "Core Rules")
        ]
    newhero2.itemlist = [
        Item.create_item(name = "Sword", category = "Melee Weapon", source = "Core Rules"),
        Item.create_item(name = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        Item.create_item(name = "Shield", category = "Armour & Protection", source = "Core Rules")
        ]
    newhero3.itemlist = [
        Item.create_item(name = "Long Bow", category = "Missile Weapon", source = "Core Rules"),
        Item.create_item(name = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        ]
    newhero4.itemlist = [
        Item.create_item(name = "Long Bow", category = "Missile Weapon", source = "Core Rules"),
        Item.create_item(name = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        ]
    newhero5.itemlist = [
        Item.create_item(name = "Long Bow", category = "Missile Weapon", source = "Core Rules"),
        Item.create_item(name = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
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
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    newsquad2 = Squad.create_squad(
        name = "Cadet2",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    newsquad3 = Squad.create_squad(
        name = "Cadet3",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    newsquad4 = Squad.create_squad(
        name = "Cadet4",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )

    
    # Adding items to the squads
    newsquad.equip_squad(name = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    newsquad2.equip_squad(name = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    newsquad3.equip_squad(name = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    newsquad4.equip_squad(name = "Long Bow", category = "Missile Weapon", source = "Core Rules")

    # adding the squads to the squadlist
    wbid.squadlist.append(newsquad)
    wbid.squadlist.append(newsquad2)
    wbid.squadlist.append(newsquad3)
    wbid.squadlist.append(newsquad4)

    cache_warband(wbid)
    save_warband(wbid)
    print("Update completed")

if __name__ == "__main__":
    name = "Full WB test"
    race = "High Elf"
    source = "Broheim"
    warband= "High Elves"

    test_createWarband(name, race, source, warband)    # Creates an object and caches it to cache.json
    test_updateWarband()                            # gets object from cache.json and updates it, then saves it to a warband savefile