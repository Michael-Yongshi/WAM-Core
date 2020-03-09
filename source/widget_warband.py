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
from source.widget_items import WidgetItemsWarband

class WidgetWarband(QRaisedFrame):
    def __init__(self, mainwindow, configfile = {}):
        super().__init__()

        self.mainwindow = mainwindow

        self.configfile = {
            'wbdetail': {'row': 0, 'column': 0, 'width': 2, 'height': 1, 'children': {
                'wbnamelabel': {'row': 0, 'column': 0, 'width': 1, 'height': 1, 'text': f"Name: <b>{self.mainwindow.wbid.name}</b>", 'tooltip': "Name",},
                'wbracelabel': {'row': 1, 'column': 0, 'width': 1, 'height': 1, 'text': f"Race: <b>{self.mainwindow.wbid.race}</b>", 'tooltip': "Race",},
                'wbsrclabel': {'row': 2, 'column': 0, 'width': 1, 'height': 1, 'text': f"Source: <b>{self.mainwindow.wbid.source}</b>", 'tooltip': "Source",},
                'wbtypelabel': {'row': 3, 'column': 0, 'width': 1, 'height': 1, 'text': f"Type: <b>{self.mainwindow.wbid.warband}</b>", 'tooltip': "Type",},
                'goldlabel': {'row': 0, 'column': 1, 'width': 1, 'height': 1, 'text': f"Gold: <b>{self.mainwindow.wbid.treasury.gold}</b>", 'tooltip': "This is the amount of gold your warband holds.",},
                'wyrdlabel': {'row': 2, 'column': 1, 'width': 1, 'height': 1, 'text': f"Wyrdstone: <b>{self.mainwindow.wbid.treasury.wyrd}</b>", 'tooltip': "This is the amount of wyrdstone (equivalent) your warband holds.",},
                },
            },
            'wbitembox': {'row': 0, 'column': 1, 'width': 1, 'height': 1,},
        }

        print(self.configfile)

        wbbox = QGridLayout()
        config =self.configfile['wbdetail']
        wbbox.addWidget(self.set_detailbox(), config['row'], config['column'], config['width'], config['height'])
        config =self.configfile['wbitembox']
        wbbox.addWidget(WidgetItemsWarband(self.mainwindow), config['row'], config['column'], config['width'], config['height'])

        self.setToolTip("Here you can explore details about your warband")
        self.setLayout(wbbox)

    def set_detailbox(self):
        
        wbdetail = QGridLayout()

        config = self.configfile['wbdetail']
        children = config['children']
        
        for key in children:
            config = children[key]
            label = QLabel()
            label.setText(config['text'])
            label.setToolTip(config['tooltip'])
            wbdetail.addWidget(label, config['row'], config['column'], config['width'], config['height'])

        printablerules = []
        for r in self.mainwindow.wbid.rulelist:
            printablerules += [r.name]

        wbdetailframe = QBorderlessFrame()
        wbdetailframe.setLayout(wbdetail)
        wbdetailframe.setToolTip(f"Special Rules: {printablerules}\n\n{self.mainwindow.wbid.description}")

        return wbdetailframe

    def dialog_treasury(self):
        
        newgold, okPressed = QInputDialog.getInt(self, 'Gold change', f"Change gold amount to:", self.mainwindow.wbid.treasury.gold, 0, 99999, 1)
        if okPressed:
            self.mainwindow.wbid.treasury.gold = newgold

        newwyrd, okPressed = QInputDialog.getInt(self, 'Wyrd change', f"Change wyrd amount to:", self.mainwindow.wbid.treasury.wyrd, 0, 99999, 1)
        if okPressed:
            self.mainwindow.wbid.treasury.wyrd = newwyrd

        # relaunch ui to process changes in ui
        self.initUI()