class Inventory(object):
    def __init__(self, gold=0, wyrd=0, itemlist=[]):
        self.gold = gold
        self.wyrd = wyrd
        self.itemlist = itemlist

    def add_item(self, itemname):
        itemlis.append(itemname)

    def get_totalitems(self):
        itemlist = self.itemlist if self.itemlist else None
        return itemlist

    def create_dict_inventory(self):  
        dictinv = {}
        dictinv['Inventory'] = {
            'gold': self.gold,
            'wyrd': self.wyrd,
            'itemlist': self.itemlist
            # for item in self.itemlist
            #     dictitemlist = {}
            #     dictitemlist['itemlist'] = []
            #     dictitemlist['itemlist'].append({
            #         'name': item.name,
            #         'category': item.category,
            #         'price': item.price,
            #         'desc': item.desc'
            #     })        
        }

        return dictinv 

class Item(object):
    def __init__(self, name, category, skill, abilitylist=[], desc=None, price=0):
        self.name = name
        self.category = category
        self.desc = desc
        self.skill = skill if skill else Skill()
        self.abilitylist = abilitylist
        self.price = price