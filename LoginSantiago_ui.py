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
        MainWindow.resize(500, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setMaximumSize(QSize(500, 500))
        MainWindow.setBaseSize(QSize(10, 10))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(196, 200, 255);")
        MainWindow.setAnimated(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 211, 41))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"color: rgb(255, 85, 255);\n"
"font: 24pt \"Segoe UI\";\n"
"\n"
"\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMargin(-1)
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setGeometry(QRect(130, 220, 211, 41))
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.password.setMouseTracking(False)
        self.password.setAutoFillBackground(False)
        self.password.setStyleSheet(u";\n"
"background-color: rgb(240, 187, 255);\n"
"border-color: rgb(170, 170, 255);\n"
"")
        self.password.setFrame(True)
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        self.password.setPlaceholderText(u"")
        self.Username = QLabel(self.centralwidget)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(160, 80, 141, 31))
        self.Username.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.Username.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password2 = QLabel(self.centralwidget)
        self.password2.setObjectName(u"password2")
        self.password2.setGeometry(QRect(160, 180, 141, 31))
        self.password2.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.password2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(130, 270, 131, 31))
        self.checkBox.setCursor(QCursor(Qt.CursorShape.CrossCursor))
        self.checkBox.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 0, 255);")
        self.link1 = QCommandLinkButton(self.centralwidget)
        self.link1.setObjectName(u"link1")
        self.link1.setEnabled(True)
        self.link1.setGeometry(QRect(40, 380, 211, 41))
        self.link1.setStyleSheet(u"color: rgb(255, 85, 255);\n"
"font: 12pt \"Segoe UI\";")
        self.link2 = QCommandLinkButton(self.centralwidget)
        self.link2.setObjectName(u"link2")
        self.link2.setEnabled(True)
        self.link2.setGeometry(QRect(280, 380, 171, 41))
        self.link2.setStyleSheet(u"font: 12pt \"Segoe UI\";\n"
"color: rgb(255, 85, 255);")
        self.Usuario = QLineEdit(self.centralwidget)
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(130, 130, 211, 41))
        sizePolicy.setHeightForWidth(self.Usuario.sizePolicy().hasHeightForWidth())
        self.Usuario.setSizePolicy(sizePolicy)
        self.Usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Usuario.setMouseTracking(False)
        self.Usuario.setAutoFillBackground(False)
        self.Usuario.setStyleSheet(u"background-color: rgb(240, 187, 255);\n"
"border-color: rgb(170, 170, 255);\n"
"")
        self.Usuario.setFrame(True)
        self.Usuario.setEchoMode(QLineEdit.EchoMode.Normal)
        self.Usuario.setPlaceholderText(u"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 310, 181, 51))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.pushButton.setStyleSheet(u"background-color:rgb(240, 187, 255);\n"
"font: 20pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login ERP", None))
        self.password.setInputMask("")
        self.password.setText("")
        self.Username.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.password2.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Recordarme", None))
        self.link1.setText(QCoreApplication.translate("MainWindow", u"Don't have an account?", None))
        self.link2.setText(QCoreApplication.translate("MainWindow", u"Forgot password?", None))
        self.Usuario.setInputMask("")
        self.Usuario.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar sesi\u00f3n", None))
    # retranslateUi

