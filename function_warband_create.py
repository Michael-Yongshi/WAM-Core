from database.json import * # Refer to JSON methods
from class_hierarchy import * # Refer to class methods 
from generic_methods import * # Refer to generic methods


def test_createWarband(wbname, wbrace):
   
    # create_warband
    wbid = Warband(
        name=wbname,
        race=wbrace,
        description="No description"
        )

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
        Item(name="Test item", source = "manual", category="Other")
        ]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name="Avareac", 
        race="High Elf", 
        source="High Elves",
        category="Loremaster"
        )
    
    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(name = "Dagger", source = "Core Rules"),
        Item.create_item(name = "Mage Staff", source = "Core Rules")
        ]

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
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

    # Adding items to the squads
    squad1.equip_squad(name = "Dagger", source = "Core Rules")
    squad1.equip_squad(name = "Spear", source = "Core Rules")

    squad2.equip_squad(name = "Dagger", source = "Core Rules")
    squad2.equip_squad(name = "Greatsword", source = "Core Rules")

    # adding the squads to the squadlist
    wbid.squadlist = [
        squad1,
        squad2
        ]

    # Current gold minus cost of the warband
    startgold = 500
    wbid.treasury.gold = startgold - wbid.get_warbandprice()
    print(wbid.treasury.gold)
    
    # create warband dictionary
    datadict = wbid.to_dict()

    # Push new warband to JSON cache
    # To do: write to global variable
    cache_warband(datadict)
    

if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    wbrace = "High Elves"
    test_createWarband(wbname, wbrace)