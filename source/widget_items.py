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
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QInputDialog,
    QLabel,
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
from source.widget_abilitymagic import WidgetAbility

class WidgetItemsWarband(QBorderlessFrame):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        itemlistbox = QVBoxLayout() # create a vertical layout to show them in a neat line
        for item in self.mainwindow.wbid.itemlist:
            label = QClickLabel()
            label.setText(f"<b>{item.subcategory}<b/>")
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            box = QVBoxLayout()
            box.addWidget(label)
            frame = QRaisedFrame()
            frame.setLayout(box)
            frame.clicked.connect(self.create_method_remove(warband = self.mainwindow.wbid, item = item))
            itemlistbox.addWidget(frame) #adds the item to a label and at it to the vertical item layout
            
        self.setLayout(itemlistbox)
            
        label = QClickLabel()
        label.setText(f"<font>New Item<font/>")
        label.clicked.connect(self.create_new)
        itemlistbox.addWidget(label) #adds the new item to a label and at it to the vertical item layout

        self.setToolTip("These are your warbands items.")
        self.setLayout(itemlistbox)
        
    def create_new(self):

        """Create a new item and store it in this warband"""
        new_item = dialog_choose_item(self)
        if new_item != "Cancel":
            wbidgold = self.mainwindow.wbid.treasury.gold
            itemprice = new_item.price
            if wbidgold >= itemprice:
                self.mainwindow.wbid.treasury.gold = wbidgold - itemprice
                self.mainwindow.wbid.itemlist.append(new_item)
                self.mainwindow.initUI()
            else:
                message = QMessageBox.information(self, 'Lack of funds!', "Can't add new item, lack of funds", QMessageBox.Ok)

    def create_method_remove(self, warband, item):          

        def remove():

            remove = QMessageBox.question(self, 'Remove item', f"Do you want to remove this item?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                itemprice = 0

                for item in warband.itemlist:
                    if item.name == item.name and item.subcategory == item.subcategory:
                        if process_gold == QMessageBox.Yes:
                            itemprice += item.price
                        index = warband.itemlist.index(item)
                        warband.itemlist.pop(index)
                        break

                self.mainwindow.wbid.treasury.gold += itemprice
                self.mainwindow.initUI()
        
        return remove



class WidgetItemsUnit(QBorderlessFrame):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow
        unit = self.mainwindow.currentunit

        itemlistbox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in unit.itemlist:
            itembox = QHBoxLayout()

            label = QClickLabel()
            label.setText(f"<b>{item.subcategory}<b/>") # label.setText(f"<b>{item.subcategory} - {item.name}<b/>")
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            label.clicked.connect(self.create_method_remove(unit = unit, item = item))
            itembox.addWidget(label)
            itembox.addWidget(WidgetAbility(self.mainwindow, abilitylist = item.abilitylist, skip = True)) # adds the ability layout to the grid

            frame = QRaisedFrame()
            frame.setLayout(itembox)
            itemlistbox.addWidget(frame) #adds the item to a label and at it to the vertical item layout

        # add new item widget
        label = QClickLabel()
        label.setText(f"<font>New Item<font/>")
        label.setToolTip(f"Buy a new item for this unit.")
        label.clicked.connect(self.create_method_new(unit=unit))
        itemlistbox.addWidget(label) #adds the item to a label and at it to the vertical item layout

        self.setLayout(itemlistbox)
        self.setToolTip("These are your units items.")

    def create_method_new(self, unit):
        """Method for creating a new item and receiving as attribute the unit it should be added to."""
        
        def create_new():
            new_item = dialog_choose_item(self)
            if new_item != "Cancel":
                itemprice = new_item.price
                if self.mainwindow.wbid.treasury.gold >= itemprice:
                    
                    if unit.ishero == True:
                        for hero in self.mainwindow.wbid.herolist:
                            if unit is hero:
                                hero.itemlist.append(new_item)
                                self.mainwindow.wbid.treasury.gold -= itemprice
                                self.mainwindow.initUI()

                    if unit.ishero == False:
                        for squad in self.mainwindow.wbid.squadlist:
                            if unit is squad.henchmanlist[0]:
                                for henchman in squad.henchmanlist:
                                    henchman.itemlist.append(new_item)
                                    self.mainwindow.wbid.treasury.gold -= itemprice
                                self.mainwindow.initUI()

                else:
                    message = QMessageBox.information(self, 'Lack of funds!', "Can't add new item, lack of funds", QMessageBox.Ok)
            
        return create_new

    def create_method_remove(self, unit, item):          
        """ """

        def remove():

            remove = QMessageBox.question(self, 'Remove item', f"Do you want to remove this item?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                itemprice = 0

                if unit.ishero == True:
                    for hero in self.mainwindow.wbid.herolist:
                        if unit is hero:
                            for i in hero.itemlist:
                                if i is item:
                                    if process_gold == QMessageBox.Yes:
                                        itemprice += item.price
                                    index = hero.itemlist.index(item)
                                    hero.itemlist.pop(index)
                                    break

                elif unit.ishero == False:
                    for squad in self.mainwindow.wbid.squadlist:
                        if unit is squad.henchmanlist[0]:
                            for henchman in squad.henchmanlist:
                                for i in henchman.itemlist:
                                    if i is item:
                                        if process_gold == QMessageBox.Yes:
                                            itemprice += item.price
                                        index = henchman.itemlist.index(item)
                                        henchman.itemlist.pop(index)
                                        break

                self.mainwindow.wbid.treasury.gold += itemprice
                self.mainwindow.initUI()
        
        return remove


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