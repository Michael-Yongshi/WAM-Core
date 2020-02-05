from database.json import open_json

from generic_methods import save_warband
from generic_methods import load_warband
from generic_methods import cache_warband

from class_hierarchy import Warband
from class_hierarchy import Squad
from class_hierarchy import Character
from class_hierarchy import Hero
from class_hierarchy import Henchman

from class_components import Rule
from class_components import Treasury
from class_components import Item
from class_components import Skill
from class_components import Ability
from class_components import Magic

# create_warband
wbid = Warband(
    name="Myriac",
    race="High Elf",
    description=("High Elves originate from the island kingdom of Ulthuan far to the west of the Empire, which is belaugered continuously by raids from their hated Dark Elven brethren, the fearless Norscans, and the incursions of Chaos which rack all civilized lands."
    "The fair elven folk learn how to fight from childhood, and thanks to their extremely long lifespans they often grow in skill to become unrivaled in their prowess by other mortals. Despite their individual ability, their numbers are few compared to their co-inhabitants of the Old World and they are always in search of some edge with which to gain an advantage over their foes."
    "Thus the High Elves are unrivaled practitioners of the arcane arts and their specialized school of Spell craft is so highly regarded it is referred to simply as the High Magic by other Wizards. The Elven Mages are very proficient at many aspects of Magic, including astrology and the prediction of what is to come. So it was that the coming of the comet known in the Empire as the Hammer of Sigmar was not a suprise to the inhabitants of Ulthuan."
    "The Loremasters foretold the great power it would bring in the form of wyrdstone, but also the danger as they knew the substance was riddled with the Chaos taint and would spread the evils of corruption to all new levels. Therefore the Pheonix King, advised by the Loremasters, issued a decree: Wyrdstone must be destroyed whenever possible, and any brave enough to undertake the hardships of travel across the lands of the Humans and to bear the dangers of the Damned city to seek out and destroy the Chaos-tainted stones would be forever honored in the lands of the Elves."
    "From across the provinces bands of young would-be heroes volunteered to pledge their blades to the Kings edict, and the Loremasters dispatched many apprentices to accompany them in their journey and lead them to the fell substance. Furthermore the Loremasters crafted magical devices called Wyrd-breakers to counter the Chaos taint of the wyrdstone and render the substance into more mundane gemstones thereby effectively destroying the wyrdstone but still allowing the Elves a source of revenue. Each of the young mages was given one and sent forth to rid the world of the taint of wyrdstone."
    )
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
wbid.itemlist=[
    Item(name="Wyrd Breaker", source = "High Elves", category="Other")
    ]

# Creating heroes

hero1 = Hero.create_character(
    name="Viriadon", 
    race="High Elf", 
    source="High Elves",
    category="Loremaster", 
    )
hero2 = Hero.create_character(
    name="Olri`in", 
    race="High Elf", 
    source="High Elves",
    category="Sword Warden"
    )

# Adding items to heroes
hero1.itemlist = [
    Item.create_item(name = "Dagger", source = "Core Rules"),
    Item.create_item(name = "Mage Staff", source = "Core Rules")
    ]
hero2.itemlist = [
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
wbid.treasury.gold = startgold - wbid.get_warbandprice()
print(wbid.treasury.gold)

# create warband dictionary
datadict = wbid.to_dict()

# Cache, save and load warband
cache_warband(datadict)
save_warband(wbid.name)
load_warband(wbid.name)
