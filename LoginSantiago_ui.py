# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginSantiago.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 400))
        MainWindow.setMaximumSize(QSize(400, 400))
        MainWindow.setBaseSize(QSize(10, 10))
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(196, 200, 255);")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 0, 121, 41))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Noto Naskh Arabic"])
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 16pt \"Noto Naskh Arabic\";\n"
"\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMargin(-1)
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(70, 120, 151, 22))
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(170, 170, 255);\n"
"")
        self.password.setFrame(True)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText(u"")
        self.Iniciar = QPushButton(self.centralwidget)
        self.Iniciar.setObjectName(u"Iniciar")
        self.Iniciar.setGeometry(QRect(70, 180, 111, 41))
        sizePolicy.setHeightForWidth(self.Iniciar.sizePolicy().hasHeightForWidth())
        self.Iniciar.setSizePolicy(sizePolicy)
        self.Iniciar.setCursor(QCursor(Qt.CursorShape.WhatsThisCursor))
        self.Iniciar.setStyleSheet(u"border-color: rgb(170, 170, 255);")
        self.Iniciar.setCheckable(False)
        self.Iniciar.setAutoDefault(False)
        self.Iniciar.setFlat(False)
        self.Usuario = QLineEdit(self.centralwidget)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(70, 70, 151, 21))
        sizePolicy.setHeightForWidth(self.Usuario.sizePolicy().hasHeightForWidth())
        self.Usuario.setSizePolicy(sizePolicy)
        self.Usuario.setMinimumSize(QSize(0, 0))
        self.Usuario.setSizeIncrement(QSize(2, 2))
        self.Usuario.setBaseSize(QSize(2, 2))
        self.Usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Usuario.setMouseTracking(False)
        self.Usuario.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.Usuario.setAutoFillBackground(False)
        self.Usuario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(170, 170, 255);")
        self.Usuario.setDragEnabled(False)
        self.Username = QLabel(self.centralwidget)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(70, 50, 101, 16))
        self.password2 = QLabel(self.centralwidget)
        self.password2.setObjectName(u"password2")
        self.password2.setGeometry(QRect(70, 100, 101, 16))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(70, 150, 101, 20))
        self.link1 = QCommandLinkButton(self.centralwidget)
        self.link1.setObjectName(u"link1")
        self.link1.setGeometry(QRect(30, 240, 151, 41))
        self.link1.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.link2 = QCommandLinkButton(self.centralwidget)
        self.link2.setObjectName(u"link2")
        self.link2.setGeometry(QRect(210, 240, 151, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 400, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.Iniciar.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login ERP", None))
        self.password.setInputMask("")
        self.password.setText("")
        self.Iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
        self.Usuario.setText("")
        self.Usuario.setPlaceholderText("")
        self.Username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.password2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Recordarme", None))
        self.link1.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.link2.setText(QCoreApplication.translate("MainWindow", u"Forgot password?", None))
    # retranslateUi

