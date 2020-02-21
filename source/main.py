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

from source.widget_system import WidgetSystem
from source.widget_herobox import WidgetHeroes
from source.widget_template import *


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
        topbox.addWidget(WidgetSystem())
        topboxwidget = QBorderedWidget()
        topboxwidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        topboxwidget.setLayout(topbox)

        return topboxwidget

    def set_botbox(self):
        # wrapping heroes, squads and extra details in the bottom horizontal layout
        botbox = QHBoxLayout()
        botbox.addWidget(WidgetHeroes(self.wbid, self.currentunit))
        botbox.addWidget(self.set_squadbox())
        botbox.addWidget(self.set_currentbox())
        botboxwidget = QInteractiveWidget()
        botboxwidget.clicked.connect(self.create_method_focus(unit=None))
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

        # add items
        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for item in self.wbid.itemlist:
            label = QLabel()
            label.setText(str(item.subcategory))
            label.setToolTip(f"<font><b>{item.subcategory} </b>{item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            itemwidget.clicked.connect(self.create_method_remove_item(item=item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout
        
        # add new item widget
        label = QLabel()
        label.setText("New Item")
        itemwrap = QVBoxLayout()
        itemwrap.addWidget(label)
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itemwrap)
        itemwidget.clicked.connect(self.create_new_wbitem)
        itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

        itemboxwidget = QBorderedWidget()
        itemboxwidget.setLayout(itembox)
        itemboxwidget.setToolTip("These are your warbands items.")
        wbinvbox.addWidget(itemboxwidget) # adds the item layout to the grid

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

    def set_squadbox(self):
        # right bottom squads
        squadbox = QVBoxLayout()

        s = 0
        for squad in self.wbid.squadlist:
            s += 1
            squadgrid = QGridLayout()
            
            numlabel = QLabel()
            numlabel.setText(str(squad.get_totalhenchman()))
            numbox = QVBoxLayout()
            numbox.addWidget(numlabel)
            numwidget = QInteractiveWidget()
            numwidget.setLayout(numbox)
            numwidget.clicked.connect(self.create_method_change_squad_number(squad))
            squadgrid.addWidget(numwidget, 0, 0, 1, 1)

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

        if s <= 5:
            s += 1
            squadgrid = QGridLayout()
            namelabel = QLabel()
            namelabel.setText("Add New Squad")
            squadgrid.addWidget(namelabel, 0, 0)

            squadwidget = QInteractiveWidget()
            squadwidget.setLayout(squadgrid)
            squadwidget.clicked.connect(self.create_new_squad)
            squadbox.addWidget(squadwidget)

        while s <= 5:
            s += 1
            squadwidget = QUnBorderedWidget()
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
        namebox.addWidget(namelabel, 0, 0)
        catlabel = QLabel()
        catlabel.setText(self.currentunit.category)
        namebox.addWidget(catlabel, 1, 0,)
        herolabel = QLabel()
        herolabel.setText(str(self.currentunit.ishero))
        namebox.addWidget(herolabel, 1, 1)
        btnremove = QPushButton('Remove Unit', self)
        btnremove.setToolTip('Remove current unit')
        btnremove.clicked.connect(self.create_method_remove_squad(self.currentunit))
        namebox.addWidget(btnremove, 0, 1)

        namewidget = QInteractiveWidget()
        namewidget.setLayout(namebox)
        
        #show abilities
        abilitybox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for ability in self.currentunit.abilitylist:
            label = QLabel()
            label.setText(str(ability.name))
            label.setToolTip(f"<font><b>{ability.name}</b> <br/><br/> {ability.description}</font>")
            abilitybox.addWidget(label) #adds the ability to a label and at it to the vertical ability layout
        # Wait for item abilities to add new ability and add it to the bot widget.

        #show magic
        magicbox = QVBoxLayout() # create a vertical layout to show them in a neat line

        for magic in self.currentunit.magiclist:
            label = QLabel()
            label.setText(str(magic.name))
            label.setToolTip(f"<font><b>{magic.name}</b> <br/>Difficulty: {magic.difficulty} <br/><br/> {magic.description}</font>")
            magicbox.addWidget(label) #adds the magic to a label and at it to the vertical magic layout
        # Wait for item magic to add new ability and add it to the bot widget.

        #add items
        itembox = QVBoxLayout() # create a vertical layout to show them in a neat line
        
        totalskills = self.currentunit.skill.to_list()

        for item in self.currentunit.itemlist:
            label = QLabel()
            label.setText(str(item.subcategory + " " + item.name))
            label.setToolTip(f"<font><b>{item.subcategory}</b> {item.name} <br/> category: {item.category} <br/> distance: {item.distance} <br/> <nobr>{item.skill.to_string()}</nobr> <br/> price: {item.price} <br/> {item.description}</font>")
            itemwrap = QVBoxLayout()
            itemwrap.addWidget(label)
            itemwidget = QInteractiveWidget()
            itemwidget.setLayout(itemwrap)
            itemwidget.clicked.connect(self.create_method_remove_item(item=item))
            itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

            pairskills = [sum(pair) for pair in zip(totalskills, item.skill.to_list())]
            totalskills = pairskills

            for ability in item.abilitylist:
                label = QLabel()
                label.setText(f"{ability.name} (source: {item.subcategory})")
                label.setToolTip(f"<font><b>{ability.name}</b> <br/>(source: {item.subcategory}) <br/><br/>{ability.description}</font>")
                abilitybox.addWidget(label) #adds the ability to a label and at it to the vertical ability layout
        
            for magic in item.magiclist:
                label = QLabel()
                label.setText(f"{magic.name} (source: {item.subcategory})")
                label.setToolTip(f"<font><b>{magic.name}</b> <br/>(source: {item.subcategory}) <br/>Difficulty: {magic.difficulty}<br/><br/>{magic.description}</font>")
                magicbox.addWidget(label) #adds the magic to a label and at it to the vertical magic layout

        #show skills at bottom left
        skillbox = QHBoxLayout() # create a horizontal layout to show the skills in a neat line
        
        skillobject = Skill.from_list(totalskills)
        skilldict = skillobject.to_dict()

        # print(skilldict)
        for key in skilldict:
            label = QLabel()
            label.setText(key[:2] + "\n" + str(skilldict[key]))  
            label.setToolTip(f"The total <b>{key}</b> skill, <br/>including both base model scores and item influences.")
            skillbox.addWidget(label)

        skillwidget = QBorderedWidget()
        skillwidget.setLayout(skillbox)

        # add new item widget
        label = QLabel()
        label.setText("New Item")
        itemwrap = QVBoxLayout()
        itemwrap.addWidget(label)
        itemwidget = QInteractiveWidget()
        itemwidget.setLayout(itemwrap)
        itemwidget.setToolTip(f"Buy a new item for this unit.")
        itemwidget.clicked.connect(self.create_method_new_item(unit=self.currentunit))
        itembox.addWidget(itemwidget) #adds the item to a label and at it to the vertical item layout

        itemboxwidget = QBorderedWidget()
        itemboxwidget.setLayout(itembox)
        itemboxwidget.setToolTip("These are your units items.")

        # add new ability widget
        label = QLabel()
        label.setText("New Ability")
        abilitywrap = QVBoxLayout()
        abilitywrap.addWidget(label)
        abilitywidget = QInteractiveWidget()
        abilitywidget.setLayout(abilitywrap)
        abilitywidget.setToolTip(f"Add manually a new ability for this unit.")
        abilitywidget.clicked.connect(self.create_method_new_ability(unit=self.currentunit))
        abilitybox.addWidget(abilitywidget) #adds the ability to a label and at it to the vertical item layout

        abilitywidget = QInteractiveWidget()
        abilitywidget.setLayout(abilitybox)
        
        # add new magic widget
        label = QLabel()
        label.setText("New Magic")
        magicwrap = QVBoxLayout()
        magicwrap.addWidget(label)
        magicwidget = QInteractiveWidget()
        magicwidget.setLayout(magicwrap)
        magicwidget.setToolTip(f"Add manually a new magic skill for this unit.")
        magicwidget.clicked.connect(self.create_method_new_magic(unit=self.currentunit))
        magicbox.addWidget(magicwidget) #adds the magic to a label and at it to the vertical item layout

        magicwidget = QInteractiveWidget()
        magicwidget.setLayout(magicbox)
        
        # Add abilities, items and magic to the listbox
        listbox = QHBoxLayout()
        listbox.addWidget(itemboxwidget) # adds the item layout to the grid
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

    def dialog_treasury(self):
        
        newgold, okPressed = QInputDialog.getInt(self, 'Gold change', f"Change gold amount to:", self.wbid.treasury.gold, 0, 99999, 1)
        if okPressed:
            self.wbid.treasury.gold = newgold

        newwyrd, okPressed = QInputDialog.getInt(self, 'Wyrd change', f"Change wyrd amount to:", self.wbid.treasury.wyrd, 0, 99999, 1)
        if okPressed:
            self.wbid.treasury.wyrd = newwyrd

        # relaunch ui to process changes in ui
        self.initUI()
        
    def create_method_focus(self, unit):          
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current unit and then passes it to the currentunit attribute of the main window"""
        def focus_unit():

            if unit == None:
                self.currentunit = create_template_char()
                self.initUI()
            elif unit != self.currentunit:
                self.currentunit = unit
                self.initUI()

        return focus_unit

    def create_method_change_squad_number(self, squad):          
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current item and then creates a window based on the attribute"""
        def change_squad_number():
         
                self.currentunit = create_template_char()
                currentsize = squad.get_totalhenchman()

                newsize, okPressed = QInputDialog.getInt(self, 'Squad members', f"Change squad size to:", currentsize, 0, 6, 1)
                if okPressed:
                    if newsize != 0:
                        deltasize = newsize - currentsize
                        squad.change_henchman_count(deltasize)
                        process_gold = QMessageBox.question(self, "Process gold", "Is change due to an event?", QMessageBox.Yes | QMessageBox.No)
                        if process_gold == QMessageBox.No:
                            deltagold = deltasize * squad.henchmanlist[0].get_price()
                            if deltagold < self.wbid.treasury.gold:
                                self.wbid.treasury.gold -= deltagold
                                self.initUI()
                            else:
                                print("Lack of funds")
                        else:
                            self.initUI()
                        
                    else:
                        print("Can't remove the last member, please disband the whole squad")

        return change_squad_number

    def create_method_remove_squad(self, unit): 
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current unit and then creates a window based on the attribute"""
        def remove_squad():

            if unit == None:
                self.currentthing = None               
            elif unit != self.currentthing:
                self.currentthing = unit
                remove = QMessageBox.question(self, 'Remove unit', f"Do you want to remove this unit?", QMessageBox.Yes | QMessageBox.No)
                if remove == QMessageBox.Yes:
                    process_gold = QMessageBox.question(self, "Process gold", "Is change due to an event?", QMessageBox.Yes | QMessageBox.No)
                    unitprice = 0

                    if self.currentunit.ishero == True:
                        for hero in self.wbid.herolist:
                            if hero == self.currentunit:
                                if process_gold == QMessageBox.No:
                                    unitprice += hero.price
                                    for item in hero.itemlist:
                                        unitprice += item.price
                                index = self.wbid.herolist.index(hero)
                                self.wbid.herolist.pop(index)
                                break

                    else:
                        for squad in self.wbid.squadlist:
                            if squad.henchmanlist[0] == self.currentunit:
                                if process_gold == QMessageBox.No:
                                    squadsize = len(squad.henchmanlist)
                                    henchprice = self.currentunit.price
                                    for item in self.currentunit.itemlist:
                                        henchprice += item.price
                                    unitprice = henchprice * squadsize
                                index = self.wbid.squadlist.index(squad)
                                self.wbid.squadlist.pop(index)
                                break

                    self.wbid.treasury.gold += unitprice
                    self.initUI()
        
        return remove_squad

    def create_method_remove_item(self, item):          
        """This method is used in order to create a new method that holds a reference to a passed attribute,
        this is used when a widget needs to be clickable but the signal needs to carry information other than the signal itself.
        This one specifically gets a current item and then creates a window based on the attribute"""
        def remove_item():

            if item == None:
                self.currentthing = None               
            elif item != self.currentthing:
                self.currentthing = item
                remove = QMessageBox.question(self, 'Remove item', f"Do you want to remove this item?", QMessageBox.Yes | QMessageBox.No)
                if remove == QMessageBox.Yes:
                    process_gold = QMessageBox.question(self, "Process gold", "Is change due to an event?", QMessageBox.Yes | QMessageBox.No)
                    itemprice = 0

                    if self.currentunit.ishero == True:
                        for hero in self.wbid.herolist:
                            if hero == self.currentunit:
                                for i in hero.itemlist:
                                    if i.name == item.name and i.subcategory == item.subcategory:
                                        if process_gold == QMessageBox.No:
                                            itemprice += item.price
                                        index = hero.itemlist.index(i)
                                        hero.itemlist.pop(index)
                                        break

                    else:
                        for squad in self.wbid.squadlist:
                            if squad.henchmanlist[0] == self.currentunit:
                                for h in squad.henchmanlist:
                                    for i in h.itemlist:
                                        if i.name == item.name and i.subcategory == item.subcategory:
                                            if process_gold == QMessageBox.No:
                                                itemprice += item.price
                                            index = h.itemlist.index(i)
                                            h.itemlist.pop(index)
                                            break
                    self.wbid.treasury.gold += itemprice
                    self.initUI()
        
        return remove_item

    def create_method_new_item(self, unit):
        """Method for creating a new item and receiving as attribute the unit it should be added to.
                    """
        def create_item_for_unit():
            new_item = self.dialog_choose_item()
            if new_item != "Cancel":
                itemprice = new_item.price
                if self.wbid.treasury.gold >= itemprice:
                    
                    if unit.ishero == True:
                        for hero in self.wbid.herolist:
                            if unit.name == hero.name:
                                hero.itemlist.append(new_item)
                                self.wbid.treasury.gold -= itemprice
                                self.initUI()
                                
                    else:
                        for s in self.wbid.squadlist:
                            if unit.name == s.name:
                                for henchman in s.henchmanlist:
                                    henchman.itemlist.append(new_item)
                                    self.wbid.treasury.gold -= itemprice
                                self.initUI()

                else:
                    message = QMessageBox.information(self, 'Lack of funds!', "Can't add new item, lack of funds", QMessageBox.Ok)
            
        return create_item_for_unit

    def create_method_new_ability(self, unit):
        """Method for creating a new ability and receiving as attribute the unit it should be added to.
                    """
        def create_ability_for_unit():
            abilitydict = open_json("database/references/abilities_ref.json")
            sources = []
            for key in abilitydict:
                sources.append(key)

            source, okPressed = QInputDialog.getItem(self, "Select source", "Choose a source", sources, 0, False)
            if okPressed and source:
            
                # get all available categories
                categories = []
                for key in abilitydict[source]:
                    categories.append(key)

                category, okPressed = QInputDialog.getItem(self, "Select category", "Choose a category", categories, 0, False)
                if okPressed and category:

                    # get all available abilities
                    abilities = []
                    for key in abilitydict[source][category]:
                        abilities.append(key)

                    ability, okPressed = QInputDialog.getItem(self, "Create", "Choose an ability", abilities, 0, False)
                    if okPressed and ability:
                        new_ability = Ability(
                            source = source,
                            category = category,
                            name = ability,
                            description = abilitydict[source][category][ability]["description"],
                        )
                        
                        if unit.ishero == True:
                            for hero in self.wbid.herolist:
                                if unit.name == hero.name:
                                    hero.abilitylist.append(new_ability)
                                    self.initUI()
                                    
                        else:
                            for s in self.wbid.squadlist:
                                if unit.name == s.name:
                                    for henchman in s.henchmanlist:
                                        henchman.abilitylist.append(new_ability)
                                    self.initUI()

        return create_ability_for_unit

    def create_method_new_magic(self, unit):
        """Method for creating a new magic and receiving as attribute the unit it should be added to.
                    """
        def create_magic_for_unit():
            magicdict = open_json("database/references/magic_ref.json")
            sources = []
            for key in magicdict:
                sources.append(key)

            source, okPressed = QInputDialog.getItem(self, "Select source", "Choose a source", sources, 0, False)
            if okPressed and source:
            
                # get all available categories
                categories = []
                for key in magicdict[source]:
                    categories.append(key)

                category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
                if okPressed and category:

                    # get all available magic
                    magics = []
                    for key in magicdict[source][category]:
                        magics.append(key)

                    magic, okPressed = QInputDialog.getItem(self, "Create", "Choose magic", magics, 0, False)
                    if okPressed and magic:
                        new_magic = Magic.create_magic(
                            name = magic,
                            category = category,
                            source = source,
                        )
                        
                        if unit.ishero == True:
                            for hero in self.wbid.herolist:
                                if unit.name == hero.name:
                                    hero.magiclist.append(new_magic)
                                    self.initUI()
                                    
                        else:
                            for s in self.wbid.squadlist:
                                if unit.name == s.name:
                                    for henchman in s.henchmanlist:
                                        henchman.magiclist.append(new_magic)
                                    self.initUI()

        return create_magic_for_unit

    def create_new_squad(self):

        """Create a new squad and store it in this warband"""
        name, okPressed = QInputDialog.getText(self, "Create", "Name your squad:")
        if okPressed and name:
            
            # get all categories in references
            wbrace = self.wbid.race
            wbsource = self.wbid.source
            wbwarband = self.wbid.warband
            catdict = open_json("database/references/characters_ref.json")
            categories = []
            
            for key in catdict[wbrace][wbsource][wbwarband]:
                if catdict[wbrace][wbsource][wbwarband][key]["ishero"] == False:
                    categories.append(key)

            category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
            if okPressed and category:
                new_squad = Squad.create_squad(
                    name=name,
                    race=wbrace,
                    source=wbsource,
                    warband=wbwarband,
                    category=category,
                )

                if new_squad.henchmanlist[0] != None:

                    wbidgold = self.wbid.treasury.gold
                    squadprice = catdict[wbrace][wbsource][wbwarband][category]["price"]
                    if wbidgold >= squadprice:
                        self.wbid.treasury.gold = wbidgold - squadprice
                        self.wbid.squadlist.append(new_squad)
                        self.currentunit = new_squad.henchmanlist[0]
                        self.initUI()
                    else:
                        message = QMessageBox.information(self, "Can't add squad!", "Lack of funds!", QMessageBox.Ok)
                else:
                    message = QMessageBox.information(self, "Can't add squad!", "Heroes can't be added to a squad!", QMessageBox.Ok)

    def create_new_wbitem(self):

        """Create a new item and store it in this warband"""
        new_item = self.dialog_choose_item()
        if new_item != "Cancel":
            wbidgold = self.wbid.treasury.gold
            itemprice = new_item.price
            if wbidgold >= itemprice:
                self.wbid.treasury.gold = wbidgold - itemprice
                self.wbid.itemlist.append(new_item)
                self.initUI()
            else:
                print("can't add new item, lack of funds")

    def dialog_choose_item(self):
        
        itemdict = open_json("database/references/items_ref.json")
        
        sources = []
        for key in itemdict:
            sources.append(key)

        source, okPressed = QInputDialog.getItem(self, "Select source", "Choose a source", sources, 0, False)
        if okPressed and source:
        
            # categories
            categories = []
            for key in itemdict[source]:
                categories.append(key)

            category, okPressed = QInputDialog.getItem(self, "Create", "Choose a category", categories, 0, False)
            if okPressed and category:
            
                # subcategories
                subcategories = []
                for key in itemdict[source][category]:
                    subcategories.append(key)

                subcategory, okPressed = QInputDialog.getItem(self, "Create", "Choose an item", subcategories, 0, False)
                if okPressed and subcategory:
                    new_item = Item.create_item(
                        subcategory = subcategory,
                        category = category,
                        source = source,
                    )
                    return new_item
                    
                else:
                    string = "Cancel"
                    return string
            else:
                string = "Cancel"
                return string
        else:
            string = "Cancel"
            return string

def run():
    global app
    app = QMainApplication(sys.argv)
    global main
    main = WarbandOverview()
    sys.exit(app.exec_())
