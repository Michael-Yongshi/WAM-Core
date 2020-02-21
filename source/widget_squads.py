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
from source.widget_items import WidgetItemsSquad
# from source.widget_currentbox import *



class WidgetSquads(QBorderedWidget):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        squadbox = QVBoxLayout()

        s = 0
        for squad in self.mainwindow.wbid.squadlist:
            s += 1
            squadgrid = QGridLayout()
            
            numlabel = QLabel()
            numlabel.setText(str(squad.get_totalhenchman()))
            numbox = QVBoxLayout()
            numbox.addWidget(numlabel)
            numwidget = QInteractiveWidget()
            numwidget.setLayout(numbox)
            numwidget.clicked.connect(self.create_method_change_number(squad))
            squadgrid.addWidget(numwidget, 0, 0, 1, 1)

            namelabel = QLabel()
            if squad.henchmanlist[0] == self.mainwindow.currentunit:
                namelabel.setText(squad.name + " (selected)")
            else:
                namelabel.setText(squad.name)
            squadgrid.addWidget(namelabel, 0, 1, 1, 3)
            
            catlabel = QLabel()
            catlabel.setText(squad.henchmanlist[0].category)
            catlabel.setToolTip(f"This is your squad`s unit type. The unit type determines what the squads abilities are, what kind of items it can carry and how expensive it is to replace.")
            squadgrid.addWidget(catlabel, 0, 4, 1, 3) 
            
            # sets the complete squad grid layout to a squadwidget in order to add to the vertical list
            squadwidget = QInteractiveWidget()
            squadwidget.setLayout(squadgrid)
            
            squadwidget.clicked.connect(self.create_method_focus(squad))
            squadbox.addWidget(squadwidget)

        if s <= 5:
            s += 1
            squadgrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText("Add New Squad")
            squadgrid.addWidget(namelabel, 0, 0)

            squadwidget = QInteractiveWidget()
            squadwidget.setLayout(squadgrid)
            squadwidget.clicked.connect(self.create_new)
            squadbox.addWidget(squadwidget)

        while s <= 5:
            s += 1
            squadwidget = QUnBorderedWidget()
            squadbox.addWidget(squadwidget)

        self.setToolTip('These are your <b>squads</b>')
        self.setLayout(squadbox)

    def create_method_focus(self, squad):          
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current unit and then passes it to the currentunit attribute of the main window"""
        
        def focus_unit():
            
            self.mainwindow.currentunit = squad.henchmanlist[0]
            self.mainwindow.initUI()

        return focus_unit

    def create_method_change_number(self, squad):          
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current item and then creates a window based on the attribute"""

        def change_number():

            currentsize = squad.get_totalhenchman()
            newsize, okPressed = QInputDialog.getInt(self, 'Squad members', f"Change squad size to:", currentsize, 0, 6, 1)
            if okPressed:
                if newsize != 0:
                    deltasize = newsize - currentsize
                    squad.change_henchman_count(deltasize)
                    process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                    if process_gold == QMessageBox.Yes:
                        deltagold = deltasize * squad.henchmanlist[0].get_price()
                        if deltagold < self.mainwindow.wbid.treasury.gold:
                            self.mainwindow.wbid.treasury.gold -= deltagold
                            self.mainwindow.initUI()
                        else:
                            print("Lack of funds")
                    else:
                        self.mainwindow.initUI()
                    
                else:
                    print("Can't remove the last member, please disband the whole squad")

        return change_number

    def create_method_remove(self, squad): 
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current squad and then creates a window based on the attribute"""

        def remove():

            remove = QMessageBox.question(self, 'Remove squad', f"Do you want to remove this squad?", QMessageBox.Yes | QMessageBox.No)
            if remove == QMessageBox.Yes:
                process_gold = QMessageBox.question(self, "Process gold", "Do you want to process an exchange for gold?", QMessageBox.Yes | QMessageBox.No)
                squadprice = 0

                for squad in self.mainwindow.wbid.squadlist:
                    if squad.henchmanlist[0] == self.mainwindow.currentunit:
                        if process_gold == QMessageBox.Yes:
                            squadsize = len(squad.henchmanlist)
                            henchprice = self.mainwindow.currentunit.price
                            for item in self.mainwindow.currentunit.itemlist:
                                henchprice += item.price
                            squadprice = henchprice * squadsize
                        index = self.mainwindow.wbid.squadlist.index(squad)
                        self.mainwindow.wbid.squadlist.pop(index)
                        break

                self.mainwindow.wbid.treasury.gold += squadprice
                self.mainwindow.initUI()
        
        return remove

    def create_new(self):
        """Create a new squad and store it in this warband"""

        name, okPressed = QInputDialog.getText(self, "Create", "Name your squad:")
        if okPressed and name:
            
            # get all categories in references
            wbrace = self.mainwindow.wbid.race
            wbsource = self.mainwindow.wbid.source
            wbwarband = self.mainwindow.wbid.warband
            catdict = open_json("database/references/characters_ref.json")
            categories = []
            
            for key in catdict[wbrace][wbsource][wbwarband]:
                if catdict[wbrace][wbsource][wbwarband][key]["ishero"] == False:
                    categories.append(key)

            category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
            if okPressed and category:
                new_squad = Squad.create_squad(
                    name=name,
                    race=wbrace,
                    source=wbsource,
                    warband=wbwarband,
                    category=category,
                )

                if new_squad.henchmanlist[0] != None:

                    wbidgold = self.mainwindow.wbid.treasury.gold
                    squadprice = catdict[wbrace][wbsource][wbwarband][category]["price"]
                    if wbidgold >= squadprice:
                        self.mainwindow.wbid.treasury.gold = wbidgold - squadprice
                        self.mainwindow.wbid.squadlist.append(new_squad)
                        self.mainwindow.currentunit = new_squad.henchmanlist[0]
                        self.mainwindow.initUI()
                    else:
                        message = QMessageBox.information(self, "Can't add squad!", "Lack of funds!", QMessageBox.Ok)
                else:
                    message = QMessageBox.information(self, "Can't add squad!", "Heroes can't be added to a squad!", QMessageBox.Ok)