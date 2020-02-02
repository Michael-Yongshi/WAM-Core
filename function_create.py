from database.json import *
from class_hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def test_createWarband(wbname, wbrace):
   
    # create_warband
    wbid = Warband(
        name=wbname,
        race=wbrace
        )
    # print(wbid)

    # insert details of warband
    wbid.rulelist=[
            Rule(name="Excellent Sight", description="Elves have eyesight unmatched by mere humans. Elves spot Hidden enemies from two times as far away as other warriors (ie, twice their Initiative value in inches)."), 
            Rule(name="Haughty", description="The High Elves are a very proud and noble race. A High Elf Warband may never include hired swords that are not of High Elven blood, nor can they use any equipment of Dwarf origin. This includes Gromril weapons and armour."),
            Rule(name="Honourable", description="High Elves can never use poison or drugs of any kind no matter what the circumstance."),
            Rule(name="The Old Ways", description="The High Elves may never use black powder weapons of any sort. This goes against their ancestors and the traditions of the Old Ways."),
            Rule(name="Resolve", description="The High Elves have been fighting the Dark Elves for countless centuries. When fighting their dark kin the High Elves are driven by unwavering determination. They are considered to have a Leadership of 10 when taking Rout Tests against the Dark Elves. In addition, High Elves can never choose to voluntarily Rout as they must stop their evil kin at any cost.")
            ]

    wbid.inventory.itemlist=[
        Item(name="Test item", category="Other")
        ]
        
    wbid.herolist = [
        Character.create_character(
            name="Hero1", 
            race="High Elf", 
            source="High Elves",
            category="Loremaster", 
            ), 
        Character.create_character(
            name="Hero1", 
            race="High Elf", 
            source="High Elves",
            category="Sword Warden"
            )
        ]
        # adding items to heroes
    wbid.squadlist = [
        Squad(
            name="Spearguard", 
            category="Seaguard", 
            henchmanlist=[
                Character.create_character(
                    name="Spearguard1", 
                    race="High Elf", 
                    source="High Elves",
                    category="Seaguard"
                    ),
                Character.create_character(
                    name="Spearguard2", 
                    race="High Elf", 
                    source="High Elves",
                    category="Seaguard"
                    )
                ]
            # adding items to squad
            ), 
        Squad(
            name="Bladeguard", 
            category="Seaguard", 
            henchmanlist=[
                Character.create_character(
                    name="Bladeguard1", 
                    race="High Elf", 
                    source="High Elves",
                    category="Seaguard"
                    )
                ]
            ),
        Squad(
            name="Cadet Archers", 
            category="Cadet", 
            henchmanlist=[
                Character.create_character(
                    name="Cadet1", 
                    race="High Elf", 
                    source="High Elves",
                    category="Cadet", 
                    )
                ]
            )
        ]
    
    # Current gold minus cost of the warband
    startgold = 500
    # wbid.inventory.gold = startgold - wbid.get_warbandprice()
    # print(wbid.inventory.gold)
    
    # create warband dictionary
    datadict = wbid.to_dict()

    # Push new warband to JSON cache
    # To do: write to global variable
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("New Warband placed in cache")


if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    wbrace = "High Elves"
    test_createWarband(wbname, wbrace)