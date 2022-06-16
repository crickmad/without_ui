from PySide6 import QtCore, QtGui,  QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform, QMovie)
from PySide6.QtWidgets import *

from main import *
import sys
import os, time
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
from modules import *
from widgets import *

from splashui import Ui_SplashScreen

import PySimpleGUI as er

# FIX Problem for High DPI and Scale above 100%
os.environ["QT_FONT_DPI"] = "96"
# SET AS GLOBAL WIDGETS
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        global widgets
        widgets = self.ui
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        title = "ZIA - Modern AI"
        description = "ZIA - Personal Voice Assistant."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        widgets.toggleButton.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.button)
        widgets.btn_new.clicked.connect(self.buttonClick)
        # widgets.btn_save.clicked.connect(self.buttonClick)


        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        self.show()
        
        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)
            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(
            UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        
        startExc.start()
        
    def button(self):
        startExc.quit()
    def buttonClick(self):
        pass
        
    def resizeEvent(self, event):
        pass

counter = 0
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## CREATE DROP SHADOWN EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        ## SET DROP SHADOWN EFFECT IN FRAME
        self.ui.dropShowdan.setGraphicsEffect(self.shadow)
        
        # QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(100)

        ## SHOW MAIN WINDOWS
        self.show()
        
    
    def progress(self):
        global counter

        #SET VALUE TO PROGRESS
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEM AND OPEN THING
        if counter == 0:
            self.ui.labelSubName.setText("<strong style=\"color:white\">Initializing AI personal assistant</strong><font></font>")
        if counter == 10:
            speak(f"Initializing AI personal assistant") 
            self.ui.labelSubName.setText("<strong style=\"color:white\">Starting all systems applications</strong><font></font>")   
        if counter == 20:
            speak("Starting all systems applications")
        if counter == 30:
            self.ui.labelSubName.setText("<strong style=\"color:white\">Calibrating and examining all the core processors</strong><font></font>")
        if counter == 40:
            speak("Calibrating and examining all the core processors")
            self.ui.labelSubName.setText("<strong style=\"color:white\">All drivers are up and running</strong><font></font>")
        if counter == 50:
            speak("All drivers are up and running")
        if counter == 60:
            self.ui.labelSubName.setText("<strong style=\"color:white\">Checking the internet connection</strong><font></font>")
        if counter == 70:
            speak("Checking the internet connection")
            self.ui.labelSubName.setText("<strong style=\"color:white\">All systems have been activated</strong><font></font>")
        if counter == 80:
            speak("All systems have been activated")   
            self.ui.labelSubName.setText("<strong style=\"color:white\">Face the camera to verify your access</strong><font></font>")
        if counter == 90:
            speak("Face the camera to verify your access")
            if face(): 
                self.ui.labelSubName.setText("<strong style=\"color:white\">Starting up ZIA interface</strong><font></font>")
                speak("Starting up ZIA interface")  
            else:
                speak("Access denied")
                er.Popup("        Access denied        ")
                print("Access denied")
                self.close()
                os.sys.exit(0)
        if counter == 100:
            self.timer.stop()
            ## CREATE FORM CENTRAL
            self.main = MainWindow()
            ## SHOW MAIN WINDOWS / FORM CENTRAL
            if check_int() == True:
                ref ="online"  
            else :
                ref ="Offline"
            speak(f"I am {BOTNAME}. {ref} and ready. Please tell me how may I help you")
            self.main.show()
            self.close()
        counter+=1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec())
 