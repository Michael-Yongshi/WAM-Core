from database.json import * # Refer to JSON methods
from class_hierarchy import * # Refer to class methods 
from generic_methods import * # Refer to generic methods


# create_warband
wbid = Warband(
    name="Myriac",
    race="High Elf"
    )
# print(wbid)

# Manually adding rules of warband
wbid.rulelist=[
        Rule(name="Excellent Sight", description="Elves have eyesight unmatched by mere humans. Elves spot Hidden enemies from two times as far away as other warriors (ie, twice their Initiative value in inches)."), 
        Rule(name="Haughty", description="The High Elves are a very proud and noble race. A High Elf Warband may never include hired swords that are not of High Elven blood, nor can they use any equipment of Dwarf origin. This includes Gromril weapons and armour."),
        Rule(name="Honourable", description="High Elves can never use poison or drugs of any kind no matter what the circumstance."),
        Rule(name="The Old Ways", description="The High Elves may never use black powder weapons of any sort. This goes against their ancestors and the traditions of the Old Ways."),
        Rule(name="Resolve", description="The High Elves have been fighting the Dark Elves for countless centuries. When fighting their dark kin the High Elves are driven by unwavering determination. They are considered to have a Leadership of 10 when taking Rout Tests against the Dark Elves. In addition, High Elves can never choose to voluntarily Rout as they must stop their evil kin at any cost.")
        ]

# Manually adding an item
wbid.inventory.itemlist=[
    Item(name="Wyrd Breaker", source = "High Elves", category="Other")
    ]

# Creating heroes

hero1 = Character.create_character(
    name="Viriadon", 
    race="High Elf", 
    source="High Elves",
    category="Loremaster", 
    )
hero2 = Character.create_character(
    name="Olri`in", 
    race="High Elf", 
    source="High Elves",
    category="Sword Warden"
    )

# Adding items to heroes
hero1.inventory.itemlist = [
    Item.create_item(name = "Dagger", source = "Core Rules"),
    Item.create_item(name = "Mage Staff", source = "Core Rules")
    ]
hero2.inventory.itemlist = [
    Item.create_item(name = "Dagger", source = "Core Rules"),
    Item.create_item(name = "Sword", source = "Core Rules"),
    Item.create_item(name = "Light Armour", source = "Core Rules"),
    Item.create_item(name = "Shield", source = "Core Rules")
    ]

# adding the heroes to the warband hero list
wbid.herolist = [
    hero1,
    hero2
    ]

# Create Squads and the henchmen within
squad1 = Squad.create_squad(
    name = "Spearguard",
    race = "High Elf",
    source = 'High Elves',
    category = "Seaguard",
    number = 2
    )
squad2 = Squad.create_squad(
    name = "Bladeguard",
    race = "High Elf",
    source = 'High Elves',
    category = "Seaguard",
    number = 1
    )
squad3 = Squad.create_squad(
    name = "Cadets",
    race = "High Elf",
    source = 'High Elves',
    category = "Cadet",
    number = 1
    )

# Adding items to the squads
squad1.equip_squad(name = "Dagger", source = "Core Rules")
squad1.equip_squad(name = "Spear", source = "Core Rules")
squad1.equip_squad(name = "Long Bow", source = "Core Rules")

squad2.equip_squad(name = "Dagger", source = "Core Rules")
squad2.equip_squad(name = "Greatsword", source = "Core Rules")
squad2.equip_squad(name = "Long Bow", source = "Core Rules")

squad3.equip_squad(name = "Dagger", source = "Core Rules")
squad3.equip_squad(name = "Long Bow", source = "Core Rules")

# adding the squads to the squadlist
wbid.squadlist = [
    squad1,
    squad2,
    squad3
    ]

# Current gold minus cost of the warband
startgold = 500
wbid.inventory.gold = startgold - wbid.get_warbandprice()
print(wbid.inventory.gold)

# create warband dictionary
datadict = wbid.to_dict()

# Cache, save and load warband
cache_warband(datadict)
save_warband(wbid.name)
load_warband(wbid.name)
