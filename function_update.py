from database.json import *
from hierarchy import * # reference to the hierarchic classes that are used, 
# like warband that consists of heroes and squads, that in turn reference to henchman


def test_updateWarband():
    # Open cached warband
    filepath = "database/saves/cache.json"
    datadict = open_json(filepath)

    wbname = datadict["Warband"]["name"]
    wbrace = datadict["Warband"]["race"]
    wbid = Warband(name=wbname, race=wbrace)
    # wbdatadict = datadict["Warband"]
    # wbid = Warband(**wbdatadict)

    # insert details of warband
    wbid.rulelist=[
            Rule(name="Excellent Sight", description="Elves have eyesight unmatched by mere humans. Elves spot Hidden enemies from two times as far away as other warriors (ie, twice their Initiative value in inches)."), 
            Rule(name="Haughty", description="The High Elves are a very proud and noble race. A High Elf Warband may never include hired swords that are not of High Elven blood, nor can they use any equipment of Dwarf origin. This includes Gromril weapons and armour."),
            Rule(name="Honourable", description="High Elves can never use poison or drugs of any kind no matter what the circumstance."),
            Rule(name="The Old Ways", description="The High Elves may never use black powder weapons of any sort. This goes against their ancestors and the traditions of the Old Ways."),
            Rule(name="Resolve", description="The High Elves have been fighting the Dark Elves for countless centuries. When fighting their dark kin the High Elves are driven by unwavering determination. They are considered to have a Leadership of 10 when taking Rout Tests against the Dark Elves. In addition, High Elves can never choose to voluntarily Rout as they must stop their evil kin at any cost.")
            ]

    # Get default starting gold
    wbid.inventory.gold = 500

    # Buying of heroes
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
        
     # Buying of henchman (groups)
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
    
    # Resolving gold expenses
    currentgold = wbid.inventory.gold
    wbid.inventory.gold = currentgold - wbid.get_warbandprice()

    datadict = wbid.to_dict()

    # Push save to JSON cache
    # To do: write to global variable
    save_json(data=datadict, jsonfile="database/saves/cache.json")
    print("Update completed")


if __name__ == "__main__":
    test_updateWarband()