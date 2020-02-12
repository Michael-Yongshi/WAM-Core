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
    QTextEdit,
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

from class_hierarchy import (
    Character,
)

from class_components import (
    Skill,
)

class QBorderedWidget(QWidget):
    """A widget which is the default, but with some different stylesheet details (borders)"""
    def __init__(self, *args):
        super().__init__(*args)

        self.setStyleSheet("border: 1px solid rgb(100, 100, 100)")

class QUnBorderedWidget(QWidget):
    """A widget which is the default, but with some different stylesheet details (borders)"""
    def __init__(self, *args):
        super().__init__(*args)

        self.setStyleSheet("border: 0px")

class QInteractiveWidget(QBorderedWidget):
    """A bordered widget, but which is clickable"""
    def __init__(self, *args):
        super().__init__(*args)

    clicked = pyqtSignal()

    def mousePressEvent(self, ev):
        if app.mouseButtons() & Qt.LeftButton:
            self.clicked.emit()

class QHighlightedWidget(QInteractiveWidget):
    """A widget which is the default, but with some different stylesheet details (highlights)"""
    def __init__(self, *args):
        super().__init__(*args)

        self.setPalette(QPalette())

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

class QMainApplication(QApplication):
    """A Dark styled application."""
    def __init__(self, *__args):
        super().__init__(*__args)
        self.setStyle("Fusion")
        self.setPalette(QDarkPalette())
        self.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
        
class WarbandOverview(QMainWindow):
    """The main window that everything runs in"""
    def __init__(self):
        super().__init__()

        self.wbid = get_current_warband()
        self.currentunit = self.create_template_char()
        self.initUI()

    def initUI(self):
        
        # Some window settings
        self.setWindowTitle('Warband Manager')
        self.setToolTip('This is your <b>Warband</b> overview')
        self.setWindowIcon(QIcon('icon.png'))     

        # build overview
        nested_widget = self.set_nested_widget()

        self.setCentralWidget(nested_widget)
        self.showMaximized()

    def set_nested_widget(self):
        # build top part
        topboxwidget = self.set_topbox()
        topboxwidget.setSizePolicy
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
        topbox.addWidget(self.set_systembox())
        topboxwidget = QBorderedWidget()
        topboxwidget.setLayout(topbox)

        return topboxwidget

    def set_botbox(self):
        # wrapping heroes, squads and extra details in the bottom horizontal layout
        botbox = QHBoxLayout()
        botbox.addWidget(self.set_herobox())
        botbox.addWidget(self.set_squadbox())
        botbox.addWidget(self.set_currentbox())
        botboxwidget = QBorderedWidget()
        botboxwidget.setLayout(botbox)

        return botboxwidget

    def set_systembox(self):
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

        return sysboxwidget

    def set_wbinvbox(self):
        # Top middle
        wbinvbox = QHBoxLayout()
        treabox = QVBoxLayout()

        goldlabel = QLabel()
        goldlabel.setText(str(self.wbid.treasury.gold))
        treabox.addWidget(goldlabel)
        wyrdlabel = QLabel()
        wyrdlabel.setText(str(self.wbid.treasury.wyrd))
        treabox.addWidget(wyrdlabel)
        
        treaboxwidget = QBorderedWidget()
        treaboxwidget.setLayout(treabox)
        wbinvbox.addWidget(treaboxwidget)

        # add items
        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in self.wbid.itemlist:
            label = QLabel()
            label.setText(str(item.name))
            itembox.addWidget(label) #adds the item to a label and at it to the vertical item layout
        
        itemwidget = QBorderedWidget()
        itemwidget.setLayout(itembox)
        wbinvbox.addWidget(itemwidget) # adds the item layout to the grid

        wbinvboxwidget = QBorderedWidget()
        wbinvboxwidget.setLayout(wbinvbox)

        return wbinvboxwidget
    
    def set_wbname(self):
        # top left warband info
        wbnamelabel = QLabel()
        wbnamelabel.setToolTip('This is your <b>Warband`s</b> name')
        wbbox = QVBoxLayout()
        wbbox.addWidget(wbnamelabel)
        wbboxwidget = QBorderedWidget()
        wbboxwidget.setLayout(wbbox)

        # update wb info
        wbnamelabel.setText("Your warband " + self.wbid.name)

        return wbboxwidget

    def set_herobox(self):
        # left bottom heroes
        herobox = QVBoxLayout() # To show all heroes below each other dynamically (based on actual number of heroes)
        h = 0
        for hero in self.wbid.herolist:
            h += 1
            herogrid = QGridLayout() # create a grid layout to position all information more accurately
            
            namelabel = QLabel()
            if hero == self.currentunit:
                namelabel.setText(hero.name + " (selected)")
            else:
                namelabel.setText(hero.name)
            namelabel.setToolTip(f"This is your hero`s name")
            herogrid.addWidget(namelabel, 0, 0) # add the name and category box to the herogrid
            
            catlabel = QLabel()
            catlabel.setText(hero.category)
            catlabel.setToolTip(f"This is your hero`s unit type. The unit type determines what the heroes abilities are, what kind of items it can carry and how expensive it is to replace.")
            herogrid.addWidget(catlabel, 0, 1) # add the cat and category box to the herogrid

            # sets the complete hero grid layout to a herowidget in order to add to the vertical list of heroes
            herowidget = QInteractiveWidget()
            herowidget.setLayout(herogrid)

            # bound a click on the widget to showing details in character view
            herowidget.clicked.connect(self.create_method_focus(unit=hero))
            herobox.addWidget(herowidget)

        while h <= 5:
            h += 1
            herogrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText("Add New Hero")
            herogrid.addWidget(namelabel, 0, 0)

            herowidget = QBorderedWidget()
            herowidget.setLayout(herogrid)
            herobox.addWidget(herowidget)

        heroboxwidget = QBorderedWidget()
        heroboxwidget.setLayout(herobox)
        heroboxwidget.setToolTip('These are your <b>heroes</b>')

        return heroboxwidget

    def set_squadbox(self):
        # right bottom squads
        squadbox = QVBoxLayout()

        s = 0
        for squad in self.wbid.squadlist:
            s += 1
            squadgrid = QGridLayout()
            
            numlabel = QLabel()
            numlabel.setText(str(squad.get_totalhenchman()))
            squadgrid.addWidget(numlabel, 0, 0, 1, 1)

            namelabel = QLabel()
            if squad.henchmanlist[0] == self.currentunit:
                namelabel.setText(squad.name + " (selected)")
            else:
                namelabel.setText(squad.name)
            squadgrid.addWidget(namelabel, 0, 1, 1, 3)
            
            catlabel = QLabel()
            catlabel.setText(squad.henchmanlist[0].category)
            catlabel.setToolTip(f"This is your squad`s unit type. The unit type determines what the squads abilities are, what kind of items it can carry and how expensive it is to replace.")
            squadgrid.addWidget(catlabel, 0, 4, 1, 3) 
            
            # sets the complete squad grid layout to a squadwidget in order to add to the vertical list
            squadwidget = QInteractiveWidget()
            squadwidget.setLayout(squadgrid)
            
            squadwidget.clicked.connect(self.create_method_focus(unit=squad.henchmanlist[0]))
            squadbox.addWidget(squadwidget)

        while s <= 5:
            s += 1
            squadgrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText("Add New Squad")
            squadgrid.addWidget(namelabel, 0, 0)

            squadwidget = QBorderedWidget()
            squadwidget.setLayout(squadgrid)
            squadbox.addWidget(squadwidget)

        squadboxwidget = QBorderedWidget()
        squadboxwidget.setLayout(squadbox)
        squadboxwidget.setToolTip('These are your <b>squads</b>')

        return squadboxwidget

    def set_currentbox(self):
        # Current unit field        
        namebox = QGridLayout()
        
        namelabel = QLabel()
    
        namelabel.setText(self.currentunit.name)    
        namebox.addWidget(namelabel,0,0)
        catlabel = QLabel()
        catlabel.setText(self.currentunit.category)
        namebox.addWidget(catlabel, 0, 1)
        herolabel = QLabel()
        herolabel.setText(str(self.currentunit.ishero))
        namebox.addWidget(herolabel, 1, 0)
        
        namewidget = QInteractiveWidget()
        namewidget.setLayout(namebox)

        #show skills at bottom left
        skillbox = QHBoxLayout() # create a horizontal layout to show the skills in a neat line
        
        skilldict = self.currentunit.skill.to_dict()
        # print(skilldict)
        for key in skilldict:
            label = QLabel()
            if skilldict['wounds'] >= 1:
                label.setText(key[:2] + "\n" + str(skilldict[key]))  
            else: 
                label.setText("")
            skillbox.addWidget(label)
  
        skillwidget = QBorderedWidget()
        skillwidget.setLayout(skillbox)
        

        #add items
        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in self.currentunit.itemlist:
            label = QLabel()
            label.setText(str(item.name))
            label.setToolTip(f"<font><b>{item.name}</b> <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itembox.addWidget(label) #adds the item to a label and at it to the vertical item layout
        
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itembox)

        #show abilities
        abilitybox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for ability in self.currentunit.abilitylist:
            label = QLabel()
            label.setText(str(ability.name))
            label.setToolTip(f"<font><b>{ability.name}</b> <br/> {ability.description}</font>")
            abilitybox.addWidget(label) #adds the ability to a label and at it to the vertical ability layout
        
        abilitywidget = QInteractiveWidget()
        abilitywidget.setLayout(abilitybox)

        #show magic
        magicbox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for magic in self.currentunit.magiclist:
            label = QLabel()
            label.setText(str(magic.name))
            label.setToolTip(f"<font><b>{magic.name}</b> <br/> {magic.description}</font>")
            magicbox.addWidget(label) #adds the magic to a label and at it to the vertical magic layout
        
        magicwidget = QInteractiveWidget()
        
        magicwidget.setLayout(magicbox)
        
        listbox = QHBoxLayout()
        listbox.addWidget(itemwidget) # adds the item layout to the grid
        listbox.addWidget(abilitywidget) # adds the ability layout to the grid
        listbox.addWidget(magicwidget) # adds the magic layout to the grid

        listwidget = QInteractiveWidget()
        listwidget.setLayout(listbox)

        currentbox = QGridLayout()
        currentbox.addWidget(namewidget, 0, 0, 1, 1)
        currentbox.addWidget(skillwidget, 1, 0, 1, 1)
        currentbox.addWidget(listwidget, 2, 0, 2, 1)

        currentboxwidget = QBorderedWidget()
        currentboxwidget.setLayout(currentbox)

        return currentboxwidget

    def create_method_focus(self, unit):          
        
        def focus_unit():
            if self.currentunit != unit:
                self.currentunit = unit
                self.initUI()

        return focus_unit
       
    def create_template_char(self):
        template_char = Character(
            name="",
            race="", 
            source="", 
            skill=Skill(0,0,0,0,0,0,0,0,0,0), 
            category="", 
            ishero=""
        )
        return template_char

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
            self.currentunit = self.create_template_char()
            self.initUI()                       # Restart the window to force changes


if __name__ == '__main__':
    app = QMainApplication(sys.argv)
    main = WarbandOverview()

    sys.exit(app.exec_())
