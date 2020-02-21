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
from source.widget_items import WidgetItemsWarband
from source.widget_system import WidgetSystem
from source.widget_heroes import WidgetHeroes
from source.widget_squads import WidgetSquads


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
        self.wbid = create_template_wb()
        self.currentunit = create_template_char()
        self.currentthing = None
        self.initUI()

    def initUI(self):
       
        # Some window settings
        self.setWindowTitle('WAM')
        self.setToolTip('Warhammer Army Manager')
        self.setWindowIcon(QIcon('war_72R_icon.ico'))     

        # build overview
        nested_widget = self.set_nested_widget()

        self.setCentralWidget(nested_widget)
        self.showMaximized()

    def set_nested_widget(self):
        # build top part
        topboxwidget = self.set_topbox()

        # build bot part
        botboxwidget = self.set_botbox()

        # vertical layout for top and char part
        overviewbox = QGridLayout()
        overviewbox.addWidget(topboxwidget, 0, 0, 1, 3)
        overviewbox.addWidget(botboxwidget, 1, 0, 3, 3)
        overviewboxwidget = QBorderedWidget()
        overviewboxwidget.setLayout(overviewbox)

        return overviewboxwidget

    def set_topbox(self):
        # top wrapping warband and system in the top horizontal layout
        topbox = QHBoxLayout()
        topbox.addWidget(self.set_wbname())
        topbox.addWidget(self.set_wbinvbox())
        topbox.addWidget(WidgetSystem(self))
        topboxwidget = QBorderedWidget()
        topboxwidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        topboxwidget.setLayout(topbox)

        return topboxwidget

    def set_botbox(self):
        # wrapping heroes, squads and extra details in the bottom horizontal layout
        botbox = QGridLayout()
        botbox.addWidget(WidgetHeroes(self), 0, 0)
        botbox.addWidget(WidgetSquads(self), 0, 1)
        botbox.addWidget(WidgetCurrent(self), 0, 2, 1, 2)
        botboxwidget = QInteractiveWidget()
        botboxwidget.clicked.connect(self.remove_focus)
        botboxwidget.setLayout(botbox)

        return botboxwidget

    def set_wbinvbox(self):
        # Top middle
        wbinvbox = QHBoxLayout()
        treabox = QVBoxLayout()

        goldlabel = QLabel()
        goldlabel.setText("Gold: " + str(self.wbid.treasury.gold))
        goldlabel.setToolTip("This is the amount of gold your warband holds.")
        treabox.addWidget(goldlabel)
        wyrdlabel = QLabel()
        wyrdlabel.setText("Wyrdstones: " + str(self.wbid.treasury.wyrd))
        wyrdlabel.setToolTip("This is the amount of wyrdstones, or their equivalent, your warband holds.")
        treabox.addWidget(wyrdlabel)
        
        treaboxwidget = QInteractiveWidget()
        treaboxwidget.setLayout(treabox)
        treaboxwidget.clicked.connect(self.dialog_treasury)
        wbinvbox.addWidget(treaboxwidget)

        # add item widget   
        wbinvbox.addWidget(WidgetItemsWarband(self)) # adds the item layout to the grid

        wbinvboxwidget = QBorderedWidget()
        wbinvboxwidget.setLayout(wbinvbox)

        return wbinvboxwidget

    def set_wbname(self):
        # top left warband info
        wbnamelabel = QLabel()
        wbnamelabel.setText("Name: " + self.wbid.name)
        wbracelabel = QLabel()
        wbracelabel.setText("Race: " + self.wbid.race)
        wbsrclabel = QLabel()
        wbsrclabel.setText("Source: " + self.wbid.source)
        wbtypelabel = QLabel()
        wbtypelabel.setText("Type: " + self.wbid.warband)

        wbbox = QVBoxLayout()
        wbbox.addWidget(wbnamelabel)
        wbbox.addWidget(wbracelabel)
        wbbox.addWidget(wbsrclabel)
        wbbox.addWidget(wbtypelabel)

        wbboxwidget = QBorderedWidget()
        wbboxwidget.setLayout(wbbox)
        
        # make rules printable for tooltip
        printablerules = []
        for r in self.wbid.rulelist:
            printablerules += [r.name]
    
        wbboxwidget.setToolTip(f"Special Rules: {printablerules}\n\n{self.wbid.description}")

        # update wb info
        

        return wbboxwidget

    def dialog_treasury(self):
        
        newgold, okPressed = QInputDialog.getInt(self, 'Gold change', f"Change gold amount to:", self.wbid.treasury.gold, 0, 99999, 1)
        if okPressed:
            self.wbid.treasury.gold = newgold

        newwyrd, okPressed = QInputDialog.getInt(self, 'Wyrd change', f"Change wyrd amount to:", self.wbid.treasury.wyrd, 0, 99999, 1)
        if okPressed:
            self.wbid.treasury.wyrd = newwyrd

        # relaunch ui to process changes in ui
        self.initUI()

    def remove_focus(self):
        self.currentunit = None
        self.initUI

def run():
    global app
    app = QMainApplication(sys.argv)
    global main
    main = WarbandOverview()
    sys.exit(app.exec_())
