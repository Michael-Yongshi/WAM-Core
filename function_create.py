from database.json import *
from hierarchy import * # reference to the hierarchic classes that are used, 
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

    wbid.herolist = [
        Hero(
            name="Hero1", 
            race="High Elves", 
            category="Loremaster", 
            skill=Skill(5,4,4,3,3,1,6,1,9,0), 
            abilitylist=[
                Ability(name="High Elven Magic") 
                ], 
            inventory=Inventory(itemlist=[
                Item(
                    name="Mage staff", 
                    category="Melee Weapon",
                    skill=Skill(0,0,0,1,0,0,0,0,0,0),
                    abilitylist=[
                        Ability(name="Concussion", description="Stunned also happens on a roll of 2 on the injury roll."),
                        Ability(name="One or Two handed", description="Strength bonus is 1 if used twohanded, no bonus if used one handed.")
                        ],
                    desc="Mage Staves of Hoeth are forged from the finest Ithilmar, and are works of art that are truly beautiful to behold. They are usually decorated with gems and other precious materials. Only a Loremaster may use a Mage Staff.",
                    price=20
                    ), 
                Item(
                    name="Dagger", 
                    category="Melee Weapon",
                    abilitylist=[Ability(name="Trouble With Normal Clothing", description="For daggers even default clothing is regarded as armour. Add +1 to the enemy`s armour save.")],
                    price=0
                    )
                ]),
            experience=20,
            price=80
            ), 
        Hero(
            name="Hero2", 
            race="High Elves", 
            category="Swordwarden", 
            skill=Skill(5,5,4,3,3,1,6,1,8,0), 
            abilitylist=[
                Ability("Excellent Sight"), 
                ], 
            inventory=Inventory(itemlist=[
                Item(
                    name="Sword", 
                    category="Melee Weapon",
                    abilitylist=[Ability(name="Parry", description="A sword can parry a single attack.")],
                    price=10
                    ), 
                Item(
                    name="Dagger", 
                    category="Melee Weapon",
                    abilitylist=[Ability(name="Trouble With Normal Clothing", description="For daggers even default clothing is regarded as armour. Add +1 to the enemy`s armour save.")],
                    price=0
                    ),
                Item(
                    name="Shield", 
                    category="Armour",
                    skill=Skill(0,0,0,0,0,0,0,0,0,1),
                    price=5
                    ), 
                Item(
                    name="Light Armour", 
                    category="Armour",
                    skill=Skill(0,0,0,0,0,0,0,0,0,1),
                    price=20
                    )
                ]),
            experience=11,
            price=50
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
                    abilitylist=[
                        # Ability("Excellent Sight"), 
                    ],
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Spear", 
                            category="Melee Weapon",
                            abilitylist=[Ability(name="First Strike", description="A spear allows to strike first even when charged, or evens the odds against other First Strike enabled characters.")],
                            price=10
                            ),
                        Item(
                            name="Longbow", 
                            category="Missile Weapon",
                            abilitylist=[Ability(name="Range", description="A bow with a range of 30 inch.")],
                            price=15
                            ),
                        Item(
                            name="Dagger", 
                            category="Melee Weapon",
                            abilitylist=[Ability(name="Trouble With Normal Clothing", description="For daggers even default clothing is regarded as armour. Add +1 to the enemy`s armour save.")],
                            price=0
                            )
                        ]),
                    experience=0,
                    price=35
                    ),
                Henchman(
                    name="Spearguard2", 
                    race="High Elves", 
                    category="Seaguard", 
                    skill=Skill(5,4,4,3,3,1,6,1,8,0), 
                    abilitylist=[
                        # Ability("Excellent Sight"), 
                    ],
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Spear", 
                            category="Melee Weapon",
                            abilitylist=[Ability(name="First Strike", description="A spear allows to strike first even when charged, or evens the odds against other First Strike enabled characters.")],
                            price=10
                            ),                        
                        Item(
                            name="Longbow", 
                            category="Missile Weapon",
                            abilitylist=[Ability(name="Range", description="A bow with a range of 30 inch.")],
                            price=15
                            ),
                        Item(
                            name="Dagger", 
                            category="Melee Weapon",
                            abilitylist=[Ability(name="Trouble With Normal Clothing", description="For daggers even default clothing is regarded as armour. Add +1 to the enemy`s armour save.")],
                            price=0
                            )
                        ]),
                    experience=0,
                    price=35
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
                    abilitylist=[
                        # Ability("Excellent Sight"), 
                    ],
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Greatsword", 
                            category="Melee Weapon",
                            skill=Skill(0,0,0,2,0,0,0,0,0,0),
                            abilitylist=[Ability(name="Last Strike", description="A greatsword will always strike last even when charging, except against other Last Strike enabled characters.")],
                            price=15
                            ),                        
                        Item(
                            name="Longbow", 
                            category="Missile Weapon",
                            abilitylist=[Ability(name="Range", description="A bow with a range of 30 inch.")],
                            price=15
                            ),
                        Item(
                            name="Dagger", 
                            category="Melee Weapon",
                            abilitylist=[Ability(name="Trouble With Normal Clothing", description="For daggers even default clothing is regarded as armour. Add +1 to the enemy`s armour save.")],
                            price=0
                            )
                        ]),
                    experience=0,
                    price=35
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
                    skill=Skill(5,3,3,3,3,1,5,1,8,0), 
                    abilitylist=[
                        # Ability("Excellent Sight"), 
                    ],
                    inventory=Inventory(itemlist=[
                        Item(
                            name="Longbow", 
                            category="Missile Weapon",
                            abilitylist=[Ability(name="Range", description="A bow with a range of 30 inch.")],
                            price=15
                            ),
                        Item(
                            name="Dagger", 
                            category="Melee Weapon",
                            abilitylist=[Ability(name="Trouble With Normal Clothing", description="For daggers even default clothing is regarded as armour. Add +1 to the enemy`s armour save.")],
                            price=0
                            )
                        ]),
                    experience=0,
                    price=30
                    )
                ]
            )
        ]
    
    # Current gold minus cost of the warband
    startgold = 500
    wbid.inventory.gold = startgold - wbid.get_warbandprice()
    # print(wbid.inventory.gold)
    
    # create warband dictionary
    datadict = wbid.to_dict()

        # Todo: generic to_dict function? get an object and create a dict from it
        # Todo: for saving get rid of the hechman and save their (redundant) info in the squad dict
        # Todo: These elements should become methods of their resepctive class
    datadict = {}
    wbdict = wbid.to_dict()
    datadict.update(wbdict)
    # print("save warband info")

    # print("save warband rulelist")
    datadict["Warband"]["rulelist"]={} # change in a dict before setting dict values
    r = 1
    for rule in wbid.rulelist:
        ruleref = "Rule" + str(r) # to make sure it has a unique key
        # print(ruleref)
        ruledict = rule.to_dict(ref=ruleref)
        datadict["Warband"]["rulelist"].update(ruledict)
        r += 1

    invdict = wbid.inventory.to_dict(ref="inventory")
    datadict["Warband"].update(invdict) # add new inventory dict to warband, practically replacing original value of inventory

    # print("save warband itemlist")
    datadict["Warband"]["inventory"]["itemlist"]={} # change in a dict before setting dict values
    i = 1
    for item in wbid.inventory.itemlist:
        itemref = "Item" + str(i) # to make sure it has a unique key
        # print(itemref)
        itemdict = item.to_dict(ref=itemref)
        datadict["Warband"]["inventory"]["itemlist"].update(itemdict)
        i += 1

        # print("save warband item abilities")
        datadict["Warband"]["inventory"]["itemlist"][itemref]["abilitylist"]={} # change in a dict before setting dict values
        ia = 1
        for ability in item.abilitylist:
            abilityref = "Ability" + str(ia) # to make sure it has a unique key
            # print(abilityref)
            abilitydict = ability.to_dict(ref=abilityref)
            datadict["Warband"]["inventory"]["itemlist"][itemref]["abilitylist"].update(abilitydict)
            ia += 1

    # print("save herolist")
    datadict["Warband"]["herolist"]={} # change in a dict before setting dict values
    h = 1
    for hero in wbid.herolist:
        heroref = "Hero" + str(h) # to make sure it has a unique key
        # print(heroref)
        herodict = hero.to_dict(ref=heroref)
        datadict["Warband"]["herolist"].update(herodict)
        h += 1
        
        skilldict = hero.skill.to_dict(ref="skill")
        datadict["Warband"]["herolist"][heroref].update(skilldict) # add new skill dict, practically replacing original value of inventory

        datadict["Warband"]["herolist"][heroref]["abilitylist"]={} # change in a dict before setting dict values
        a = 1
        for ability in hero.abilitylist:
            abilityref = "Ability" + str(a) # to make sure it has a unique key
            # print(abilityref)
            abilitydict = ability.to_dict(ref=abilityref)
            datadict["Warband"]["herolist"][heroref]["abilitylist"].update(abilitydict)
            a += 1

        invdict = hero.inventory.to_dict(ref="inventory")
        datadict["Warband"]["herolist"][heroref].update(invdict) # add new inventory dict, practically replacing original value of inventory
    
        datadict["Warband"]["herolist"][heroref]["inventory"]["itemlist"]={} # change in a dict before setting dict values
        i = 1
        for item in hero.inventory.itemlist:
            itemref = "Item" + str(i) # to make sure it has a unique key
            # print(itemref)
            itemdict = item.to_dict(ref=itemref)
            datadict["Warband"]["herolist"][heroref]["inventory"]["itemlist"].update(itemdict)
            i += 1
    
            datadict["Warband"]["herolist"][heroref]["inventory"]["itemlist"][itemref]["abilitylist"]={} # change in a dict before setting dict values
            ia = 1
            for ability in item.abilitylist:
                abilityref = "Ability" + str(ia) # to make sure it has a unique key
                # print(abilityref)
                abilitydict = ability.to_dict(ref=abilityref)
                datadict["Warband"]["herolist"][heroref]["inventory"]["itemlist"][itemref]["abilitylist"].update(abilitydict)
                ia += 1
    
    datadict["Warband"]["squadlist"]={} # change in a dict before setting dict values
    sq = 1
    for squad in wbid.squadlist:
        squadref = "squad" + str(sq) # to make sure it has a unique key
        # print(squadref)
        squaddict = squad.to_dict(ref=squadref)
        datadict["Warband"]["squadlist"].update(squaddict)
        sq += 1

        datadict["Warband"]["squadlist"][squadref]["henchmanlist"]={} # change in a dict before setting dict values
        h = 1
        for henchman in squad.henchmanlist:
            henchmanref = "Henchman" + str(h) # to make sure it has a unique key
            # print(henchmanref)
            henchmandict = henchman.to_dict(ref=henchmanref)
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"].update(henchmandict)
            h += 1
            
            skilldict = henchman.skill.to_dict(ref="skill")
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref].update(skilldict) # add new skill dict, practically replacing original value of inventory

            datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["abilitylist"]={} # change in a dict before setting dict values
            a = 1
            for ability in henchman.abilitylist:
                abilityref = "Ability" + str(a) # to make sure it has a unique key
                # print(abilityref)
                abilitydict = ability.to_dict(ref=abilityref)
                datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["abilitylist"].update(abilitydict)
                a += 1

            invdict = henchman.inventory.to_dict(ref="inventory")
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref].update(invdict) # add new inventory dict to warband, practically replacing original value of inventory
        
            datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["inventory"]["itemlist"]={} # change in a dict before setting dict values
            i = 1
            for item in henchman.inventory.itemlist:
                itemref = "Item" + str(i) # to make sure it has a unique key
                # print(itemref)
                itemdict = item.to_dict(ref=itemref)
                datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["inventory"]["itemlist"].update(itemdict)
                i += 1

                datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["inventory"]["itemlist"][itemref]["abilitylist"]={} # change in a dict before setting dict values
                ia = 1
                for ability in item.abilitylist:
                    abilityref = "Ability" + str(ia) # to make sure it has a unique key
                    # print(abilityref)
                    abilitydict = ability.to_dict(ref=abilityref)
                    datadict["Warband"]["squadlist"][squadref]["henchmanlist"][henchmanref]["inventory"]["itemlist"][itemref]["abilitylist"].update(abilitydict)
                    ia += 1

    # Determine filepath of new save
    filepath = "database/saves/" + wbid.name + ".json"     
    # Save new warband to JSON file
    save_json(data=datadict, jsonfile=filepath)
    print("save completed")


if __name__ == "__main__":
    wbname = "Uthluan Wyrdbreakers"
    wbrace = "High Elves"
    test_createWarband(wbname, wbrace)