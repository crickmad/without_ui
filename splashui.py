from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(797, 551)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShowdan = QFrame(self.centralwidget)
        self.dropShowdan.setObjectName(u"dropShowdan")
        self.dropShowdan.setStyleSheet(u"QFrame {	\n"
"\n"
"	background-color: rgb(43, 2, 61);\n"
"\n"
"	color: rgb(220, 220, 220);\n"
"\n"
"	border-radius: 15px;\n"
"\n"
"}")
        self.dropShowdan.setFrameShape(QFrame.StyledPanel)
        self.dropShowdan.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.dropShowdan)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(9, 300, 761, 41))
        self.progressBar.setStyleSheet(u"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(225, 158, 255, 1), stop:1 rgba(176, 0, 255, 1));\n"
"}\n"
"\n"
"QProgressBar {\n"
"	background-color: rgb(57, 2, 82);\n"
"	color: #fff;\n"
"	border-style: none;\n"
"	font-size: 30px;\n"
"	border-radius: 35px;\n"
"	text-align: center;\n"
"	height: 45px;\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(0)
        self.labelName = QLabel(self.dropShowdan)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(0, 120, 777, 66))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(48)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet(u"QLabel{\n"
" color: rgb(253, 89, 255)\n"
"}")
        self.labelName.setAlignment(Qt.AlignCenter)
        self.labelSubName = QLabel(self.dropShowdan)
        self.labelSubName.setObjectName(u"labelSubName")
        self.labelSubName.setGeometry(QRect(0, 200, 777, 21))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(12)
        self.labelSubName.setFont(font1)
        self.labelSubName.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelSubName.setAlignment(Qt.AlignCenter)
        self.labelLoading = QLabel(self.dropShowdan)
        self.labelLoading.setObjectName(u"labelLoading")
        self.labelLoading.setGeometry(QRect(0, 370, 777, 21))
        self.labelLoading.setFont(font1)
        self.labelLoading.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelCreated = QLabel(self.dropShowdan)
        self.labelCreated.setObjectName(u"labelCreated")
        self.labelCreated.setGeometry(QRect(3, 490, 761, 20))
        self.labelCreated.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelCreated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShowdan)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelName.setText(QCoreApplication.translate("SplashScreen", u"<strong style=\"color: #bd93f9\" >ZIA</strong>", None))
        self.labelSubName.setText(QCoreApplication.translate("SplashScreen", u"<strong>Loading</strong> presets ", None))
        self.labelLoading.setText(QCoreApplication.translate("SplashScreen", u"<strong style=\"color:white\">loading.......</strong>", None))
        self.labelCreated.setText(QCoreApplication.translate("SplashScreen", u"<font style=\"color: #bd93f9\">Dev by </font><strong style=\"color:white\"> Noob?tech</strong> <font style=\"color:white\">v0.hdg.1</font>", None))
    # retranslateUi

