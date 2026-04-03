# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kurs.ui'
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
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1155, 800)
        self.horizontalLayout_12 = QHBoxLayout(Form)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frLeftBar = QFrame(Form)
        self.frLeftBar.setObjectName(u"frLeftBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frLeftBar.sizePolicy().hasHeightForWidth())
        self.frLeftBar.setSizePolicy(sizePolicy)
        self.frLeftBar.setMinimumSize(QSize(0, 0))
        self.frLeftBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frLeftBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frLeftBar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btClose = QPushButton(self.frLeftBar)
        self.btClose.setObjectName(u"btClose")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btClose.sizePolicy().hasHeightForWidth())
        self.btClose.setSizePolicy(sizePolicy1)
        self.btClose.setMinimumSize(QSize(115, 115))
        self.btClose.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        self.btClose.setFont(font)
        self.btClose.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        icon = QIcon()
        icon.addFile(u"img/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btClose.setIcon(icon)
        self.btClose.setIconSize(QSize(64, 64))

        self.gridLayout.addWidget(self.btClose, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.frLeftBar)

        self.frMain = QFrame(Form)
        self.frMain.setObjectName(u"frMain")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frMain.sizePolicy().hasHeightForWidth())
        self.frMain.setSizePolicy(sizePolicy2)
        self.frMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frMain)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frTabs = QFrame(self.frMain)
        self.frTabs.setObjectName(u"frTabs")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frTabs.sizePolicy().hasHeightForWidth())
        self.frTabs.setSizePolicy(sizePolicy3)
        self.frTabs.setMinimumSize(QSize(0, 50))
        self.frTabs.setFrameShape(QFrame.Shape.NoFrame)
        self.frTabs.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frTabs)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tabWidget = QTabWidget(self.frTabs)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(32)
        font1.setBold(True)
        self.tabWidget.setFont(font1)
        self.taKursowka = QWidget()
        self.taKursowka.setObjectName(u"taKursowka")
        self.horizontalLayout_13 = QHBoxLayout(self.taKursowka)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frKursowka = QFrame(self.taKursowka)
        self.frKursowka.setObjectName(u"frKursowka")
        self.frKursowka.setFrameShape(QFrame.Shape.NoFrame)
        self.frKursowka.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frKursowka)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frKursowka1 = QFrame(self.frKursowka)
        self.frKursowka1.setObjectName(u"frKursowka1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frKursowka1.sizePolicy().hasHeightForWidth())
        self.frKursowka1.setSizePolicy(sizePolicy4)
        self.frKursowka1.setMinimumSize(QSize(0, 375))
        self.frKursowka1.setFrameShape(QFrame.Shape.NoFrame)
        self.frKursowka1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frKursowka1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frKursowkaLinia1 = QFrame(self.frKursowka1)
        self.frKursowkaLinia1.setObjectName(u"frKursowkaLinia1")
        self.frKursowkaLinia1.setFrameShape(QFrame.Shape.NoFrame)
        self.frKursowkaLinia1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frKursowkaLinia1)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frKursowkaLinia2 = QFrame(self.frKursowkaLinia1)
        self.frKursowkaLinia2.setObjectName(u"frKursowkaLinia2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frKursowkaLinia2.sizePolicy().hasHeightForWidth())
        self.frKursowkaLinia2.setSizePolicy(sizePolicy5)
        self.frKursowkaLinia2.setMinimumSize(QSize(650, 0))
        self.frKursowkaLinia2.setFrameShape(QFrame.Shape.NoFrame)
        self.frKursowkaLinia2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frKursowkaLinia2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.lbKursowkaLiniaName = QLabel(self.frKursowkaLinia2)
        self.lbKursowkaLiniaName.setObjectName(u"lbKursowkaLiniaName")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lbKursowkaLiniaName.sizePolicy().hasHeightForWidth())
        self.lbKursowkaLiniaName.setSizePolicy(sizePolicy6)
        self.lbKursowkaLiniaName.setMinimumSize(QSize(0, 0))
        self.lbKursowkaLiniaName.setFont(font1)
        self.lbKursowkaLiniaName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.lbKursowkaLiniaName)

        self.btKursowkaLiniaInput = QPushButton(self.frKursowkaLinia2)
        self.btKursowkaLiniaInput.setObjectName(u"btKursowkaLiniaInput")
        sizePolicy1.setHeightForWidth(self.btKursowkaLiniaInput.sizePolicy().hasHeightForWidth())
        self.btKursowkaLiniaInput.setSizePolicy(sizePolicy1)
        self.btKursowkaLiniaInput.setMinimumSize(QSize(400, 75))
        self.btKursowkaLiniaInput.setFont(font1)
        self.btKursowkaLiniaInput.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);")

        self.horizontalLayout.addWidget(self.btKursowkaLiniaInput)


        self.horizontalLayout_8.addWidget(self.frKursowkaLinia2)


        self.verticalLayout_5.addWidget(self.frKursowkaLinia1)

        self.frBrygada1 = QFrame(self.frKursowka1)
        self.frBrygada1.setObjectName(u"frBrygada1")
        self.frBrygada1.setFrameShape(QFrame.Shape.NoFrame)
        self.frBrygada1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frBrygada1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frBrygada2 = QFrame(self.frBrygada1)
        self.frBrygada2.setObjectName(u"frBrygada2")
        sizePolicy5.setHeightForWidth(self.frBrygada2.sizePolicy().hasHeightForWidth())
        self.frBrygada2.setSizePolicy(sizePolicy5)
        self.frBrygada2.setMinimumSize(QSize(650, 0))
        self.frBrygada2.setFrameShape(QFrame.Shape.NoFrame)
        self.frBrygada2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frBrygada2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lbBrygadaName = QLabel(self.frBrygada2)
        self.lbBrygadaName.setObjectName(u"lbBrygadaName")
        sizePolicy6.setHeightForWidth(self.lbBrygadaName.sizePolicy().hasHeightForWidth())
        self.lbBrygadaName.setSizePolicy(sizePolicy6)
        self.lbBrygadaName.setMinimumSize(QSize(0, 0))
        self.lbBrygadaName.setFont(font1)
        self.lbBrygadaName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.lbBrygadaName)

        self.btBrygadaInput = QPushButton(self.frBrygada2)
        self.btBrygadaInput.setObjectName(u"btBrygadaInput")
        sizePolicy1.setHeightForWidth(self.btBrygadaInput.sizePolicy().hasHeightForWidth())
        self.btBrygadaInput.setSizePolicy(sizePolicy1)
        self.btBrygadaInput.setMinimumSize(QSize(400, 75))
        self.btBrygadaInput.setFont(font1)
        self.btBrygadaInput.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);")

        self.horizontalLayout_4.addWidget(self.btBrygadaInput)


        self.horizontalLayout_9.addWidget(self.frBrygada2)


        self.verticalLayout_5.addWidget(self.frBrygada1)

        self.frTypDnia1 = QFrame(self.frKursowka1)
        self.frTypDnia1.setObjectName(u"frTypDnia1")
        self.frTypDnia1.setFrameShape(QFrame.Shape.NoFrame)
        self.frTypDnia1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frTypDnia1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frTypDnia2 = QFrame(self.frTypDnia1)
        self.frTypDnia2.setObjectName(u"frTypDnia2")
        sizePolicy5.setHeightForWidth(self.frTypDnia2.sizePolicy().hasHeightForWidth())
        self.frTypDnia2.setSizePolicy(sizePolicy5)
        self.frTypDnia2.setMinimumSize(QSize(650, 0))
        self.frTypDnia2.setFrameShape(QFrame.Shape.NoFrame)
        self.frTypDnia2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frTypDnia2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lbTypDniaName = QLabel(self.frTypDnia2)
        self.lbTypDniaName.setObjectName(u"lbTypDniaName")
        sizePolicy6.setHeightForWidth(self.lbTypDniaName.sizePolicy().hasHeightForWidth())
        self.lbTypDniaName.setSizePolicy(sizePolicy6)
        self.lbTypDniaName.setMinimumSize(QSize(0, 0))
        self.lbTypDniaName.setFont(font1)
        self.lbTypDniaName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.lbTypDniaName)

        self.btTypDniaInput = QPushButton(self.frTypDnia2)
        self.btTypDniaInput.setObjectName(u"btTypDniaInput")
        sizePolicy1.setHeightForWidth(self.btTypDniaInput.sizePolicy().hasHeightForWidth())
        self.btTypDniaInput.setSizePolicy(sizePolicy1)
        self.btTypDniaInput.setMinimumSize(QSize(400, 75))
        self.btTypDniaInput.setFont(font1)
        self.btTypDniaInput.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);")

        self.horizontalLayout_6.addWidget(self.btTypDniaInput)


        self.horizontalLayout_10.addWidget(self.frTypDnia2)


        self.verticalLayout_5.addWidget(self.frTypDnia1)


        self.verticalLayout_2.addWidget(self.frKursowka1)

        self.frKursowkaAcceptButton = QFrame(self.frKursowka)
        self.frKursowkaAcceptButton.setObjectName(u"frKursowkaAcceptButton")
        sizePolicy3.setHeightForWidth(self.frKursowkaAcceptButton.sizePolicy().hasHeightForWidth())
        self.frKursowkaAcceptButton.setSizePolicy(sizePolicy3)
        self.frKursowkaAcceptButton.setMinimumSize(QSize(0, 0))
        self.frKursowkaAcceptButton.setFrameShape(QFrame.Shape.NoFrame)
        self.frKursowkaAcceptButton.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frKursowkaAcceptButton)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btKursowkaAccept = QPushButton(self.frKursowkaAcceptButton)
        self.btKursowkaAccept.setObjectName(u"btKursowkaAccept")
        sizePolicy1.setHeightForWidth(self.btKursowkaAccept.sizePolicy().hasHeightForWidth())
        self.btKursowkaAccept.setSizePolicy(sizePolicy1)
        self.btKursowkaAccept.setMinimumSize(QSize(500, 150))
        self.btKursowkaAccept.setMaximumSize(QSize(16777215, 16777215))
        self.btKursowkaAccept.setFont(font)
        self.btKursowkaAccept.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btKursowkaAccept.setIconSize(QSize(64, 64))

        self.horizontalLayout_7.addWidget(self.btKursowkaAccept)


        self.verticalLayout_2.addWidget(self.frKursowkaAcceptButton)


        self.horizontalLayout_13.addWidget(self.frKursowka)

        self.tabWidget.addTab(self.taKursowka, "")
        self.taLiniaWariant = QWidget()
        self.taLiniaWariant.setObjectName(u"taLiniaWariant")
        self.verticalLayout_3 = QVBoxLayout(self.taLiniaWariant)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frLiniaWariant = QFrame(self.taLiniaWariant)
        self.frLiniaWariant.setObjectName(u"frLiniaWariant")
        self.frLiniaWariant.setFrameShape(QFrame.Shape.NoFrame)
        self.frLiniaWariant.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frLiniaWariant)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frLiniaWariant1 = QFrame(self.frLiniaWariant)
        self.frLiniaWariant1.setObjectName(u"frLiniaWariant1")
        sizePolicy4.setHeightForWidth(self.frLiniaWariant1.sizePolicy().hasHeightForWidth())
        self.frLiniaWariant1.setSizePolicy(sizePolicy4)
        self.frLiniaWariant1.setMinimumSize(QSize(0, 375))
        self.frLiniaWariant1.setFrameShape(QFrame.Shape.NoFrame)
        self.frLiniaWariant1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frLiniaWariant1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frLWLinia1 = QFrame(self.frLiniaWariant1)
        self.frLWLinia1.setObjectName(u"frLWLinia1")
        self.frLWLinia1.setFrameShape(QFrame.Shape.NoFrame)
        self.frLWLinia1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frLWLinia1)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frLWLinia2 = QFrame(self.frLWLinia1)
        self.frLWLinia2.setObjectName(u"frLWLinia2")
        sizePolicy5.setHeightForWidth(self.frLWLinia2.sizePolicy().hasHeightForWidth())
        self.frLWLinia2.setSizePolicy(sizePolicy5)
        self.frLWLinia2.setMinimumSize(QSize(650, 0))
        self.frLWLinia2.setFrameShape(QFrame.Shape.NoFrame)
        self.frLWLinia2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frLWLinia2)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_16.setContentsMargins(9, -1, -1, -1)
        self.lbLWLiniaName = QLabel(self.frLWLinia2)
        self.lbLWLiniaName.setObjectName(u"lbLWLiniaName")
        sizePolicy6.setHeightForWidth(self.lbLWLiniaName.sizePolicy().hasHeightForWidth())
        self.lbLWLiniaName.setSizePolicy(sizePolicy6)
        self.lbLWLiniaName.setMinimumSize(QSize(0, 0))
        self.lbLWLiniaName.setFont(font1)
        self.lbLWLiniaName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_16.addWidget(self.lbLWLiniaName)

        self.btLWLiniaInput = QPushButton(self.frLWLinia2)
        self.btLWLiniaInput.setObjectName(u"btLWLiniaInput")
        sizePolicy1.setHeightForWidth(self.btLWLiniaInput.sizePolicy().hasHeightForWidth())
        self.btLWLiniaInput.setSizePolicy(sizePolicy1)
        self.btLWLiniaInput.setMinimumSize(QSize(400, 75))
        self.btLWLiniaInput.setFont(font1)
        self.btLWLiniaInput.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);")

        self.horizontalLayout_16.addWidget(self.btLWLiniaInput)


        self.horizontalLayout_15.addWidget(self.frLWLinia2)


        self.verticalLayout_6.addWidget(self.frLWLinia1)

        self.frWariant1 = QFrame(self.frLiniaWariant1)
        self.frWariant1.setObjectName(u"frWariant1")
        self.frWariant1.setFrameShape(QFrame.Shape.NoFrame)
        self.frWariant1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frWariant1)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frWariant2 = QFrame(self.frWariant1)
        self.frWariant2.setObjectName(u"frWariant2")
        sizePolicy5.setHeightForWidth(self.frWariant2.sizePolicy().hasHeightForWidth())
        self.frWariant2.setSizePolicy(sizePolicy5)
        self.frWariant2.setMinimumSize(QSize(650, 0))
        self.frWariant2.setFrameShape(QFrame.Shape.NoFrame)
        self.frWariant2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frWariant2)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lbWariantName = QLabel(self.frWariant2)
        self.lbWariantName.setObjectName(u"lbWariantName")
        sizePolicy6.setHeightForWidth(self.lbWariantName.sizePolicy().hasHeightForWidth())
        self.lbWariantName.setSizePolicy(sizePolicy6)
        self.lbWariantName.setMinimumSize(QSize(0, 0))
        self.lbWariantName.setFont(font1)
        self.lbWariantName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_19.addWidget(self.lbWariantName)

        self.btWariantInput = QPushButton(self.frWariant2)
        self.btWariantInput.setObjectName(u"btWariantInput")
        sizePolicy1.setHeightForWidth(self.btWariantInput.sizePolicy().hasHeightForWidth())
        self.btWariantInput.setSizePolicy(sizePolicy1)
        self.btWariantInput.setMinimumSize(QSize(400, 75))
        self.btWariantInput.setFont(font1)
        self.btWariantInput.setStyleSheet(u"background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);background-color: rgb(59, 59, 59);\n"
"border-color: rgb(141, 143, 140);")

        self.horizontalLayout_19.addWidget(self.btWariantInput)


        self.horizontalLayout_18.addWidget(self.frWariant2)


        self.verticalLayout_6.addWidget(self.frWariant1)


        self.verticalLayout_4.addWidget(self.frLiniaWariant1)

        self.frLiniaWariantAcceptButton = QFrame(self.frLiniaWariant)
        self.frLiniaWariantAcceptButton.setObjectName(u"frLiniaWariantAcceptButton")
        self.frLiniaWariantAcceptButton.setFrameShape(QFrame.Shape.NoFrame)
        self.frLiniaWariantAcceptButton.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frLiniaWariantAcceptButton)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btLiniaWariantAccept = QPushButton(self.frLiniaWariantAcceptButton)
        self.btLiniaWariantAccept.setObjectName(u"btLiniaWariantAccept")
        sizePolicy1.setHeightForWidth(self.btLiniaWariantAccept.sizePolicy().hasHeightForWidth())
        self.btLiniaWariantAccept.setSizePolicy(sizePolicy1)
        self.btLiniaWariantAccept.setMinimumSize(QSize(500, 150))
        self.btLiniaWariantAccept.setMaximumSize(QSize(16777215, 16777215))
        self.btLiniaWariantAccept.setFont(font)
        self.btLiniaWariantAccept.setStyleSheet(u"background-color: rgb(37, 150, 190);")
        self.btLiniaWariantAccept.setIconSize(QSize(64, 64))

        self.horizontalLayout_14.addWidget(self.btLiniaWariantAccept)


        self.verticalLayout_4.addWidget(self.frLiniaWariantAcceptButton)


        self.verticalLayout_3.addWidget(self.frLiniaWariant)

        self.tabWidget.addTab(self.taLiniaWariant, "")

        self.horizontalLayout_11.addWidget(self.tabWidget)


        self.verticalLayout.addWidget(self.frTabs)


        self.horizontalLayout_12.addWidget(self.frMain)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btClose.setText("")
        self.lbKursowkaLiniaName.setText(QCoreApplication.translate("Form", u"Linia:", None))
        self.btKursowkaLiniaInput.setText("")
        self.lbBrygadaName.setText(QCoreApplication.translate("Form", u"Brygada:", None))
        self.btBrygadaInput.setText("")
        self.lbTypDniaName.setText(QCoreApplication.translate("Form", u"Typ dnia:", None))
        self.btTypDniaInput.setText("")
        self.btKursowkaAccept.setText(QCoreApplication.translate("Form", u"Zatwierd\u017a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.taKursowka), QCoreApplication.translate("Form", u"Kurs\u00f3wka", None))
        self.lbLWLiniaName.setText(QCoreApplication.translate("Form", u"Linia:", None))
        self.btLWLiniaInput.setText("")
        self.lbWariantName.setText(QCoreApplication.translate("Form", u"Wariant:", None))
        self.btWariantInput.setText("")
        self.btLiniaWariantAccept.setText(QCoreApplication.translate("Form", u"Zatwierd\u017a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.taLiniaWariant), QCoreApplication.translate("Form", u"Linia i wariant", None))
    # retranslateUi

