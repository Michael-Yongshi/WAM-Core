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
# from source.widget_currentbox import *


class WidgetHeroes(QBorderedWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        # def set_herobox(self, currentbox):
        # as we give this class a reference to currentbox, we can manipulate currentbox from here
        # currentbox.set_current_hero(hero)

        herobox = QVBoxLayout() # To show all heroes below each other dynamically (based on actual number of heroes)
        
        h = 0
        for hero in self.mainwindow.wbid.herolist: # First iterate over the heroes in your warband
            h += 1
            herogrid = QGridLayout() # create a grid layout to position all information more accurately
            
            namelabel = QLabel()
            if hero == self.mainwindow.currentunit:
                namelabel.setText(hero.name + " (selected)")
            else:
                namelabel.setText(hero.name)
            namelabel.setToolTip(f"This is your hero`s name")
            herogrid.addWidget(namelabel, 0, 0) # add the name and category box to the herogrid
            
            catlabel = QLabel()
            catlabel.setText(hero.category)
            catlabel.setToolTip(f"This is your hero`s unit type. The unit type determines what the heroes abilities are, what kind of items it can carry and how expensive it is to replace.")
            herogrid.addWidget(catlabel, 0, 1) # add the cat and category box to the herogrid

            # sets the complete hero grid layout to a herowidget in order to add to the vertical list of heroes
            herowidget = QInteractiveWidget()
            herowidget.setLayout(herogrid)

            # bound a click on the widget to showing details in character view
            herowidget.clicked.connect(self.create_method_focus(hero))
            herobox.addWidget(herowidget)

        if h <= 5: # If there is still room in your warband add a new hero widget
            h += 1
            herogrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText("Add New Hero")
            herogrid.addWidget(namelabel, 0, 0)

            herowidget = QInteractiveWidget()
            herowidget.setLayout(herogrid)
            herowidget.clicked.connect(self.create_new)
            herobox.addWidget(herowidget)
        
        while h <= 5: # if there is still room, add some empty widgets to fill up the space
            h += 1
            herowidget = QUnBorderedWidget()
            herobox.addWidget(herowidget)

        self.setToolTip('These are your <b>heroes</b>')
        self.setLayout(herobox)
        
    def create_method_focus(self, hero):          
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current unit and then passes it to the currentunit attribute of the main window"""
        
        def focus_unit():
            
            self.mainwindow.currentunit = hero
            self.mainwindow.initUI()

        return focus_unit

    def create_method_remove(self, hero): 
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current hero and then creates a window based on the attribute"""

        def remove():

            remove = QMessageBox.question(self, 'Remove hero', f"Do you want to remove this hero?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                heroprice = 0

                for hero in self.mainwindow.wbid.herolist:
                    if hero == self.mainwindow.scurrentunit:
                        if process_gold == QMessageBox.Yes:
                            heroprice += hero.price
                            for item in hero.itemlist:
                                heroprice += item.price
                        index = self.mainwindow.wbid.herolist.index(hero)
                        self.mainwindow.wbid.herolist.pop(index)
                        break

                self.mainwindow.wbid.treasury.gold += heroprice
                self.mainwindow.initUI()
        
        return remove

    def create_new(self):
        
        """Create a new hero, store it in the warband object and set to currentunit"""
        name, okPressed = QInputDialog.getText(self, "Create", "Name your hero:")
        if okPressed and name:
            
            # get all categories in references
            wbrace = self.mainwindow.wbid.race
            wbsource = self.mainwindow.wbid.source
            wbwarband = self.mainwindow.wbid.warband
            catdict = open_json("database/references/characters_ref.json")
            categories = []
            
            for key in catdict[wbrace][wbsource][wbwarband]:
                if catdict[wbrace][wbsource][wbwarband][key]["ishero"] == True:
                    categories.append(key)

            category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
            if okPressed and category:
                new_hero = Hero.create_character(
                    name=name,
                    race=wbrace,
                    source=wbsource,
                    warband=wbwarband,
                    category=category,
                )

                wbidgold = self.mainwindow.wbid.treasury.gold
                heroprice = catdict[wbrace][wbsource][wbwarband][category]["price"]
                if wbidgold >= heroprice:
                    self.mainwindow.wbid.treasury.gold = wbidgold - heroprice
                    self.mainwindow.wbid.herolist.append(new_hero)
                    self.mainwindow.currentunit = new_hero
                    self.mainwindow.initUI()
                else:
                    print("can't add new hero, lack of funds")

