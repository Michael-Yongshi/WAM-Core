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
    QDialog,
    QDialogButtonBox,
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

from gui.widget_template import *
from gui.widget_items import WidgetItemsWarband

class WidgetWarband(QRaisedFrame):
    def __init__(self, mainwindow, configfile = {}):
        super().__init__()

        self.mainwindow = mainwindow

        self.configfile = {
            'wbdetail': {'row': 0, 'column': 0, 'width': 2, 'height': 1, 'children': {
                'wbnamelabel': {'row': 0, 'column': 0, 'width': 1, 'height': 1, 'text': f"Name: <b>{self.mainwindow.wbid.name}</b>", 'tooltip': "Name", 'connect': self.dialog_name,},
                'wbracelabel': {'row': 1, 'column': 0, 'width': 1, 'height': 1, 'text': f"Race: <b>{self.mainwindow.wbid.race}</b>", 'tooltip': "Race", 'connect': "",},
                'wbsrclabel': {'row': 2, 'column': 0, 'width': 1, 'height': 1, 'text': f"Source: <b>{self.mainwindow.wbid.source}</b>", 'tooltip': "Source", 'connect': "",},
                'wbtypelabel': {'row': 3, 'column': 0, 'width': 1, 'height': 1, 'text': f"Type: <b>{self.mainwindow.wbid.warband}</b>", 'tooltip': "Type", 'connect': "",},
                'goldlabel': {'row': 0, 'column': 1, 'width': 1, 'height': 1, 'text': f"Gold: <b>{self.mainwindow.wbid.treasury.gold}</b>", 'tooltip': "This is the amount of gold your warband holds.", 'connect': self.dialog_gold,},
                'wyrdlabel': {'row': 2, 'column': 1, 'width': 1, 'height': 1, 'text': f"Wyrdstone: <b>{self.mainwindow.wbid.treasury.wyrd}</b>", 'tooltip': "This is the amount of wyrdstone (equivalent) your warband holds.", 'connect': self.dialog_wyrd,},
                'rules': {'row': 4, 'column': 0, 'width': 1, 'height': 1, 'text': f"<font>Rules</font>", 'tooltip': f"{self.mainwindow.wbid.get_rulelist()}", 'connect': "",},
                'description': {'row': 4, 'column': 1, 'width': 1, 'height': 1, 'text': f"<font>Description</font>", 'tooltip': f"{self.mainwindow.wbid.description}", 'connect': self.dialog_desc,},
                },
            },
            'wbitembox': {'row': 0, 'column': 1, 'width': 1, 'height': 1,},
        }

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
            label = QClickLabel()
            label.setText(config['text'])
            label.setToolTip(config['tooltip'])
            if config['connect'] != "":
                label.clicked.connect(config['connect'])
            wbdetail.addWidget(label, config['row'], config['column'], config['width'], config['height'])

        wbdetailframe = QBorderlessFrame()
        wbdetailframe.setLayout(wbdetail)

        return wbdetailframe

    def dialog_gold(self):
        
        newgold, okPressed = QInputDialog.getInt(self, 'Gold change', f"Change gold amount to:", self.mainwindow.wbid.treasury.gold, 0, 99999, 1)
        if okPressed:
            self.mainwindow.wbid.treasury.gold = newgold

        # relaunch ui to process changes in ui
        self.mainwindow.initUI()

    def dialog_wyrd(self):

        newwyrd, okPressed = QInputDialog.getInt(self, 'Wyrd change', f"Change wyrd amount to:", self.mainwindow.wbid.treasury.wyrd, 0, 99999, 1)
        if okPressed:
            self.mainwindow.wbid.treasury.wyrd = newwyrd

        # relaunch ui to process changes in ui
        self.mainwindow.initUI()
    
    def dialog_name(self):

        newname, okPressed = QInputDialog.getText(self, 'Name change', f"Change name to:", text=self.mainwindow.wbid.name)
        if okPressed and newname:
            self.mainwindow.wbid.name = newname

        # relaunch ui to process changes in ui
        self.mainwindow.initUI()

    def dialog_desc(self):

        desc_dialog = DescriptionDialog(self.mainwindow)

class DescriptionDialog(QDialog):
    def __init__(self, mainwindow):
        super().__init__()

        self.mainwindow = mainwindow

        self.text_edit = QTextEdit()
        self.text_edit.setText(self.mainwindow.wbid.description)

        self.buttonbox = QDialogButtonBox(self)

        self.buttonbox.addButton("Apply", QDialogButtonBox.AcceptRole)
        self.buttonbox.accepted.connect(self.apply)
        self.buttonbox.addButton("Cancel", QDialogButtonBox.RejectRole)
        self.buttonbox.rejected.connect(self.cancel)

        dialog_layout = QGridLayout()
        dialog_layout.addWidget(self.text_edit, 0, 0, 9, 1)
        dialog_layout.addWidget(self.buttonbox, 10, 0, 1, 1)
        
        self.setLayout(dialog_layout)
        self.resize(600, 800)
        self.setWindowTitle("Enter or change the description")
        self.setWindowModality(Qt.ApplicationModal)
        self.exec_()

    def apply(self):
        self.mainwindow.wbid.description = self.text_edit.toHtml()
        self.mainwindow.initUI()
        self.accept()

    def cancel(self):
        self.reject()