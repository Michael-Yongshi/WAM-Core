# pip3 install --user pyqt5

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


class QInteractiveWidget(QBorderedWidget):
    """A bordered widget, but which is clickable"""
    def __init__(self, *args):
        super().__init__(*args)

    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if app.mouseButtons() & Qt.LeftButton:
            self.clicked.emit()

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

        # Top middle
        topmidbox = QHBoxLayout()
        wbdesclabel = QLabel()
        wbdesclabel.setText(self.wbid.description)
        wbdesclabel.setWordWrap(True)
        wbdesclabel.setToolTip("this is your warbands description")
        topmidbox.addWidget(wbdesclabel)
        topmidboxwidget = QBorderedWidget()
        topmidboxwidget.setLayout(topmidbox)

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
        topbox.addWidget(topmidboxwidget)
        topbox.addWidget(sysboxwidget)
        topboxwidget = QBorderedWidget()
        topboxwidget.setLayout(topbox)

        # left bottom heroes
        herobox = QVBoxLayout() # To show all heroes below each other dynamically (based on actual number of heroes)
        h = 0
        for hero in self.wbid.herolist:
            h += 1
            herogrid = QGridLayout() # create a grid layout to position all information more accurately
            
            #show name and experience at top left corner of the grid
            namebox = QHBoxLayout() # combine name and category to place on single row beside each other

            namelabel = QLabel()
            namelabel.setText(hero.name)
            namelabel.setToolTip(f"This is your hero`s name")
            namebox.addWidget(namelabel) #create name label and set it to the namebox layout
            explabel = QLabel()
            explabel.setText(f"Experience: {hero.experience}")
            explabel.setToolTip(f"This is your hero`s experience. Next level up at 30 experience.")
            namebox.addWidget(explabel) # #create experience label and set it to the namebox layout

            namewidget = QBorderedWidget()
            namewidget.setLayout(namebox)
            herogrid.addWidget(namewidget, 0, 0) # add the name and category box to the herogrid
            
            #show race and category at top left corner of the grid
            catbox = QHBoxLayout() # combine cat and category to place on single row beside each other

            catlabel = QLabel()
            catlabel.setText(hero.category)
            catlabel.setToolTip(f"This is your hero`s unit type. The unit type determines what the heroes abilities are, what kind of items it can carry and how expensive it is to replace.")
            catbox.addWidget(catlabel) #create category label and set it to the catbox layout
            racelabel = QLabel()
            racelabel.setText(f"{hero.race}")
            racelabel.setToolTip(f"This is your hero`s race. Usually your warband consists of mostly the same race, although hired swords and other characters can deviate from this")
            catbox.addWidget(racelabel) # #create race label and set it to the catbox layout

            catwidget = QBorderedWidget()
            catwidget.setLayout(catbox)
            herogrid.addWidget(catwidget, 1, 0) # add the cat and category box to the herogrid

            #show skills at bottom left
            skillbox = QHBoxLayout() # create a horizontal layout to show the skills in a neat line

            mlabel = QLabel()
            mlabel.setText("Mov\n" + str(hero.skill.movement))
            skillbox.addWidget(mlabel) #adds the movement skill to a label and at it to the horizontal skill layout
            wslabel = QLabel()
            wslabel.setText("Ws\n" + str(hero.skill.weapon))
            skillbox.addWidget(wslabel)
            bslabel = QLabel()
            bslabel.setText("Bs\n" + str(hero.skill.ballistic))
            skillbox.addWidget(bslabel)
            slabel = QLabel()
            slabel.setText("Str\n" + str(hero.skill.strength))
            skillbox.addWidget(slabel)
            tlabel = QLabel()
            tlabel.setText("Tou\n" + str(hero.skill.toughness))
            skillbox.addWidget(tlabel)
            wlabel = QLabel()
            wlabel.setText("Wou\n" + str(hero.skill.wounds))
            skillbox.addWidget(wlabel)
            ilabel = QLabel()
            ilabel.setText("Ini\n" + str(hero.skill.initiative))
            skillbox.addWidget(ilabel)
            aclabel = QLabel()
            aclabel.setText("Act\n" + str(hero.skill.actions))
            skillbox.addWidget(aclabel)
            ldlabel = QLabel()
            ldlabel.setText("Ld\n" + str(hero.skill.leadership))
            skillbox.addWidget(ldlabel)
            aslabel = QLabel()
            aslabel.setText("As\n" + str(hero.skill.armoursave))
            skillbox.addWidget(aslabel)
            
            skillwidget = QBorderedWidget()
            skillwidget.setLayout(skillbox)
            herogrid.addWidget(skillwidget, 2, 0) # adds the skill layout to the bottom left of the grid
            

            # #show abilities top 0 left -1
            # abilitybox = QVBoxLayout() # create a vertical layout to show them in a neat line

            # for ability in hero.abilitylist:
            #     label = QLabel()
            #     label.setText(str(ability.name))
            #     abilitybox.addWidget(label) #adds the ability to a label and at it to the vertical ability layout
            
            # abilitywidget = QBorderedWidget()
            # abilitywidget.setLayout(abilitybox)
            # herogrid.addWidget(abilitywidget, 0, 1) # adds the ability layout to the grid

            # #show magic top 0 left -1
            # magicbox = QVBoxLayout() # create a vertical layout to show them in a neat line

            # for magic in hero.magiclist:
            #     label = QLabel()
            #     label.setText(str(magic.name))
            #     magicbox.addWidget(label) #adds the magic to a label and at it to the vertical magic layout
            
            # magicwidget = QBorderedWidget()
            # magicwidget.setLayout(magicbox)
            # herogrid.addWidget(magicwidget, 1, 1) # adds the magic layout to the grid

            # #show items top -1 left -1
            # itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

            # for item in hero.itemlist:
            #     label = QLabel()
            #     label.setText(str(item.name))
            #     itembox.addWidget(label) #adds the item to a label and at it to the vertical item layout
            
            # itemwidget = QBorderedWidget()
            # itemwidget.setLayout(itembox)
            # herogrid.addWidget(itemwidget, 2, 1) # adds the item layout to the grid

            # sets the complete hero grid layout to a herowidget in order to add to the vertical list of heroes
            herowidget = QInteractiveWidget()
            herowidget.setLayout(herogrid)
            herowidget.clicked.connect(self.focus_hero)
            herobox.addWidget(herowidget)

        heroboxwidget = QBorderedWidget()
        heroboxwidget.setLayout(herobox)
        heroboxwidget.setToolTip('These are your <b>heroes</b>')

        # right bottom squads
        squadbox = QVBoxLayout()

        s = 0
        for squad in self.wbid.squadlist:
            s += 1
            squadgrid = QGridLayout()
            
            namelabel = QLabel()
            namelabel.setText(squad.name)
            squadgrid.addWidget(namelabel, 0, 0)
            numberlabel = QLabel()
            numberlabel.setText(str(squad.get_totalhenchman()))
            squadgrid.addWidget(numberlabel, 1, 0)

            # sets the complete squad grid layout to a squadwidget in order to add to the vertical list
            squadwidget = QInteractiveWidget()
            squadwidget.setLayout(squadgrid)
            squadwidget.clicked.connect(self.focus_squad)
            squadbox.addWidget(squadwidget)

        squadboxwidget = QBorderedWidget()
        squadboxwidget.setLayout(squadbox)
        squadboxwidget.setToolTip('These are your <b>squads</b>')

        currentbox = QGridLayout()

        currentname = QLabel()
        currentname.setText("Name of the selected unit")
        currentbox.addWidget(currentname)

        currentboxwidget = QBorderedWidget()
        currentboxwidget.setLayout(currentbox)
        currentboxwidget.setToolTip("Current unit details")
        

        # wrapping heroes, squads and extra details in the bottom horizontal layout
        botbox = QHBoxLayout()
        botbox.addWidget(heroboxwidget)
        botbox.addWidget(squadboxwidget)
        botbox.addWidget(currentboxwidget)
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

    def focus_hero(self):
        print(f"clicked hero {str(self)}")
            # change background of widget to light grey and text to black and borders to white
            # fill current widget with the hero or squad information

    def focus_squad(self):
        print(f"clicked squad")
        
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
