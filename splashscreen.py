

import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



# GUI FILE
from ui_splash_screen import Ui_SplashScreen
from main import (MainThread, check_int,speak,BOTNAME)



# GLOBALS
counter = 0
jumper = 10
###################


## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(15)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        
        self.show()
        
        ## ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter
        
        # HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:38pt;">{VALUE}</span><span style=" font-size:28pt; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            # APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 10

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """if counter == 10:
            pass
        if counter == 20:
            speak(f"Initializing AI personal assistant")
            counter = 20
        if counter == 30:
            speak("Starting all systems applications")
            counter = 30
        if counter == 40:
            pass
        if counter == 50:
            speak("Calibrating and examining all the core processors")
            counter = 50
        if counter == 60:
            speak("All drivers are up and running")
            counter = 60
        if counter == 70:
            pass
        if counter == 80:
            speak("Checking the internet connection")
            counter = 80
        if counter == 90:
            speak("All systems have been activated")
            counter = 90
        """
            
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        # CLOSE SPLASH SCREE AND OPEN APP
        if counter == 100:
            # STOP TIMER
            self.timer.stop()

            
            
            # SHOW MAIN WINDOW
            self.main = MainThread()
            self.main.show()
            #MainThread()
            # CLOSE SPLASH SCREEN
            self.close()
            if check_int() == True:
                ref ="online"  
            else :
                ref ="Offline"
            speak(f"I am {BOTNAME}. {ref} and ready sir. Please tell me how may I help you")
            

        # INCREASE COUNTER
        counter += 0.5
    ########################################################
    
    ## DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        # APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
