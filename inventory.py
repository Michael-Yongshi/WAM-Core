class Inventory(object):
    def __init__(self, gold=0, wyrd=0, itemlist=None):
        self.gold = gold
        self.wyrd = wyrd
        self.itemlist = itemlist if itemlist else []

    def add_item(self, itemname):
        itemlis.append(itemname)

    def get_totalitems(self):
        itemlist = self.itemlist if self.itemlist else None
        return itemlist


class Item(object):
    def __init__(self, name, type, desc=None, price=0):
        self.name = name
        self.type = type
        self.desc = desc
        self.price = price