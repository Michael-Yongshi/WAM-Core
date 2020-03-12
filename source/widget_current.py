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
    def __init__(self, mainwindow, configfile = {}):
        super().__init__()

        self.mainwindow = mainwindow

        self.configfile = {
            'namebox': {'row': 0, 'column': 0, 'width': 1, 'height': 1, 'children': {
                'namelabel': {'row': 0, 'column': 0, 'width': 1, 'height': 1, 'text': f"Name: <b>{self.mainwindow.currentunit.name}</b>", 'tooltip': "Name", 'connect': self.create_method_change_name(self.mainwindow.currentunit.name)},
                'catlabel': {'row': 1, 'column': 0, 'width': 1, 'height': 1, 'text': f"Category: <b>{self.mainwindow.currentunit.category}</b>", 'tooltip': "Category", 'connect': ""},
                'pricelabel': {'row': 2, 'column': 0, 'width': 1, 'height': 1, 'text': f"Price: <b>{self.mainwindow.currentunit.price}</b>", 'tooltip': "Price", 'connect': "",},
                'maxlabel': {'row': 2, 'column': 1, 'width': 1, 'height': 1, 'text': f"Maximum: <b>{self.mainwindow.currentunit.maxcount}</b>", 'tooltip': "Maximum", 'connect': "",},
                'explabel': {'row': 0, 'column': 1, 'width': 1, 'height': 1, 'text': f"Experience: <b>{self.mainwindow.currentunit.experience}</b>", 'tooltip': f"Next Advance at experience: <b> 8 </b>", 'connect': self.create_method_change_experience(self.mainwindow.currentunit.experience),},
                }
            },
            'skillbox': {'row': 1, 'column': 0, 'width': 1, 'height': 1,
            },
            'listbox': {'row': 2, 'column': 0, 'width': 4, 'height': 1,
            },
        }

        if self.mainwindow.currentunit.ishero != "":
            currentbox = QGridLayout()

            config = self.configfile['namebox']
            currentbox.addWidget(self.set_namebox(), config['row'], config['column'], config['width'], config['height'])

            config = self.configfile['skillbox']
            currentbox.addWidget(self.set_skillbox(), config['row'], config['column'], config['width'], config['height'])

            config = self.configfile['listbox']
            currentbox.addWidget(self.set_listbox(), config['row'], config['column'], config['width'], config['height'])

            self.setToolTip("This is the currently selected unit")
            self.setLayout(currentbox)

    def set_namebox(self):
        namebox = QGridLayout()
        
        config = self.configfile['namebox']
        children = config['children']
        
        for key in children:
            config = children[key]
            label = QClickLabel()
            label.setText(config['text'])
            label.setToolTip(config['tooltip'])
            if config['connect'] != "":
                label.clicked.connect(config['connect'])
            namebox.addWidget(label, config['row'], config['column'], config['width'], config['height'])

        nameframe = QBorderlessFrame()
        nameframe.setLayout(namebox)
        
        return nameframe

    def set_skillbox(self):
        #show skills in middle
        skillbox = QHBoxLayout() # create a horizontal layout to show the skills in a neat line
        
        skilldict = self.mainwindow.currentunit.get_total_skilldict()
        for key in skilldict:
            label = QLabel()
            label.setText(f"<b>{key[:2]}<br/>{skilldict[key]['total']}</b>")
            
            # build tooltip - base
            tooltip = f"The total <b>{key}</b> skill of this character<br/><br/>The base {key} of this character is: {skilldict[key]['children']['base']}<br/>"
            # add events
            tooltip += "<br/>The change due to events is: <br/>"
            for key2 in skilldict[key]['children']:
                if key2 == 'event':
                    tooltip += f" - {key2}: {skilldict[key]['children'][key2]}<br/"
            # add items
            tooltip += "<br/>The change due to items is: <br/>"
            for key2 in skilldict[key]['children']:
                if key2[:4] == 'item':
                    tooltip += f" - {key2[6:]}: {skilldict[key]['children'][key2]}<br/>"
                    print(tooltip)

            label.setToolTip(tooltip)

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

    def create_method_change_name(self, name):
        
        def change_name():
            new_name, okPressed = QInputDialog.getText(self, "Choose a name", "Name your unit:", text="default")
            if okPressed and new_name:
                self.mainwindow.currentunit.name = new_name
                self.mainwindow.initUI()
        
        return change_name

    def create_method_change_experience(self, experience):
        
        def change_experience():
            change_experience, okPressed = QInputDialog.getInt(self, "Change Experience", "How much to increase or decrease the experience?", 0, -99, 99, 1)
            if okPressed and change_experience:
                new_experience = self.mainwindow.currentunit.experience + change_experience
                self.mainwindow.currentunit.experience = new_experience
                self.mainwindow.initUI()
        
        return change_experience