# import sys

from PyQt5.QtCore import (
    # QRect,
    Qt,
    pyqtSignal,
    )

from PyQt5.QtWidgets import (
    # QAction,
    QApplication,
    # QDesktopWidget,
    # QInputDialog,
    # QLabel,
    # QGridLayout,
    # QVBoxLayout,
    # QHBoxLayout,
    # QLineEdit,
    # QListWidget,
    # QListWidgetItem,
    # QMainWindow,
    # QMessageBox,
    QPushButton, 
    # QSizePolicy,
    # QTableWidget,
    # QTableWidgetItem,
    # QTextEdit,
    QToolTip, 
    # QVBoxLayout,
    QWidget, 
    )

from PyQt5.QtGui import (
    QColor,
    QFont,
    QFontDatabase,
    QIcon,
    QPalette,
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
        if QApplication.mouseButtons() & Qt.LeftButton:
            self.clicked.emit()

# class QHighlightedWidget(QInteractiveWidget):
#     """A widget which is the default, but with some different stylesheet details (highlights)"""
#     def __init__(self, *args):
#         super().__init__(*args)

#         self.setPalette(QPalette())

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
