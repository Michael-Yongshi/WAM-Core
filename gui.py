# pip3 install --user pyqt5

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import (
    QWidget, 
    QToolTip, 
    QPushButton, 
    QApplication,
    )
from PyQt5.QtGui import (
    QIcon,
    QFont,
    )


class WarbandOverview(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif', 10))

        # Creates the main window
        self.setGeometry(0, 0, 1000, 1000)
        self.setWindowTitle('Icon')
        self.setToolTip('This is your <b>Warband</b> overview')
        self.setWindowIcon(QIcon('icon.png'))        
        self.setStyleSheet("color: grey; background-color:black")

        # creates a button
        btn = QPushButton('Choose Warband', self)
        btn.setToolTip('Choose an existing <b>Warband</b>')
        btn.setStyleSheet("color: grey")
        btn.resize(btn.sizeHint())
        btn.move(50, 50) 

        # creates a button
        btn = QPushButton('Create Warband', self)
        btn.setToolTip('Create a new <b>Warband</b>')
        btn.setStyleSheet("color: grey")
        btn.resize(btn.sizeHint())
        btn.move(300, 50) 

        self.show()
        
        
if __name__ == '__main__':
    # Create an application in the OS
    app = QApplication(sys.argv)

    # Use the class to create a window object
    wbo = WarbandOverview()

    # Make sure we can exit the application object normally
    sys.exit(app.exec_())
