from source.reference_methods import (
    create_warbandref,
    create_characterref,
    create_itemref,
    create_magicref,
    add_warbandref,
    add_characterref,
    add_itemref,
    add_magicref,
    get_warbandref,
    get_characterref,
    get_itemref,
    get_magicref,
)


if __name__ == "__main__":
    create_warbandref()
    
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Reikland",
        rulelist = [
            {"name": "Excellent Leadership", "description": "Reikland Mercenaries are accustomed to the demands of military discipline and have a strongly developed loyalty between officers and men. To represent this, fighters may use their Captain’s Leadership if within 12 inch rather than the usual 6 inch."}, 
            {"name": "Trained Marksmen", "description": "A strong tradition of martial training is also responsible for the high standards of archery amongst the people of Reikland. All Marksmen therefore start with 4 of Ballistic Skill instead of the normal 3, whether they are recruited when the warband is first formed or added later."}, 
        ],
        description = (
            "Reikland lies at the heart of the Empire and its greatest city is Altdorf, home of the Grand Theogonist and seat of the Temple of Sigmar. Reiklanders are devout followers of Sigmar, the founder, first Emperor, and patron god of the Empire."
            "The Grand Prince of Reikland (as Siegfried, the ruler of Reikland, styles himself) is supported in his claim to the throne by the Grand Theogonist and opposed most strongly by the Count of Middenheim and the Priests of Ulric."
            "Throughout the Empire Reiklanders are commonly supposed to embody the discipline and loyalty of the professional warrior. Brave and well-versed in the arts of war, Reiklanders disdain fashionable clothing in favour of well-made and practical wargear." 
            "In battle they often wear coloured ribbons as marks of identification or authority. They are justly proud of their dynamic and ambitious Grand Prince and contemptuous of other claimants to the throne, especially the Count of Middenheim, Mannfred Todbringer, whom they sneeringly call the ‘lap-dog of Ulric’."
            "<i>-Ah, Reiklanders, the finest of men! Disciplined, magnificent archers and good, solid warriors! Reiklanders need the best leaders, so you’d better shape up boy! For these warriors are good at almost all the skills of war, and they are more likely to hold their nerve than others in Mordheim.-</i>"
        ),
    )
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Middenheim",
        rulelist = [
            {"name": "Body Builders", "description": "The men of Middenheim are famous for their physical prowess. To represent their advantage in size and bulk, the Champions and Captains of a Middenheim warband start with Strength 4 instead of 3."}, 
        ],
        description = (
            "Middenheim stands on a mountain pinnacle surrounded by dark forest in the centre of Middenland, and is also known as the City of the White Wolf after Ulric, the old god of wolves and winter. The Priesthood of Ulric is still strong in Middenheim where Ulric is venerated as the patron of the city."
            "The tradition of rivalry between Middenheim and Reikland goes back hundreds of years, and the Count of Middenheim, Mannfred Todbringer, is one of the chief contenders for the Emperor’s throne. As a result there has always been a great deal of friction between Middenheimers and the Temple of Sigmar."
            "Middenheimers are typically large, strongly built men with a well deserved reputation for ferocity. Many wear wolf pelts which custom decrees to be the mark of those who have slain a wolf with their own hands. These grim warriors are famously contemptuous of danger."
            "They frequently go into battle bare-headed, scoffing at those who choose, for reasons of good sense, to wear helmets. As Middenheimers favour long hair and beards their lack of headgear makes them look especially fierce when they charge upon their enemies howling their brutal battle-cries."
            "<i>-These Northerners are nutters, madmen, berserkers! They are as strong as Ogres and meaner than Orcs. Watch out for them in close quarters – the chances are they’ll crush your skull with a hammer or behead you with one of those hefty axes they carry around with them.-</i>"
        ),
    )
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Marienburg",
        rulelist = [
            {"name": "Natural Traders", "description": "As natural traders with contacts in the merchant guilds Marienburg warbands receive a +1 bonus when attempting to find rare items (see the Trading section for rules). To reflect their enormous wealth Marienburgers start off with an extra 100 gold crowns (600 in total) when fighting in a campaign. In a one-off game they are permitted an extra 20 percent gold crowns when recruiting a warband. For example, in a 1,000 gold crown game a Marienburger warband will have 1,200gc."}, 
        ],
        description = (
            "Marienburg is the largest and most prosperous trading city in the Old World. Many call it the City of Gold which alone conveys a good idea of the wealth of this sprawling cosmopolitan city."
            "Nowhere else can be found the vast array of shops selling goods from as far away as the Elven kingdoms of Ulthuan in the west and distant Cathay in the east. The city’s craftsmen represent every skill known to man, and a few others beside, so that it is said in Marienburg there is no activity that cannot be quickly turned to profit."
            "Many mercantile guilds have their headquarters in Marienburg, most important of all the secretive High Order of Honourable Freetraders which represents the elite amongst mercantile society. This large, rich, and ambitious body of men feel themselves shackled by the old order and are eager to seize power for themselves."
            "Their champion for the Emperor’s throne is the Lady Magritta. Thanks to the unseen influence of Freetraders throughout the Empire all the minor Electors were persuaded to support the Lady Magritta’s claim. It was only the Grand Theogonist’s refusal to crown her that denied Marienburg the throne driving a wedge between the City of Gold and the Temple of Sigmar."
            "Warbands sent to Mordheim are sumptuously dressed and armed. Though Marienburgers are often ridiculed as foppish and effete, their skill at arms and complete ruthlessness has earned them grudging respect. Their chief skills lie in duelling and in the use of poisons and other clandestine fighting methods. Richer individuals dress flamboyantly and wear jewellery."
            "However, the bulk of most warbands are recruited from the dockland thugs, ships’ crews, and stevedores who favour a simpler appearance: leather coats, bandanas and short swords that are easy to conceal."
            "<i>-Don’t let their fancy clothes and flash jewellery fool you, though. They’re not wearing those weapons just for show, they know how to use them as well!-</i>"
        ),
    )
    add_warbandref(
        race = "Chaos Human",
        source = "Core Rules",
        name = "The Cult of the Possessed",
        rulelist = [],
        description = (
            "There is never any shortage of men willing to risk their lives for a chance of real power: men whose ambitions lie beyond the scope of their birthright, or whose sorcerous skills or physical deformities place them in constant danger of persecution. What do such men have to lose if they pledge their souls to the dark gods of Chaos!"
            "In the aftermath of the destruction of Mordheim all manner of mutants have appeared whilst many hitherto unblemished folk feel the stirring of strange powers, the first awakenings of magical gifts destined to bring them to a fiery death at the hands of the Witch Hunters. Now a leader has appeared, a new Dark Emperor, who claims lordship of the City of the Damned."
            "He is called the Shadowlord, Master of the Possessed, and followers of the cults of Chaos gather from all over the Empire to pledge their souls to him. Though none know whether he is man or Daemon all proclaim him their saviour and eagerly seek to do his bidding. As all students of the dark arts know, it is by the power of magic that creatures such as Daemons and spirits are able to stalk the mortal world."
            "The wyrdstone that proliferates in Mordheim grants unnatural life to many vile things that by all natural rights should never exist. The Possessed were once men but by surrendering themselves wholly to the dark gods they have allowed Daemons to possess their bodies. Their appearance is horrific – corrupted from within, their flesh is twisted into a new and monstrous form."
            "With the power of the Possessed behind them the followers of the Shadowlord have grown powerful in Mordheim. In the Massacre of Silver Street the Cult of the Possessed ambushed and destroyed a large force sent in to hunt them down. Now the streets of Mordheim belong to the Shadowlord and his servants. The contaminated air does not affect them at all or, more likely, it nourishes their inner corruption."
            "Men who venture into Mordheim alone are hunted down and sacrificed to the dark gods. All warbands of the Possessed gather wyrdstone for the Shadowlord who remains hidden in the Pit where he is said to be guarded by titanic Possessed the size of houses. A few shards of the precious stone are kept by the warbands and used to create more of the Possessed. Cult of the possessed."
            "The leaders of cult warbands are called Magisters and each leads a group of cultists: minions of the dark gods of Chaos. These are men whose hunger for power knows no bounds, who willingly give their bodies over to possession. All take part in the blood sacrifices, dark rituals, and worship of Daemons – nothing is too base for them!"
            "These degenerate humans are joined by other creatures as vile as they – things half-man half-beast that call themselves Gors, and which men refer to as Beastmen. There are few sights as horrific as a cult warband. Deranged warriors smeared with blood and dirt wave jagged weapons and chant blasphemous rites as they throw themselves upon their foes."
            "Many are hardly recognisable as human, their bodies are so scarred and disfigured. The stigmata of mutation is borne by most, but the most unsettling of all are the Possessed themselves – melded flesh made of men, beasts, and metal driven by the implacable will of a Daemon."
            "<i>-The Possessed. The Damned. The bogeymen. These scum are the worst of the worst. They are dangerous creatures, perhaps more so than any other group in the entire city. This Chaos-worshipping scum consists of mutants, Beastmen and cultists, and even worse things called the Possessed. If you ever let them get close to you, you’ll be in big trouble – there are few who are a match for this scum in close quarters.-</i>"
        ),
    )
    get_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Reikland",
    )
    create_characterref()
    # Add Reikland characters
    add_characterref(
        race = "Human",
        source = "Core Rules - Reikland",
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
        source = "Core Rules - Reikland",
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
        source = "Core Rules - Reikland",
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
        source = "Core Rules - Reikland",
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
        source = "Core Rules - Reikland",
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
        source = "Core Rules - Reikland",
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

    # Add Middenheim characters
    add_characterref(
        race = "Human",
        source = "Core Rules - Middenheim",
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
        source = "Core Rules - Middenheim",
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
        source = "Core Rules - Middenheim",
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
        source = "Core Rules - Middenheim",
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
        source = "Core Rules - Middenheim",
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
        source = "Core Rules - Middenheim",
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

    # Add Marienburg characters
    add_characterref(
        race = "Human",
        source = "Core Rules - Marienburg",
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
        source = "Core Rules - Marienburg",
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
        source = "Core Rules - Marienburg",
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
        source = "Core Rules - Marienburg",
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
        source = "Core Rules - Marienburg",
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
        source = "Core Rules - Marienburg",
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
    
    # Add the possessed
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Magister",
        ishero = True,
        skill = [4, 4, 4, 3, 3, 1, 3, 1, 8, 0],
        abilitylist = [
            {"name": "Leader", "description": "Any models in the warband within 6 inch of the Magister may use his Leadership instead of their own."},
            {"name": "Chaos Ritualist", "description": "The Magister is a wizard and uses Chaos Rituals. See the Magic section for details."},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 20,
        price = 70,
        maxcount = 1,
        description = "Magisters lead the covens of the Possessed. They have been granted magical powers by their patron gods. They are fanatical followers of the Dark gods, utterly dedicated to bringing Chaos to the world."
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Possessed",
        ishero = True,
        skill = [5, 4, 0, 4, 4, 2, 4, 2, 7, 0],
        abilitylist = [
            {"name": "Unarmed and Unarmoured", "description": "The Possessed never use weapons or armour."},
            {"name": "Fear", "description":" The Possessed are terrifying, twisted creatures and therefore cause fear. See the Psychology section for details."},
            {"name": "Mutations", "description": "Possessed may start the game with one or more mutations each. See the Mutations list over the page for costs."},        
        ],
        magiclist = [],
        itemlist = [],
        experience = 8,
        price = 90,
        maxcount = 2,
        description = "The Possessed have committed the greatest of heresies: they have given their bodies to Daemons. As a result, they are nightmarish creatures, a melding of flesh, metal and black magic. Inside them lives a supernatural thing of evil, a Daemon from the dark reaches of the Realm of Chaos."
        "The powerful spirit of a Daemon can meld several creatures together, be they men or animals, into a multi-faceted horror. These monstrous Possessed are perhaps the most dangerous of the creatures of Mordheim, and certainly the most loathsome and dreadful."
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Mutant",
        ishero = True,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Mutations", "description": "Mutants must start the game with one or more mutations each. See the Mutations list over the page for the cost."},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 25,
        maxcount = 2,
        description = "Mutants are revered as the favoured ones of the Dark gods, their physical disfigurements marking out the vileness of their soul. They come in many shapes and sizes, each more bizarre than the next."
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Darksoul",
        ishero = False,
        skill = [4, 2, 2, 4, 3, 1, 3, 1, 6, 0],
        abilitylist = [
            {"name": "Crazed", "description":"Darksouls have been driven insane by daemonic possession and know no fear. They automatically pass any Leadership tests they are required to take."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Darksouls are men who have been driven insane by the daemonic possession which became all too common after the destruction of Mordheim. The Daemons have left the bodies of these men, but their minds have been scarred by the horror of the experience. Their insane strength makes Darksouls dangerous fighters. The Cultists regard them as holy men, and let them work out their unreasoning rage in battle. In their tortured minds the Darksouls believe themselves to be Daemons. They wear leering daemonic masks and garb themselves in armour and clothing resembling the scaled skin of Daemons."
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Brethren",
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
        description = "Brethren are the crazed human followers of the cults of the dark gods, eager to descend into damnation. Their vile deeds and unspeakable acts have driven them to the brink of insanity."
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Beastman",
        ishero = False,
        skill = [4, 4, 3, 3, 4, 2, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one."}
        ],
        experience = 0,
        price = 45,
        maxcount = 3,
        description = "Beastmen are mutated monstrosities that infest the forests of the Empire: massive horned creatures with an inhuman resistance to pain. The destruction of Mordheim brought many Beastmen into the ruined city to prey upon the survivors. They readily ally with the Magisters of the Possessed warbands."
        )

    # High Elves characters from the other website
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Loremaster",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 9, 0],
        abilitylist = [
            {"name": "Excellent Sight", "description":"Spot hidden objects at double the range."},
            {"name": "High Elven Magician", "description":"Character is able to use High Elven magic."}
            ],
        magiclist = [],
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
        distance = 24,
        skill = [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        abilitylist = [],
        magiclist = [],
        price = 10,
        description = "The bow is carried by most races and used extensively in warfare. It is a compact yet powerful weapon, that is cheap to make and easy to maintain."
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
        description = "A long bow is made of alternating layers of either yew or elm. A skilled archer can hit a chosen leaf on a tree from three hundred paces with this weapon. The long bow is favored by experienced archers due to its great reach and accuracy."
    )
    add_itemref(
        source = "Core Rules",
        category = "Missile Weapon",
        name = "Elf Bow",
        distance = 36,
        skill = [0, 0, 0, 3, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Armour Piercing", "description": "An Elf bow has a -1 save modifier on armor saves against it"},
        ],
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
        description = "Light armor encompasses a wide variety of materials from hardened leather tunics to chain shirts forged from steel. It does not offer complete protection against arrows or swords, but it is better than having nothing at all. Light armor does not inhibit movement."
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Heavy Armour",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        abilitylist = [
            {"name": "Encumbered", "description": "A warrior that is armed with both heavy armor and a shield suffers a -1 Movement penalty."},
        ],
        magiclist = [],
        price = 50,
        description = "Typical heavy armor is made from metal links and is called chain mail. Forging chain mail is a laborious and time consuming process, as the blacksmith must put together hundreds, sometimes thousands, of metal links. This makes chain mail expensive, but this type of armor provides excellent protection for anyone who can afford it. There are other types of heavy armor as well, of which the best known are the steel breastplates and greaves worn by the foot knights of the Templar orders."
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Ithilmar Armour",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        abilitylist = [],
        magiclist = [],
        price = 90,
        description = "Ithilmar is a silvery metal which is as light as silk and stronger than steel. Elves are experts at fashioning weapons and armor from Ithilmar, and the Elven kingdom of Caledor is the only place in the world where this metal can be found. Ithilmar armor gives the wearer a 5+ basic save, and does not slow him down if he is also armed with a shield."
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Helmet",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Hardhead", "description": "A model that is equipped with a helmet has a special 4+ save on a D6 against being stunned. If the save is made, treat the stunned result as knocked down instead. This save is not modified by the opponent’s Strength."},
        ],
        magiclist = [],
        price = 10,
        description = "From the shining steel helmets of Bretonnian knights to the leather caps of the Skaven, all sensible warriors try to protect the most vulnerable part of their body – their head. Even the most vain fighters still use a helmet, as it can be festooned with plumes, horns and other decorations. Helmets come in varying shapes and sizes, but their basic function remains the same."
    )    
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Buckler",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Parry", "description": "Swords offer an excellent balance of defense and offence. A model armed with a sword may parry blows. When his opponent rolls to hit, the model armed with a sword may roll a D6. If the score is greater than the highest to hit score of his opponent, the model has parried the blow, and that attack is discarded. A model may not parry attacks made with double or more its own Strength – they are simply too powerful to be stopped."}],
        magiclist = [],
        price = 5,
        description = "Bucklers are small, round shields designed for parrying or deflecting blows. They are usually made of steel for they need to be tremendously durable to survive the brutal blows of hand-to-hand combat. Using a buckler requires great skill, but a nimble warrior can protect himself from blows which would otherwise cripple him."
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Shield",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        abilitylist = [],
        magiclist = [],
        price = 5,
        description = "There are two types of shield common to the warriors of Mordheim: the first is made of wood, occasionally reinforced with metal plates. This basic type of shield, although strong, does tend to splinter, but this can sometimes save the user’s life as his enemy’s weapon can get trapped allowing him to strike back whilst his enemy struggles to free his weapon. Metal shields are heavy and cumbersome, but last much longer and can take a battering. A typical Empire shield is either round or triangular, and carries the emblem of the province or city of its owner."
    )
    add_itemref(
        source = "Core Rules",
        category = "Consumables",
        name = "Elven Wine",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Fearless", "description": "An elven warband that drinks Elven Wine before a battle will be immune to Fear for the whole of the battle."}
        ],
        magiclist = [],
        price = 50,
        description = "High Elven wines are well known to be the best in the world, and some are even rumored to have magical qualities. A fine Elven Wine can cast out doubt and fear and leave a general feeling of wellbeing in a warrior."
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [],
        magiclist = [],
        price = 20,
        description = "Temporary item, When you buy a map, roll a D6. Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot."
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Fake Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Fake Mordheim Map", "description": "The map is a fake, and is completely worthless. It leads you on a fool’s errand. Your opponent may automatically choose the next scenario you play."}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot."
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Vague Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Vague Mordheim Map", "description": "Though crude, the map is generally accurate (well… parts of it are… perhaps!). You may re-roll any one dice during the next exploration phase if you wish but you must accept the result of the second roll."}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot."
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Catacomb Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Catacomb Mordheim Map", "description": "The map shows a way through the catacombs into the city. You may automatically choose the scenario next time you fight a battle."}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot."
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Accurate Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Accurate Mordheim Map", "description": "The map is recently made and very detailed. You may re-roll up to three dice during the next exploration phase if you wish. You must accept the result of the second roll."}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot."
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Master Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Master Mordheim Map", "description": "This is one of the twelve master maps of Mordheim made for Count von Steinhardt of Ostermark. From now on you may always re-roll one dice when rolling on the Exploration chart as long as the Hero who possesses this map was not taken out of action in the battle."}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot."
    )

    #  Specific Broheim - High Elves items
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
#     'restriction': 'High Elf, Loremaster',
#     'desc': 'A Loremaster’s knowledge of magic goes far beyond that of any other race. When an enemy spellcaster successfully casts a spell the Loremaster may attempt to dispel it. If the Loremaster rolls greater then his opponent’s casting roll for the spell then it is dispelled. Only the Loremaster may have this skill.'
# })
# data['abilities_ref'].append({
#     'name': 'Stand and Fire',
#     'restriction': 'High Elf',
#     'desc': 'If the Elf passes a leadership test he may choose to stand and fire at a charging opponent. The Elf suffers a –1 penalty to hit and may only fire once, at a single opponent. If his opponent is knocked down or stunned, place him halfway between the Elf and where he started from (or in view if he was out of sight).'
# })
# data['abilities_ref'].append({
#     'name': 'Miniath',
#     'restriction': 'High Elf',
#     'desc': 'The Elf has been trained in the martial art of the White Tower known as Miniath, allowing him to parry with any weapon. If he has a weapon that he can parry with he gains an additional parry attempt.'
# })
# data['abilities_ref'].append({
#     'name': 'Unerring Strike',
#     'restriction': 'High Elf',
#     'desc': 'The Elf is an expert at delivering deadly accurate blows. He may re-roll any failed to wound rolls.'
# })
# data['abilities_ref'].append({
#     'name': 'Fey Quickness',
#     'restriction': 'High Elf',
#     'desc': 'Few can ever hope to match an Elf’s inhuman quickness and agility. An Elf with Fey Quickness can avoid melee or missile attacks on a roll of 6. If the Elf also has Step Aside or Dodge this will increase to a 4+ in the relevant area. For example, an Elf with Fey Quickness and Step Aside avoids melee attacks on a 4+ and missile attacks on a 6.'
# })

# with open('database/references/abilities_ref.json', 'w') as outfile:
#     json.dump(data, outfile, indent=4)

