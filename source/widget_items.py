import sys

from PyQt5.QtCore import (
    QRect,
    Qt,
    pyqtSignal,
    )

from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QDesktopWidget,
    QInputDialog,
    QLabel,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton, 
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QToolTip, 
    QVBoxLayout,
    QWidget, 
    )

from PyQt5.QtGui import (
    QColor,
    QFont,
    QFontDatabase,
    QIcon,
    QPalette,
    )

from source.methods_json import (
    open_json,
    save_json,
    )

from source.methods_engine import (
    save_warband,
    load_warband,
    cache_warband,
    show_saved_warbands,
    get_current_warband,
    create_template_wb,
    create_template_char,
    )

from source.class_hierarchy import (
    Warband,
    Squad,
    Character,
    Hero,
    Henchman,
    )

from source.class_hierarchy import (
    Rule,
    Treasury,
    Item,
    Skill,
    Ability,
    Magic,
    )

from source.widget_template import *


class WidgetItemsWarband(QBorderedWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line
        for item in self.mainwindow.wbid.itemlist:
            label = QLabel()
            label.setText(str(item.subcategory))
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            itemwidget.clicked.connect(self.create_method_remove_item(warband = self.mainwindow.wbid, item = item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout
            
        self.setLayout(itembox)
            
        label = QLabel()
        label.setText("New Item")
        itemwrap = QVBoxLayout()
        itemwrap.addWidget(label)
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itemwrap)
        itemwidget.clicked.connect(self.create_new_item)
        itembox.addWidget(itemwidget) #adds the new item to a label and at it to the vertical item layout

        self.setToolTip("These are your warbands items.")
        self.setLayout(itembox)
        
    def create_new_item(self):

        """Create a new item and store it in this warband"""
        new_item = self.dialog_choose_item()
        if new_item != "Cancel":
            wbidgold = self.wbid.treasury.gold
            itemprice = new_item.price
            if wbidgold >= itemprice:
                self.wbid.treasury.gold = wbidgold - itemprice
                self.wbid.itemlist.append(new_item)
                self.initUI()
            else:
                print("can't add new item, lack of funds")

    def create_method_remove_item(self, warband, item):          

        def remove_item():

            remove = QMessageBox.question(self, 'Remove item', f"Do you want to remove this item?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                itemprice = 0

                for i in warband.itemlist:
                    if i.name == item.name and i.subcategory == item.subcategory:
                        if process_gold == QMessageBox.Yes:
                            itemprice += item.price
                        index = warband.itemlist.index(i)
                        warband.itemlist.pop(index)
                        break

                self.mainwindow.wbid.treasury.gold += itemprice
                self.mainwindow.initUI()
        
        return remove_item



class WidgetItemsHero(QBorderedWidget):
    def __init__(self, mainwindow, hero):
        super().__init__()

        self.mainwindow = mainwindow
        self.hero = hero

        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in hero.itemlist:
            label = QLabel()
            label.setText(str(item.subcategory))
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            itemwidget.clicked.connect(self.create_method_remove_item_hero(hero = hero, item = item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout
            
        self.setLayout(itembox)

    def create_method_new_item(self, unit):
        """Method for creating a new item and receiving as attribute the unit it should be added to."""
        
        def create_item_for_unit():
            new_item = self.dialog_choose_item()
            if new_item != "Cancel":
                itemprice = new_item.price
                if self.wbid.treasury.gold >= itemprice:
                    
                    for hero in self.wbid.herolist:
                        if unit.name == hero.name:
                            hero.itemlist.append(new_item)
                            self.wbid.treasury.gold -= itemprice
                            self.initUI()
                                
                else:
                    message = QMessageBox.information(self, 'Lack of funds!', "Can't add new item, lack of funds", QMessageBox.Ok)
            
        return create_item_for_unit

    def create_method_remove_item_hero(self, hero, item):          
        """ """

        def remove_item():

            remove = QMessageBox.question(self, 'Remove item', f"Do you want to remove this item?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                itemprice = 0

                for hero in self.wbid.herolist:
                    for i in hero.itemlist:
                        if i.name == item.name and i.subcategory == item.subcategory:
                            if process_gold == QMessageBox.Yes:
                                itemprice += item.price
                            index = hero.itemlist.index(i)
                            hero.itemlist.pop(index)
                            break

                self.mainwindow.wbid.treasury.gold += itemprice
                self.mainwindow.initUI()
        
        return remove_item


class WidgetItemsSquad(QBorderedWidget):
    def __init__(self, mainwindow, squad):
        super().__init__()

        self.mainwindow = mainwindow
        self.squad = squad

        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in squad.henchmanlist[0].itemlist:
            label = QLabel()
            label.setText(str(item.subcategory))
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            itemwidget.clicked.connect(self.create_method_remove_item_squad(squad = squad, item = item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout
            
        self.setLayout(itembox)

    def create_method_new_item(self, unit):
        """Method for creating a new item and receiving as attribute the unit it should be added to."""

        def create_item_for_unit():
            new_item = self.dialog_choose_item()
            if new_item != "Cancel":
                itemprice = new_item.price
                if self.wbid.treasury.gold >= itemprice:
                    
                    for s in self.wbid.squadlist:
                        if unit.name == s.name:
                            for henchman in s.henchmanlist:
                                henchman.itemlist.append(new_item)
                                self.wbid.treasury.gold -= itemprice
                            self.initUI()

                else:
                    message = QMessageBox.information(self, 'Lack of funds!', "Can't add new item, lack of funds", QMessageBox.Ok)
            
        return create_item_for_unit

    def create_method_remove_item_squad(self, squad, item):          

        def remove_item():

            remove = QMessageBox.question(self, 'Remove item', f"Do you want to remove this item?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                itemprice = 0

                for h in squad.henchmanlist:
                    for i in h.itemlist:
                        if i.name == item.name and i.subcategory == item.subcategory:
                            if process_gold == QMessageBox.Yes:
                                itemprice += item.price
                            index = h.itemlist.index(i)
                            h.itemlist.pop(index)
                            break

        return remove_item


def dialog_choose_item(self):
    
    itemdict = open_json("database/references/items_ref.json")
    
    sources = []
    for key in itemdict:
        sources.append(key)

    source, okPressed = QInputDialog.getItem(self, "Select source", "Choose a source", sources, 0, False)
    if okPressed and source:
    
        # categories
        categories = []
        for key in itemdict[source]:
            categories.append(key)

        category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
        if okPressed and category:
        
            # subcategories
            subcategories = []
            for key in itemdict[source][category]:
                subcategories.append(key)

            subcategory, okPressed = QInputDialog.getItem(self, "Create", "Choose an item", subcategories, 0, False)
            if okPressed and subcategory:
                new_item = Item.create_item(
                    subcategory = subcategory,
                    category = category,
                    source = source,
                )
                return new_item
                
            else:
                string = "Cancel"
                return string
        else:
            string = "Cancel"
            return string
    else:
        string = "Cancel"
        return string