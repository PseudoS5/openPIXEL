# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wkursie.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1155, 800)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.frBottomBar = QFrame(Form)
        self.frBottomBar.setObjectName(u"frBottomBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frBottomBar.sizePolicy().hasHeightForWidth())
        self.frBottomBar.setSizePolicy(sizePolicy)
        self.frBottomBar.setMinimumSize(QSize(0, 125))
        self.frBottomBar.setBaseSize(QSize(0, 0))
        self.frBottomBar.setStyleSheet(u"background-color: rgb(0, 93, 110);")
        self.frBottomBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frBottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frBottomBar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btMenu = QPushButton(self.frBottomBar)
        self.btMenu.setObjectName(u"btMenu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btMenu.sizePolicy().hasHeightForWidth())
        self.btMenu.setSizePolicy(sizePolicy1)
        self.btMenu.setMinimumSize(QSize(250, 0))
        font = QFont()
        font.setPointSize(38)
        font.setBold(True)
        self.btMenu.setFont(font)
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
        sizePolicy.setHeightForWidth(self.frStatusIcons.sizePolicy().hasHeightForWidth())
        self.frStatusIcons.setSizePolicy(sizePolicy)
        self.frStatusIcons.setMinimumSize(QSize(200, 0))
        self.frStatusIcons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frStatusIcons.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frStatusIcons)


        self.formLayout.setWidget(1, QFormLayout.ItemRole.SpanningRole, self.frBottomBar)

        self.frLeftBar = QFrame(Form)
        self.frLeftBar.setObjectName(u"frLeftBar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frLeftBar.sizePolicy().hasHeightForWidth())
        self.frLeftBar.setSizePolicy(sizePolicy2)
        self.frLeftBar.setMinimumSize(QSize(0, 0))
        self.frLeftBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frLeftBar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frLeftBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btKurs = QPushButton(self.frLeftBar)
        self.btKurs.setObjectName(u"btKurs")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btKurs.sizePolicy().hasHeightForWidth())
        self.btKurs.setSizePolicy(sizePolicy3)
        self.btKurs.setMinimumSize(QSize(0, 0))
        self.btKurs.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.btKurs.setFont(font1)
        self.btKurs.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btKurs.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btKurs)

        self.btKas = QPushButton(self.frLeftBar)
        self.btKas.setObjectName(u"btKas")
        self.btKas.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btKas.sizePolicy().hasHeightForWidth())
        self.btKas.setSizePolicy(sizePolicy3)
        self.btKas.setMinimumSize(QSize(0, 0))
        self.btKas.setMaximumSize(QSize(16777215, 16777215))
        self.btKas.setFont(font1)
        self.btKas.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon1 = QIcon()
        icon1.addFile(u"img/kas.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btKas.setIcon(icon1)
        self.btKas.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btKas)

        self.btCCTV = QPushButton(self.frLeftBar)
        self.btCCTV.setObjectName(u"btCCTV")
        sizePolicy3.setHeightForWidth(self.btCCTV.sizePolicy().hasHeightForWidth())
        self.btCCTV.setSizePolicy(sizePolicy3)
        self.btCCTV.setMinimumSize(QSize(0, 0))
        self.btCCTV.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(24)
        self.btCCTV.setFont(font2)
        self.btCCTV.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon2 = QIcon()
        icon2.addFile(u"img/cctv.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btCCTV.setIcon(icon2)
        self.btCCTV.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btCCTV)

        self.btVol = QPushButton(self.frLeftBar)
        self.btVol.setObjectName(u"btVol")
        sizePolicy3.setHeightForWidth(self.btVol.sizePolicy().hasHeightForWidth())
        self.btVol.setSizePolicy(sizePolicy3)
        self.btVol.setMinimumSize(QSize(0, 0))
        self.btVol.setMaximumSize(QSize(16777215, 16777215))
        self.btVol.setFont(font2)
        self.btVol.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon3 = QIcon()
        icon3.addFile(u"img/spk.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btVol.setIcon(icon3)
        self.btVol.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.btVol)

        self.btSerwis = QPushButton(self.frLeftBar)
        self.btSerwis.setObjectName(u"btSerwis")
        sizePolicy3.setHeightForWidth(self.btSerwis.sizePolicy().hasHeightForWidth())
        self.btSerwis.setSizePolicy(sizePolicy3)
        self.btSerwis.setMinimumSize(QSize(0, 0))
        self.btSerwis.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setUnderline(False)
        self.btSerwis.setFont(font3)
        self.btSerwis.setAutoFillBackground(False)
        self.btSerwis.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btSerwis.setIconSize(QSize(64, 64))
        self.btSerwis.setFlat(False)

        self.verticalLayout.addWidget(self.btSerwis)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.frLeftBar)

        self.frMain = QFrame(Form)
        self.frMain.setObjectName(u"frMain")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frMain.sizePolicy().hasHeightForWidth())
        self.frMain.setSizePolicy(sizePolicy4)
        self.frMain.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(34)
        font4.setBold(True)
        self.frMain.setFont(font4)
        self.frMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frMain)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frTop = QFrame(self.frMain)
        self.frTop.setObjectName(u"frTop")
        self.frTop.setFrameShape(QFrame.Shape.NoFrame)
        self.frTop.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frTop)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.frLK = QFrame(self.frTop)
        self.frLK.setObjectName(u"frLK")
        self.frLK.setFrameShape(QFrame.Shape.NoFrame)
        self.frLK.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frLK)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frLK)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbKierunek = QLabel(self.frame)
        self.lbKierunek.setObjectName(u"lbKierunek")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lbKierunek.sizePolicy().hasHeightForWidth())
        self.lbKierunek.setSizePolicy(sizePolicy5)
        self.lbKierunek.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lbKierunek)

        self.lbTime = QLabel(self.frame)
        self.lbTime.setObjectName(u"lbTime")
        self.lbTime.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbTime)


        self.verticalLayout_2.addWidget(self.frame)

        self.btLK = QPushButton(self.frLK)
        self.btLK.setObjectName(u"btLK")
        sizePolicy1.setHeightForWidth(self.btLK.sizePolicy().hasHeightForWidth())
        self.btLK.setSizePolicy(sizePolicy1)
        self.btLK.setMinimumSize(QSize(250, 0))
        self.btLK.setFont(font)
        self.btLK.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btLK.setIconSize(QSize(56, 56))
        self.btLK.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.btLK)


        self.verticalLayout_3.addWidget(self.frLK)

        self.frZadNrPoj = QFrame(self.frTop)
        self.frZadNrPoj.setObjectName(u"frZadNrPoj")
        self.frZadNrPoj.setFrameShape(QFrame.Shape.NoFrame)
        self.frZadNrPoj.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frZadNrPoj)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbZadanie = QLabel(self.frZadNrPoj)
        self.lbZadanie.setObjectName(u"lbZadanie")
        sizePolicy5.setHeightForWidth(self.lbZadanie.sizePolicy().hasHeightForWidth())
        self.lbZadanie.setSizePolicy(sizePolicy5)
        self.lbZadanie.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lbZadanie)

        self.lbKierunek_3 = QLabel(self.frZadNrPoj)
        self.lbKierunek_3.setObjectName(u"lbKierunek_3")
        sizePolicy5.setHeightForWidth(self.lbKierunek_3.sizePolicy().hasHeightForWidth())
        self.lbKierunek_3.setSizePolicy(sizePolicy5)
        self.lbKierunek_3.setFont(font1)
        self.lbKierunek_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbKierunek_3)


        self.verticalLayout_3.addWidget(self.frZadNrPoj)

        self.verticalSpacer = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.lbIloscPrzystankow = QLabel(self.frTop)
        self.lbIloscPrzystankow.setObjectName(u"lbIloscPrzystankow")
        sizePolicy5.setHeightForWidth(self.lbIloscPrzystankow.sizePolicy().hasHeightForWidth())
        self.lbIloscPrzystankow.setSizePolicy(sizePolicy5)
        self.lbIloscPrzystankow.setFont(font1)

        self.verticalLayout_3.addWidget(self.lbIloscPrzystankow)


        self.verticalLayout_4.addWidget(self.frTop)

        self.frPrzystanki = QFrame(self.frMain)
        self.frPrzystanki.setObjectName(u"frPrzystanki")
        self.frPrzystanki.setFrameShape(QFrame.Shape.NoFrame)
        self.frPrzystanki.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frPrzystanki)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btPrzystanek1 = QPushButton(self.frPrzystanki)
        self.btPrzystanek1.setObjectName(u"btPrzystanek1")
        sizePolicy1.setHeightForWidth(self.btPrzystanek1.sizePolicy().hasHeightForWidth())
        self.btPrzystanek1.setSizePolicy(sizePolicy1)
        self.btPrzystanek1.setMinimumSize(QSize(250, 0))
        font5 = QFont()
        font5.setPointSize(22)
        font5.setBold(True)
        self.btPrzystanek1.setFont(font5)
        self.btPrzystanek1.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btPrzystanek1.setIconSize(QSize(56, 56))
        self.btPrzystanek1.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btPrzystanek1, 1, 1, 1, 1)

        self.btPrzystanek2 = QPushButton(self.frPrzystanki)
        self.btPrzystanek2.setObjectName(u"btPrzystanek2")
        sizePolicy1.setHeightForWidth(self.btPrzystanek2.sizePolicy().hasHeightForWidth())
        self.btPrzystanek2.setSizePolicy(sizePolicy1)
        self.btPrzystanek2.setMinimumSize(QSize(250, 0))
        self.btPrzystanek2.setFont(font5)
        self.btPrzystanek2.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btPrzystanek2.setIconSize(QSize(56, 56))
        self.btPrzystanek2.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btPrzystanek2, 2, 1, 1, 1)

        self.btOdchylka = QPushButton(self.frPrzystanki)
        self.btOdchylka.setObjectName(u"btOdchylka")
        sizePolicy1.setHeightForWidth(self.btOdchylka.sizePolicy().hasHeightForWidth())
        self.btOdchylka.setSizePolicy(sizePolicy1)
        self.btOdchylka.setMinimumSize(QSize(250, 0))
        font6 = QFont()
        font6.setPointSize(50)
        font6.setBold(True)
        self.btOdchylka.setFont(font6)
        self.btOdchylka.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btOdchylka.setIconSize(QSize(56, 56))
        self.btOdchylka.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btOdchylka, 1, 0, 2, 1)

        self.btPrzystanek = QPushButton(self.frPrzystanki)
        self.btPrzystanek.setObjectName(u"btPrzystanek")
        sizePolicy1.setHeightForWidth(self.btPrzystanek.sizePolicy().hasHeightForWidth())
        self.btPrzystanek.setSizePolicy(sizePolicy1)
        self.btPrzystanek.setMinimumSize(QSize(250, 0))
        font7 = QFont()
        font7.setPointSize(27)
        font7.setBold(True)
        self.btPrzystanek.setFont(font7)
        self.btPrzystanek.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btPrzystanek.setIconSize(QSize(56, 56))
        self.btPrzystanek.setAutoExclusive(False)

        self.gridLayout.addWidget(self.btPrzystanek, 0, 0, 1, 2)


        self.verticalLayout_4.addWidget(self.frPrzystanki)

        self.frBottomBar_2 = QFrame(self.frMain)
        self.frBottomBar_2.setObjectName(u"frBottomBar_2")
        self.frBottomBar_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frBottomBar_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frBottomBar_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btLeft = QPushButton(self.frBottomBar_2)
        self.btLeft.setObjectName(u"btLeft")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btLeft.sizePolicy().hasHeightForWidth())
        self.btLeft.setSizePolicy(sizePolicy6)
        self.btLeft.setMinimumSize(QSize(115, 115))
        self.btLeft.setMaximumSize(QSize(16777215, 16777215))
        font8 = QFont()
        font8.setPointSize(60)
        font8.setBold(True)
        self.btLeft.setFont(font8)
        self.btLeft.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btLeft.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.btLeft)

        self.btCancel = QPushButton(self.frBottomBar_2)
        self.btCancel.setObjectName(u"btCancel")
        sizePolicy6.setHeightForWidth(self.btCancel.sizePolicy().hasHeightForWidth())
        self.btCancel.setSizePolicy(sizePolicy6)
        self.btCancel.setMinimumSize(QSize(150, 115))
        self.btCancel.setMaximumSize(QSize(16777215, 16777215))
        self.btCancel.setFont(font1)
        self.btCancel.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon4 = QIcon()
        icon4.addFile(u"img/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btCancel.setIcon(icon4)
        self.btCancel.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.btCancel)

        self.btAccept = QPushButton(self.frBottomBar_2)
        self.btAccept.setObjectName(u"btAccept")
        sizePolicy6.setHeightForWidth(self.btAccept.sizePolicy().hasHeightForWidth())
        self.btAccept.setSizePolicy(sizePolicy6)
        self.btAccept.setMinimumSize(QSize(150, 115))
        self.btAccept.setMaximumSize(QSize(16777215, 16777215))
        self.btAccept.setFont(font1)
        self.btAccept.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon5 = QIcon()
        icon5.addFile(u"img/yes.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btAccept.setIcon(icon5)
        self.btAccept.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.btAccept)

        self.btRight = QPushButton(self.frBottomBar_2)
        self.btRight.setObjectName(u"btRight")
        sizePolicy6.setHeightForWidth(self.btRight.sizePolicy().hasHeightForWidth())
        self.btRight.setSizePolicy(sizePolicy6)
        self.btRight.setMinimumSize(QSize(115, 115))
        self.btRight.setMaximumSize(QSize(16777215, 16777215))
        self.btRight.setFont(font8)
        self.btRight.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btRight.setIconSize(QSize(64, 64))

        self.horizontalLayout_3.addWidget(self.btRight)

        self.btWymelduj = QPushButton(self.frBottomBar_2)
        self.btWymelduj.setObjectName(u"btWymelduj")
        sizePolicy6.setHeightForWidth(self.btWymelduj.sizePolicy().hasHeightForWidth())
        self.btWymelduj.setSizePolicy(sizePolicy6)
        self.btWymelduj.setMinimumSize(QSize(250, 115))
        font9 = QFont()
        font9.setPointSize(30)
        font9.setBold(True)
        self.btWymelduj.setFont(font9)
        self.btWymelduj.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btWymelduj.setIconSize(QSize(56, 56))

        self.horizontalLayout_3.addWidget(self.btWymelduj)


        self.verticalLayout_4.addWidget(self.frBottomBar_2)


        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.frMain)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btMenu.setText(QCoreApplication.translate("Form", u" MENU", None))
        self.btKurs.setText(QCoreApplication.translate("Form", u"Kurs", None))
        self.btKas.setText("")
        self.btCCTV.setText("")
        self.btVol.setText("")
        self.btSerwis.setText(QCoreApplication.translate("Form", u"Tryb\n"
"Serwisowy", None))
        self.lbKierunek.setText(QCoreApplication.translate("Form", u"Linia/Kierunek:", None))
        self.lbTime.setText(QCoreApplication.translate("Form", u"Czas", None))
        self.btLK.setText("")
        self.lbZadanie.setText(QCoreApplication.translate("Form", u"Zadanie: L/B/TD", None))
        self.lbKierunek_3.setText(QCoreApplication.translate("Form", u"Nr pojazdu: -", None))
        self.lbIloscPrzystankow.setText(QCoreApplication.translate("Form", u"Przystanek 0/20", None))
        self.btPrzystanek1.setText("")
        self.btPrzystanek2.setText("")
        self.btOdchylka.setText("")
        self.btPrzystanek.setText("")
        self.btLeft.setText(QCoreApplication.translate("Form", u"\u25c4", None))
        self.btCancel.setText("")
        self.btAccept.setText("")
        self.btRight.setText(QCoreApplication.translate("Form", u"\u25ba", None))
        self.btWymelduj.setText(QCoreApplication.translate("Form", u"Wymelduj", None))
    # retranslateUi

