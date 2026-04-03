# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keyboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1155, 800)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 5))
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgb(3, 66, 83);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lbInput = QLabel(self.frame_4)
        self.lbInput.setObjectName(u"lbInput")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbInput.sizePolicy().hasHeightForWidth())
        self.lbInput.setSizePolicy(sizePolicy1)
        self.lbInput.setMinimumSize(QSize(350, 0))
        font1 = QFont()
        font1.setPointSize(30)
        font1.setBold(True)
        self.lbInput.setFont(font1)
        self.lbInput.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);")
        self.lbInput.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.lbInput)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.tabWidget = QTabWidget(self.frame)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setPointSize(32)
        self.tabWidget.setFont(font2)
        self.tabCyfry = QWidget()
        self.tabCyfry.setObjectName(u"tabCyfry")
        self.verticalLayout_3 = QVBoxLayout(self.tabCyfry)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frCyfry = QFrame(self.tabCyfry)
        self.frCyfry.setObjectName(u"frCyfry")
        self.frCyfry.setFrameShape(QFrame.Shape.NoFrame)
        self.frCyfry.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frCyfry)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnNum1 = QPushButton(self.frCyfry)
        self.btnNum1.setObjectName(u"btnNum1")
        sizePolicy1.setHeightForWidth(self.btnNum1.sizePolicy().hasHeightForWidth())
        self.btnNum1.setSizePolicy(sizePolicy1)
        self.btnNum1.setMinimumSize(QSize(175, 175))
        font3 = QFont()
        font3.setPointSize(93)
        font3.setBold(True)
        self.btnNum1.setFont(font3)
        self.btnNum1.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum1, 0, 0, 1, 1)

        self.btnNum2 = QPushButton(self.frCyfry)
        self.btnNum2.setObjectName(u"btnNum2")
        sizePolicy1.setHeightForWidth(self.btnNum2.sizePolicy().hasHeightForWidth())
        self.btnNum2.setSizePolicy(sizePolicy1)
        self.btnNum2.setMinimumSize(QSize(175, 175))
        self.btnNum2.setFont(font3)
        self.btnNum2.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum2, 0, 2, 1, 1)

        self.btnNum3 = QPushButton(self.frCyfry)
        self.btnNum3.setObjectName(u"btnNum3")
        sizePolicy1.setHeightForWidth(self.btnNum3.sizePolicy().hasHeightForWidth())
        self.btnNum3.setSizePolicy(sizePolicy1)
        self.btnNum3.setMinimumSize(QSize(175, 175))
        self.btnNum3.setFont(font3)
        self.btnNum3.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum3, 0, 3, 1, 1)

        self.btnNum4 = QPushButton(self.frCyfry)
        self.btnNum4.setObjectName(u"btnNum4")
        sizePolicy1.setHeightForWidth(self.btnNum4.sizePolicy().hasHeightForWidth())
        self.btnNum4.setSizePolicy(sizePolicy1)
        self.btnNum4.setMinimumSize(QSize(175, 175))
        self.btnNum4.setFont(font3)
        self.btnNum4.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum4, 0, 4, 1, 1)

        self.btnNum5 = QPushButton(self.frCyfry)
        self.btnNum5.setObjectName(u"btnNum5")
        sizePolicy1.setHeightForWidth(self.btnNum5.sizePolicy().hasHeightForWidth())
        self.btnNum5.setSizePolicy(sizePolicy1)
        self.btnNum5.setMinimumSize(QSize(175, 175))
        self.btnNum5.setFont(font3)
        self.btnNum5.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum5, 0, 5, 1, 1)

        self.btnNum6 = QPushButton(self.frCyfry)
        self.btnNum6.setObjectName(u"btnNum6")
        sizePolicy1.setHeightForWidth(self.btnNum6.sizePolicy().hasHeightForWidth())
        self.btnNum6.setSizePolicy(sizePolicy1)
        self.btnNum6.setMinimumSize(QSize(175, 175))
        self.btnNum6.setFont(font3)
        self.btnNum6.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum6, 6, 0, 1, 1)

        self.btnNum7 = QPushButton(self.frCyfry)
        self.btnNum7.setObjectName(u"btnNum7")
        sizePolicy1.setHeightForWidth(self.btnNum7.sizePolicy().hasHeightForWidth())
        self.btnNum7.setSizePolicy(sizePolicy1)
        self.btnNum7.setMinimumSize(QSize(175, 175))
        self.btnNum7.setFont(font3)
        self.btnNum7.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum7, 6, 2, 1, 1)

        self.btnNum8 = QPushButton(self.frCyfry)
        self.btnNum8.setObjectName(u"btnNum8")
        sizePolicy1.setHeightForWidth(self.btnNum8.sizePolicy().hasHeightForWidth())
        self.btnNum8.setSizePolicy(sizePolicy1)
        self.btnNum8.setMinimumSize(QSize(175, 175))
        self.btnNum8.setFont(font3)
        self.btnNum8.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum8, 6, 3, 1, 1)

        self.btnNum9 = QPushButton(self.frCyfry)
        self.btnNum9.setObjectName(u"btnNum9")
        sizePolicy1.setHeightForWidth(self.btnNum9.sizePolicy().hasHeightForWidth())
        self.btnNum9.setSizePolicy(sizePolicy1)
        self.btnNum9.setMinimumSize(QSize(175, 175))
        self.btnNum9.setFont(font3)
        self.btnNum9.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum9, 6, 4, 1, 1)

        self.btnNum0 = QPushButton(self.frCyfry)
        self.btnNum0.setObjectName(u"btnNum0")
        sizePolicy1.setHeightForWidth(self.btnNum0.sizePolicy().hasHeightForWidth())
        self.btnNum0.setSizePolicy(sizePolicy1)
        self.btnNum0.setMinimumSize(QSize(175, 175))
        self.btnNum0.setFont(font3)
        self.btnNum0.setStyleSheet(u"background-color: rgb(37, 150, 190);")

        self.gridLayout.addWidget(self.btnNum0, 6, 5, 1, 1)


        self.verticalLayout_3.addWidget(self.frCyfry)

        self.tabWidget.addTab(self.tabCyfry, "")
        self.tabLitery = QWidget()
        self.tabLitery.setObjectName(u"tabLitery")
        self.tabWidget.addTab(self.tabLitery, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 125))
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 93, 110);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btBack = QPushButton(self.frame_2)
        self.btBack.setObjectName(u"btBack")
        sizePolicy1.setHeightForWidth(self.btBack.sizePolicy().hasHeightForWidth())
        self.btBack.setSizePolicy(sizePolicy1)
        self.btBack.setMinimumSize(QSize(115, 115))
        self.btBack.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(60)
        font4.setBold(True)
        self.btBack.setFont(font4)
        self.btBack.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btBack.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.btBack)

        self.btClose = QPushButton(self.frame_2)
        self.btClose.setObjectName(u"btClose")
        sizePolicy1.setHeightForWidth(self.btClose.sizePolicy().hasHeightForWidth())
        self.btClose.setSizePolicy(sizePolicy1)
        self.btClose.setMinimumSize(QSize(115, 115))
        self.btClose.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(24)
        font5.setBold(True)
        self.btClose.setFont(font5)
        self.btClose.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon = QIcon()
        icon.addFile(u"img/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btClose.setIcon(icon)
        self.btClose.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.btClose)

        self.btAccept = QPushButton(self.frame_2)
        self.btAccept.setObjectName(u"btAccept")
        sizePolicy1.setHeightForWidth(self.btAccept.sizePolicy().hasHeightForWidth())
        self.btAccept.setSizePolicy(sizePolicy1)
        self.btAccept.setMinimumSize(QSize(115, 115))
        self.btAccept.setMaximumSize(QSize(16777215, 16777215))
        self.btAccept.setFont(font5)
        self.btAccept.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon1 = QIcon()
        icon1.addFile(u"img/yes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btAccept.setIcon(icon1)
        self.btAccept.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.btAccept)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Klawiatura", None))
        self.lbInput.setText("")
        self.btnNum1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btnNum2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btnNum3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btnNum4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btnNum5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btnNum6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btnNum7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btnNum8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btnNum9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btnNum0.setText(QCoreApplication.translate("Form", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCyfry), QCoreApplication.translate("Form", u"Cyfry", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLitery), QCoreApplication.translate("Form", u"Litery", None))
        self.btBack.setText(QCoreApplication.translate("Form", u"\u25c4", None))
        self.btClose.setText("")
        self.btAccept.setText("")
    # retranslateUi

