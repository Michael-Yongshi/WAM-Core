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
        ishero = True,
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
        ishero = True,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
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
        ishero = True,
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
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range."}, {"name": "Fear", "description": "Spreads fear in nearby enemies."}],
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
        abilitylist = [],
        magiclist = [],
        price = 0,
        description = "A basic dagger. Most units already carry one."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Dagger",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [],
        magiclist = [],
        price = 2,
        description = "A extra dagger. For units that want to dual wield daggers."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Sword",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Parry", "description": "Enables a single parry of an attackers hit. Parries when dicethrow is greater than attackers throw."}],
        magiclist = [],
        price = 10,
        description = "A basic Sword."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Spear",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "First Strike", "description":"Enables the wielder to always attack first, even when charged."}],
        magiclist = [],
        price = 15,
        description = "A basic Spear."
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Greatsword",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Last Strike", "description": "Disables the wielder to attack first, even when charging."}],
        magiclist = [],
        price = 15,
        description = "A very large sword that strikes slow but powerfull."
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
            {"name": "Concussion", "description": "Stunned happens also on a trow of 2 at the injury roll."}
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


