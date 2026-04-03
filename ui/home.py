# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1155, 800)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.frMain = QFrame(Form)
        self.frMain.setObjectName(u"frMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMain.sizePolicy().hasHeightForWidth())
        self.frMain.setSizePolicy(sizePolicy)
        self.frMain.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(34)
        font.setBold(True)
        self.frMain.setFont(font)
        self.frMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frMain)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbTime = QLabel(self.frMain)
        self.lbTime.setObjectName(u"lbTime")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbTime.sizePolicy().hasHeightForWidth())
        self.lbTime.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(100)
        font1.setBold(True)
        font1.setKerning(True)
        self.lbTime.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbTime)

        self.lbDay = QLabel(self.frMain)
        self.lbDay.setObjectName(u"lbDay")
        sizePolicy1.setHeightForWidth(self.lbDay.sizePolicy().hasHeightForWidth())
        self.lbDay.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setPointSize(48)
        font2.setBold(True)
        self.lbDay.setFont(font2)

        self.verticalLayout_2.addWidget(self.lbDay)

        self.lbDate = QLabel(self.frMain)
        self.lbDate.setObjectName(u"lbDate")
        sizePolicy1.setHeightForWidth(self.lbDate.sizePolicy().hasHeightForWidth())
        self.lbDate.setSizePolicy(sizePolicy1)
        self.lbDate.setFont(font2)

        self.verticalLayout_2.addWidget(self.lbDate)

        self.verticalSpacer_2 = QSpacerItem(50, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.lbVehNumber = QLabel(self.frMain)
        self.lbVehNumber.setObjectName(u"lbVehNumber")
        sizePolicy1.setHeightForWidth(self.lbVehNumber.sizePolicy().hasHeightForWidth())
        self.lbVehNumber.setSizePolicy(sizePolicy1)
        self.lbVehNumber.setFont(font2)

        self.verticalLayout_2.addWidget(self.lbVehNumber)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.frMain)

        self.frBottomBar = QFrame(Form)
        self.frBottomBar.setObjectName(u"frBottomBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frBottomBar.sizePolicy().hasHeightForWidth())
        self.frBottomBar.setSizePolicy(sizePolicy2)
        self.frBottomBar.setMinimumSize(QSize(0, 125))
        self.frBottomBar.setBaseSize(QSize(0, 0))
        self.frBottomBar.setStyleSheet(u"background-color: rgb(0, 93, 110);")
        self.frBottomBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frBottomBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btMenu = QPushButton(self.frBottomBar)
        self.btMenu.setObjectName(u"btMenu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btMenu.sizePolicy().hasHeightForWidth())
        self.btMenu.setSizePolicy(sizePolicy3)
        self.btMenu.setMinimumSize(QSize(250, 0))
        font3 = QFont()
        font3.setPointSize(38)
        font3.setBold(True)
        self.btMenu.setFont(font3)
        self.btMenu.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon = QIcon()
        icon.addFile(u"img/menu.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btMenu.setIcon(icon)
        self.btMenu.setIconSize(QSize(56, 56))

        self.horizontalLayout.addWidget(self.btMenu)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frStatusIcons = QFrame(self.frBottomBar)
        self.frStatusIcons.setObjectName(u"frStatusIcons")
        sizePolicy2.setHeightForWidth(self.frStatusIcons.sizePolicy().hasHeightForWidth())
        self.frStatusIcons.setSizePolicy(sizePolicy2)
        self.frStatusIcons.setMinimumSize(QSize(200, 0))
        self.frStatusIcons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frStatusIcons.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frStatusIcons)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.frBottomBar)

        self.frLeftBar = QFrame(Form)
        self.frLeftBar.setObjectName(u"frLeftBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frLeftBar.sizePolicy().hasHeightForWidth())
        self.frLeftBar.setSizePolicy(sizePolicy4)
        self.frLeftBar.setMinimumSize(QSize(0, 0))
        self.frLeftBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frLeftBar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frLeftBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btKurs = QPushButton(self.frLeftBar)
        self.btKurs.setObjectName(u"btKurs")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btKurs.sizePolicy().hasHeightForWidth())
        self.btKurs.setSizePolicy(sizePolicy5)
        self.btKurs.setMinimumSize(QSize(0, 0))
        self.btKurs.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        self.btKurs.setFont(font4)
        self.btKurs.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btKurs.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btKurs)

        self.btKas = QPushButton(self.frLeftBar)
        self.btKas.setObjectName(u"btKas")
        self.btKas.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.btKas.sizePolicy().hasHeightForWidth())
        self.btKas.setSizePolicy(sizePolicy5)
        self.btKas.setMinimumSize(QSize(0, 0))
        self.btKas.setMaximumSize(QSize(16777215, 16777215))
        self.btKas.setFont(font4)
        self.btKas.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon1 = QIcon()
        icon1.addFile(u"img/kas.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btKas.setIcon(icon1)
        self.btKas.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btKas)

        self.btCCTV = QPushButton(self.frLeftBar)
        self.btCCTV.setObjectName(u"btCCTV")
        sizePolicy5.setHeightForWidth(self.btCCTV.sizePolicy().hasHeightForWidth())
        self.btCCTV.setSizePolicy(sizePolicy5)
        self.btCCTV.setMinimumSize(QSize(0, 0))
        self.btCCTV.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setPointSize(24)
        self.btCCTV.setFont(font5)
        self.btCCTV.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon2 = QIcon()
        icon2.addFile(u"img/cctv.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btCCTV.setIcon(icon2)
        self.btCCTV.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btCCTV)

        self.btVol = QPushButton(self.frLeftBar)
        self.btVol.setObjectName(u"btVol")
        sizePolicy5.setHeightForWidth(self.btVol.sizePolicy().hasHeightForWidth())
        self.btVol.setSizePolicy(sizePolicy5)
        self.btVol.setMinimumSize(QSize(0, 0))
        self.btVol.setMaximumSize(QSize(16777215, 16777215))
        self.btVol.setFont(font5)
        self.btVol.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon3 = QIcon()
        icon3.addFile(u"img/spk.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btVol.setIcon(icon3)
        self.btVol.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btVol)

        self.btSerwis = QPushButton(self.frLeftBar)
        self.btSerwis.setObjectName(u"btSerwis")
        sizePolicy5.setHeightForWidth(self.btSerwis.sizePolicy().hasHeightForWidth())
        self.btSerwis.setSizePolicy(sizePolicy5)
        self.btSerwis.setMinimumSize(QSize(0, 0))
        self.btSerwis.setMaximumSize(QSize(16777215, 16777215))
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        font6.setUnderline(False)
        self.btSerwis.setFont(font6)
        self.btSerwis.setAutoFillBackground(False)
        self.btSerwis.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btSerwis.setIconSize(QSize(64, 64))
        self.btSerwis.setFlat(False)

        self.verticalLayout.addWidget(self.btSerwis)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.frLeftBar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbTime.setText(QCoreApplication.translate("Form", u"Czas", None))
        self.lbDay.setText(QCoreApplication.translate("Form", u"Dzie\u0144", None))
        self.lbDate.setText(QCoreApplication.translate("Form", u"Data", None))
        self.lbVehNumber.setText(QCoreApplication.translate("Form", u"Nr pojazdu: -", None))
        self.btMenu.setText(QCoreApplication.translate("Form", u" MENU", None))
        self.btKurs.setText(QCoreApplication.translate("Form", u"Kurs", None))
        self.btKas.setText("")
        self.btCCTV.setText("")
        self.btVol.setText("")
        self.btSerwis.setText(QCoreApplication.translate("Form", u"Tryb\n"
"Serwisowy", None))
    # retranslateUi

