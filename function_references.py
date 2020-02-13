from database.json import (
    open_json,
    save_json,
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

def create_characterref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # Create data file
    data = {}

    print(f"Created characterfile")
    save_json(data, filepath)


def add_characterref(race, source, category, ishero, skill, abilitylist, magiclist, itemlist, experience, price, maxcount, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if race already exists
    if race in data:
        pass
    else:
        data[race] = {}

    # Second check if source already exists
    if source in data[race]:
        pass
    else:
        data[race][source] = {}

    skilldict = {
        "movement": skill[0],
        "weapon": skill[1],
        "ballistic": skill[2],
        "strength": skill[3],
        "toughness": skill[4],
        "wounds": skill[5],
        "initiative": skill[6],
        "actions": skill[7],
        "leadership": skill[8],
        "armoursave": skill[9]
        },

    data[race][source][category]={
        'race': race,
        'source': source,
        'category': category,
        'ishero': ishero,
        "skill": skilldict,
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'itemlist': itemlist,
        'experience': experience,
        'price': price,
        'maxcount': maxcount,
        'description': description
    }

    print(f"Added character: {category}")
    save_json(data, filepath)


def get_characterref(race, source, category):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if race exists
    if race in data:
        # Second check if source exists
        if source in data[race]:
            # Third check if character exists
            if category in data[race][source]: 
                characterdict = data[race][source][category]
            else:
                print(f"Type:{category} does not exist")
        else:
            print(f"source {source} does not exist")
    else:
        print(f"Race {race} does not exist")

    print(f"Here is data for {category}")
    print(characterdict)
    return characterdict




def create_itemref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "items_ref.json"

    # Create data file
    data = {}
    data["Core Rules"] = {}

    print(f"Created itemfile")
    save_json(data, filepath)


def add_itemref(category, name, distance, skill, abilitylist, magiclist, price, description, source="Manual"):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "items_ref.json"
    
    # open items_ref.json
    data = open_json(filepath)

    # First check if source already exists
    if source in data:
        pass
    else:
        data[source] = {}

    skilldict = {
        "movement": skill[0],
        "weapon": skill[1],
        "ballistic": skill[2],
        "strength": skill[3],
        "toughness": skill[4],
        "wounds": skill[5],
        "initiative": skill[6],
        "actions": skill[7],
        "leadership": skill[8],
        "armoursave": skill[9]
        },

    # Add data
    data[source][name]={
        'category': category,
        'distance': distance,
        'skill': skilldict,
        'abilitylist': abilitylist,
        'magiclist': magiclist,
        'price': price,
        'description': description
    }
   
    print(f"Added item: {name}")
    save_json(data, filepath)


def get_itemref(source, item):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "items_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if source exists
    if source in data:
        # Second check if item exists
        if item in data[source]: 
            itemdict = data[source][item]
        else:
            print(f"Item:{item} does not exist")
    else:
        print(f"Source {source} does not exist")

    print(f"Here is data for {item}")
    print(itemdict)
    return itemdict



def create_magicref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "magic_ref.json"

    # Create data file
    data = {}
    data["Core Rules"] = {}

    print(f"Created magicfile")
    save_json(data, filepath)


def add_magicref(source, category, name, difficulty, description):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "magic_ref.json"
    
    # open magics_ref.json
    data = open_json(filepath)

    # First check if source already exists
    if source in data:
        pass
    else:
        data[source] = {}

    # Second check if category already exists
    if category in data[source]:
        pass
    else:
        data[source][category] = {}

    # Add data
    data[source][category][name]={
        'difficulty': difficulty,
        'description': description
    }
   
    print(f"Added magic: {name}")
    save_json(data, filepath)


def get_magicref(source, category, name):
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "magic_ref.json"

    # open ref json
    data = open_json(filepath)

    # First check if source exists
    if source in data:
        if category in data[source]:
            # Third check if magic exists
            if name in data[source][category]: 
                magicdict = data[source][category][name]
            else:
                print(f"magic:{name} does not exist")
        else:
            print(f"Category: {category} does not exist")
    else:
        print(f"Source {source} does not exist")

    print(f"Here is data for {name}")
    print(magicdict)
    return magicdict


if __name__ == "__main__":
    create_characterref()
    # Add Reikland warband
    add_characterref(
        race = "Human",
        source = "Reikland",
        category = "Mercenary Captain",
        ishero = True,
        skill = [4, 4, 4, 3, 3, 1, 4, 1, 8, 0],
        abilitylist = [
            {"name": "Leader", "description":"Nearby units (12 inch) can use this characters leader skill"},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "A Mercenary Captain is a tough professional warrior, a man who will fight for anyone or against anything so long as the price is right. Mordheim offers such a man the chance to become rich beyond his dreams, though at great risk. But as ruthlessness and lack of mercy and pity are the hallmarks of a successful Mercenary Captain, it is no wonder that they flock to Mordheim."
        )
    add_characterref(
        race = "Human",
        source = "Reikland",
        category = "Champion",
        ishero = True,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 8,
        price = 35,
        maxcount = 2,
        description = "In any Mercenary warband there is one warrior who is bigger, stronger (and often uglier) than his comrades. These men are called Champions (or berserkers, first swordsmen and various other names). Champions are amongst the toughest and the best fighters in the warband. They often answer challenges issued to the warband and, after the Captain, they get the pick of any equipment and loot."
        )
    add_characterref(
        race = "Human",
        source = "Reikland",
        category = "Youngblood",
        ishero = True,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 6, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 15,
        maxcount = 2,
        description = "These are young fighters who are still inexperienced, but eager to win their spurs in the savage fighting in and around the ruins of Mordheim."
        )
    add_characterref(
        race = "Human",
        source = "Reikland",
        category = "Warrior",
        ishero = False,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "These dogs of war are grim, seasoned fighters, fearing no man as long as they have their weapons and armour. They form the core of any Mercenary warband."
        )
    add_characterref(
        race = "Human",
        source = "Reikland",
        category = "Marksman",
        ishero = False,
        skill = [4, 3, 4, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 7,
        description = "The archers and hunters of the Old World are famed for their skill, and it is said that they can hit a coin from 300 paces with a long bow. In the savage street fights of Mordheim they snipe at the enemy from the windows of ruined buildings and pick out enemy leaders with their arrows."
        )
    add_characterref(
        race = "Human",
        source = "Reikland",
        category = "Swordsman",
        ishero = False,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Expert Swordsmen", "description":"Swordsmen are so skilled with their weapons that they may re-roll any failed hits when charging. Note that this only applies when they are armed with normal swords, and not with doublehanded swords or any other weapons."},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Swordsmen are professional warriors, experts at taking on and beating several opponents at once. They are much sought after by warband leaders, as their skills are ideally suited for fighting in Mordheim."
        )

    # Add Middenheim warband
    add_characterref(
        race = "Human",
        source = "Middenheim",
        category = "Mercenary Captain",
        ishero = True,
        skill = [4, 4, 4, 4, 3, 1, 4, 1, 8, 0],
        abilitylist = [
            {"name": "Leader", "description":"Nearby units (6 inch) can use this characters leader skill"},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "A Mercenary Captain is a tough professional warrior, a man who will fight for anyone or against anything so long as the price is right. Mordheim offers such a man the chance to become rich beyond his dreams, though at great risk. But as ruthlessness and lack of mercy and pity are the hallmarks of a successful Mercenary Captain, it is no wonder that they flock to Mordheim."
        )
    add_characterref(
        race = "Human",
        source = "Middenheim",
        category = "Champion",
        ishero = True,
        skill = [4, 4, 3, 4, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 8,
        price = 35,
        maxcount = 2,
        description = "In any Mercenary warband there is one warrior who is bigger, stronger (and often uglier) than his comrades. These men are called Champions (or berserkers, first swordsmen and various other names). Champions are amongst the toughest and the best fighters in the warband. They often answer challenges issued to the warband and, after the Captain, they get the pick of any equipment and loot."
        )
    add_characterref(
        race = "Human",
        source = "Middenheim",
        category = "Youngblood",
        ishero = True,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 6, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 15,
        maxcount = 2,
        description = "These are young fighters who are still inexperienced, but eager to win their spurs in the savage fighting in and around the ruins of Mordheim."
        )
    add_characterref(
        race = "Human",
        source = "Middenheim",
        category = "Warrior",
        ishero = False,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "These dogs of war are grim, seasoned fighters, fearing no man as long as they have their weapons and armour. They form the core of any Mercenary warband."
        )
    add_characterref(
        race = "Human",
        source = "Middenheim",
        category = "Marksman",
        ishero = False,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 7,
        description = "The archers and hunters of the Old World are famed for their skill, and it is said that they can hit a coin from 300 paces with a long bow. In the savage street fights of Mordheim they snipe at the enemy from the windows of ruined buildings and pick out enemy leaders with their arrows."
        )
    add_characterref(
        race = "Human",
        source = "Middenheim",
        category = "Swordsman",
        ishero = False,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Expert Swordsmen", "description":"Swordsmen are so skilled with their weapons that they may re-roll any failed hits when charging. Note that this only applies when they are armed with normal swords, and not with doublehanded swords or any other weapons."},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Swordsmen are professional warriors, experts at taking on and beating several opponents at once. They are much sought after by warband leaders, as their skills are ideally suited for fighting in Mordheim."
        )

    # Add Marienburg warband
    add_characterref(
        race = "Human",
        source = "Marienburg",
        category = "Mercenary Captain",
        ishero = True,
        skill = [4, 4, 4, 3, 3, 1, 4, 1, 8, 0],
        abilitylist = [
            {"name": "Leader", "description":"Nearby units (6 inch) can use this characters leader skill"},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "A Mercenary Captain is a tough professional warrior, a man who will fight for anyone or against anything so long as the price is right. Mordheim offers such a man the chance to become rich beyond his dreams, though at great risk. But as ruthlessness and lack of mercy and pity are the hallmarks of a successful Mercenary Captain, it is no wonder that they flock to Mordheim."
        )
    add_characterref(
        race = "Human",
        source = "Marienburg",
        category = "Champion",
        ishero = True,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 8,
        price = 35,
        maxcount = 2,
        description = "In any Mercenary warband there is one warrior who is bigger, stronger (and often uglier) than his comrades. These men are called Champions (or berserkers, first swordsmen and various other names). Champions are amongst the toughest and the best fighters in the warband. They often answer challenges issued to the warband and, after the Captain, they get the pick of any equipment and loot."
        )
    add_characterref(
        race = "Human",
        source = "Marienburg",
        category = "Youngblood",
        ishero = True,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 6, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 15,
        maxcount = 2,
        description = "These are young fighters who are still inexperienced, but eager to win their spurs in the savage fighting in and around the ruins of Mordheim."
        )
    add_characterref(
        race = "Human",
        source = "Marienburg",
        category = "Warrior",
        ishero = False,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "These dogs of war are grim, seasoned fighters, fearing no man as long as they have their weapons and armour. They form the core of any Mercenary warband."
        )
    add_characterref(
        race = "Human",
        source = "Marienburg",
        category = "Marksman",
        ishero = False,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 7,
        description = "The archers and hunters of the Old World are famed for their skill, and it is said that they can hit a coin from 300 paces with a long bow. In the savage street fights of Mordheim they snipe at the enemy from the windows of ruined buildings and pick out enemy leaders with their arrows."
        )
    add_characterref(
        race = "Human",
        source = "Marienburg",
        category = "Swordsman",
        ishero = False,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Expert Swordsmen", "description":"Swordsmen are so skilled with their weapons that they may re-roll any failed hits when charging. Note that this only applies when they are armed with normal swords, and not with doublehanded swords or any other weapons."},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Swordsmen are professional warriors, experts at taking on and beating several opponents at once. They are much sought after by warband leaders, as their skills are ideally suited for fighting in Mordheim."
        )

    # High Elves warband from the other website
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Loremaster",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 9, 0],
        abilitylist = [
            {"name": "Excellent Sight", "description":"Spot hidden objects at double the range."},
            {"name": "High Elven Magic", "description":"Character is able to use High Elven magic."}
            ],
        magiclist = [
            {"source": "High Elves", "category": "High Elven Magic", "name": "Fiery Wrath", "difficulty": 8, "description": "With one delicate movement the Elven Mage traces an intricate Sigil of Flame in the air. Range 12 inch. May be cast on any model within range. The target is hit with Strength 4. Any models within 3 inch of the target model suffer a Strength 3 hit on a D6 roll of 4+. Take armour saves as normal."}
        ],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."},
            {"name": "Wyrdbreaker", "category": "Other", "source": "Core Rules", "distance": 0, "description": "test"},
        ],
        experience = 20,
        price = 80,
        maxcount = 1,
        description = "Loremasters are the most powerful mages in the entire Warhammer world. Their knowledge of the arcane arts and their intensive training at the Tower of Hoeth makes them perfect for leading expeditions into Lustria. They are capable and efficient with years of extensive training and skill at their disposal. Loremasters alone command magic powerful enough to match the might of the mysterious Slann. They delve into the temple cities of the Lizardmen in search of any remaining artifacts of the Old Ones power."
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Ranger",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range."}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 8,
        price = 45,
        maxcount = 2,
        description = "Elf Rangers are expert trackers and woodsman. Their keen eyesight and excellent archery skills help them to serve as the perfect lookouts. Rangers are more solitary then other High Elves and their quick decisiveness and ability to work on their own makes them invaluable elements of the Warband. Their skills alone have brought many expeditions back from the brink of death. They have saved countless Elven lives and continue to prove their worth in battle time and time again."
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Sword Warden",
        ishero = True,
        skill = [5, 5, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range."}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 11,
        price = 50,
        maxcount = 2,
        description = "Sword Wardens are young Sword Masters in training recently sent out from the White Tower in order to better hone and refine their martial prowess. Though not as deadly as a full-fledged Sword Master, their skills are still beyond the understanding of ordinary Elves. In battle a Sword Warden wields his trademark Greatsword with effortless grace, dashing aside enemy missiles as he charges into combat. They are the elite warriors of the Warband and their lighting fast strikes have left many enemies lying dead at their feet. Sword Wardens serve as the Loremaster’s personal attendants and protectors."
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Seaguard",
        ishero = False,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range."}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 35,
        maxcount = 0,
        description = "Most Elven soldiery is called to arms only in times of great need, for there are too few Elves to maintain armies at all times. The Seaguard however, are always kept at strength and they retain a full-time contingent of warriors for this purpose. As a result they are better equipped and better trained then Citizen Levy Troops."
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Cadet",
        ishero = False,
        skill = [5, 3, 3, 3, 3, 1, 5, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range."}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 30,
        maxcount = 5,
        description = "Cadets are young Citizen Levy of Ulthuan serving in the High Elf army for the first time. Their skills have yet to fully develop and most of them have yet to see battle. They are expert archers and travel light, thus making the perfect quick striking troops. Cadets are used primarily as scouts and are assigned the less important duties within the Citadel of Dusk and aboard High Elf Dragonships."
    )
    add_characterref(
        race = "High Elf",
        source = "Manual",
        category = "Khaine",
        ishero = True,
        skill = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        abilitylist = [
            {"name": "Excellent Sight", "description":"Spot hidden objects at double the range."}, {"name": "Fear", "description": "Spreads fear in nearby enemies."},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 100,
        price = 30,
        maxcount = 5,
        description = "Cadets are young Citizen Levy of Ulthuan serving in the High Elf army for the first time. Their skills have yet to fully develop and most of them have yet to see battle. They are expert archers and travel light, thus making the perfect quick striking troops. Cadets are used primarily as scouts and are assigned the less important duties within the Citadel of Dusk and aboard High Elf Dragonships."
    )
    get_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Loremaster"
    )

    create_itemref()
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Starting Dagger",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Enemy Armor Save", "description": "These weapons are not the best weapons to use for penetrating an enemy model’s armor. An enemy wounded by it gains a +1 bonus to his armor save, and a 6+ armor save if he has none normally."},
            ],
        magiclist = [],
        price = 0,
        description = "Daggers and knives are extremely common, and men are allowed to carry them in enclaves where weapons are otherwise forbidden. Many a warrior in Mordheim has died with a dagger in his back."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Extra Dagger",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Enemy Armor Save", "description": "These weapons are not the best weapons to use for penetrating an enemy model’s armor. An enemy wounded by it gains a +1 bonus to his armor save, and a 6+ armor save if he has none normally."},
            ],
        magiclist = [],
        price = 2,
        description = "A extra dagger. For units that want to dual wield daggers."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Club",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries."}],
        magiclist = [],
        price = 3,
        description = "Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Mace",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries."}],
        magiclist = [],
        price = 3,
        description = "Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Hammer",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Cutting Edge", "description": "An axe has an extra save modifier of -1, so a model with Strength 4 using an axe has a -2 save modifier when he hits an opponent in hand-to-hand combat."}],
        magiclist = [],
        price = 3,
        description = "Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Axe",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries."}],
        magiclist = [],
        price = 5,
        description = "The axe is the traditional weapon of Empire woodsmen, and is also used as a weapon in poorer rural areas. Axes have a heavy blade and, if swung by a strong man, can cause a lot of damage. The blade of an axe can easily cut through armor, though it requires considerable strength from the wielder. Of all the warriors in the Old World, Dwarfs are the most adept at making axes. Their axes are invaluable to the warriors of the Old World and are some of the most sought after weapons."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Sword",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Parry", "description": "Swords offer an excellent balance of defense and offence. A model armed with a sword may parry blows. When his opponent rolls to hit, the model armed with a sword may roll a D6. If the score is greater than the highest to hit score of his opponent, the model has parried the blow, and that attack is discarded. A model may not parry attacks made with double or more its own Strength – they are simply too powerful to be stopped."}],
        magiclist = [],
        price = 10,
        description = "The sword is often referred to as the ‘king of weapons’. The most common sword available, the broadsword of the Empire, is a masterpiece by the standards of any smith: four full feet of gleaming steel, double-edged and razor-sharp. Swords are much more effective weapons than crude clubs and axes, though learning to use a sword is a long and difficult process. It takes years to truly master this weapon – most warriors in Mordheim die long before they get this far!"
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Spear",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "First Strike", "description": "A warrior with a spear strikes first in the first turn of hand-to-hand combat."},
            {"name": "Unwieldy", "description": "A warrior with a spear may only use a shield or a buckler in his other hand. He may not use a second weapon."},
            {"name": "Cavalry Bonus", "description": "If using the rules for mounted models, a mounted warrior armed with a spear receives a +1 Strength bonus when he charges. This bonus only applies for that turn."},
        ],
        magiclist = [],
        price = 10,
        description = "Spears range from sharpened sticks used by Goblins to the impressive cavalry spears typical of the Elves."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Halberd",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Two Handed", "description":"A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting."}],
        magiclist = [],
        price = 10,
        description = "The halberd’s heavy blade is mounted upon a sturdy shaft of oak or steel and has a point like a spear and a cutting edge like an axe. Since it can be used to chop as well as thrust, it is an adaptable weapon, but is difficult to use inside buildings."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Great Sword",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Two Handed", "description": "A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting."},
            {"name": "Last Strike", "description": "These Double-handed weapons are so heavy that the model using them always strikes last, even when charging."},
            ],
        magiclist = [],
        price = 15,
        description = "A blow from a double-handed axe or sword can cut a foe in half and break armor apart. It takes a long time to learn how to use these weapons and even then only extremely strong men are able to wield them effectively."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Great Axe",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Two Handed", "description": "A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting."},
            {"name": "Last Strike", "description": "These Double-handed weapons are so heavy that the model using them always strikes last, even when charging."},
            ],
        magiclist = [],
        price = 15,
        description = "A blow from a double-handed axe or sword can cut a foe in half and break armor apart. It takes a long time to learn how to use these weapons and even then only extremely strong men are able to wield them effectively."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Flail",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Two Handed", "description": "A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting."},
            {"name": "Heavy", "description": "A flail is extremely tiring to use and thus the +2 Strength bonus applies only in the first turn of each hand-to-hand combat."},
            ],
        magiclist = [],
        price = 15,
        description = "The flail is a heavy weapon wielded with both hands. It normally consists of heavy weights, often spiked, attached to a pole or handle by means of heavy chains. Flails drain the user’s stamina quickly, but are awesomely destructive in the hands of a skilled (or unhinged) warrior."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Morning Star",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Difficult to Use", "description": "A model with a morning star may not use a second weapon or buckler in his other hand because it requires all his skill to wield it. He may carry a shield as normal though."},
            {"name": "Heavy", "description": "A flail is extremely tiring to use and thus the +1 Strength bonus applies only in the first turn of each hand-to-hand combat."},
            ],
        magiclist = [],
        price = 15,
        description = "The flail is a heavy weapon wielded with both hands. It normally consists of heavy weights, often spiked, attached to a pole or handle by means of heavy chains. Flails drain the user’s stamina quickly, but are awesomely destructive in the hands of a skilled (or unhinged) warrior."
        )
    add_itemref(
        source = "Core Rules",
        category = "Missile Weapon",
        name = "Bow",
        distance = 16,
        skill = [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        abilitylist = [],
        magiclist = [],
        price = 10,
        description = "A basic bow."
    )  
    add_itemref(
        source = "Core Rules",
        category = "Missile Weapon",
        name = "Long Bow",
        distance = 30,
        skill = [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        abilitylist = [],
        magiclist = [],
        price = 15,
        description = "A Long bow."
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Light Armour",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        abilitylist = [],
        magiclist = [],
        price = 20,
        description = "Some lightweighted armour."
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Shield",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        abilitylist = [],
        magiclist = [],
        price = 20,
        description = "A basic shield."
    )
     
    #  Specific Broheim - High Elves warband items
    add_itemref(
        source = "Broheim - High Elves",
        category = "Melee Weapon",
        name = "Mage Staff (One Handed)",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries."}
            ],
        magiclist = [],
        price = 20,
        description = "A staff used by mages."
        )
    add_itemref(
        source = "Broheim - High Elves",
        category = "Melee Weapon",
        name = "Mage Staff (Two Handed)",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Concussion", "description": "Stunned happens also on a trow of 2 at the injury roll."}
            ],
        magiclist = [],
        price = 20,
        description = "A staff used by mages."
        )

    get_itemref(
        source = "Broheim - High Elves", 
        item = "Mage Staff (One Handed)"
    )

    create_magicref()
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "Word of Power",
        difficulty = 8,
        description = "The Elven Mage utters the True Name of Asuryan, the lord of the Elf gods. Shaken by his awesome power, the enemies of the Elves become weak and ineffective. Any enemies within 8 inch of the Mage suffer a -3 Weaponskill penalty, down to a minimum of one. Lasts until the beginning of the next High Elf turn."
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "Fiery Wrath",
        difficulty = 8,
        description = "With one delicate movement the Elven Mage traces an intricate Sigil of Flame in the air. Range 12 inch. May be cast on any model within range. The target is hit with Strength 4. Any models within 3 inch of the target model suffer a Strength 3 hit on a D6 roll of 4+. Take armour saves as normal."
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "The Phoenix Crown",
        difficulty = 9,
        description = "A crown of white flames appears above the head of the Elf Mage, enveloping him within a glorious array of flames. The Elf Mage has an armour save of 2+ that replaces his normal armour save. In addition, he gains a +2 to his Weaponskill and a +1 to his Strength. Roll at the beginning of each turn in the recovery phase. On a D6 roll of 1 or 2 the Phoenix Crown disappears."
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "Roar of the Dragon",
        difficulty = 8,
        description = "A shadow of a wrathful Dragon strikes out from the outstretched hand of the mage, and speeds forward roaring its anger. The roar of the Dragon has a range of 12 inch and it is absolutely straight. Any model in its path must roll equal or under its Strength or be Knocked Down. If the spell hits a building it stops."
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "The Anger of the Earth",
        difficulty = 10,
        description = "At the command of the Elven Mage, the very earth raises up against the enemies of the Elves. Draw a 12 inch direct line from the mage in any direction. The line is 1 inch wide and absolutely straight. Any model in its path suffers a single S5 hit."
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "The Light of Glory",
        difficulty = 8,
        description = "A radiant white light emerges from the mage`s hand, banishing all fear and doubt in his comrades. Any friendly models within 8 inch of the Elven mage are immune to psychology and will never break from combat. This spell lasts until the mage suffers a wound. If the mage suffers a wound then the enchanted Elves become startled and uneasy. All models with 8 inch must take a Leadership test. If any fail, they are treated as if they had failed an All Alone test."
    )
    get_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name= "The Anger of the Earth"
    )


# # (re-)creating an abilities-ref json file
# data = {}
# data['abilities_ref'] = []
# data['abilities_ref'].append({
#     'name': 'High Sorcery',
#     'restriction': 'High Elves, Loremaster',
#     'desc': 'A Loremaster’s knowledge of magic goes far beyond that of any other race. When an enemy spellcaster successfully casts a spell the Loremaster may attempt to dispel it. If the Loremaster rolls greater then his opponent’s casting roll for the spell then it is dispelled. Only the Loremaster may have this skill.'
# })
# data['abilities_ref'].append({
#     'name': 'Stand and Fire',
#     'restriction': 'High Elves',
#     'desc': 'If the Elf passes a leadership test he may choose to stand and fire at a charging opponent. The Elf suffers a –1 penalty to hit and may only fire once, at a single opponent. If his opponent is knocked down or stunned, place him halfway between the Elf and where he started from (or in view if he was out of sight).'
# })
# data['abilities_ref'].append({
#     'name': 'Miniath',
#     'restriction': 'High Elves',
#     'desc': 'The Elf has been trained in the martial art of the White Tower known as Miniath, allowing him to parry with any weapon. If he has a weapon that he can parry with he gains an additional parry attempt.'
# })
# data['abilities_ref'].append({
#     'name': 'Unerring Strike',
#     'restriction': 'High Elves',
#     'desc': 'The Elf is an expert at delivering deadly accurate blows. He may re-roll any failed to wound rolls.'
# })
# data['abilities_ref'].append({
#     'name': 'Fey Quickness',
#     'restriction': 'High Elves',
#     'desc': 'Few can ever hope to match an Elf’s inhuman quickness and agility. An Elf with Fey Quickness can avoid melee or missile attacks on a roll of 6. If the Elf also has Step Aside or Dodge this will increase to a 4+ in the relevant area. For example, an Elf with Fey Quickness and Step Aside avoids melee attacks on a 4+ and missile attacks on a 6.'
# })

# with open('database/references/abilities_ref.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)


