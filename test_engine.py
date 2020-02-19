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
        Item.create_item(source = "Broheim", category="Other", subcategory="Wyrdbreaker")
        ]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name="Hero A", 
        race="High Elf", 
        source="Broheim",
        warband="High Elves",
        category="Loremaster",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Mage Quarter Staff", category = "Melee Weapon", source = "Broheim")
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
    squad1.equip_squad(subcategory = "Spear", category = "Melee Weapon", source = "Core Rules")
    print("squad1 item succesfull")

    squad2.equip_squad(subcategory = "Great Sword", category = "Melee Weapon", source = "Core Rules")
    print("squad2 item succesfull")

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
    print("warband extraction succesfull")

    # Add another hero
    newhero = Hero.create_character(
        name="Bearand", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Sword Warden"
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name="Crypton", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Sword Warden"
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name="Danan", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Ranger"
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name="Everia", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Ranger"
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name="Felicia", 
        race="High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category="Ranger"
        )
    print("hero5 creation succesful")
    # Add items for new hero
    newhero.itemlist = [
        Item.create_item(subcategory = "Sword", category = "Melee Weapon", source = "Core Rules"),
        Item.create_item(subcategory = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        Item.create_item(subcategory = "Shield", category = "Armour & Protection", source = "Core Rules")
        ]
    print("newhero1 item succesfull")
    newhero2.itemlist = [
        Item.create_item(subcategory = "Sword", category = "Melee Weapon", source = "Core Rules"),
        Item.create_item(subcategory = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        Item.create_item(subcategory = "Shield", category = "Armour & Protection", source = "Core Rules")
        ]
    print("newhero2 item succesfull")
    newhero3.itemlist = [
        Item.create_item(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules"),
        Item.create_item(subcategory = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        ]
    print("newhero3 item succesfull")
    newhero4.itemlist = [
        Item.create_item(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules"),
        Item.create_item(subcategory = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        ]
    print("newhero4 item succesfull")
    newhero5.itemlist = [
        Item.create_item(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules"),
        Item.create_item(subcategory = "Light Armour", category = "Armour & Protection", source = "Core Rules"),
        ]
    print("newhero5 item succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist.append(newhero)
    wbid.herolist.append(newhero2)
    wbid.herolist.append(newhero3)
    wbid.herolist.append(newhero4)
    wbid.herolist.append(newhero5)
    print("hero assigning succesful")

    # Create Squads and the henchmen within
    newsquad = Squad.create_squad(
        name = "Cadet",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Cadet2",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Cadet3",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Cadet4",
        race = "High Elf",
        source = "Broheim",
        warband = "High Elves",
        category = "Cadet",
        number = 1
        )
    print("squad4 creation succesful")
    
    # Adding items to the squads
    newsquad.equip_squad(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    newsquad2.equip_squad(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    newsquad3.equip_squad(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    newsquad4.equip_squad(subcategory = "Long Bow", category = "Missile Weapon", source = "Core Rules")
    print("squad equipment creation succesful")
    
    # adding the squads to the squadlist
    wbid.squadlist.append(newsquad)
    wbid.squadlist.append(newsquad2)
    wbid.squadlist.append(newsquad3)
    wbid.squadlist.append(newsquad4)
    print("squad assigning succesful")

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