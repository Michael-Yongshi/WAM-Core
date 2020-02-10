# pip3 install --user pyqt5

import sys

from PyQt5.QtCore import (
    QRect,
    Qt,
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
    QTableWidget,
    QTableWidgetItem,
    QToolTip, 
    QVBoxLayout,
    QWidget, 
    )

from PyQt5.QtGui import (
    QColor,
    QFont,
    QIcon,
    QPalette,
    )

from generic_methods import (
    save_warband,
    load_warband,
    show_saved_warbands,
    get_current_warband,
)


class QBorderedWidget(QWidget):
    """A widget which is the default, but with some different stylesheet details (borders)"""
    def __init__(self, *args):
        super().__init__(*args)

        self.setStyleSheet("border: 1px solid rgb(100, 100, 100)")

class QDarkPalette(QPalette):
    """A Dark palette meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)

        self.setColor(QPalette.Window, QColor(53, 53, 53))          #dark grey
        self.setColor(QPalette.WindowText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.Base, QColor(25, 25, 25))            #darker grey
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))   #dark grey
        self.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))  #white
        self.setColor(QPalette.ToolTipText, QColor(255, 255, 255))  #white
        self.setColor(QPalette.Text, QColor(255, 255, 255))         #white
        self.setColor(QPalette.Button, QColor(53, 53, 53))          #dark grey
        self.setColor(QPalette.ButtonText, QColor(255, 255, 255))   #white
        self.setColor(QPalette.BrightText, QColor(255, 0, 0))       #red
        self.setColor(QPalette.Link, QColor(42, 130, 218))          #blue
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))     #blue
        self.setColor(QPalette.HighlightedText, QColor(0, 0, 0))    #black

       
class WarbandOverview(QMainWindow):
    """The main window that everything runs in"""
    def __init__(self):
        super().__init__()

        self.wbid = get_current_warband()
        self.initUI()

    def initUI(self):
        
        # Some window settings
        self.setWindowTitle('Warband Manager')
        self.setToolTip('This is your <b>Warband</b> overview')
        self.setWindowIcon(QIcon('icon.png'))     

        # buttons for interaction     
        btnchoose = QPushButton('Choose Warband', self)
        btnchoose.setToolTip('Choose an existing <b>Warband</b>')
        btnchoose.clicked.connect(self.choose_warband)

        btncreate = QPushButton('Create Warband', self)
        btncreate.setToolTip('Create a new <b>Warband</b>')
        btncreate.clicked.connect(self.create_warband)
        
        btnquit = QPushButton('Quit', self)
        btnquit.setToolTip('Quit the program')
        btnquit.clicked.connect(QApplication.instance().quit)

        # top right
        sysbox = QVBoxLayout()
        sysbox.addWidget(btncreate)
        sysbox.addWidget(btnchoose)
        sysbox.addWidget(btnquit)
        sysboxwidget = QBorderedWidget()
        sysboxwidget.setLayout(sysbox)

        # top left warband info
        wbnamelabel = QLabel()
        wbnamelabel.setToolTip('This is your <b>Warband`s</b> name')
        wbbox = QVBoxLayout()
        wbbox.addWidget(wbnamelabel)
        wbboxwidget = QBorderedWidget()
        wbboxwidget.setLayout(wbbox)

        # update wb info
        wbnamelabel.setText("Your warband " + self.wbid.name)

        # top wrapping warband and system in the top horizontal layout
        topbox = QHBoxLayout()
        topbox.addWidget(wbboxwidget)
        topbox.addWidget(sysboxwidget)
        topboxwidget = QBorderedWidget()
        topboxwidget.setLayout(topbox)

        # left bottom heroes
        herobox = QVBoxLayout()
        for hero in self.wbid.herolist:
            herogrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText(hero.name)
            herogrid.addWidget(namelabel, 0, 0)
            catlabel = QLabel()
            catlabel.setText(hero.category)
            herogrid.addWidget(catlabel, 1, 0)
            skilllabel = QLabel()
            skilllabel.setText("skills: m1, ws1, bs1, s1, t1, a1, i1, w1, ld1, as1")
            herogrid.addWidget(skilllabel, 3, 0)
            explabel = QLabel()
            explabel.setText("Level: " + str(hero.experience))
            herogrid.addWidget(explabel, 2, 0)
            herowidget = QBorderedWidget()
            herowidget.setLayout(herogrid)
            herobox.addWidget(herowidget)

        heroboxwidget = QBorderedWidget()
        heroboxwidget.setLayout(herobox)
        heroboxwidget.setToolTip('These are your <b>heroes</b>')

        # right bottom squads
        squadbox = QVBoxLayout()
        for squad in self.wbid.squadlist:
            squadgrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText(squad.name)
            squadgrid.addWidget(namelabel, 0, 0)
            numberlabel = QLabel()
            numberlabel.setText(str(squad.get_totalhenchman()))
            squadgrid.addWidget(numberlabel, 1, 0)
            squadwidget = QBorderedWidget()
            squadwidget.setLayout(squadgrid)
            squadbox.addWidget(squadwidget)
        squadboxwidget = QBorderedWidget()
        squadboxwidget.setLayout(squadbox)
        squadboxwidget.setToolTip('These are your <b>squads</b>')

        # wrapping heroes and squads in the bottom horizontal layout
        botbox = QHBoxLayout()
        botbox.addWidget(heroboxwidget)
        botbox.addWidget(squadboxwidget)
        botboxwidget = QBorderedWidget()
        botboxwidget.setLayout(botbox)

        # vertical layout for top and char part
        overviewbox = QVBoxLayout()
        overviewbox.addWidget(topboxwidget)
        overviewbox.addWidget(botboxwidget)
        overviewboxwidget = QBorderedWidget()
        overviewboxwidget.setLayout(overviewbox)

        self.setCentralWidget(overviewboxwidget)
        self.showMaximized()

    def create_warband(self):
        """Create a new warband and store it in cache"""
        warband, okPressed = QInputDialog.getText(self, "Create", "Name your warband:")
        if okPressed and warband:
            print(warband)

    def choose_warband(self):
        """Choose a warband to be loaded into cache and then shown on screen"""
        warbands = show_saved_warbands()
        wbname, okPressed = QInputDialog.getItem(self, "Choose", "Choose your warband", warbands, 0, False)
        if okPressed and wbname:
            load_warband(wbname)                # Load from save json into cache json
            self.wbid = get_current_warband()   # bring cache json to python obj (warband class .from_dict method)
            self.initUI()                       # Restart the window to force changes
            

if __name__ == '__main__':
    # Create an application in the OS with the class
    # App().start()

    # Create an application manually
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(QDarkPalette())
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
    main = WarbandOverview()

    # Make sure we can exit the application object normally
    sys.exit(app.exec_())
