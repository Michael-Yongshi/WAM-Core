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
            {"name": "Excellent Leadership", "description": "Reikland Mercenaries are accustomed to the demands of military discipline and have a strongly developed loyalty between officers and men. To represent this, fighters may use their Captain’s Leadership if within 12 inch rather than the usual 6 inch. "}, 
            {"name": "Trained Marksmen", "description": "A strong tradition of martial training is also responsible for the high standards of archery amongst the people of Reikland. All Marksmen therefore start with 4 of Ballistic Skill instead of the normal 3, whether they are recruited when the warband is first formed or added later. "}, 
        ],
        description = (
            "This is a time of unremitting war, civil strife, violence and famine. A time of orphan children and wanton slaughter. For warriors these are good times! Since the discovery of wyrdstone Mordheim has become a magnet for fighting men from all over the Empire. Nobles, merchants, and the Temple of Sigmar itself offer rich rewards for shards of the mysterious stone. "
            "Foremost amongst the patrons of mercenary warriors are the three most powerful contenders for the Emperor’s throne: the Grand Prince of Reikland, the Count of Middenheim, and Lady Magritta of Marienburg – favourite of the merchant guilds. As a mercenary warband you must decide which of the three contenders for Sigmar’s throne you are fighting for. "
            "Warbands from different places will vary in many respects, offering different benefits as well as having a unique appearance and character. "
            "Reikland lies at the heart of the Empire and its greatest city is Altdorf, home of the Grand Theogonist and seat of the Temple of Sigmar. Reiklanders are devout followers of Sigmar, the founder, first Emperor, and patron god of the Empire. "
            "The Grand Prince of Reikland (as Siegfried, the ruler of Reikland, styles himself) is supported in his claim to the throne by the Grand Theogonist and opposed most strongly by the Count of Middenheim and the Priests of Ulric. "
            "Throughout the Empire Reiklanders are commonly supposed to embody the discipline and loyalty of the professional warrior. Brave and well-versed in the arts of war, Reiklanders disdain fashionable clothing in favour of well-made and practical wargear. " 
            "In battle they often wear coloured ribbons as marks of identification or authority. They are justly proud of their dynamic and ambitious Grand Prince and contemptuous of other claimants to the throne, especially the Count of Middenheim, Mannfred Todbringer, whom they sneeringly call the ‘lap-dog of Ulric’. "
            "<i>-Ah, Reiklanders, the finest of men! Disciplined, magnificent archers and good, solid warriors! Reiklanders need the best leaders, so you’d better shape up boy! For these warriors are good at almost all the skills of war, and they are more likely to hold their nerve than others in Mordheim.-</i>"
        ),
    )
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Middenheim",
        rulelist = [
            {"name": "Body Builders", "description": "The men of Middenheim are famous for their physical prowess. To represent their advantage in size and bulk, the Champions and Captains of a Middenheim warband start with Strength 4 instead of 3. "}, 
        ],
        description = (
            "This is a time of unremitting war, civil strife, violence and famine. A time of orphan children and wanton slaughter. For warriors these are good times! Since the discovery of wyrdstone Mordheim has become a magnet for fighting men from all over the Empire. Nobles, merchants, and the Temple of Sigmar itself offer rich rewards for shards of the mysterious stone. "
            "Foremost amongst the patrons of mercenary warriors are the three most powerful contenders for the Emperor’s throne: the Grand Prince of Reikland, the Count of Middenheim, and Lady Magritta of Marienburg – favourite of the merchant guilds. As a mercenary warband you must decide which of the three contenders for Sigmar’s throne you are fighting for. "
            "Warbands from different places will vary in many respects, offering different benefits as well as having a unique appearance and character. "
            "Middenheim stands on a mountain pinnacle surrounded by dark forest in the centre of Middenland, and is also known as the City of the White Wolf after Ulric, the old god of wolves and winter. The Priesthood of Ulric is still strong in Middenheim where Ulric is venerated as the patron of the city. "
            "The tradition of rivalry between Middenheim and Reikland goes back hundreds of years, and the Count of Middenheim, Mannfred Todbringer, is one of the chief contenders for the Emperor’s throne. As a result there has always been a great deal of friction between Middenheimers and the Temple of Sigmar. "
            "Middenheimers are typically large, strongly built men with a well deserved reputation for ferocity. Many wear wolf pelts which custom decrees to be the mark of those who have slain a wolf with their own hands. These grim warriors are famously contemptuous of danger. "
            "They frequently go into battle bare-headed, scoffing at those who choose, for reasons of good sense, to wear helmets. As Middenheimers favour long hair and beards their lack of headgear makes them look especially fierce when they charge upon their enemies howling their brutal battle-cries. "
            "<i>-These Northerners are nutters, madmen, berserkers! They are as strong as Ogres and meaner than Orcs. Watch out for them in close quarters – the chances are they’ll crush your skull with a hammer or behead you with one of those hefty axes they carry around with them.-</i>"
        ),
    )
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Marienburg",
        rulelist = [
            {"name": "Natural Traders", "description": "As natural traders with contacts in the merchant guilds Marienburg warbands receive a +1 bonus when attempting to find rare items (see the Trading section for rules). To reflect their enormous wealth Marienburgers start off with an extra 100 gold crowns (600 in total) when fighting in a campaign. In a one-off game they are permitted an extra 20 percent gold crowns when recruiting a warband. For example, in a 1,000 gold crown game a Marienburger warband will have 1,200gc. "}, 
        ],
        description = (
            "This is a time of unremitting war, civil strife, violence and famine. A time of orphan children and wanton slaughter. For warriors these are good times! Since the discovery of wyrdstone Mordheim has become a magnet for fighting men from all over the Empire. Nobles, merchants, and the Temple of Sigmar itself offer rich rewards for shards of the mysterious stone. "
            "Foremost amongst the patrons of mercenary warriors are the three most powerful contenders for the Emperor’s throne: the Grand Prince of Reikland, the Count of Middenheim, and Lady Magritta of Marienburg – favourite of the merchant guilds. As a mercenary warband you must decide which of the three contenders for Sigmar’s throne you are fighting for. "
            "Warbands from different places will vary in many respects, offering different benefits as well as having a unique appearance and character. "
            "Marienburg is the largest and most prosperous trading city in the Old World. Many call it the City of Gold which alone conveys a good idea of the wealth of this sprawling cosmopolitan city. "
            "Nowhere else can be found the vast array of shops selling goods from as far away as the Elven kingdoms of Ulthuan in the west and distant Cathay in the east. The city’s craftsmen represent every skill known to man, and a few others beside, so that it is said in Marienburg there is no activity that cannot be quickly turned to profit. "
            "Many mercantile guilds have their headquarters in Marienburg, most important of all the secretive High Order of Honourable Freetraders which represents the elite amongst mercantile society. This large, rich, and ambitious body of men feel themselves shackled by the old order and are eager to seize power for themselves. "
            "Their champion for the Emperor’s throne is the Lady Magritta. Thanks to the unseen influence of Freetraders throughout the Empire all the minor Electors were persuaded to support the Lady Magritta’s claim. It was only the Grand Theogonist’s refusal to crown her that denied Marienburg the throne driving a wedge between the City of Gold and the Temple of Sigmar. "
            "Warbands sent to Mordheim are sumptuously dressed and armed. Though Marienburgers are often ridiculed as foppish and effete, their skill at arms and complete ruthlessness has earned them grudging respect. Their chief skills lie in duelling and in the use of poisons and other clandestine fighting methods. Richer individuals dress flamboyantly and wear jewellery. "
            "However, the bulk of most warbands are recruited from the dockland thugs, ships’ crews, and stevedores who favour a simpler appearance: leather coats, bandanas and short swords that are easy to conceal. "
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
            "In the aftermath of the destruction of Mordheim all manner of mutants have appeared whilst many hitherto unblemished folk feel the stirring of strange powers, the first awakenings of magical gifts destined to bring them to a fiery death at the hands of the Witch Hunters. Now a leader has appeared, a new Dark Emperor, who claims lordship of the City of the Damned. "
            "He is called the Shadowlord, Master of the Possessed, and followers of the cults of Chaos gather from all over the Empire to pledge their souls to him. Though none know whether he is man or Daemon all proclaim him their saviour and eagerly seek to do his bidding. As all students of the dark arts know, it is by the power of magic that creatures such as Daemons and spirits are able to stalk the mortal world. "
            "The wyrdstone that proliferates in Mordheim grants unnatural life to many vile things that by all natural rights should never exist. The Possessed were once men but by surrendering themselves wholly to the dark gods they have allowed Daemons to possess their bodies. Their appearance is horrific – corrupted from within, their flesh is twisted into a new and monstrous form. "
            "With the power of the Possessed behind them the followers of the Shadowlord have grown powerful in Mordheim. In the Massacre of Silver Street the Cult of the Possessed ambushed and destroyed a large force sent in to hunt them down. Now the streets of Mordheim belong to the Shadowlord and his servants. The contaminated air does not affect them at all or, more likely, it nourishes their inner corruption. "
            "Men who venture into Mordheim alone are hunted down and sacrificed to the dark gods. All warbands of the Possessed gather wyrdstone for the Shadowlord who remains hidden in the Pit where he is said to be guarded by titanic Possessed the size of houses. A few shards of the precious stone are kept by the warbands and used to create more of the Possessed. Cult of the possessed. "
            "The leaders of cult warbands are called Magisters and each leads a group of cultists: minions of the dark gods of Chaos. These are men whose hunger for power knows no bounds, who willingly give their bodies over to possession. All take part in the blood sacrifices, dark rituals, and worship of Daemons – nothing is too base for them!"
            "These degenerate humans are joined by other creatures as vile as they – things half-man half-beast that call themselves Gors, and which men refer to as Beastmen. There are few sights as horrific as a cult warband. Deranged warriors smeared with blood and dirt wave jagged weapons and chant blasphemous rites as they throw themselves upon their foes. "
            "Many are hardly recognisable as human, their bodies are so scarred and disfigured. The stigmata of mutation is borne by most, but the most unsettling of all are the Possessed themselves – melded flesh made of men, beasts, and metal driven by the implacable will of a Daemon. "
            "<i>-The Possessed. The Damned. The bogeymen. These scum are the worst of the worst. They are dangerous creatures, perhaps more so than any other group in the entire city. This Chaos-worshipping scum consists of mutants, Beastmen and cultists, and even worse things called the Possessed. If you ever let them get close to you, you’ll be in big trouble – there are few who are a match for this scum in close quarters.-</i>"
        ),
    )

# Mutations
# Cult of the possessed
# Mutations may be bought for a Mutant or a Possessed warrior only when they are recruited; you may not buy new mutations for a model after recruitment. Any Mutant or Possessed may have one or more mutations. The first mutation is bought at the price indicated, but second and subsequent mutations bought for the same model cost double.
# Those who dwell in Mordheim soon develop horrible mutations, and the Cult of the Possessed seem to be especially susceptible. In addition, Mordheim attracts mutants from all over the Empire, who are always quick to join the Chaos covens. Most mutations are simply inconvenient or hideous, but some make their bearers extremely dangerous in combat.
# daemon soul A Daemon lives within the mutant’s soul. This gives him a 4+ save against the effects of spells or prayers. Cost: 20 gold crowns. great claw One of the mutant’s arms ends in a great, crab-like claw. He may carry no weapons in this arm, but gains an extra attack in hand-to-hand combat with a +1 Strength bonus. Cost: 50 gold crowns. cloven hoofs The warrior gains +1 Movement. Cost: 40 gold crowns
# tentacle One of the mutant’s arms ends in a tentacle. He may grapple his opponent in close combat to reduce his attacks by -1, down to a minimum of 1. The mutant may decide which attack his opponent loses. Cost: 35 gold crowns blackblood If the model loses a wound in close combat, anyone in base contact with the model suffers a Strength 3 hit (no critical hits) from the spurting corrosive blood. Cost: 30 gold crowns spines Any model in base contact with the mutant suffers an automatic Strength 1 hit at the beginning of each close combat phase. Spines will never cause critical hits. Cost: 35 gold crowns scorpion tail The mutant has a long barbed tail with a venomed tip, allowing him to make an extra Strength 5 attack in each hand-to-hand combat phase. If the model hit by the tail is immune to poison, the Strength of the hit is reduced to 2. Cost: 40 gold crowns extra arm The mutant may use any single-handed weapon in the extra arm, giving him +1 attack when fighting in hand-to-hand combat. Alternatively, he may carry a shield or a buckler in the extra arm. If a Possessed chooses to do this, he gains an extra attack but still cannot carry a weapon. Cost: 40 gold crowns hideous The mutant causes fear. See the Psychology section for details. Cost: 40 gold crowns
    
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Witch Hunters",
        rulelist = [],
        description = (
            "The Order of the Templars of Sigmar, universally known as the Witch Hunters, is an organisation dedicated to the eradication of heretics, be they warlocks, witches, sorcerers, fortune-tellers, necromancers, worshippers of the dark gods, deviants, mutants, blasphemers, sinners, utterers of profanities, servants of Daemons, or composers of corrupting music. "
            "Indeed, there are few who altogether escape the suspicions of the Witch Hunters with the possible exception of other Witch Hunters. It is wise to remember that the practice of magic in all its forms is deemed a most heinous crime in the Empire. Death by fire is the proscribed punishment for this particular heresy. Many of the Witch Hunters’ victims treacherously avoid their fate by perishing under torture before making a full confession. "
            "In these troubled times the Witch Hunters are kept busy as more and more men turn to the dark arts. The most dangerous of all these heretics are the followers of the Chaos gods. These depraved individuals practise Daemon worship and (it is claimed) even offer human sacrifices in the name of their vile masters. Of all the enemies of Sigmar they are the most abhorrent! "
            "The destruction of Mordheim has fired the Witch Hunters with a new and irresistible sense of purpose. In the light of events the Grand Theogonist has proclaimed Sigmar’s punishment on the City of the Damned. The Witch Hunters rejoice that their crusade against widespread corruption has been vindicated. Now they are ready to complete Sigmar’s holy purpose by destroying his enemies within the ruins of the city itself. "
            "The Grand Theogonist has commanded the Witch Hunters to go unto that place and recover the wyrdstone for Sigmar’s temple. Their crusade also pits them into the same arena as their old enemies the so-called Sisters of Sigmar – those loathsome Daemon-worshipping she-heretics whose very existence is a vile affront to the majesty of Sigmar. Witch Hunters are charismatic rabble-rousers who can soon turn a crowd to their own ends. "
            "They are universally dreaded, for everyone has something or someone to hide, and there are countless individuals who would willingly and enthusiastically hunt down and burn their own kin were a Witch Hunter to command them to do so. Bands of Witch Hunters are often accompanied by zealous citizens, Flagellants, and even holy Priests of Sigmar as well as the huge vicious warhounds which the Witch Hunters employ to track and bring down fugitives. "
            "As men accustomed to fighting Witch Hunters are well-armed and sturdy individuals. They favour hooded cloaks and headgear which conceal their appearance from the overly curious. Some wear chains about their throats to remind them of fallen comrades and old rivalries and also, so it is said, so that the iron might serve as protection against witchcraft. "
            "The followers of the Witch Hunters, the rabble that accompany  them to Mordheim, are a far more dire sight indeed – crazed and self-mutilated men who have lost or surrendered all their worldly goods and, most likely, their reason as well."
            "<i>-Witch Hunters will burn you and your warband if you give them the slightest reason. They are well armed and equipped, and show no mercy to anyone who dares to stand in their way. They are followed everywhere in Mordheim by a rabble of fanatics and those crazed Flagellants. One word from a Witch Hunter and they’ll tear you apart, burn you, decapitate you and excommunicate you from the grace of Sigmar.-</i>"
        ),
    )
    add_warbandref(
        race = "Human",
        source = "Core Rules",
        name = "Sisters of Sigmar",
        rulelist = [],
        description = (
            "For centuries the nobility of the Empire has sent its wayward or troublesome daughters to the Holy Convent of the Order of Merciful Sisters of Sigmar in Mordheim to be initiated into the only order of priestesses dedicated to the Empire’s patron god. The Sisters of Sigmar, as they are commonly called, have traditionally travelled the Empire administering to the sick and poor, tending to the needs of orphans, curing the diseased and mending broken bodies. "
            "As well as the healing arts, which they practise with expert knowledge of herb-lore and prayer, their advice is frequently sought by those about to make an important decision, for the Sisters of Sigmar are famed for their ability to predict the fickle course of fate. Though once much loved by the common people, the Sisters have seen their popularity wane in recent years. "
            "Rabble-rousing Witch Hunters have denounced them as witches and heretics, so that even in the countryside they are attacked and driven away by the very peasants they seek to help. Many of Sigmar’s priests wish to disband the order altogether, claiming that women have no right to teach the holy word of Sigmar. "
            "Even the Grand Theogonist, ostensibly the chief authority over the order, has cooled towards the sisterhood, denying the throne to Magritta of Marienburg who was brought up by the Sisters and said to be sympathetic to their cause. These days the Sisters of Sigmar have retreated to their convent situated high on the craggy island of Sigmar’s Rock in the river Stir in Mordheim. "
            "Of all the inhabitants of Mordheim only the Sisters of Sigmar were prepared for its destruction. Seeress Cassandora foretold of the disaster and at their nightly vigil the Maidens of Sigmar heard the voice of Sigmar speaking in their dreaming minds. "
            "Thus they knew that they would be safe in their fortress high above the city, raised as it is above the polluted vapours, if only they were prepared to survive the fire of Sigmar’s Fury. While the rest of Mordheim fell under a spell of madness the Sisters of Sigmar offered prayer after prayer, scourging themselves to drive out all thoughts of sin, fervently accepting a punishing penitential regime to harden their minds against the wantonness running rampant outside their walls. "
            "When the blow finally came the Sisters gathered beneath the great temple dome of their convent which, well built and fortified as it was by the prayers of the Sisters, protected them from the fire and heat of their master’s ire. "
            "The Sisters believe they have a holy mission, a task that they have been set by Sigmar himself and to which they must submit themselves body and soul. Their sacred duty is to gather up the shards of wyrdstone and hide it deep beneath Sigmar’s Rock in the vaults of their convent where, shielded by a great depth of solid granite and guarded by the eternal prayers of the sisterhood, it will cause no harm to Sigmar’s people. "
            "It is a nigh hopeless task, for there are few Sisters and countless shards of stone. Worse still, there are many who want the stone for themselves, to take it from Mordheim and spread its contagion amongst the cities of the Empire.  The warbands of the sisterhood are led by tough Matriarchs, each accompanied by a body of warrior sisters. "
            "The training and harsh discipline of the convent includes mastery of martial as well as ecclesiastic skills, for mastery of the body is but the first step towards the mastery of the soul. Their favoured weapon is the warhammer, the instrument of Sigmar, seen as his holy symbol, alongside the twintailed comet."
            "<i>-Don’t believe everything those Witch Hunters say about the Sisters. They’re no more heretics than I am and I’ll skewer any man that says different. Not that the Sisters need looking after – they’re mean fighters and you gotta be tough just to live like they do in that big fortress in the middle of Mordheim.-</i>"
        ),
    )
    add_warbandref(
        race = "Undead / Vampires",
        source = "Core Rules",
        name = "The Undead",
        rulelist = [],
        description = (
            "Count Vlad von Carstein and his wife Isabella have ruled the province of Sylvania for as long as anyone can remember – peasants whisper of some dark secret, Witch Hunters revile them, and the Priests of Sigmar shun their court. Indeed, Sylvania has the most dire reputation of all the provinces of the Empire. "
            "Few men sent to spy on the rulers of Sylvania have ever returned from those dark Sylvanian forests, and then rarely with their sanity intact. In the dimly-lit chamber of the Drakenhof castle, on a throne of black obsidian, sits Vlad von Carstein, the ruler of Sylvania. He waits in shadows, having set himself apart from the politics and bickering of the Empire. "
            "For he holds a terrible secret: he, and all the ruling aristocracy of his province are Vampires, undying monsters from beyond the grave. Here he patiently waits, drinking the blood of maidens from gold goblets. For many long years Vlad has gathered his strength and mustered his Undead legions in secrecy. "
            "One day soon he will march from the forests of Sylvania at the head of an army of restless dead. The pieces of magic stone that lie scattered among the ruins of Mordheim can give the Count the power to challenge the nobles of the Empire and enslave the men of the Old World. "
            "Wyrdstone holds enough captured magical energy to unleash a great spell of doom to rival that of Nagash the Black. If the Count is successful, he will raise all the dead between the Worlds Edge Mountains and the borders of Stirland, and go to war against the divided rulers of the Empire. "
            "His plans laid out, Vlad sends his thralls, the immortal Vampires, to do his bidding. During dark, moonless nights, black coaches arrive at the gates of Mordheim carrying coffins. Ghouls scuttle from their hiding places to greet them, and corpses are stirred by a command which the living cannot hear. Following the commands of the Vampire, they hunt for shards of wyrdstone. The night belongs to the Undead, and in Mordheim it is always night. "
            "<i>-The Restless Dead plague Mordheim. Zombies, Ghouls and huge hellhounds prowl the streets, and woe to anyone caught by them. He’ll be eaten alive, or end up as one of the walking corpses himself. I lost my eye to one of the fanged horrors who leads the Undead. Let me tell you, that thing was not human. I put my sword through it and it still kept coming.-</i>"
        ),
    )
    add_warbandref(
        race = "Skaven",
        source = "Core Rules",
        name = "Skaven",
        rulelist = [],
        description = (
            "Unbeknownst to man, for thousands of years he has shared his world with another and altogether different race. There have always been signs for those who cared to see them: a scurrying black shadow, an inhuman scream from the sewer, scuttling shapes at the back of the cellar. All these years these creatures have worked away in secret, burrowing beneath the world of man, undermining his great cities, infiltrating his sewers and cellars, and joining all up into a vast worldspanning labyrinth of tunnels and nests. "
            "These creatures call themselves Skaven and they are ratmen, the mutant spawn of an older age of chaos and mutation. Doubtless one day the Skaven will be ready to emerge from their tunnels and wage open war upon mankind. For centuries they have been content to feed upon his ruins, to seed plague in his cities, and spread contagion amongst his lands. At least they were content to wait and watch, for now everything has suddenly changed. "
            "Now the destruction of Mordheim has created new opportunities in the secret war against mankind. Since ancient times the Skaven have searched the world for the stones of power that men in their ignorance call wyrdstone but which Skaven have long since known as warpstone, blackstone, or seerstone. "
            "It was as a result of gnawing upon this magic stone in ages past that commonplace rats began the slow process of mutation that spawned the Skaven race. Wyrdstone is quite literally in their blood, for they feed upon it and make use of it in their foul sorceries. "
            "Until now the ratmen’s search for wyrdstone has been difficult and time-consuming as the stone has grown increasingly rare, but now a new and abundant source has appeared – a dark blessing from the skies! For the Skaven of Clan Eshin, this is an especially opportune time for such a thing to happen, for, just as the Empire is divided, so the Skaven race is divided amongst itself. "
            "Clan fights clan the world over, each struggling for domination of the Council of Thirteen whose masters rule the Skaven race. Mordheim’s secret is not yet revealed to all the clans, or else the City of the Damned would already be overrun with ratmen. The Nightmaster of Clan Eshin is keen to guard this secret, and for this reason has not sent his multitudinous armies into Mordheim. "
            "Instead, he has sent small warbands of Skaven skittering through secret tunnels into the city to gather up the shining stones and bring them back to the clan nests. The Skaven of Clan Eshin are supremely adapted to their task. Masters of the art of bringing silent death to their foes, they are skilled in the use of poison and trained in the thousand secrets of the assassin. "
            "Since birth Skaven warriors practise martial crafts in the ruinous temples of the Horned Rat, their everhungering and hideous god. There are none better amongst their verminous kind to gather up the treasure of Mordheim, but they must be silent, swift and efficient. Were rival Skaven clans to discover the secret of Mordheim there would come not hundreds, not thousands, but millions upon millions to contend for the wyrdstone in the City of the Damned."
            "<i>-These are no ordinary vermin - big as a man, fast on their feet, and smart too, not like common rats. The whole city’s full of ’em and the worse of it is they’re waitin’ in the old drains and sewers, watchin’ for a chance to catch you on your own. Let ’em and you’re a dead man.-</i>"
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "A Mercenary Captain is a tough professional warrior, a man who will fight for anyone or against anything so long as the price is right. Mordheim offers such a man the chance to become rich beyond his dreams, though at great risk. But as ruthlessness and lack of mercy and pity are the hallmarks of a successful Mercenary Captain, it is no wonder that they flock to Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 35,
        maxcount = 2,
        description = "In any Mercenary warband there is one warrior who is bigger, stronger (and often uglier) than his comrades. These men are called Champions (or berserkers, first swordsmen and various other names). Champions are amongst the toughest and the best fighters in the warband. They often answer challenges issued to the warband and, after the Captain, they get the pick of any equipment and loot. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 15,
        maxcount = 2,
        description = "These are young fighters who are still inexperienced, but eager to win their spurs in the savage fighting in and around the ruins of Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "These dogs of war are grim, seasoned fighters, fearing no man as long as they have their weapons and armour. They form the core of any Mercenary warband. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 7,
        description = "The archers and hunters of the Old World are famed for their skill, and it is said that they can hit a coin from 300 paces with a long bow. In the savage street fights of Mordheim they snipe at the enemy from the windows of ruined buildings and pick out enemy leaders with their arrows. "
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Reikland",
        category = "Swordsman",
        ishero = False,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Expert Swordsmen", "description":"Swordsmen are so skilled with their weapons that they may re-roll any failed hits when charging. Note that this only applies when they are armed with normal swords, and not with doublehanded swords or any other weapons. "},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Swordsmen are professional warriors, experts at taking on and beating several opponents at once. They are much sought after by warband leaders, as their skills are ideally suited for fighting in Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "A Mercenary Captain is a tough professional warrior, a man who will fight for anyone or against anything so long as the price is right. Mordheim offers such a man the chance to become rich beyond his dreams, though at great risk. But as ruthlessness and lack of mercy and pity are the hallmarks of a successful Mercenary Captain, it is no wonder that they flock to Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 35,
        maxcount = 2,
        description = "In any Mercenary warband there is one warrior who is bigger, stronger (and often uglier) than his comrades. These men are called Champions (or berserkers, first swordsmen and various other names). Champions are amongst the toughest and the best fighters in the warband. They often answer challenges issued to the warband and, after the Captain, they get the pick of any equipment and loot. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 15,
        maxcount = 2,
        description = "These are young fighters who are still inexperienced, but eager to win their spurs in the savage fighting in and around the ruins of Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "These dogs of war are grim, seasoned fighters, fearing no man as long as they have their weapons and armour. They form the core of any Mercenary warband. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 7,
        description = "The archers and hunters of the Old World are famed for their skill, and it is said that they can hit a coin from 300 paces with a long bow. In the savage street fights of Mordheim they snipe at the enemy from the windows of ruined buildings and pick out enemy leaders with their arrows. "
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Middenheim",
        category = "Swordsman",
        ishero = False,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Expert Swordsmen", "description":"Swordsmen are so skilled with their weapons that they may re-roll any failed hits when charging. Note that this only applies when they are armed with normal swords, and not with doublehanded swords or any other weapons. "},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Swordsmen are professional warriors, experts at taking on and beating several opponents at once. They are much sought after by warband leaders, as their skills are ideally suited for fighting in Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "A Mercenary Captain is a tough professional warrior, a man who will fight for anyone or against anything so long as the price is right. Mordheim offers such a man the chance to become rich beyond his dreams, though at great risk. But as ruthlessness and lack of mercy and pity are the hallmarks of a successful Mercenary Captain, it is no wonder that they flock to Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 35,
        maxcount = 2,
        description = "In any Mercenary warband there is one warrior who is bigger, stronger (and often uglier) than his comrades. These men are called Champions (or berserkers, first swordsmen and various other names). Champions are amongst the toughest and the best fighters in the warband. They often answer challenges issued to the warband and, after the Captain, they get the pick of any equipment and loot. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 15,
        maxcount = 2,
        description = "These are young fighters who are still inexperienced, but eager to win their spurs in the savage fighting in and around the ruins of Mordheim. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "These dogs of war are grim, seasoned fighters, fearing no man as long as they have their weapons and armour. They form the core of any Mercenary warband. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 7,
        description = "The archers and hunters of the Old World are famed for their skill, and it is said that they can hit a coin from 300 paces with a long bow. In the savage street fights of Mordheim they snipe at the enemy from the windows of ruined buildings and pick out enemy leaders with their arrows. "
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Marienburg",
        category = "Swordsman",
        ishero = False,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Expert Swordsmen", "description":"Swordsmen are so skilled with their weapons that they may re-roll any failed hits when charging. Note that this only applies when they are armed with normal swords, and not with doublehanded swords or any other weapons. "},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Swordsmen are professional warriors, experts at taking on and beating several opponents at once. They are much sought after by warband leaders, as their skills are ideally suited for fighting in Mordheim. "
        )
    
    # Add the possessed
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Magister",
        ishero = True,
        skill = [4, 4, 4, 3, 3, 1, 3, 1, 8, 0],
        abilitylist = [
            {"name": "Leader", "description": "Any models in the warband within 6 inch of the Magister may use his Leadership instead of their own. "},
            {"name": "Chaos Ritualist", "description": "The Magister is a wizard and uses Chaos Rituals. See the Magic section for details. "},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 70,
        maxcount = 1,
        description = "Magisters lead the covens of the Possessed. They have been granted magical powers by their patron gods. They are fanatical followers of the Dark gods, utterly dedicated to bringing Chaos to the world. "
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Possessed",
        ishero = True,
        skill = [5, 4, 0, 4, 4, 2, 4, 2, 7, 0],
        abilitylist = [
            {"name": "Unarmed and Unarmoured", "description": "The Possessed never use weapons or armour. "},
            {"name": "Fear", "description":" The Possessed are terrifying, twisted creatures and therefore cause fear. See the Psychology section for details. "},
            {"name": "Mutations", "description": "Possessed may start the game with one or more mutations each. See the Mutations list over the page for costs. "},        
        ],
        magiclist = [],
        itemlist = [],
        experience = 8,
        price = 90,
        maxcount = 2,
        description = "The Possessed have committed the greatest of heresies: they have given their bodies to Daemons. As a result, they are nightmarish creatures, a melding of flesh, metal and black magic. Inside them lives a supernatural thing of evil, a Daemon from the dark reaches of the Realm of Chaos. "
        "The powerful spirit of a Daemon can meld several creatures together, be they men or animals, into a multi-faceted horror. These monstrous Possessed are perhaps the most dangerous of the creatures of Mordheim, and certainly the most loathsome and dreadful. "
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Mutant",
        ishero = True,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Mutations", "description": "Mutants must start the game with one or more mutations each. See the Mutations list over the page for the cost. "},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 2,
        description = "Mutants are revered as the favoured ones of the Dark gods, their physical disfigurements marking out the vileness of their soul. They come in many shapes and sizes, each more bizarre than the next. "
        )
    add_characterref(
        race = "Chaos Human",
        source = "Core Rules - The Cult of the Possessed",
        category = "Darksoul",
        ishero = False,
        skill = [4, 2, 2, 4, 3, 1, 3, 1, 6, 0],
        abilitylist = [
            {"name": "Crazed", "description":"Darksouls have been driven insane by daemonic possession and know no fear. They automatically pass any Leadership tests they are required to take. "},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 35,
        maxcount = 5,
        description = "Darksouls are men who have been driven insane by the daemonic possession which became all too common after the destruction of Mordheim. The Daemons have left the bodies of these men, but their minds have been scarred by the horror of the experience. Their insane strength makes Darksouls dangerous fighters. The Cultists regard them as holy men, and let them work out their unreasoning rage in battle. In their tortured minds the Darksouls believe themselves to be Daemons. They wear leering daemonic masks and garb themselves in armour and clothing resembling the scaled skin of Daemons. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "Brethren are the crazed human followers of the cults of the dark gods, eager to descend into damnation. Their vile deeds and unspeakable acts have driven them to the brink of insanity. "
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
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 45,
        maxcount = 3,
        description = "Beastmen are mutated monstrosities that infest the forests of the Empire: massive horned creatures with an inhuman resistance to pain. The destruction of Mordheim brought many Beastmen into the ruined city to prey upon the survivors. They readily ally with the Magisters of the Possessed warbands. "
        )

    # With hunter characters
    add_characterref(
        race = "Human",
        source = "Core Rules - Witch Hunters",
        category = "Witch Hunter Captain",
        ishero = True,
        skill = [4, 4, 4, 3, 3, 1, 4, 1, 8, 0],
        abilitylist = [            
            {"name": "Leader", "description": "Any models in the warband within 6 inch of the Magister may use his Leadership instead of their own. "},
            {"name": "Burn the Witch!", "description":"A Witch Hunter Captain hates all models who can cast spells."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "Driven by fanaticism, Witch Hunter Captains are obsessed with cleansing Mordheim and bringing the justice of Sigmar to all. Carrying the edict of the Grand Theogonist himself, they have the divine right to judge and execute warlocks, witches, Chaos worshippers… in fact all who dare to oppose them."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Witch Hunters",
        category = "Warrior Priest",
        ishero = True,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 8, 0],
        abilitylist = [
            {"name": "Prayers", "description":"A Warrior-Priest is a servant of Sigmar and may use the Prayers of Sigmar as detailed in the Magic section."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 12,
        price = 40,
        maxcount = 1,
        description = "Many powerful fighting men have come from the ranks of the faithful. The Priests of Sigmar are no exception, and the military wing of the cult is feared and respected throughout the Empire. The Grand Theogonist himself has granted the Warrior-Priests an edict to cleanse Mordheim of Chaos filth. With fire burning in their eyes, the WarriorPriests stride into battle, chanting aloud the Deus Sigmar, the praise of the patron god of the Empire."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Witch Hunters",
        category = "Witch Hunter",
        ishero = True,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Burn the Witch!", "description":"A Witch Hunter hates all models who can cast spells."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 25,
        maxcount = 3,
        description = "Witch Hunters are members of the grim Order of Witch Hunters, dedicated to eradicating Chaos and all its minions. Usually they prowl the Old World individually trying and executing the enemies of Sigmar, but the situation in Mordheim requires them to band together."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Witch Hunters",
        category = "Zealot",
        ishero = False,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 20,
        maxcount = 0,
        description = "When a man loses his family, home and all he cared for, religion is often the last refuge left to him. Such men become wandering pilgrims, bitter and dangerous fanatics who are prepared to avenge their loss at any cost. These men are called Zealots. Zealots have forsaken their former lives and exist only to destroy evil and the minions of Chaos. Whilst they might have been peasants and craftsmen before, and thus may not be as dangerous in a fight as seasoned mercenaries, their determination and fanaticism should not be underestimated. Witch Hunters find ready allies in their ranks, and many a band of Zealots is led by Witch Hunters."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Witch Hunters",
        category = "Flagellant",
        ishero = False,
        skill = [4, 3, 3, 4, 4, 1, 3, 1, 10, 0],
        abilitylist = [
            {"name": "Missile Aversion", "description": "Flagellants never use missile weapons, even if they gain an Advance roll which would otherwise allow them to do so."},
            {"name": "Fanatical", "description": "Flagellants are convinced that the end of the world is nigh, and nothing in this world holds any terror for them. Flagellants automatically pass all Leadership-based tests they are required to take. A Flagellant may never become a warband leader."},
        ],
        magiclist = [],
        itemlist = [],
        experience = 0,
        price = 40,
        maxcount = 5,
        description = "Flagellants are fanatics and madmen obsessed with the end of the world. They are often men who have lost their families to war or the ravages of nature, and have also lost their minds. With insane persistence, they travel the length and breadth of the Empire, preaching their view of the end of the world. With their rousing speeches, Witch Hunters can muster these dangerous lunatics to fight in the streets of Mordheim, where no sane man dares tread. Flagellants are extremely dangerous opponents in close combat, for they have the strength of madmen, and their bodies have become inured to pain because of self-mutilation."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Witch Hunters",
        category = "Warhound",
        ishero = False,
        skill = [6, 4, 0, 4, 3, 1, 4, 1, 5, 0],
        abilitylist = [
            {"name": "Unarmed and Unarmoured", "description": "Jaws and brutality! Warhounds never use or need weapons and armour."},
            {"name": "Animal", "description": "Warhounds are animals and thus do not gain experience."},
        ],
        magiclist = [],
        itemlist = [],
        experience = 0,
        price = 0,
        maxcount = 5,
        description = "Witch Hunters often keep packs of ferocious hunting dogs. With their huge jaws and powerful bite, they are perfect for hunting down (and tearing apart) any heretics, mutants, deviants and witches."
        )

    # Sisters of sigmar characters
    add_characterref(
        race = "Human",
        source = "Core Rules - Sisters of Sigmar",
        category = "Sigmarite Matriarch",
        ishero = True,
        skill = [4, 4, 4, 3, 3, 1, 4, 1, 8, 0],
        abilitylist = [
            {"name": "Leader", "description": "Any models in the warband within 6 inch of the Magister may use his Leadership instead of their own. "},
            {"name": "Prayers of Sigmar", "description": "The Matriarch has studied the Prayers of Sigmar. See the Magic section."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 70,
        maxcount = 1,
        description = "The Sigmarite Matriarchs, of whom there is an inner circle of twelve, are answerable to the High Matriarch of the temple. Each must lead a warband of Sisters in frequent searches of the city in order to purge the ruins. Matriarchs are driven by a zealous devotion to the Cult of Sigmar and a relentless determination to redeem the Sisterhood in His eyes."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Sisters of Sigmar",
        category = "Sister Superior",
        ishero = True,
        skill = [4, 4, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 35,
        maxcount = 3,
        description = "Each of the Sisters Superior is a long-serving priestess of the Cult of Sigmar, well versed in the rituals of the temple and an example to the younger Sisters and Novices. The Sisters Superior are entrusted with maintaining the faith and fervour of the order. Any peril or foe that may lurk in the ruins of Mordheim is as nothing compared to the wrath of a Sister Superior."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Sisters of Sigmar",
        category = "Augur",
        ishero = True,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Unarmoured", "description": "Augurs never wear armour."},
            {"name": "Blessed Sight", "description": "An Augur can re-roll any failed characteristic tests (climbing, resisting spells or any other reason), and any rolls to hit in close combat or shooting. You must accept the second result. In addition, an Augur can use her Blessed Sight to help the Sisterhood when they are searching the city for wyrdstone. If the Augur is not put out of action in the battle, you may roll two dice for her in the exploration phase and pick either dice as the result."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 1,
        description = "The blind Augurs of the Sisterhood are blessed beyond their comrades. By giving up their sight they have gained something far more, second sight – a gift from their patron god. Only a very few are marked this way, and they are greatly revered by the Sisterhood. Unlike the rest of the priestesses, they shave their heads, save for a single long braid."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Sisters of Sigmar",
        category = "Novice",
        ishero = False,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 6, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 15,
        maxcount = 10,
        description = "By tradition, the Sisters draw their recruits only from the most noble houses of the Empire, and families consider it a great honour to have their daughter accepted into the order. Only maidens of noble lineage can be relied upon to have the devotion to duty and innate sense of honour. Few though the recruits may be, they must endure several years as Novices during which time their devotion will be tested to the full. All are eager to prove themselves worthy to be the handmaidens of Sigmar."
        )
    add_characterref(
        race = "Human",
        source = "Core Rules - Sisters of Sigmar",
        category = "Sister",
        ishero = False,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 25,
        maxcount = 0,
        description = "Sigmarite Sisters know that their entire order is shamed in the eyes of their Lord Sigmar. Every one of them is sworn upon His altar to pacify the city and thereby redeem themselves. Whatever the perils and horrors that stand in their way, they will be overcome!"
        )

    # Undead characters
    add_characterref(
        race = "Undead / Vampires",
        source = "Core Rules - The Undead",
        category = "Vampire",
        ishero = True,
        skill = [6, 4, 4, 4, 4, 2, 5, 2, 8, 0],
        abilitylist = [
            {"name": "Leader", "description": "Any models in the warband within 6 inch of the Magister may use his Leadership instead of their own."},
            {"name": "Cause Fear", "description": "Vampires are terrifying Undead creatures and therefore cause fear."},
            {"name": "Immune to Psychology", "description": "Vampires are not affected by psychology (such as fear) and never leave combat."},
            {"name": "Immune to Poison", "description": "Vampires are not affected by any poison."},
            {"name": "Immune to Pain", "description": "Vampires treat a ‘stunned’ result on the Injury chart as ‘knocked down’."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 110,
        maxcount = 1,
        description = "Vampires lead the Undead in their search for the magical stones that will give their master the power to conquer the Empire. Although but pale shadows when compared to the dread Vampire Lords, the immortal servants of Vlad are still some of the most powerful creatures who fight in Mordheim. Most of them serve the undying count of Sylvania, but some have found the city to their liking, and have become independent."
        )
    add_characterref(
        race = "Undead / Vampires",
        source = "Core Rules - The Undead",
        category = "Necromancer",
        ishero = True,
        skill = [4, 3, 3, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [
            {"name": "Necromancer", "description": "Necromancers are wizards and so are able to use Necromantic magic. See the Magic section for details."}
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 35,
        maxcount = 1,
        description = "Necromancers are evil wizards, studying the corrupt art of Necromancy. Many of them are acolytes and servants of Vlad von Carstein, and follow the agents of their master to the city of the Damned. Others are recruited from amongst wizards and warlocks who have come under the suspicion of the various agents of Sigmar and have fled to Mordheim to avoid persecution."
        )
    add_characterref(
        race = "Undead / Vampires",
        source = "Core Rules - The Undead",
        category = "Dreg",
        ishero = True,
        skill = [4, 2, 2, 3, 3, 1, 3, 1, 7, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 20,
        maxcount = 3,
        description = ("Dregs are the most miserable human survivors of the demise of Mordheim. They are deformed and rejected individuals, shunned even by the other men and women who still live in the ruins and catacombs of the city. Vampires often recruit Dregs as their servants and treat them with surprising kindness. "
            "As a result, Dregs are often fanatically loyal to their Undead overlords and will do anything to protect and serve them. Dregs are very useful to their masters as they can be sent to buy equipment, weapons and supplies from the settlements around Mordheim which would often not welcome Necromancers or where Vampires would fall under the suspicion of the Witch Hunters. They can also do the bidding of their vampiric master during daylight, when the Vampires must rest in their coffins."
        ),
    )
    add_characterref(
        race = "Undead / Vampires",
        source = "Core Rules - The Undead",
        category = "Zombie",
        ishero = False,
        skill = [4, 2, 0, 3, 3, 1, 1, 1, 5, 0],
        abilitylist = [
            {"name": "Unarmed and Unarmoured", "description": "Zombies may not have any weapons or armour and suffer no penalties for this."},
            {"name": "Cause Fear", "description": "Zombies are terrifying Undead creatures and therefore cause fear."},
            {"name": "Immune to Psychology", "description": "Zombies are not affected by psychology (such as fear) and never leave combat."},
            {"name": "Immune to Poison", "description": "Zombies are not affected by any poison."},
            {"name": "Immune to Pain", "description": "Zombies treat a ‘stunned’ result on the Injury chart as ‘knocked down’."},
            {"name": "No Brain", "description": "Zombies never gain experience. They do not learn from their mistakes. What did you expect?"},
            {"name": "May not Run", "description": "Zombies are slow Undead creatures and may not run (but may charge normally)."},
        ],
        magiclist = [],
        itemlist = [],
        experience = 0,
        price = 15,
        maxcount = 0,
        description = "Zombies are the most common of the Undead: creatures animated by the will of their Necromantic masters.",
        )
    add_characterref(
        race = "Undead / Vampires",
        source = "Core Rules - The Undead",
        category = "Ghoul",
        ishero = False,
        skill = [4, 2, 2, 3, 4, 1, 3, 2, 5, 0],
        abilitylist = [
            {"name": "Unarmed", "description": "Ghouls never carry any equipment, apart from a few bones which they use as primitive weapons."},
            {"name": "Cause Fear", "description": "Ghouls are twisted and repulsive creatures and therefore cause fear."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 40,
        maxcount = 0,
        description = ("Ghouls are the descendants of evil and insane men who ate the flesh of the dead. When the lean and hungry times of famine come upon the Old World, the most depraved and destitute took to feasting on corpses to survive. Driven by their unspeakable craving for the meat of their fellow men, these creatures have given up their human life and dwell near graveyards, crypts and tombs, digging up the rotting corpses of the recently buried and consuming the cold flesh with their bare teeth and claws. "
        "The destruction of Mordheim attracted many Ghoul clans from the north, and now they have taken up permanent residence in the crypts and cemeteries of the ruined city."
        ),
    )
    add_characterref(
        race = "Undead / Vampires",
        source = "Core Rules - The Undead",
        category = "Dire Wolf",
        ishero = False,
        skill = [9, 3, 0, 4, 3, 1, 2, 1, 4, 0],
        abilitylist = [
            {"name": "Double Charge", "description": "Dire Wolves are slavering creatures that overpower their opponents when they charge. Dire Wolves fight with 2 attacks instead of 1 during the turn they charge."},
            {"name": "Unarmed and Unarmoured", "description": "Jaws and brutality! Dire Wolves never use or need weapons and armour."},
            {"name": "Cause Fear", "description": "Dire Wolves are terrifying Undead creatures and therefore cause fear."},
            {"name": "Immune to Psychology", "description": "Dire Wolves are not affected by psychology (such as fear) and never leave combat."},
            {"name": "Immune to Poison", "description": "Dire Wolves are not affected by any poison."},
            {"name": "Immune to Pain", "description": "Dire Wolves treat a ‘stunned’ result on the Injury chart as ‘knocked down’."},
            {"name": "May not Run", "description": " Dire Wolves are slow to react and may not run (but may charge normally)."},
            {"name": "Unliving", "description": "Dire Wolves do not gain experience. You can’t teach an old dog new tricks!"},
        ],
        magiclist = [],
        itemlist = [],
        experience = 0,
        price = 50,
        maxcount = 5,
        description = "Dire Wolves are slavering Undead hounds, the animated remains of the giant wolves of the Worlds Edge Mountains. Their chilling howls can strike fear into the hearts of even the bravest warriors or most ruthless Dwarf mercenaries. They prowl the streets of Mordheim like shadows, and many men have died with the cold jaws of a Dire Wolf around their neck."
        )

    # Skaven characters
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Assessin Adept",
        ishero = True,
        skill = [6, 4, 4, 4, 3, 1, 5, 1, 7, 0],
        abilitylist = [
            {"name": "Leader", "description": "Any models in the warband within 6 inch of the Magister may use his Leadership instead of their own."},
            {"name": "Armour Piercing", "description": "An Assassin Adept always has an extra -1 modifier to any armour save the enemy has to take against wounds they inflicted (both with shooting and close combat weapons)."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 20,
        price = 60,
        maxcount = 1,
        description = "The Nightmaster of Clan Eshin has sent the Assassin to collect precious wyrdstone. Success means many breeders, wealth and a better position amongst the clan. Failure, on the other hand, is best not contemplated…"
        )
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Eshin Sorcerer",
        ishero = True,
        skill = [5, 3, 3, 3, 3, 1, 4, 1, 6, 0],
        abilitylist = [
            {"name": "Horned Rat Sorcerer", "description": "An Eshin Sorcerer is a wizard and uses the Magic of the Horned Rat. See the Magic section for details."},
        ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 0,
        maxcount = 1,
        description = "The Sorcerers of Clan Eshin are black magicians who manufacture the enchanted weapons of the Assassins. Though their power is slight compared to the Warlocks of Clan Skryre or the mighty Grey Seer, their black sorcery is still potent."
        )
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Black Skaven",
        ishero = True,
        skill = [6, 4, 3, 4, 3, 1, 5, 1, 6, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 40,
        maxcount = 2,
        description = "Black Skaven are the most powerful fighters of Clan Eshin: black-furred killers trained in the martial arts of their clan. In Mordheim they excel at ambushing and assassinating man-things."
        )
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Night Runner",
        ishero = True,
        skill = [6, 2, 3, 3, 3, 1, 4, 1, 4, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 20,
        maxcount = 2,
        description = "Night Runners are the young apprentices of Clan Eshin. Recently initiated into the secrets of the clan, they make up for their lack of knowledge with their ambition and energy."
        )
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Verminkin",
        ishero = False,
        skill = [5, 3, 3, 3, 3, 1, 4, 1, 5, 0],
        abilitylist = [],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 20,
        maxcount = 0,
        description = "Verminkin are the Clanrats of Clan Eshin. The strongest amongst them are initiated into the secrets of the clans and begin their training to become Assassins, the most feared warriors of the Skaven warbands. All the Clanrats of Clan Eshin dream of rising to the status of an Assassin one day."
        )
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Giant Rats",
        ishero = False,
        skill = [6, 4, 4, 4, 4, 2, 5, 2, 8, 0],
        abilitylist = [
            {"name": "Unarmed and Unarmoured", "description": "Giant Rats never use any armour or weapons."},
            {"name": "Pack size", "description": "You can recruit as many Giant Rats as you wish."},
            {"name": "Animal", "description": "Giant Rats are animals and do not gain experience."},
        ],
        magiclist = [],
        itemlist = [],
        experience = 0,
        price = 15,
        maxcount = 0,
        description = "Giant Rats are creations of the twisted genius of the Skaven. They are mutated monstrosities the size of dogs. They fight alongside the Skaven, overpowering any opponents by sheer weight of numbers."
        )
    add_characterref(
        race = "Skaven",
        source = "Core Rules - Skaven",
        category = "Rat Ogre",
        ishero = False,
        skill = [6, 3, 3, 5, 5, 3, 4, 3, 4, 0],
        abilitylist = [
            {"name": "Unarmed and Unarmoured", "description": "Jaws, claws and brute force! Rat Ogres can never use weapons or armour."},
            {"name": "Cause Fear", "description": "Rat Ogres are so frightening they cause fear."},
            {"name": "Stupidity", "description": "A Rat Ogre is subject to stupidity unless a Skaven Hero is within 6 inch of it."},
            {"name": "Animal", "description": "Rat Ogres are animals and do not gain experience."},
            {"name": "Large Target", "description": "Rat Ogres are Large Targets as defined in the shooting rules."},
        ],
        magiclist = [],
        itemlist = [],
        experience = 0,
        price = 210,
        maxcount = 1,
        description = "These horrible monsters are much in demand as bodyguards to important Skaven."
        )

    # High Elves characters from the Broheim website
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Loremaster",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 9, 0],
        abilitylist = [
            {"name": "Excellent Sight", "description":"Spot hidden objects at double the range. "},
            {"name": "High Elven Magician", "description":"Character is able to use High Elven magic. "}
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "},
            {"name": "Wyrdbreaker", "category": "Other", "source": "Core Rules", "distance": 0, "description": "test"},
        ],
        experience = 20,
        price = 80,
        maxcount = 1,
        description = "Loremasters are the most powerful mages in the entire Warhammer world. Their knowledge of the arcane arts and their intensive training at the Tower of Hoeth makes them perfect for leading expeditions into Lustria. They are capable and efficient with years of extensive training and skill at their disposal. Loremasters alone command magic powerful enough to match the might of the mysterious Slann. They delve into the temple cities of the Lizardmen in search of any remaining artifacts of the Old Ones power. "
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Ranger",
        ishero = True,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range. "}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 8,
        price = 45,
        maxcount = 2,
        description = "Elf Rangers are expert trackers and woodsman. Their keen eyesight and excellent archery skills help them to serve as the perfect lookouts. Rangers are more solitary then other High Elves and their quick decisiveness and ability to work on their own makes them invaluable elements of the Warband. Their skills alone have brought many expeditions back from the brink of death. They have saved countless Elven lives and continue to prove their worth in battle time and time again. "
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Sword Warden",
        ishero = True,
        skill = [5, 5, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range. "}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 11,
        price = 50,
        maxcount = 2,
        description = "Sword Wardens are young Sword Masters in training recently sent out from the White Tower in order to better hone and refine their martial prowess. Though not as deadly as a full-fledged Sword Master, their skills are still beyond the understanding of ordinary Elves. In battle a Sword Warden wields his trademark Greatsword with effortless grace, dashing aside enemy missiles as he charges into combat. They are the elite warriors of the Warband and their lighting fast strikes have left many enemies lying dead at their feet. Sword Wardens serve as the Loremaster’s personal attendants and protectors. "
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Seaguard",
        ishero = False,
        skill = [5, 4, 4, 3, 3, 1, 6, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range. "}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 35,
        maxcount = 0,
        description = "Most Elven soldiery is called to arms only in times of great need, for there are too few Elves to maintain armies at all times. The Seaguard however, are always kept at strength and they retain a full-time contingent of warriors for this purpose. As a result they are better equipped and better trained then Citizen Levy Troops. "
    )
    add_characterref(
        race = "High Elf",
        source = "Broheim - High Elves",
        category = "Cadet",
        ishero = False,
        skill = [5, 3, 3, 3, 3, 1, 5, 1, 8, 0],
        abilitylist = [{"name": "Excellent Sight", "description":"Spot hidden objects at double the range. "}],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 0,
        price = 30,
        maxcount = 5,
        description = "Cadets are young Citizen Levy of Ulthuan serving in the High Elf army for the first time. Their skills have yet to fully develop and most of them have yet to see battle. They are expert archers and travel light, thus making the perfect quick striking troops. Cadets are used primarily as scouts and are assigned the less important duties within the Citadel of Dusk and aboard High Elf Dragonships. "
    )
    add_characterref(
        race = "High Elf",
        source = "Manual",
        category = "Khaine",
        ishero = True,
        skill = [6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
        abilitylist = [
            {"name": "Excellent Sight", "description":"Spot hidden objects at double the range. "}, {"name": "Fear", "description": "Spreads fear in nearby enemies. "},
            ],
        magiclist = [],
        itemlist = [
            {"name": "Starting Dagger", "category": "Melee Weapon", "source": "Core Rules", "distance": 0, "description": "A basic dagger. Most units already carry one. "}
        ],
        experience = 100,
        price = 30,
        maxcount = 5,
        description = "Cadets are young Citizen Levy of Ulthuan serving in the High Elf army for the first time. Their skills have yet to fully develop and most of them have yet to see battle. They are expert archers and travel light, thus making the perfect quick striking troops. Cadets are used primarily as scouts and are assigned the less important duties within the Citadel of Dusk and aboard High Elf Dragonships. "
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
            {"name": "Enemy Armor Save", "description": "These weapons are not the best weapons to use for penetrating an enemy model’s armor. An enemy wounded by it gains a +1 bonus to his armor save, and a 6+ armor save if he has none normally. "},
            ],
        magiclist = [],
        price = 0,
        description = "Daggers and knives are extremely common, and men are allowed to carry them in enclaves where weapons are otherwise forbidden. Many a warrior in Mordheim has died with a dagger in his back. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Extra Dagger",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Enemy Armor Save", "description": "These weapons are not the best weapons to use for penetrating an enemy model’s armor. An enemy wounded by it gains a +1 bonus to his armor save, and a 6+ armor save if he has none normally. "},
            ],
        magiclist = [],
        price = 2,
        description = "A extra dagger. For units that want to dual wield daggers. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Club",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries. "}],
        magiclist = [],
        price = 3,
        description = "Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Mace",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries. "}],
        magiclist = [],
        price = 3,
        description = "Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Hammer",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Cutting Edge", "description": "An axe has an extra save modifier of -1, so a model with Strength 4 using an axe has a -2 save modifier when he hits an opponent in hand-to-hand combat. "}],
        magiclist = [],
        price = 3,
        description = "Perhaps the simplest type of weapon, these brutal, bludgeoning instruments range from primitive wooden clubs to elaborately forged Dwarf hammers made from the finest steel. A blow from a mace can easily crush a skull or knock a man unconscious. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Axe",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries. "}],
        magiclist = [],
        price = 5,
        description = "The axe is the traditional weapon of Empire woodsmen, and is also used as a weapon in poorer rural areas. Axes have a heavy blade and, if swung by a strong man, can cause a lot of damage. The blade of an axe can easily cut through armor, though it requires considerable strength from the wielder. Of all the warriors in the Old World, Dwarfs are the most adept at making axes. Their axes are invaluable to the warriors of the Old World and are some of the most sought after weapons. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Sword",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Parry", "description": "Swords offer an excellent balance of defense and offence. A model armed with a sword may parry blows. When his opponent rolls to hit, the model armed with a sword may roll a D6. If the score is greater than the highest to hit score of his opponent, the model has parried the blow, and that attack is discarded. A model may not parry attacks made with double or more its own Strength – they are simply too powerful to be stopped. "}],
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
            {"name": "First Strike", "description": "A warrior with a spear strikes first in the first turn of hand-to-hand combat. "},
            {"name": "Unwieldy", "description": "A warrior with a spear may only use a shield or a buckler in his other hand. He may not use a second weapon. "},
            {"name": "Cavalry Bonus", "description": "If using the rules for mounted models, a mounted warrior armed with a spear receives a +1 Strength bonus when he charges. This bonus only applies for that turn. "},
        ],
        magiclist = [],
        price = 10,
        description = "Spears range from sharpened sticks used by Goblins to the impressive cavalry spears typical of the Elves. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Halberd",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Two Handed", "description":"A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting. "}],
        magiclist = [],
        price = 10,
        description = "The halberd’s heavy blade is mounted upon a sturdy shaft of oak or steel and has a point like a spear and a cutting edge like an axe. Since it can be used to chop as well as thrust, it is an adaptable weapon, but is difficult to use inside buildings. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Great Sword",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Two Handed", "description": "A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting. "},
            {"name": "Last Strike", "description": "These Double-handed weapons are so heavy that the model using them always strikes last, even when charging. "},
            ],
        magiclist = [],
        price = 15,
        description = "A blow from a double-handed axe or sword can cut a foe in half and break armor apart. It takes a long time to learn how to use these weapons and even then only extremely strong men are able to wield them effectively. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Great Axe",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Two Handed", "description": "A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting. "},
            {"name": "Last Strike", "description": "These Double-handed weapons are so heavy that the model using them always strikes last, even when charging. "},
            ],
        magiclist = [],
        price = 15,
        description = "A blow from a double-handed axe or sword can cut a foe in half and break armor apart. It takes a long time to learn how to use these weapons and even then only extremely strong men are able to wield them effectively. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Flail",
        distance = 0,
        skill = [0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Two Handed", "description": "A model armed with a double-handed weapon may not use a shield, buckler or additional weapon in close combat. If the model is equipped with a shield he will still get a +1 bonus to his armor save against shooting. "},
            {"name": "Heavy", "description": "A flail is extremely tiring to use and thus the +2 Strength bonus applies only in the first turn of each hand-to-hand combat. "},
            ],
        magiclist = [],
        price = 15,
        description = "The flail is a heavy weapon wielded with both hands. It normally consists of heavy weights, often spiked, attached to a pole or handle by means of heavy chains. Flails drain the user’s stamina quickly, but are awesomely destructive in the hands of a skilled (or unhinged) warrior. "
        )
    add_itemref(
        source = "Core Rules",
        category = "Melee Weapon",
        name = "Morning Star",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Difficult to Use", "description": "A model with a morning star may not use a second weapon or buckler in his other hand because it requires all his skill to wield it. He may carry a shield as normal though. "},
            {"name": "Heavy", "description": "A flail is extremely tiring to use and thus the +1 Strength bonus applies only in the first turn of each hand-to-hand combat. "},
            ],
        magiclist = [],
        price = 15,
        description = "The flail is a heavy weapon wielded with both hands. It normally consists of heavy weights, often spiked, attached to a pole or handle by means of heavy chains. Flails drain the user’s stamina quickly, but are awesomely destructive in the hands of a skilled (or unhinged) warrior. "
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
        description = "The bow is carried by most races and used extensively in warfare. It is a compact yet powerful weapon, that is cheap to make and easy to maintain. "
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
        description = "A long bow is made of alternating layers of either yew or elm. A skilled archer can hit a chosen leaf on a tree from three hundred paces with this weapon. The long bow is favored by experienced archers due to its great reach and accuracy. "
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
        description = "A Long bow. "
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
        description = "Light armor encompasses a wide variety of materials from hardened leather tunics to chain shirts forged from steel. It does not offer complete protection against arrows or swords, but it is better than having nothing at all. Light armor does not inhibit movement. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Heavy Armour",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
        abilitylist = [
            {"name": "Encumbered", "description": "A warrior that is armed with both heavy armor and a shield suffers a -1 Movement penalty. "},
        ],
        magiclist = [],
        price = 50,
        description = "Typical heavy armor is made from metal links and is called chain mail. Forging chain mail is a laborious and time consuming process, as the blacksmith must put together hundreds, sometimes thousands, of metal links. This makes chain mail expensive, but this type of armor provides excellent protection for anyone who can afford it. There are other types of heavy armor as well, of which the best known are the steel breastplates and greaves worn by the foot knights of the Templar orders. "
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
        description = "Ithilmar is a silvery metal which is as light as silk and stronger than steel. Elves are experts at fashioning weapons and armor from Ithilmar, and the Elven kingdom of Caledor is the only place in the world where this metal can be found. Ithilmar armor gives the wearer a 5+ basic save, and does not slow him down if he is also armed with a shield. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Helmet",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Hardhead", "description": "A model that is equipped with a helmet has a special 4+ save on a D6 against being stunned. If the save is made, treat the stunned result as knocked down instead. This save is not modified by the opponent’s Strength. "},
        ],
        magiclist = [],
        price = 10,
        description = "From the shining steel helmets of Bretonnian knights to the leather caps of the Skaven, all sensible warriors try to protect the most vulnerable part of their body – their head. Even the most vain fighters still use a helmet, as it can be festooned with plumes, horns and other decorations. Helmets come in varying shapes and sizes, but their basic function remains the same. "
    )    
    add_itemref(
        source = "Core Rules",
        category = "Armour & Protection",
        name = "Buckler",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [{"name": "Parry", "description": "Swords offer an excellent balance of defense and offence. A model armed with a sword may parry blows. When his opponent rolls to hit, the model armed with a sword may roll a D6. If the score is greater than the highest to hit score of his opponent, the model has parried the blow, and that attack is discarded. A model may not parry attacks made with double or more its own Strength – they are simply too powerful to be stopped. "}],
        magiclist = [],
        price = 5,
        description = "Bucklers are small, round shields designed for parrying or deflecting blows. They are usually made of steel for they need to be tremendously durable to survive the brutal blows of hand-to-hand combat. Using a buckler requires great skill, but a nimble warrior can protect himself from blows which would otherwise cripple him. "
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
        description = "There are two types of shield common to the warriors of Mordheim: the first is made of wood, occasionally reinforced with metal plates. This basic type of shield, although strong, does tend to splinter, but this can sometimes save the user’s life as his enemy’s weapon can get trapped allowing him to strike back whilst his enemy struggles to free his weapon. Metal shields are heavy and cumbersome, but last much longer and can take a battering. A typical Empire shield is either round or triangular, and carries the emblem of the province or city of its owner. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Consumables",
        name = "Elven Wine",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Fearless", "description": "An elven warband that drinks Elven Wine before a battle will be immune to Fear for the whole of the battle. "}
        ],
        magiclist = [],
        price = 50,
        description = "High Elven wines are well known to be the best in the world, and some are even rumored to have magical qualities. A fine Elven Wine can cast out doubt and fear and leave a general feeling of wellbeing in a warrior. "
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
        description = "Temporary item, When you buy a map, roll a D6. Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Fake Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Fake Mordheim Map", "description": "The map is a fake, and is completely worthless. It leads you on a fool’s errand. Your opponent may automatically choose the next scenario you play. "}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Vague Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Vague Mordheim Map", "description": "Though crude, the map is generally accurate (well… parts of it are… perhaps!). You may re-roll any one dice during the next exploration phase if you wish but you must accept the result of the second roll. "}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Catacomb Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Catacomb Mordheim Map", "description": "The map shows a way through the catacombs into the city. You may automatically choose the scenario next time you fight a battle. "}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Accurate Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Accurate Mordheim Map", "description": "The map is recently made and very detailed. You may re-roll up to three dice during the next exploration phase if you wish. You must accept the result of the second roll. "}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot. "
    )
    add_itemref(
        source = "Core Rules",
        category = "Other",
        name = "Master Mordheim Map",
        distance = 0,
        skill = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Master Mordheim Map", "description": "This is one of the twelve master maps of Mordheim made for Count von Steinhardt of Ostermark. From now on you may always re-roll one dice when rolling on the Exploration chart as long as the Hero who possesses this map was not taken out of action in the battle. "}
        ],
        magiclist = [],
        price = 20,
        description = "Some survivors of the cataclysm still remain in the many settlements around Mordheim, and make a living by preparing maps of the city from memory. Many of these maps are faked, and even real ones are often crude and inaccurate. A map can help a warband find their way through the confusing maze of streets and into areas with rich buildings to loot. "
    )

    #  Specific Broheim - High Elves items
    add_itemref(
        source = "Broheim - High Elves",
        category = "Melee Weapon",
        name = "Mage Staff (One Handed)",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Concussion", "description": "Hammers and other bludgeoning weapons are excellent to use for striking your enemy senseless. When using a hammer, club or mace, a roll of 2-4 is treated as stunned when rolling to see the extent of a model’s injuries. "}
            ],
        magiclist = [],
        price = 20,
        description = "A staff used by mages. "
        )
    add_itemref(
        source = "Broheim - High Elves",
        category = "Melee Weapon",
        name = "Mage Staff (Two Handed)",
        distance = 0,
        skill = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        abilitylist = [
            {"name": "Concussion", "description": "Stunned happens also on a trow of 2 at the injury roll. "}
            ],
        magiclist = [],
        price = 20,
        description = "A staff used by mages. "
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
        description = "The Elven Mage utters the True Name of Asuryan, the lord of the Elf gods. Shaken by his awesome power, the enemies of the Elves become weak and ineffective. Any enemies within 8 inch of the Mage suffer a -3 Weaponskill penalty, down to a minimum of one. Lasts until the beginning of the next High Elf turn. "
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "Fiery Wrath",
        difficulty = 8,
        description = "With one delicate movement the Elven Mage traces an intricate Sigil of Flame in the air. Range 12 inch. May be cast on any model within range. The target is hit with Strength 4. Any models within 3 inch of the target model suffer a Strength 3 hit on a D6 roll of 4+. Take armour saves as normal. "
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "The Phoenix Crown",
        difficulty = 9,
        description = "A crown of white flames appears above the head of the Elf Mage, enveloping him within a glorious array of flames. The Elf Mage has an armour save of 2+ that replaces his normal armour save. In addition, he gains a +2 to his Weaponskill and a +1 to his Strength. Roll at the beginning of each turn in the recovery phase. On a D6 roll of 1 or 2 the Phoenix Crown disappears. "
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "Roar of the Dragon",
        difficulty = 8,
        description = "A shadow of a wrathful Dragon strikes out from the outstretched hand of the mage, and speeds forward roaring its anger. The roar of the Dragon has a range of 12 inch and it is absolutely straight. Any model in its path must roll equal or under its Strength or be Knocked Down. If the spell hits a building it stops. "
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "The Anger of the Earth",
        difficulty = 10,
        description = "At the command of the Elven Mage, the very earth raises up against the enemies of the Elves. Draw a 12 inch direct line from the mage in any direction. The line is 1 inch wide and absolutely straight. Any model in its path suffers a single S5 hit. "
    )
    add_magicref(
        source = "Broheim - High Elves", 
        category = "High Elven Magic",
        name = "The Light of Glory",
        difficulty = 8,
        description = "A radiant white light emerges from the mage`s hand, banishing all fear and doubt in his comrades. Any friendly models within 8 inch of the Elven mage are immune to psychology and will never break from combat. This spell lasts until the mage suffers a wound. If the mage suffers a wound then the enchanted Elves become startled and uneasy. All models with 8 inch must take a Leadership test. If any fail, they are treated as if they had failed an All Alone test. "
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

# Special skills The Sisters of Sigmar may use the following skill list instead of the standard skill lists. Sisters of Sigmar
# Sign of Sigmar The Sister is favoured by the great god Sigmar. Possessed or Undead opponents lose their first attack against the Priestess in the first round of hand-to-hand combat (down to a minimum of 1). Protection of Sigmar The Sister has been blessed by the High Matriarch. Any spell which would affect her is nullified on a D6 roll of 4+. Note that if the spell is nullified it will not affect any other models either. Utter Determination Only the Matriarch may have this skill, which allows her to re-roll any failed Rout tests.
# Righteous Fury The Sister feels cold fury and utter contempt towards any evil that pollutes the soil of the holy Empire with its presence. The model hates all Skaven, Undead or Possessed warbands and all models in them. Absolute Faith The Sister puts her faith in Sigmar, and faces dangers unflinchingly. She may re-roll any Fear tests and does not have to test if she is fighting alone against several opponents.

# Skaven special skills
# Skaven
# 30
# Skaven Heroes may choose to use the following Skill list instead of any of the standard Skill tables available to them. black hunger The Skaven can draw upon the dreaded Black Hunger, the fighting frenzy which gives him unnatural strength and speed but can ravage him from inside. The Skaven Hero may declare at the beginning of his turn that he is using this skill. The Hero may add +1 attack and +D3" to the total move to his profile for the duration of his own turn but will suffer D3 S3 hits with no armour save possible at the end of the turn. tail fighting The Skaven may wield a shield, knife or a sword with its tail. The model gains an extra attack with the appropriate weapon or a +1 bonus to its armour save. wall runner The Skaven does not need to take an Initiative test when climbing up walls and other sheer surfaces. infiltration A Skaven with this skill is always placed on the battlefield after the opposing warband and can be placed anywhere on the table as long as it is out of sight of the opposing warband and more than 12" away from any enemy model. If both players have models which infiltrate, roll a D6 for each, and the lowest roll sets up first. art of silent death The Skaven has patiently mastered the deadly art of open-hand fighting, as taught by the mystics of Cathay in the temples of the far East. In hand-to-hand combat, the Skaven can fight with his bare paws without any penalties and counts as having two weapons (ie, +1 attack). In addition, a Skaven Hero with this skill will cause a critical hit on a To Wound roll of 5-6 instead of just 6. This skill may be used in conjunction with the Eshin Fighting Claws (+2 Attacks instead of +1).


# Mutations
# Cult of the possessed
# Mutations may be bought for a Mutant or a Possessed warrior only when they are recruited; you may not buy new mutations for a model after recruitment. Any Mutant or Possessed may have one or more mutations. The first mutation is bought at the price indicated, but second and subsequent mutations bought for the same model cost double.
# Those who dwell in Mordheim soon develop horrible mutations, and the Cult of the Possessed seem to be especially susceptible. In addition, Mordheim attracts mutants from all over the Empire, who are always quick to join the Chaos covens. Most mutations are simply inconvenient or hideous, but some make their bearers extremely dangerous in combat.
# daemon soul A Daemon lives within the mutant’s soul. This gives him a 4+ save against the effects of spells or prayers. Cost: 20 gold crowns. great claw One of the mutant’s arms ends in a great, crab-like claw. He may carry no weapons in this arm, but gains an extra attack in hand-to-hand combat with a +1 Strength bonus. Cost: 50 gold crowns. cloven hoofs The warrior gains +1 Movement. Cost: 40 gold crowns
# tentacle One of the mutant’s arms ends in a tentacle. He may grapple his opponent in close combat to reduce his attacks by -1, down to a minimum of 1. The mutant may decide which attack his opponent loses. Cost: 35 gold crowns blackblood If the model loses a wound in close combat, anyone in base contact with the model suffers a Strength 3 hit (no critical hits) from the spurting corrosive blood. Cost: 30 gold crowns spines Any model in base contact with the mutant suffers an automatic Strength 1 hit at the beginning of each close combat phase. Spines will never cause critical hits. Cost: 35 gold crowns scorpion tail The mutant has a long barbed tail with a venomed tip, allowing him to make an extra Strength 5 attack in each hand-to-hand combat phase. If the model hit by the tail is immune to poison, the Strength of the hit is reduced to 2. Cost: 40 gold crowns extra arm The mutant may use any single-handed weapon in the extra arm, giving him +1 attack when fighting in hand-to-hand combat. Alternatively, he may carry a shield or a buckler in the extra arm. If a Possessed chooses to do this, he gains an extra attack but still cannot carry a weapon. Cost: 40 gold crowns hideous The mutant causes fear. See the Psychology section for details. Cost: 40 gold crowns