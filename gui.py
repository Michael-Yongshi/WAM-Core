# pip3 install --user pyqt5

import sys

from PyQt5.QtCore import (
    QRect,
    )
from PyQt5.QtWidgets import (
    QApplication,
    QDesktopWidget,
    QMessageBox,
    QPushButton, 
    QToolTip, 
    QWidget, 
    )
from PyQt5.QtGui import (
    QIcon,
    QFont,
    )


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))
        
        # Creates the main window
        # self.setGeometry(0, 0, 1800, 1000)
        self.resize(1800, 1120)
        self.center()
        self.setWindowTitle('Warband Manager')
        self.setToolTip('This is your <b>Warband</b> overview')
        self.setWindowIcon(QIcon('icon.png'))        
        # self.setStyleSheet("color: black; background-color:grey")

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

        # creates a button for creating a new warband
        btn = QPushButton('Create Warband', self)
        btn.setToolTip('Create a new <b>Warband</b>')
        # btn.setStyleSheet("color: white; background-color:black")
        btn.resize(btn.sizeHint())
        btn.move(300, 50) 

        self.show()
        
    def center(self):
        # Get a rectangle specifying the geometry of the main window
        windowrectangle = self.frameGeometry()
        # gett desktop resolution and specifically the center point of it
        screencenter = QDesktopWidget().availableGeometry().center()
        # set the rectangle to the center point of the monitor
        windowrectangle.moveCenter(screencenter)
        # set the application window to the rectangle
        self.move(windowrectangle.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 
            'Message',
            "Are you sure to quit?", 
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No,
            )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()  
        
if __name__ == '__main__':
    # Create an application in the OS
    app = QApplication(sys.argv)

    # Use the class to create a window object
    wbo = MainWindow()

    # Make sure we can exit the application object normally
    sys.exit(app.exec_())
