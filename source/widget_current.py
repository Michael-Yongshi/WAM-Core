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
from source.widget_items import WidgetItemsHero
from source.widget_items import WidgetItemsSquad

# from source.widget_currentbox import *


class WidgetCurrent(QBorderedWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        currentbox = QGridLayout()
        currentbox.addWidget(self.set_namebox(), 0, 0, 1, 1)
        currentbox.addWidget(self.set_skillbox(), 1, 0, 1, 1)
        currentbox.addWidget(self.set_listbox(), 2, 0, 2, 1)

        self.setToolTip("This is the currently selected unit")
        self.setLayout(currentbox)


    def set_namebox(self):
        namebox = QGridLayout()
        
        print(self.mainwindow.currentunit.name)
        namelabel = QLabel()
        namelabel.setText(self.mainwindow.currentunit.name)    
        namebox.addWidget(namelabel, 0, 0)

        catlabel = QLabel()
        catlabel.setText(self.mainwindow.currentunit.category)
        namebox.addWidget(catlabel, 1, 0,)

        herolabel = QLabel()
        herolabel.setText(str(self.mainwindow.currentunit.ishero))
        namebox.addWidget(herolabel, 1, 1)

        # btnremove = QPushButton('Remove Unit', self)
        # btnremove.setToolTip('Remove current unit')
        # btnremove.clicked.connect(self.create_method_remove_squad(self.mainwindow.currentunit))
        # namebox.addWidget(btnremove, 0, 1)

        namewidget = QBorderedWidget()
        namewidget.setLayout(namebox)
        
        return namewidget

    def set_skillbox(self):
        #show skills in middle
        skillbox = QHBoxLayout() # create a horizontal layout to show the skills in a neat line
        
        skilldict = self.mainwindow.currentunit.get_total_skilldict()
        for key in skilldict:
            label = QLabel()
            label.setText(key[:2] + "\n" + str(skilldict[key]))  
            label.setToolTip(f"The total <b>{key}</b> skill, <br/>including both base model scores and item influences.")
            skillbox.addWidget(label)

        skillwidget = QBorderedWidget()
        skillwidget.setLayout(skillbox)

        return skillwidget

    def set_listbox(self):
        
        listbox = QHBoxLayout()

        # Add abilities, items and magic to the listbox
        listbox = QHBoxLayout()
        listbox.addWidget(self.set_itemwidget()) # adds the item layout to the grid
        listbox.addWidget(self.set_abilitywidget()) # adds the ability layout to the grid
        listbox.addWidget(self.set_magicwidget()) # adds the magic layout to the grid

        listwidget = QInteractiveWidget()
        listwidget.setLayout(listbox)

        return listwidget

    def set_itemwidget(self):

        #add items left bottom
        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in self.itemlist:
            label = QLabel()
            label.setText(str(item.subcategory + " " + item.name))
            label.setToolTip(f"<font><b>{item.subcategory}</b> {item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            # itemwidget.clicked.connect(create_method_remove_item(item=item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

        # add new item widget
        label = QLabel()
        label.setText("New Item")
        itemwrap = QVBoxLayout()
        itemwrap.addWidget(label)
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itemwrap)
        itemwidget.setToolTip(f"Buy a new item for this unit.")
        # itemwidget.clicked.connect(self.create_method_new_item(unit=self.mainwindow.currentunit))
        itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

        itemboxwidget = QBorderedWidget()
        itemboxwidget.setLayout(itembox)
        itemboxwidget.setToolTip("These are your units items.")
        
        return itemboxwidget

    def set_abilitywidget(self):

        #show abilities
        abilitybox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for ability in self.mainwindow.currentunit.get_total_abilitylist():
            label = QLabel()
            label.setText(str(ability.name))
            label.setToolTip(f"<font><b>{ability.name}</b> <br/><br/> {ability.description}</font>")
            abilitybox.addWidget(label) #adds the ability to a label and at it to the vertical ability layout
        
        # add new ability widget
        label = QLabel()
        label.setText("New Ability")
        abilitywrap = QVBoxLayout()
        abilitywrap.addWidget(label)
        abilitywidget = QInteractiveWidget()
        abilitywidget.setLayout(abilitywrap)
        abilitywidget.setToolTip(f"Add manually a new ability for this unit.")
        abilitywidget.clicked.connect(self.create_method_new_ability(unit=self.mainwindow.currentunit))
        abilitybox.addWidget(abilitywidget) #adds the ability to a label and at it to the vertical item layout

        abilitywidget = QInteractiveWidget()
        abilitywidget.setLayout(abilitybox)

        return abilitywidget

    def set_magicwidget(self):

        #show magic
        magicbox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for magic in self.mainwindow.currentunit.get_total_magiclist():
            label = QLabel()
            label.setText(str(magic.name))
            label.setToolTip(f"<font><b>{magic.name}</b> <br/>Difficulty: {magic.difficulty} <br/><br/> {magic.description}</font>")
            magicbox.addWidget(label) #adds the magic to a label and at it to the vertical magic layout

        # add new magic widget
        label = QLabel()
        label.setText("New Magic")
        magicwrap = QVBoxLayout()
        magicwrap.addWidget(label)
        magicwidget = QInteractiveWidget()
        magicwidget.setLayout(magicwrap)
        magicwidget.setToolTip(f"Add manually a new magic skill for this unit.")
        magicwidget.clicked.connect(self.create_method_new_magic(unit=self.mainwindow.currentunit))
        magicbox.addWidget(magicwidget) #adds the magic to a label and at it to the vertical item layout

        magicwidget = QInteractiveWidget()
        magicwidget.setLayout(magicbox)

        return magicwidget

    def create_method_new_ability(self, unit):
        """Method for creating a new ability and receiving as attribute the unit it should be added to.
                    """
        def create_ability_for_unit():
            abilitydict = open_json("database/references/abilities_ref.json")
            sources = []
            for key in abilitydict:
                sources.append(key)

            source, okPressed = QInputDialog.getItem(self, "Select source", "Choose a source", sources, 0, False)
            if okPressed and source:
            
                # get all available categories
                categories = []
                for key in abilitydict[source]:
                    categories.append(key)

                category, okPressed = QInputDialog.getItem(self, "Select category", "Choose a category", categories, 0, False)
                if okPressed and category:

                    # get all available abilities
                    abilities = []
                    for key in abilitydict[source][category]:
                        abilities.append(key)

                    ability, okPressed = QInputDialog.getItem(self, "Create", "Choose an ability", abilities, 0, False)
                    if okPressed and ability:
                        new_ability = Ability(
                            source = source,
                            category = category,
                            name = ability,
                            description = abilitydict[source][category][ability]["description"],
                        )
                        
                        if unit.ishero == True:
                            for hero in self.mainwindow.wbid.herolist:
                                if unit.name == hero.name:
                                    hero.abilitylist.append(new_ability)
                                    self.mainwindow.initUI()
                                    
                        else:
                            for s in self.mainwindow.wbid.squadlist:
                                if unit.name == s.name:
                                    for henchman in s.henchmanlist:
                                        henchman.abilitylist.append(new_ability)
                                    self.mainwindow.initUI()

        return create_ability_for_unit

    def create_method_new_magic(self, unit):
        """Method for creating a new magic and receiving as attribute the unit it should be added to.
                    """
        def create_magic_for_unit():
            magicdict = open_json("database/references/magic_ref.json")
            sources = []
            for key in magicdict:
                sources.append(key)

            source, okPressed = QInputDialog.getItem(self, "Select source", "Choose a source", sources, 0, False)
            if okPressed and source:
            
                # get all available categories
                categories = []
                for key in magicdict[source]:
                    categories.append(key)

                category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
                if okPressed and category:

                    # get all available magic
                    magics = []
                    for key in magicdict[source][category]:
                        magics.append(key)

                    magic, okPressed = QInputDialog.getItem(self, "Create", "Choose magic", magics, 0, False)
                    if okPressed and magic:
                        new_magic = Magic.create_magic(
                            name = magic,
                            category = category,
                            source = source,
                        )
                        
                        if unit.ishero == True:
                            for hero in self.mainwindow.wbid.herolist:
                                if unit.name == hero.name:
                                    hero.magiclist.append(new_magic)
                                    self.mainwindow.initUI()
                                    
                        else:
                            for s in self.mainwindow.wbid.squadlist:
                                if unit.name == s.name:
                                    for henchman in s.henchmanlist:
                                        henchman.magiclist.append(new_magic)
                                    self.mainwindow.initUI()

        return create_magic_for_unit