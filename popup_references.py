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
    QFormLayout,
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

from source.methods_json import (
    open_json,
    save_json,
    )

from source.methods_database import (
    create_warbandref,
    create_characterref,
    create_itemref,
    create_abilityref,
    create_magicref,
    add_warbandref,
    add_characterref,
    add_itemref,
    add_abilityref,
    add_magicref,
    get_warbandref,
    get_characterref,
    get_itemref,
    get_abilityref,
    get_magicref,
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

class MainReferences(QMainWindow):
    def __init__(self):
        super().__init__()

        self.warband = create_template_wb()
        self.initUI()

    def initUI(self):

        nested_widget = self.set_nested_widget()

        self.setCentralWidget(nested_widget)
        self.showMaximized()

    def set_nested_widget(self):
        box = QHBoxLayout()

        # addbutton = QPushButton('Add Warband', self)
        # addbutton.setToolTip('Add a new <b>Warband Template</b>')
        # addbutton.clicked.connect(self.fill_warband_dialog(create_template_wb()))

        box.addWidget(TableWarband())
        box.addWidget(FormWarband(self))

        frame = QRaisedFrame()
        frame.setLayout(box)

        return frame

class FormWarband(QDialog):
    def __init__(self, mainwindow):
        super().__init__()
        """dialog for edit or creation of warband"""

        self.mainwindow = mainwindow
        
        self.le_race = QLineEdit(self.mainwindow.warband.race)
        self.le_source = QLineEdit(self.mainwindow.warband.source)
        self.le_warband = QLineEdit(self.mainwindow.warband.warband)

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # le_name.setDisabled() # if wbname != "" else 
        wbform = QFormLayout()
        wbform.addRow(QLabel("Race: "), self.le_race)
        wbform.addRow(QLabel("Source: "), self.le_source)
        wbform.addRow(QLabel("Warband: "), self.le_warband)   
        wbform.addRow(buttonbox)

        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)
        # buttonbox.accepted.connect(self.accept)
        # buttonbox.rejected.connect(self.reject)

        self.setLayout(wbform)

    def accept(self):
        add_warbandref(
            race = self.le_race.text(),
            source = self.le_source.text(),
            warband = self.le_warband.text(),
            rulelist = [],
            itemlist = [],
            start_gold = 500,
            description = "",
        )   
        self.mainwindow.initUI()
        
    def reject(self):
        message = QMessageBox.information(self, 'rejected', "Your warband is rejected", QMessageBox.Ok)

class TableWarband(QTableWidget):
    def __init__(self):
        super().__init__()

        warbandsdict = open_json("database/references/warbands_ref.json")
        # charactersdict = open_json("database/references/characters_ref.json")
        # itemsdict = open_json("database/references/items_ref.json")
        # abilitiesdict = open_json("database/references/abilities_ref.json")
        # magicsdict = open_json("database/references/magic_ref.json")
        
        # open tableview of all warbands   
        warbandlist = []
        for race in warbandsdict:
            for source in warbandsdict[race]:
                for warband in warbandsdict[race][source]:
                    warbandlist += [Warband.create_warband(name = "", race = race, source = source, warband = warband)]

        self.setRowCount(len(warbandlist))
        self.setColumnCount(3)

        i = 0
        for warband in warbandlist:
            self.setItem(i, 0, QTableWidgetItem(warband.race))
            self.setItem(i, 1, QTableWidgetItem(warband.source))
            self.setItem(i, 2, QTableWidgetItem(warband.warband))
            i += 1
        
        print(len(warbandlist))

        self.doubleClicked.connect(self.on_click)

    def on_click(self, signal):
        row = signal.row()  # RETRIEVES ROW OF CELL THAT WAS DOUBLE CLICKED
        column = signal.column()  # RETRIEVES COLUMN OF CELL THAT WAS DOUBLE CLICKED
        cell_dict = self.model.itemData(signal)  # RETURNS DICT VALUE OF SIGNAL
        cell_value = cell_dict.get(0)  # RETRIEVE VALUE FROM DICT
        
        index = signal.sibling(row, 0)
        index_dict = self.model.itemData(index)
        index_value = index_dict.get(0)
        print(f"Row {row}, Column {column} clicked - value: {cell_value}\nColumn 1 contents: {index_value}")
 
        # click on warband opens details of that warband in the update warband dialog, with a deactivated name field,
        # under the table an add button, which launches the same update warband dialog, but then empty and activated name field, where you can fill in warband details
        # the dialog has a button, add items, for items to launch the update item dialog, where you can choose an item to add to the warband


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainReferences()

    sys.exit(app.exec_())
