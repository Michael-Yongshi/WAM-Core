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

from gui.widget_template import *
from gui.widget_warband import WidgetWarband
from gui.widget_items import WidgetItemsWarband
from gui.widget_system import WidgetSystem
from gui.widget_heroes import WidgetHeroes
from gui.widget_squads import WidgetSquads
from gui.widget_current import WidgetCurrent


class QMainApplication(QApplication):
    """A Dark styled application."""
    def __init__(self, *__args):
        super().__init__(*__args)
        
        QFontDatabase.addApplicationFont("source/schoensperger.otf")
        self.setStyle("Fusion")
        self.setPalette(QDarkPalette())
        # self.setFont(QFont("schoensperger", 20))
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
    

class WarbandOverview(QMainWindow):
    """The main window that everything runs in"""
    def __init__(self):
        super().__init__()
        self.wbid = Warband.create_template()
        self.currentunit = Character.create_template()
        self.currentthing = None
        self.initUI()

    def initUI(self):
       
        # Some window settings
        self.setWindowTitle('Warhammer Army Manager')
        self.setWindowIcon(QIcon('war_72R_icon.ico'))     

        # build overview
        nested_widget = self.set_nested_widget()

        self.setCentralWidget(nested_widget)
        self.showMaximized()

    def set_nested_widget(self):

        # vertical layout for top and char part
        overviewbox = QGridLayout()
        overviewbox.addWidget(self.set_topbox(), 0, 0, 1, 3)
        overviewbox.addWidget(self.set_botbox(), 1, 0, 3, 3)

        overviewboxframe = QBorderlessFrame()
        overviewboxframe.setLayout(overviewbox)

        return overviewboxframe

    def set_topbox(self):
        
        # top wrapping warband and system in the top horizontal layout
        topbox = QGridLayout()
        topbox.addWidget(WidgetWarband(self), 0, 0, 1, 4)
        topbox.addWidget(WidgetSystem(self), 0, 4, 1, 1)

        topboxframe = QBorderlessFrame()
        topboxframe.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        topboxframe.setLayout(topbox)

        return topboxframe

    def set_botbox(self):

        # wrapping heroes, squads and extra details in the bottom horizontal layout
        botbox = QGridLayout()
        botbox.addWidget(WidgetHeroes(self), 0, 0)
        botbox.addWidget(WidgetSquads(self), 0, 1)
        botbox.addWidget(WidgetCurrent(self), 0, 2, 1, 2)

        botboxframe = QBorderlessFrame()
        botboxframe.clicked.connect(self.remove_focus)
        botboxframe.setLayout(botbox)

        return botboxframe

    def remove_focus(self):
        self.currentunit = None
        self.initUI

def run():
    global app
    app = QMainApplication(sys.argv)
    global main
    main = WarbandOverview()
    sys.exit(app.exec_())
