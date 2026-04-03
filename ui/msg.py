# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msg.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1159, 800)
        self.horizontalLayout_12 = QHBoxLayout(Form)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frMain = QFrame(Form)
        self.frMain.setObjectName(u"frMain")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frMain.sizePolicy().hasHeightForWidth())
        self.frMain.setSizePolicy(sizePolicy)
        self.frMain.setFrameShape(QFrame.Shape.StyledPanel)
        self.frMain.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frMain)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbMsg = QLabel(self.frMain)
        self.lbMsg.setObjectName(u"lbMsg")
        font = QFont()
        font.setPointSize(50)
        font.setBold(True)
        self.lbMsg.setFont(font)
        self.lbMsg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lbMsg)


        self.horizontalLayout_12.addWidget(self.frMain)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbMsg.setText("")
    # retranslateUi

