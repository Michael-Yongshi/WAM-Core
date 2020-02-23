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
            itemwidget.clicked.connect(self.create_method_remove(warband = self.mainwindow.wbid, item = item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout
            
        self.setLayout(itembox)
            
        label = QLabel()
        label.setText("New Item")
        itemwrap = QVBoxLayout()
        itemwrap.addWidget(label)
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itemwrap)
        itemwidget.clicked.connect(self.create_new)
        itembox.addWidget(itemwidget) #adds the new item to a label and at it to the vertical item layout

        self.setToolTip("These are your warbands items.")
        self.setLayout(itembox)
        
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
                        index = warband.itemlist.index(i)
                        warband.itemlist.pop(index)
                        break

                self.mainwindow.wbid.treasury.gold += itemprice
                self.mainwindow.initUI()
        
        return remove



class WidgetItemsUnit(QBorderedWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow
        unit = self.mainwindow.currentunit

        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in unit.itemlist:
            label = QLabel()
            label.setText(str(item.subcategory + " " + item.name))
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            itemwidget.clicked.connect(self.create_method_remove(unit = unit, item = item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

        # add new item widget
        label = QLabel()
        label.setText("New Item")
        itemwrap = QVBoxLayout()
        itemwrap.addWidget(label)
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itemwrap)
        itemwidget.setToolTip(f"Buy a new item for this unit.")
        itemwidget.clicked.connect(self.create_method_new(unit=unit))
        itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

        self.setLayout(itembox)
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
                            if unit.name == hero.name:
                                hero.itemlist.append(new_item)
                                self.mainwindow.wbid.treasury.gold -= itemprice
                                self.mainwindow.initUI()

                    if unit.ishero == False:
                        for squad in self.mainwindow.wbid.squadlist:
                            if unit.name == squad.henchmanlist[0].name:
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
                        for item in hero.itemlist:
                            if item.name == item.name and item.subcategory == item.subcategory:
                                if process_gold == QMessageBox.Yes:
                                    itemprice += item.price
                                index = hero.itemlist.index(i)
                                hero.itemlist.pop(index)
                                break

                elif unit.ishero == False:
                    for squad in self.mainwindow.wbid.squadlist:
                        if unit.name == squad.henchmanlist[0].name:
                            for henchman in squad.henchmanlist:
                                for item in henchman.itemlist:
                                    if item.name == item.name and item.subcategory == item.subcategory:
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