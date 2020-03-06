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

from source.methods_engine import (
    save_warband,
    load_warband,
    show_warbands,
    save_reference,
    load_reference,
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
from source.widget_items import WidgetItemsUnit
from source.widget_abilitymagic import WidgetAbility, WidgetMagic

# from source.widget_currentbox import *


class WidgetCurrent(QRaisedFrame):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        if self.mainwindow.currentunit.ishero != "":
            currentbox = QGridLayout()
            currentbox.addWidget(self.set_namebox(), 0, 0, 1, 1)
            currentbox.addWidget(self.set_skillbox(), 1, 0, 1, 1)
            currentbox.addWidget(self.set_listbox(), row = 2, column = 0, rowSpan = 4, columnSpan = 1)

            self.setToolTip("This is the currently selected unit")
            self.setLayout(currentbox)


    def set_namebox(self):
        namebox = QGridLayout()
        
        # Todo: create a table with the settings for these widgets and then use a for loop to generate the labels and put them in the box
        # after that, create a generic function that uses a conf file and loop over it generating gui. then we could replace the entire code here with just a call to this function.
        namelabel = QLabel()
        namelabel.setText(f"Name: <b>{self.mainwindow.currentunit.name}</b>")    
        namebox.addWidget(namelabel, row = 0, column = 0)

        catlabel = QLabel()
        catlabel.setText(f"Category: <b>{self.mainwindow.currentunit.category}</b>")
        namebox.addWidget(catlabel, row = 1, column = 0)

        pricelabel = QLabel()
        pricelabel.setText(f"Replacement Cost: <b>{self.mainwindow.currentunit.price}</b>")
        namebox.addWidget(pricelabel, row = 2, column = 0)

        maxlabel = QLabel()
        maxlabel.setText(f"Max Units: <b>{self.mainwindow.currentunit.maxcount}</b>")
        namebox.addWidget(maxlabel, row = 2, column = 1)

        explabel = QLabel()
        explabel.setText(f"Experience: <b>{self.mainwindow.currentunit.experience}</b>")
        explabel.setToolTip(f"Next Advance at experience: <b> 8 </b>")
        namebox.addWidget(explabel, 0, 1)

        nameframe = QBorderlessFrame()
        nameframe.setLayout(namebox)
        
        return nameframe

    def set_skillbox(self):
        #show skills in middle
        skillbox = QHBoxLayout() # create a horizontal layout to show the skills in a neat line
        
        skilldict = self.mainwindow.currentunit.get_total_skilldict()
        for key in skilldict:
            label = QLabel()
            label.setText(f"<b>{key[:2]}<br/>{skilldict[key]}</b>")
            label.setToolTip(f"The total <b>{key}</b> skill, <br/>including both base model scores and item influences.")
            label.setAlignment(Qt.AlignCenter)
            box = QVBoxLayout()
            box.addWidget(label)
            frame = QFlatFrame()
            frame.setLayout(box)
            skillbox.addWidget(frame)

        skillframe = QBorderlessFrame()
        skillframe.setLayout(skillbox)

        return skillframe

    def set_listbox(self):
        
        listbox = QGridLayout()

        # for character
        listbox.addWidget(WidgetAbility(self.mainwindow, abilitylist = self.mainwindow.currentunit.abilitylist, skip = False), 0, 0) # adds the ability layout to the grid
        listbox.addWidget(WidgetMagic(self.mainwindow), 1, 0) # adds the magic layout to the grid

        # now for every item repeated
        listbox.addWidget(WidgetItemsUnit(self.mainwindow), 0, 1, 2, 2)
        
        listframe = QBorderlessFrame()
        listframe.setLayout(listbox)
        
        return listframe