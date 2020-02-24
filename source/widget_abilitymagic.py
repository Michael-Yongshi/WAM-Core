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



class WidgetAbility(QBorderlessFrame):
    def __init__(self, mainwindow, abilitylist, skip):
        super().__init__()

        self.mainwindow = mainwindow
        self.abilitylist = abilitylist
        self.skip = skip

        #show abilities
        abilitybox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for ability in abilitylist:
            label = QLabel()
            label.setText(f"{ability.name}")
            label.setToolTip(f"<font><b>{ability.name}</b> <br/><br/> {ability.description}</font>")
            box = QVBoxLayout()
            box.addWidget(label)
            frame = QRaisedFrame()
            frame.setLayout(box)
            # label.clicked.connect(self.create_method_remove(unit = unit, ability = ability)
            abilitybox.addWidget(frame) #adds the ability to a label and at it to the vertical ability layout
        
        # add new ability widget
        if skip == False:
            label = QClickLabel()
            label.setText("New Ability")
            label.setToolTip(f"Add manually a new ability for this unit.")
            label.clicked.connect(self.create_method_new_ability(unit=self.mainwindow.currentunit))
            abilitybox.addWidget(label) #adds the ability to a label and at it to the vertical item layout

        self.setLayout(abilitybox)

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

class WidgetMagic(QBorderlessFrame):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        #show magic
        magicbox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for magic in self.mainwindow.currentunit.get_magiclist():
            label = QLabel()
            label.setText(str(magic.name))
            label.setToolTip(f"<font><b>{magic.name}</b> <br/>Difficulty: {magic.difficulty} <br/><br/> {magic.description}</font>")
            box = QVBoxLayout()
            box.addWidget(label)
            frame = QRaisedFrame()
            frame.setLayout(box)
            # label.clicked.connect(self.create_method_remove(unit = unit, magic = magic)
            magicbox.addWidget(frame) #adds the magic to a label and at it to the vertical magic layout

        # add new magic widget
        label = QClickLabel()
        label.setText("New Magic")
        label.setToolTip(f"Add manually a new magic skill for this unit.")
        label.clicked.connect(self.create_method_new_magic(unit=self.mainwindow.currentunit))
        magicbox.addWidget(label) #adds the magic to a label and at it to the vertical item layout

        self.setLayout(magicbox)

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