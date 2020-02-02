from database.json import *
from class_hierarchy import *

def create_characterref():
    # Paths
    folderpath = "database/references/"
    filepath = folderpath + "characters_ref.json"

    # Create data file
    data = {}

    print(f"Created characterfile")
    save_json(data, filepath)


def add_characterref(race, source, category, ishero, skill, abilitylist, inventory, price, maxcount, description):
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

    data[race][source][category]={
        'race': race,
        'source': source,
        'category': category,
        'ishero': ishero,
        "skill": skill,
        'abilitylist': abilitylist,
        'inventory': inventory,
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
                print(f"Type:{name} does not exist")
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

    # Create data objects
    itemobject = Item(
        name = "Dagger",
        category = "Melee Weapon",
        distance = 0,
        skill = Skill(0,0,0,0,0,0,0,0,0),
        abilitylist = [Ability(name="Everything is Armour")],
        price = 2,
        desc = "A basic dagger. Everyone character starts with one, unless unable to." 
    )
    itemdict = itemobject.to_dict(itemobject.name)
    data["Core Rules"].update(itemdict)
    
    # data["Core Rules"]['Dagger'] = {
    #     'name': "Dagger",
    #     'category': 'Melee Weapon',
    #     'distance': 0,
    #     'skill': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     'abilitylist': ["Everything Is Armour"],
    #     'price': 2,
    #     'description': "A basic dagger where any character starts with"
    # }
    # data["Core Rules"]['Bow'] = {
    #     'category': 'Missile weapon',
    #     'distance': 16,
    #     'skill': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     'abilitylist': ["Everything Is Armour"],
    #     'price': 10,
    #     'description': 'A simple bow with a range of 16 inch'
    # }
    # data["Core Rules"]['Light Armour'] = {
    #     'category': 'Armour',
    #     'distance': 0,
    #     'skill': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #     'abilitylist': [],
    #     'price': 20,
    #     'description': 'Lightweight armour that provides a single armour save'
    # }

    print(f"Created itemfile")
    save_json(data, filepath)


def add_itemref(category, name, distance, skill, abilitylist, price, description, source="Manual"):
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

    # Add data
    data[source][name]={
        'category': category,
        'distance': distance,
        'skill': skill,
        'abilitylist': abilitylist,
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


if __name__ == "__main__":
    create_characterref()
    add_characterref(
        race = "High Elf",
        source = "High Elves",
        category = "Loremaster",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 9, 0],
        abilitylist = ["Excellent Sight"],
        inventory = [],
        price = 80,
        maxcount = 1,
        description = "Loremasters are the most powerful mages in the entire Warhammer world. Their knowledge of the arcane arts and their intensive training at the Tower of Hoeth makes them perfect for leading expeditions into Lustria. They are capable and efficient with years of extensive training and skill at their disposal. Loremasters alone command magic powerful enough to match the might of the mysterious Slann. They delve into the temple cities of the Lizardmen in search of any remaining artifacts of the Old Ones power."
    )
    add_characterref(
        race = "High Elf",
        source = "High Elves",
        category = "Ranger",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = ["Excellent Sight"],
        inventory = [],
        price = 45,
        maxcount = 2,
        description = "Elf Rangers are expert trackers and woodsman. Their keen eyesight and excellent archery skills help them to serve as the perfect lookouts. Rangers are more solitary then other High Elves and their quick decisiveness and ability to work on their own makes them invaluable elements of the Warband. Their skills alone have brought many expeditions back from the brink of death. They have saved countless Elven lives and continue to prove their worth in battle time and time again."
    )
    add_characterref(
        race = "High Elf",
        source = "High Elves",
        category = "Sword Warden",
        ishero = True,
        skill = [5, 5, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = ["Excellent Sight"],
        inventory = [],
        price = 50,
        maxcount = 2,
        description = "Sword Wardens are young Sword Masters in training recently sent out from the White Tower in order to better hone and refine their martial prowess. Though not as deadly as a full-fledged Sword Master, their skills are still beyond the understanding of ordinary Elves. In battle a Sword Warden wields his trademark Greatsword with effortless grace, dashing aside enemy missiles as he charges into combat. They are the elite warriors of the Warband and their lighting fast strikes have left many enemies lying dead at their feet. Sword Wardens serve as the Loremaster’s personal attendants and protectors."
    )
    add_characterref(
        race = "High Elf",
        source = "High Elves",
        category = "Seaguard",
        ishero = False,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = ["Excellent Sight"],
        inventory = [],
        price = 35,
        maxcount = 0,
        description = "Most Elven soldiery is called to arms only in times of great need, for there are too few Elves to maintain armies at all times. The Seaguard however, are always kept at strength and they retain a full-time contingent of warriors for this purpose. As a result they are better equipped and better trained then Citizen Levy Troops."
    )
    add_characterref(
        race = "High Elf",
        source = "High Elves",
        category = "Cadet",
        ishero = False,
        skill = [5, 3, 3, 3, 3, 1, 5, 1, 8, 0],
        abilitylist = ["Excellent Sight"],
        inventory = [],
        price = 30,
        maxcount = 5,
        description = "Cadets are young Citizen Levy of Ulthuan serving in the High Elf army for the first time. Their skills have yet to fully develop and most of them have yet to see battle. They are expert archers and travel light, thus making the perfect quick striking troops. Cadets are used primarily as scouts and are assigned the less important duties within the Citadel of Dusk and aboard High Elf Dragonships."
    )
    get_characterref(
        race = "High Elf",
        source = "High Elves",
        category = "Loremaster"
    )

    create_itemref()
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Sword of Khaine",
        distance = 5,
        skill = [0, 2, 0, 2, 0, 2, 0, 2, 2, 0],
        abilitylist = ["Dispel"],
        price = 999,
        description = "The sword of Khaine, when used at a range of maximum 5 inch use missile combat stats and process."
     )
    get_itemref(
        source = "Core Rules", 
        item = "Sword of Khaine"
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



# # (re-)creating a magic-ref json file
# data = {}
# data['magic_ref'] = []
# data['magic_ref'].append({
#     'name': 'Word of Power',
#     'restriction': 'High Elves',
#     'difficulty': '8',
#     'desc': 'The Elven Mage utters the True Name of Asuryan, the lord of the Elf gods. Shaken by his awesome power, the enemies of the Elves become weak and ineffective. Any enemies within 8 inch of the Mage suffer a -3 Weaponskill penalty, down to a minimum of one. Lasts until the beginning of the next High Elf turn.'
# })
# data['magic_ref'].append({
#     'name': 'Fiery Wrath',
#     'restriction': 'High Elves',
#     'difficulty': '8',
#     'desc': 'With one delicate movement the Elven Mage traces an intricate Sigil of Flame in the air. Range 12 inch. May be cast on any model within range. The target is hit with Strength 4. Any models within 3 inch of the target model suffer a Strength 3 hit on a D6 roll of 4+. Take armour saves as normal.'
# })
# data['magic_ref'].append({
#     'name': 'The Phoenix Crown',
#     'restriction': 'High Elves',
#     'difficulty': '9',
#     'desc': 'A crown of white flames appears above the head of the Elf Mage, enveloping him within a glorious array of flames. The Elf Mage has an armour save of 2+ that replaces his normal armour save. In addition, he gains a +2 to his Weaponskill and a +1 to his Strength. Roll at the beginning of each turn in the recovery phase. On a D6 roll of 1 or 2 the Phoenix Crown disappears.'
# })
# data['magic_ref'].append({
#     'name': 'Roar of the Dragon',
#     'restriction': 'High Elves',
#     'difficulty': '8',
#     'desc': 'A shadow of a wrathful Dragon strikes out from the outstretched hand of the mage, and speeds forward roaring its anger. The roar of the Dragon has a range of 12 inch and it is absolutely straight. Any model in its path must roll equal or under its Strength or be Knocked Down. If the spell hits a building it stops.'
# })
# data['magic_ref'].append({
#     'name': 'The Anger of the Earth',
#     'restriction': 'High Elves',
#     'difficulty': '10',
#     'desc': 'At the command of the Elven Mage, the very earth raises up against the enemies of the Elves. Draw a 12 inch direct line from the mage in any direction. The line is 1 inch wide and absolutely straight. Any model in its path suffers a single S5 hit.'
# })
# data['magic_ref'].append({
#     'name': 'The Light of Glory',
#     'restriction': 'High Elves',
#     'difficulty': '8',
#     'desc': 'A radiant white light emerges from the mage`s hand, banishing all fear and doubt in his comrades. Any friendly models within 8 inch of the Elven mage are immune to psychology and will never break from combat. This spell lasts until the mage suffers a wound. If the mage suffers a wound then the enchanted Elves become startled and uneasy. All models with 8 inch must take a Leadership test. If any fail, they are treated as if they had failed an All Alone test.'
# })

# with open('database/references/magic_ref.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)


