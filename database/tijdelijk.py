def to_dict(dataobject):
    datadict = {}
    wbdict = dataobject.to_dict()
    datadict.update(wbdict)
    # print("save warband info")

    # print("save warband rulelist")
    datadict["Warband"]["rulelist"]={} # change in a dict before setting dict values
    r = 1
    for rule in dataobject.rulelist:
        ruleref = "Rule" + str(r) # to make sure it has a unique key
        # print(ruleref)
        ruledict = rule.to_dict(ref=ruleref)
        datadict["Warband"]["rulelist"].update(ruledict)
        r += 1

    invdict = dataobject.inventory.to_dict(ref="inventory")
    datadict["Warband"].update(invdict) # add new inventory dict to warband, practically replacing original value of inventory

    # print("save warband itemlist")
    datadict["Warband"]["inventory"]["itemlist"]={} # change in a dict before setting dict values
    i = 1
    for item in dataobject.inventory.itemlist:
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
    for hero in dataobject.herolist:
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
    for squad in dataobject.squadlist:
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