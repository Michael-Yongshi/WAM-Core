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

from source.gui_template import *


class WidgetSystem(QBorderedWidget):
    def __init__(self):
        super().__init__()
        sysbox = QGridLayout()
        
        # buttons for interaction
        btnchoose = QPushButton('Choose Warband', self)
        btnchoose.setToolTip('Choose an existing <b>Warband</b>')
        btnchoose.clicked.connect(self.choose_warband)

        btncreate = QPushButton('Create Warband', self)
        btncreate.setToolTip('Create a new <b>Warband</b>')
        btncreate.clicked.connect(self.create_warband)

        btnsave = QPushButton('Save Warband', self)
        btnsave.setShortcut("Ctrl+S")
        btnsave.setToolTip('Save current <b>Warband</b>')
        btnsave.clicked.connect(self.save_warband)

        # btnquit = QPushButton('Quit', self)
        # btnquit.setToolTip('Quit the program')
        # btnquit.clicked.connect(QApplication.instance().quit)

        sysbox.addWidget(btncreate, 0, 0)
        sysbox.addWidget(btnsave, 0, 1)
        sysbox.addWidget(btnchoose, 1, 0)
        # sysbox.addWidget(btnquit, 1, 1)

        self.setLayout(sysbox)

    def choose_warband(self):
        """Choose a warband to be loaded into cache and then shown on screen"""
        warbands = show_saved_warbands()                                                                            # get list of save files
        wbname, okPressed = QInputDialog.getItem(self, "Choose", "Choose your warband", warbands, 0, False)         # Let user choose out of save files
        if okPressed and wbname:
            self.wbid = load_warband(wbname)                                                                        # set warband object based on save file
            self.currentunit = self.create_template_char()                                                          # set empty current unit
            self.initUI()                                                                                           # Restart the window to force changes

    def save_warband(self):
        """Save warband to cache and then to saves"""
        save_warband(self.wbid)                # save wbid to json
        cache_warband(self.wbid)                #set to run next time at stsrtup
        message = QMessageBox.information(self, "Saved", "Save successful!", QMessageBox.Ok)

    def create_warband(self):
        """Create a new warband and store it in cache"""
        name, okPressed = QInputDialog.getText(self, "Create", "Name your warband:")
        if okPressed and name:
            
            # get all races in references
            chardict = open_json("database/references/warbands_ref.json")

            races = []
            for key in chardict:
                races.append(key)

            race, okPressed = QInputDialog.getItem(self, "Create", "Choose a race", races, 0, False)
            if okPressed and race:

                sources = []
                for key in chardict[race]:
                    sources.append(key)

                source, okPressed = QInputDialog.getItem(self, "Create", "Choose a source", sources, 0, False)
                if okPressed and source:

                    warbands = []
                    for key in chardict[race][source]:
                        warbands.append(key)

                    warband, okPressed = QInputDialog.getItem(self, "Create", "Choose a warband", warbands, 0, False)
                    if okPressed and warband:
                        self.wbid = Warband.create_warband(name=name, race=race, source=source, warband=warband)
                        self.currentunit = self.create_template_char()
                        self.initUI()
