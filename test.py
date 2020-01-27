from references.json import *
from stats import *
from warband import *
from inventory import *


def print_newline():
    print(" ")


# test warband classes
def test_makeWarband():
    # Create data
    wbid = Warband(name="Uthluan Raiders", race="High Elves")
    wbid.inventory = Inventory(gold=500, itemlist=[
        Item(name="Mordheim Map", category="Miscellaneous", abilitylist=[Ability(name="Search Environment")]),
        Item(name="Elven Wine", category="Miscellaneous")
        ])
    wbid.herolist = [
        Hero(
            name="Hero1", 
            race="High Elves", 
            category="Loremaster", 
            skill=Skill(5,4,4,3,3,1,6,1,9,0), 
            abilitylist=[
                Ability("Excellent Sight"), 
                ], 
            inventory=Inventory(itemlist=[
                Item(
                    name="Mage staff", 
                    category="Melee Weapon"), 
                Item(
                    name="Dagger", 
                    category="Melee Weapon")
                ])
            ), 
        Hero(
            name="Hero2", 
            race="High Elves", 
            category="Swordwarden", 
            skill=Skill(5,4,4,3,3,1,6,1,9,0), 
            inventory=Inventory(itemlist=[
                Item(
                    name="Sword", 
                    category="Melee Weapon"
                    ), 
                Item(
                    name="Dagger", 
                    category="Melee Weapon"
                    ), 
                Item(
                    name="Shield", 
                    category="Armour"
                    ), 
                Item(
                    name="Light Armour", 
                    category="Armour"
                    )
                ])
            )
        ]
    wbid.squadlist = [
        Squad(
            name="Spearguard", 
            category="Seaguard", 
            henchmanlist=[
                Henchman(
                    name="Spearguard1", 
                    race="High Elves", 
                    category="Seaguard", 
                    skill=Skill(5,4,4,3,3,1,6,1,8,0), 
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Spear", 
                            category="Melee Weapon"
                            )
                        ])
                    ),
                Henchman(
                    name="Spearguard2", 
                    race="High Elves", 
                    category="Seaguard", 
                    skill=Skill(5,4,4,3,3,1,6,1,8,0), 
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Spear", 
                            category="Melee Weapon"
                            )
                        ])
                    )
                ]
            ), 
        Squad(
            name="Bladeguard", 
            category="Seaguard", 
            henchmanlist=[
                Henchman(
                    name="Bladeguard1", 
                    race="High Elves", 
                    category="Seaguard", 
                    skill=Skill(5,4,4,3,3,1,6,1,8,0), 
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Sword", 
                            category="Melee Weapon"
                            )
                        ])
                    )
                ]
            ), 
        Squad(
            name="Cadet Archers", 
            category="Cadet", 
            henchmanlist=[
                Henchman(
                    name="Cadet1", 
                    race="High Elves", 
                    category="Cadet", 
                    skill=Skill(5,3,3,3,3,1,6,1,7,0), 
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Longbow", 
                            category="Missile Weapon"
                            )
                        ])
                    )
                ]
            )
        ]
    
    # Load warband data
    
    # show data
    print(f"Warband testing")
    print(f"Name: {wbid.name}")
    print(f"Race: {wbid.race}")
    print(f"Gold: {wbid.inventory.gold}")
    print(f"Wyrdstones: {wbid.inventory.wyrd}")
    print(f"Inventory:{wbid.inventory.itemlist}")
    totalheroes = len(wbid.herolist)
    totalhenchman = 0
    for s in wbid.squadlist:
        totalhenchman = totalhenchman + s.get_totalhenchman()
    totalchars = totalheroes+totalhenchman
    printtotal = "Number of units: " + str(totalchars)
    print(printtotal)
    print_newline()

    for hero in wbid.herolist:
        print(f"Name: {hero.name}")
        print(f" category: {hero.category}")
        print(f" skill: m:{hero.skill.movement}, w:{hero.skill.weapon}, b:{hero.skill.ballistic}, s:{hero.skill.strength}, t:{hero.skill.toughness}, a:{hero.skill.actions}, i:{hero.skill.initiative}, w:{hero.skill.wounds}, ld:{hero.skill.leadership}, as:{hero.skill.armoursave}")
        print(f" Items: {hero.inventory.itemlist}")
    print("Squads:")
    print_newline

    for squad in wbid.squadlist:
        print(f"Name: {squad.name}")
        print(f" category: {squad.category}")
        print(f" skill: m:{squad.henchmanlist[0].skill.movement}, w:{squad.henchmanlist[0].skill.weapon}, b:{squad.henchmanlist[0].skill.ballistic}, s:{squad.henchmanlist[0].skill.strength}, t:{squad.henchmanlist[0].skill.toughness}, a:{squad.henchmanlist[0].skill.actions}, i:{squad.henchmanlist[0].skill.initiative}, w:{squad.henchmanlist[0].skill.wounds}, ld:{squad.henchmanlist[0].skill.leadership}, as:{squad.henchmanlist[0].skill.armoursave}")
        print(f" items: {squad.henchmanlist[0].inventory.itemlist}")
        print(f" (total: {squad.get_totalhenchman()})")

    # generic get_dict function? get an object and create a dict from it


    # Save data
    filepath = "saves/" + wbid.name + ".json"

    datadict = {}
    wbdict = wbid.get_dict()
    datadict.update(wbdict)
    # save_json(data=datadict, jsonfile=filepath)

    invdict = wbid.inventory.get_dict(ref="inventory")
    datadict["Warband"].update(invdict) # add new inventory dict to warband, practically replacing original value of inventory
    # save_json(data=datadict, jsonfile=filepath)

    datadict["Warband"]["inventory"]["itemlist"]={} # change in a dict before setting dict values
    i = 1
    for item in wbid.inventory.itemlist:
        itemref = "Item" + str(i) # to make sure it has a unique key
        print(itemref)
        itemdict = item.get_dict(ref=itemref)
        datadict["Warband"]["inventory"]["itemlist"].update(itemdict)
        i += 1

        datadict["Warband"]["inventory"]["itemlist"][itemref]["abilitylist"]={} # change in a dict before setting dict values
        a = 1
        print(str(item.abilitylist))
        for ability in item.abilitylist:
            abilityref = "Ability" + str(a) # to make sure it has a unique key
            print(abilityref)
            abilitydict = ability.get_dict(ref=abilityref)
            print(abilitydict)
            datadict["Warband"]["inventory"]["itemlist"][itemref]["abilitylist"].update(abilitydict)
            a += 1

    datadict["Warband"]["herolist"]={} # change in a dict before setting dict values
    h = 1
    for hero in wbid.herolist:
        heroref = "Hero" + str(h) # to make sure it has a unique key
        herodict = hero.get_dict(ref=heroref)
        datadict["Warband"]["herolist"].update(herodict)
        h += 1
        
        invdict = hero.inventory.get_dict(ref="inventory")
        datadict["Warband"]["herolist"][heroref].update(invdict) # add new inventory dict to warband, practically replacing original value of inventory
    
        datadict["Warband"]["herolist"][heroref]["inventory"]["itemlist"]={} # change in a dict before setting dict values
        i = 1
        for item in hero.inventory.itemlist:
            itemref = "Item" + str(i) # to make sure it has a unique key
            itemdict = item.get_dict(ref=itemref)
            datadict["Warband"]["herolist"][heroref]["inventory"]["itemlist"].update(itemdict)
            i += 1
    
    # save_json(data=datadict, jsonfile=filepath)
    
    datadict["Warband"]["squadlist"]={} # change in a dict before setting dict values
    s = 1
    for squad in wbid.squadlist:
        squadref = "squad" + str(s) # to make sure it has a unique key
        squaddict = squad.get_dict(ref=squadref)
        datadict["Warband"]["squadlist"].update(squaddict)
        s += 1

        datadict["Warband"]["squadlist"][squadref]["henchmanlist"]={} # change in a dict before setting dict values
        h = 1
        for henchman in squad.henchmanlist:
            henchmanref = "Henchman" + str(h) # to make sure it has a unique key
            henchmandict = henchman.get_dict(ref=henchmanref)
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"].update(henchmandict)
            h += 1
            
            invdict = henchman.inventory.get_dict(ref="inventory")
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref].update(invdict) # add new inventory dict to warband, practically replacing original value of inventory
        
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["inventory"]["itemlist"]={} # change in a dict before setting dict values
            i = 1
            for item in henchman.inventory.itemlist:
                itemref = "Item" + str(i) # to make sure it has a unique key
                itemdict = item.get_dict(ref=itemref)
                datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["inventory"]["itemlist"].update(itemdict)
                i += 1
            

    # save to file
    save_json(data=datadict, jsonfile=filepath)

if __name__ == "__main__":
    test_makeWarband()