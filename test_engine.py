import datetime

from source.methods_engine import (
    save_warband,
    load_warband,
    show_warbands,
    load_reference,
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
    Event,
    )

def test_ReiklandWarband():
    print("---Start Test Reikland")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test Reikland",
        race = "Human",
        source = "Core Rules",
        warband =  "Reikland",
        )

    # Manually adding an item
    wbid.itemlist=[]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Mercenary Captain",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Halberd", category = "Melee Weapon", source = "Core Rules")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Hardened")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = []
    print("hero1 magic succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Swordsmen",
        race = "Human",
        source = "Core Rules",
        warband = "Reikland",
        category = "Swordsman",
        number = 3
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Marksmen",
        race = "Human",
        source = "Core Rules",
        warband = "Reikland",
        category = "Marksman",
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
    
    # Add another hero
    newhero = Hero.create_character(
        name = "Barend", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Champion"
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Ceasar", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Champion"
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Dan", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Champion"
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everest", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Champion"
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Frederik", 
        race = "Human", 
        source = "Core Rules",
        warband = "Reikland",
        category = "Youngblood"
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
        name = "Warrior",
        race = "Human",
        source = "Core Rules",
        warband = "Reikland",
        category = "Warrior",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Warrior2",
        race = "Human",
        source = "Core Rules",
        warband = "Reikland",
        category = "Warrior",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Marksmen3",
        race = "Human",
        source = "Core Rules",
        warband = "Reikland",
        category = "Marksman",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Marksmen4",
        race = "Human",
        source = "Core Rules",
        warband = "Reikland",
        category = "Marksman",
        number = 1
        )
    print("squad4 creation succesful")
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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






    # add experience
    hero = wbid.herolist[0]
    hero.experience = 0

    # should become level 1 with getting 2 exp
    hero.add_experience(2) 
    # check open advances and first one set new ability
    unprocessed_advances = hero.check_advance_events()
    if len(unprocessed_advances) == 0:
        print("No unprocessed advances")
    else:
        unprocessed_advances[0].set_advance_event(Skill.create_skill_empty(), "Being Awesome")
        print(f"level 1: {unprocessed_advances[0].description}")
        
    # add another 7 exp making the hero level 3
    hero.add_experience(5) # should become level 3

    # Check if the expected 2 advances pop up
    unprocessed_advances = hero.check_advance_events()
    if len(unprocessed_advances) != 2:
        print(f"incorrect total advances, expected 2 but got {len(unprocessed_advances)}")
    else:
        
        # Give advance 2 a strength increase
        unprocessed_advances[0].set_advance_event(Skill(0,0,0,1,0,0,0,0,0,0,), "")
        print(f"level up {unprocessed_advances[0].category} processed")
        print(f"{unprocessed_advances[0].description}")

        # Give advance 3 both a wounds increase as an action increase
        unprocessed_advances[1].set_advance_event(Skill(0,0,0,0,0,1,0,1,0,0,), "")
        print(f"level up {unprocessed_advances[1].category} processed")
        print(f"{unprocessed_advances[1].description}")


    print("")
    print("current advance: " + str(hero.get_advance()))
    print("Next advance: " + str(hero.get_nextadvance()))
    print("XP needed for next advance: " + str(hero.get_xpneeded()))
    print("Check if new advance is reached: " + str(hero.check_new_advance()))
    

    save_warband(wbid.to_dict())
    
    print("Update completed")

    wbdict = load_warband(wbid.name)
    # print(wbdict)

def test_WitchWarband():
    print("---Start Test Witch Hunters")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test Witch hunters",
        race = "Human",
        source = "Core Rules",
        warband =  "Witch Hunters",
        )

    # Manually adding an item
    wbid.itemlist=[]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Human", 
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Witch Hunter Captain",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Halberd", category = "Melee Weapon", source = "Core Rules")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Hardened")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = [
        Magic.create_magic(source = "Core Rules", category = "Prayers of Sigmar", name = "Shield of Faith")
    ]
    print("hero1 magic succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Swordsmen",
        race = "Human",
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Zealot",
        number = 3
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Marksmen",
        race = "Human",
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Flagellant",
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
    
    # Add another hero
    newhero = Hero.create_character(
        name = "Barend", 
        race = "Human", 
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Warrior Priest"
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Ceasar", 
        race = "Human", 
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Witch Hunter"
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Dan", 
        race = "Human", 
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Witch Hunter"
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everest", 
        race = "Human", 
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Witch Hunter"
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Frederik", 
        race = "Human", 
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Warrior Priest"
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
        name = "Warrior",
        race = "Human",
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Warhound",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Warrior2",
        race = "Human",
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Warhound",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Marksmen3",
        race = "Human",
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Warhound",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Marksmen4",
        race = "Human",
        source = "Core Rules",
        warband = "Witch Hunters",
        category = "Warhound",
        number = 1
        )
    print("squad4 creation succesful")
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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

    save_warband(wbid.to_dict())
    print("Update completed")


def test_CultWarband():
    print("---Start Test Cult")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test Cult",
        race = "Chaos Human",
        source = "Core Rules",
        warband =  "The Cult of the Possessed",
        )

    # Manually adding an item
    wbid.itemlist=[]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Magister",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Halberd", category = "Melee Weapon", source = "Core Rules")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Hardened")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = [
        Magic.create_magic(source = "Core Rules", category = "Chaos Rituals", name = "Lure of Chaos")
    ]
    print("hero1 magic succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Swordsmen",
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Darksoul",
        number = 3
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Marksmen",
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Brethren",
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
    
    # Add another hero
    newhero = Hero.create_character(
        name = "Barend", 
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Possessed"
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Ceasar", 
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Mutant"
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Dan", 
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Mutant"
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everest", 
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Mutant"
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Frederik", 
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Possessed"
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
        name = "Warrior",
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Beastman",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Warrior2",
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Beastman",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Marksmen3",
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Beastman",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Marksmen4",
        race = "Chaos Human",
        source = "Core Rules",
        warband = "The Cult of the Possessed",
        category = "Beastman",
        number = 1
        )
    print("squad4 creation succesful")
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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

    save_warband(wbid.to_dict())
    print("Update completed")

def test_SistersWarband():
    print("---Start Test Sisters")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test Sisters",
        race = "Human",
        source = "Core Rules",
        warband =  "Sisters of Sigmar",
        )

    # Manually adding an item
    wbid.itemlist=[]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Human", 
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sigmarite Matriarch",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Halberd", category = "Melee Weapon", source = "Core Rules")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Hardened")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = [
        Magic.create_magic(source = "Core Rules", category = "Prayers of Sigmar", name = "Soulfire")
    ]
    print("hero1 magic succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Swordsmen",
        race = "Human",
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister",
        number = 3,
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Marksmen",
        race = "Human",
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Novice",
        number = 1,
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

    # Add another hero
    newhero = Hero.create_character(
        name = "Barend", 
        race = "Human", 
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister Superior",
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Ceasar", 
        race = "Human", 
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister Superior",
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Dan", 
        race = "Human", 
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister Superior",
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everest", 
        race = "Human", 
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister Superior",
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Frederik", 
        race = "Human", 
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Augur",
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
        name = "Warrior",
        race = "Human",
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Warrior2",
        race = "Human",
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Sister",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Marksmen3",
        race = "Human",
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Novice",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Marksmen4",
        race = "Human",
        source = "Core Rules",
        warband = "Sisters of Sigmar",
        category = "Novice",
        number = 1
        )
    print("squad4 creation succesful")
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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

    save_warband(wbid.to_dict())
    print("Update completed")

def test_UndeadWarband():
    print("---Start Test Undead")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test Undead",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband =  "The Undead",
        )

    # Manually adding an item
    wbid.itemlist=[]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Necromancer",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Halberd", category = "Melee Weapon", source = "Core Rules")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Hardened")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = [
        Magic.create_magic(source = "Core Rules", category = "Necromancy", name = "Re-animation")
    ]
    print("hero1 magic succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Swordsmen",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Zombie",
        number = 3
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Marksmen",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Ghoul",
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
    
    # Add another hero
    newhero = Hero.create_character(
        name = "Barend", 
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Vampire"
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Ceasar", 
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dreg"
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Dan", 
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dreg"
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everest", 
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dreg"
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Frederik", 
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dreg"
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
        name = "Warrior",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dire Wolf",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Warrior2",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dire Wolf",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Marksmen3",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dire Wolf",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Marksmen4",
        race = "Undead / Vampires",
        source = "Core Rules",
        warband = "The Undead",
        category = "Dire Wolf",
        number = 1
        )
    print("squad4 creation succesful")
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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

    save_warband(wbid.to_dict())
    print("Update completed")


def test_SkavenWarband():
    print("---Start Test Skaven")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test Skaven",
        race = "Skaven",
        source = "Core Rules",
        warband =  "Skaven",
        )

    # Manually adding an item
    wbid.itemlist=[]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Anado", 
        race = "Skaven", 
        source = "Core Rules",
        warband = "Skaven",
        category = "Assessin Adept",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Halberd", category = "Melee Weapon", source = "Core Rules")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Hardened")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = [
        Magic.create_magic(source = "Core Rules", category = "Magic of the Horned Rat", name = "Warpfire")
    ]
    print("hero1 magic succesfull")

    # adding the heroes to the warband hero list
    wbid.herolist = [
        hero1
        ]
    print("hero1 assign succesfull")

    # Create Squads and the henchmen within
    squad1 = Squad.create_squad(
        name = "Swordsmen",
        race = "Skaven",
        source = "Core Rules",
        warband = "Skaven",
        category = "Verminkin",
        number = 3,
        )
    print("squad1 create succesfull")

    squad2 = Squad.create_squad(
        name = "Marksmen",
        race = "Skaven",
        source = "Core Rules",
        warband = "Skaven",
        category = "Giant Rats",
        number = 1,
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
    
    # Add another hero
    newhero = Hero.create_character(
        name = "Barend", 
        race = "Skaven", 
        source = "Core Rules",
        warband = "Skaven",
        category = "Eshin Sorcerer",
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Ceasar", 
        race = "Skaven", 
        source = "Core Rules",
        warband = "Skaven",
        category = "Black Skaven",
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Dan", 
        race = "Skaven", 
        source = "Core Rules",
        warband = "Skaven",
        category = "Night Runner",
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everest", 
        race = "Skaven", 
        source = "Core Rules",
        warband = "Skaven",
        category = "Night Runner",
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Frederik", 
        race = "Skaven", 
        source = "Core Rules",
        warband = "Skaven",
        category = "Night Runner",
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
        name = "Warrior",
        race = "Skaven",
        source = "Core Rules",
        warband = "Skaven",
        category = "Rat Ogre",
        number = 1
        )
    print("squad1 creation succesful")
    newsquad2 = Squad.create_squad(
        name = "Warrior2",
        race = "Skaven",
        source = "Core Rules",
        warband = "Skaven",
        category = "Rat Ogre",
        number = 1
        )
    print("squad2 creation succesful")
    newsquad3 = Squad.create_squad(
        name = "Marksmen3",
        race = "Skaven",
        source = "Core Rules",
        warband = "Skaven",
        category = "Rat Ogre",
        number = 1
        )
    print("squad3 creation succesful")
    newsquad4 = Squad.create_squad(
        name = "Marksmen4",
        race = "Skaven",
        source = "Core Rules",
        warband = "Skaven",
        category = "Rat Ogre",
        number = 1
        )
    print("squad4 creation succesful")
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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

    save_warband(wbid.to_dict())
    print("Update completed")

def test_HighElfWarband():
    print("---Start Test High Elf")

    # create_warband
    wbid = Warband.create_warband(
        name = "Test High Elf",
        race = "High Elf",
        source = "Broheim",
        warband =  "High Elves",
        )

    # Manually adding an item
    wbid.itemlist=[
        Item.create_item(source = "Broheim", category = "Other", subcategory = "Wyrdbreaker")
        ]
    
    # Creating heroes
    hero1 = Hero.create_character(
        name = "Hero A", 
        race = "High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category = "Loremaster",
        )
    print("hero1 create succesfull")

    # Adding items to heroes
    hero1.itemlist = [
        Item.create_item(subcategory = "Mage Quarter Staff", category = "Melee Weapon", source = "Broheim")
        ]
    print("hero1 item succesfull")

    # Adding abilities to heroes
    hero1.abilitylist = [
        Ability.create_ability(source = "Core Rules", category = "Injury", name = "Horrible Scars")
        ]
    print("hero1 ability succesfull")

    # Adding magic to heroes
    hero1.magiclist = [
        Magic.create_magic(source = "Broheim", category = "High Elven Magic", name = "The Light of Glory")
        ]
    print("hero1 magic succesfull")

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
    
    # Add another hero
    newhero = Hero.create_character(
        name = "Bearand", 
        race = "High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category = "Sword Warden"
        )
    print("hero1 creation succesful")
    newhero2 = Hero.create_character(
        name = "Crypton", 
        race = "High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category = "Sword Warden"
        )
    print("hero2 creation succesful")
    newhero3 = Hero.create_character(
        name = "Danan", 
        race = "High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category = "Ranger"
        )
    print("hero3 creation succesful")
    newhero4 = Hero.create_character(
        name = "Everia", 
        race = "High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category = "Ranger"
        )
    print("hero4 creation succesful")
    newhero5 = Hero.create_character(
        name = "Felicia", 
        race = "High Elf", 
        source = "Broheim",
        warband = "High Elves",
        category = "Ranger"
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
    
    newsquad4.change_henchman_count(5)
    print("squad4 change count succesful")
    
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

    save_warband(wbid.to_dict())
    print("Update completed")

if __name__ == "__main__":
    test_ReiklandWarband()
    # test_WitchWarband()
    # test_SistersWarband()
    # test_CultWarband()
    # test_UndeadWarband()
    # test_SkavenWarband()
    # test_HighElfWarband()
