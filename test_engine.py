import datetime

from wamcore.methods_engine import (
    save_warband,
    load_warband,
    show_warbands,
    )

from wamcore.class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from wamcore.class_components import (
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
        Ability.create_ability(source = "Core Rules", main = "Generic Ability", category = "Injury", name = "Hardened")
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
    squad1.buy_item(
        wbid = wbid, 
        item = Item(
            name = "Spear",
            subcategory = "Spear", 
            category = "Melee Weapon", 
            source = "Core Rules"
            )
        )
    print("squad1 item succesfull")

    squad2.buy_item(
        wbid = wbid, 
        item = Item(
            name = "Spear",
            subcategory = "Great Sword", 
            category = "Melee Weapon", 
            source = "Core Rules"
            )
        )
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
        category = "Youngblood"
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
    hero = wbid.herolist[5]
    hero.experience = 0

    # should become level 1 with getting 2 exp
    hero.add_experience(2) 
    # check open advances and first one set new ability
    unprocessed_advances = hero.get_tbd_advance_events()
    if len(unprocessed_advances) == 0:
        print("No unprocessed advances")
    else:
        unprocessed_advances[0].set_advance_event(Skill.create_skill_empty(), "Being Awesome")
        print(f"level 1: {unprocessed_advances[0].description}")
        
    print(f"current advance should be 1 - {hero.get_current_advance()}")
    
    # add another 7 exp making the hero level 3
    hero.add_experience(5) # should become level 3

    # Check if the expected 2 advances pop up
    unprocessed_advances = hero.get_tbd_advance_events()
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
    print("current advance: " + str(hero.get_current_advance()))
    print("Next advance: " + str(hero.get_next_advance()))
    print("XP needed for next advance: " + str(hero.get_xpneeded()))
    print("Check if new advance is reached: " + str(hero.get_new_advance()))
    print(hero.get_historystring())    

    save_warband(wbid.to_dict())
    
    print("Update completed")

    wbdict = load_warband(wbid.name)
    # print(wbdict)

if __name__ == "__main__":
    test_ReiklandWarband()

