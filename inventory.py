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

    def get_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'gold': self.gold,
            'wyrd': self.wyrd,
            'itemlist': str(self.itemlist)
        }
        return data

class Item(object):
    def __init__(self, name, category, skill=None, abilitylist=[], desc=None, price=0):
        self.name = name
        self.category = category
        self.desc = desc
        self.skill = skill
        self.abilitylist = abilitylist
        self.price = price

    def get_dict(self, ref):  
        data = {}
        data[str(ref)] = {
            'key': str(self),
            'name': self.name,
            'category': self.category,
            'desc': self.desc,
            'skill': self.skill,
            'abilitylist': self.abilitylist,
            'price': self.price     
        }
        return data