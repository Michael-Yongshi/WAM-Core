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

def test_createWarband(wbname, wbrace):
   
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
        source="High Elves",
        category="Loremaster",
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
        category = "Loremaster",
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
    wbname = "Full WB test"
    wbrace = "High Elf"
    wbsource = "High Elves"
    test_createWarband(wbname, wbrace)