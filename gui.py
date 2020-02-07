# pip3 install --user pyqt5

import sys

from PyQt5.QtCore import (
    QRect,
    )
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QDesktopWidget,
    QInputDialog,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
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
)

from PyQt5.QtGui import QPalette, QColor


# class App(QApplication):
#     def __init__(self, *args):
#         super().__init__(self, *args)
#         self.setStyle("Fusion")
#         self.setPalette(QDarkPalette())
#         self.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
#         self.main = MainWindow()

#     @staticmethod
#     def start():
#         global app 
#         app = App(sys.argv)
#         app.exec_()


class QDarkPalette(QPalette):
    """Dark palette for a Qt application meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)

        # Set all the colors for a dark theme
        # red, green, blue
        # QColor(255, 255, 255))  Qt.White
        # QColor(255, 0, 0)) Qt.Red
        # QColor(0, 0, 0)) Qt.Black
        self.setColor(QPalette.Window, QColor(53, 53, 53))
        self.setColor(QPalette.WindowText, QColor(255, 255, 255))
        self.setColor(QPalette.Base, QColor(25, 25, 25))
        self.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        self.setColor(QPalette.ToolTipBase, QColor(255, 255, 255))
        self.setColor(QPalette.ToolTipText, QColor(255, 255, 255))
        self.setColor(QPalette.Text, QColor(255, 255, 255))
        self.setColor(QPalette.Button, QColor(53, 53, 53))
        self.setColor(QPalette.ButtonText, QColor(255, 255, 255))
        self.setColor(QPalette.BrightText, QColor(255, 0, 0))
        self.setColor(QPalette.Link, QColor(42, 130, 218))
        self.setColor(QPalette.Highlight, QColor(42, 130, 218))
        self.setColor(QPalette.HighlightedText, QColor(0, 0, 0))

    @staticmethod
    def set_stylesheet(app):
        app.setstylesheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")

       
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
       
        # Creates the main window
        # self.setGeometry(0, 0, 1800, 1000)
        self.resize(1800, 1120)

        # centering the window
        # Get a rectangle specifying the geometry of the main window
        windowrectangle = self.frameGeometry()
        # gett desktop resolution and specifically the center point of it
        screencenter = QDesktopWidget().availableGeometry().center()
        # set the rectangle to the center point of the monitor
        windowrectangle.moveCenter(screencenter)
        # set the application window to the rectangle

        self.move(windowrectangle.topLeft())
        self.setWindowTitle('Warband Manager')
        self.setToolTip('This is your <b>Warband</b> overview')
        self.setWindowIcon(QIcon('icon.png'))        

        # creates a button for quitting the app
        btn = QPushButton('Quit', self)
        btn.setToolTip('Quit the program')
        # btn.setStyleSheet("color: white; background-color:black")
        btn.resize(btn.sizeHint())
        btn.move(1600, 900) 
        btn.clicked.connect(QApplication.instance().quit)

        # creates a button for choosing an existing warband
        btn = QPushButton('Choose Warband', self)
        btn.setToolTip('Choose an existing <b>Warband</b>')
        # btn.setStyleSheet("color: white; background-color:black")
        btn.resize(btn.sizeHint())
        btn.move(50, 50) 
        btn.clicked.connect(self.choose_warband)

        # creates a button for creating a new warband
        btn = QPushButton('Create Warband', self)
        btn.setToolTip('Create a new <b>Warband</b>')
        # btn.setStyleSheet("color: white; background-color:black")
        btn.resize(btn.sizeHint())
        btn.move(300, 50)
        btn.clicked.connect(self.create_warband)
        

        self.show()
    
    def create_warband(self):
        warband, okPressed = QInputDialog.getText(self, "Create", "Name your warband:")
        if okPressed and warband:
            print(warband)
            return warband

    def choose_warband(self):
        warbands = show_saved_warbands()
        print(show_saved_warbands)
        warband, okPressed = QInputDialog.getItem(self, "Choose", "Choose your warband", warbands, 0, False)
        if okPressed and warband:
            print(warband)
            return warband

    # def closeEvent(self, event):
    #     reply = QMessageBox.question(
    #         self, 
    #         'Message',
    #         "Are you sure to quit?", 
    #         QMessageBox.Yes | QMessageBox.No, 
    #         QMessageBox.No,
    #         )

    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()  
        

class SubWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    def initUI(self):
        pass
        # listWidget = QListWidget(self)
        # # listWidget.itemDoubleClicked.connect(MainWindow)

        # for save in savelist:
        #     QListWidgetItem(save, listWidget)

        # self.setGeometry(100, 100, 100, 100)
        # self.show()

    @staticmethod
    def buildsubwindow(self):
        SubWindow()

        # # self.setGeometry(0, 0, 1800, 1000)
        # self.resize(900, 500)
        # self.center()
        # self.setWindowTitle('Choose Warband')
        # self.setToolTip('Choose here the <b>Warband</b> you want to open')
        # self.setWindowIcon(QIcon('icon.png'))        

   
class TableView(QTableWidget):

    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)

        data = {'col1':['1','2','3','4'],
                'col2':['1','2','1','3'],
                'col3':['1','1','2','1']}

        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

if __name__ == '__main__':
    # Create an application in the OS with the class
    # App().start()

    # Create an application manually
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setPalette(QDarkPalette())
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: grey; border: 1px solid white; }")
    main = MainWindow()

    # Make sure we can exit the application object normally
    sys.exit(app.exec_())
