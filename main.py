from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGraphicsView, QGraphicsScene, QFrame
)
from PySide6.QtCore import Qt, QTimer, QTime, QDate, QUrl
from PySide6.QtMultimedia import QSoundEffect
import sys

import requests
import numpy as np
from PIL import Image


from ui.home import Ui_Form as HomeUI
from ui.kurs import Ui_Form as KursUI
from ui.wkursie import Ui_Form as WKursieUI
from ui.keyboard import Ui_Form as KeyboardUI
from ui.msg import Ui_Form as MsgUI

import json

# UI_GEOMETRY_X = 1540
# UI_GEOMETRY_Y = 1040

# UI_GEOMETRY_X = 1155
# UI_GEOMETRY_Y = 800

UI_GEOMETRY_X = 1155
UI_GEOMETRY_Y = 800

START_UI_GEOMETRY_X = 1000
START_UI_GEOMETRY_Y = 500

class MainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.touchbeep = QSoundEffect()
        self.touchbeep.setSource(QUrl.fromLocalFile("img/touch2.wav"))
        self.touchbeep.setVolume(1)

        self.longbeep = QSoundEffect()
        self.longbeep.setSource(QUrl.fromLocalFile("img/long.wav"))
        self.longbeep.setVolume(1)

        self.warnbeep = QSoundEffect()
        self.warnbeep.setSource(QUrl.fromLocalFile("img/warn.wav"))
        self.warnbeep.setVolume(1)

        ########## WIDGETS SETUP ##########

        self.homeWidget = QWidget(self)
        self.homeUI = HomeUI()
        self.homeUI.setupUi(self.homeWidget)

        self.kursWidget = QWidget(self)
        self.kursUI = KursUI()
        self.kursUI.setupUi(self.kursWidget)
        self.kursWidget.hide()

        self.wKursieWidget = QWidget(self)
        self.wKursieUI = WKursieUI()
        self.wKursieUI.setupUi(self.wKursieWidget)
        self.wKursieWidget.hide()

        self.keyboardWidget = QWidget(self)
        self.keyboardUI = KeyboardUI()
        self.keyboardUI.setupUi(self.keyboardWidget)
        self.keyboardWidget.hide()

        self.msgWidget = QWidget(self)
        self.msgUI = MsgUI()
        self.msgUI.setupUi(self.msgWidget)
        self.msgWidget.hide()

        self.currentUI = self.homeWidget

        self.widgets = [self.homeWidget, self.kursWidget, self.wKursieWidget, self.keyboardWidget, self.msgWidget]

        ########## BUTTON CONNECTIONS ##########

        ##### Home #####

        self.homeUI.btKurs.clicked.connect(lambda: self.show_widget(self.kursWidget))

        ##### Kurs #####
        self.kursUI.btClose.clicked.connect(lambda: self.show_widget(self.homeWidget))
        self.kursUI.btKursowkaAccept.clicked.connect(lambda: self.accept_kursowka_data(self.kursUI.btKursowkaLiniaInput.text(), self.kursUI.btBrygadaInput.text(), self.kursUI.btTypDniaInput.text()))
        self.kursUI.btLiniaWariantAccept.clicked.connect(lambda: self.accept_lw_data(self.kursUI.btLWLiniaInput.text(), self.kursUI.btWariantInput.text()))


        self.KursUIkeyboard_showers = [self.kursUI.btKursowkaLiniaInput, self.kursUI.btBrygadaInput, self.kursUI.btTypDniaInput, self.kursUI.btLWLiniaInput, self.kursUI.btWariantInput]

        for keyboard_shower in self.KursUIkeyboard_showers:
            keyboard_shower.clicked.connect(
                lambda checked=False, ks=keyboard_shower: self.show_keyboard(ks, self.kursWidget)
            )

        ##### W kursie #####
        
        self.wKursieUI.btWymelduj.clicked.connect(lambda: self.exit_wkursie())

        ########## KEYBOARD ##########

        self.keyboardInput = ""
        self.keyboardTarget = None
        self.keyboardTargetWidget = None

        self.keyboardButtons = [
            (self.keyboardUI.btnNum0, "0"),
            (self.keyboardUI.btnNum1, "1"),
            (self.keyboardUI.btnNum2, "2"),
            (self.keyboardUI.btnNum3, "3"),
            (self.keyboardUI.btnNum4, "4"),
            (self.keyboardUI.btnNum5, "5"),
            (self.keyboardUI.btnNum6, "6"),
            (self.keyboardUI.btnNum7, "7"),
            (self.keyboardUI.btnNum8, "8"),
            (self.keyboardUI.btnNum9, "9"),
        ]

        for button, value in self.keyboardButtons:
            button.clicked.connect(lambda checked=False, v=value: self.add_to_input(v))

        self.keyboardUI.btAccept.clicked.connect(self.accept_keyboard_input)
        self.keyboardUI.btBack.clicked.connect(self.remove_from_input)
        self.keyboardUI.btClose.clicked.connect(self.close_keyboard)

        
        ########## STARTING THE CLOCK + SETTING THE SIZE ##########

        self.setFixedSize(UI_GEOMETRY_X, UI_GEOMETRY_Y)

        self.start_clock()

        self._connect_touchbeep_all_buttons()

    def exit_wkursie(self):
        self.show_widget(self.homeWidget)
        to_clear = [self.kursUI.btKursowkaLiniaInput, self.kursUI.btBrygadaInput, self.kursUI.btTypDniaInput, self.kursUI.btLWLiniaInput, self.kursUI.btWariantInput]

        for x in to_clear:
            x.setText("")

        self.send_data_to_board("blank.png")

        self.show_msg("Koniec realizacji\nprzewozów.")
        
    def show_msg(self, text):
        self.msgUI.lbMsg.setText(text)
        self.show_widget(self.msgWidget)
        QTimer.singleShot(3000, lambda: self.show_widget(self.currentUI))


    def accept_kursowka_data(self, linia, brygada, typ_dnia):
        pass

    def accept_lw_data(self, linia, wariant):




        with open("DB/warianty.json") as f:
            d = json.load(f)
            warianty = d["warianty"]
            
            matched = next(
                (x for x in warianty if x["linia"] == linia and x["wariant"] == wariant),
                None
            )

            if matched:
                self.show_widget(self.wKursieWidget)
                to_hide = [self.wKursieUI.frPrzystanki, self.wKursieUI.btRight, self.wKursieUI.btLeft, self.wKursieUI.btCancel, self.wKursieUI.btAccept, self.wKursieUI.lbIloscPrzystankow]
                for x in to_hide:
                    x.setVisible(False)

                tresci = matched["tresci"]

                self.show_msg("Rozpoczęto kurs.")
                front = next((x for x in tresci if x["tablica"] == "front"), None)
                if front:
                    self.send_data_to_board(front["tresc"])
                self.wKursieUI.btLK.setText(matched["nazwa"] + "  " + matched["kierunek"])
                self.wKursieUI.lbZadanie.setText(matched["linia"] + "/" + matched["wariant"])
            else:
                self.show_msg("Błędne dane!")

            # self.wKursieUI.btLK.setText(warianty[])


    def show_widget(self, widget):
        if widget != self.msgWidget:
            self.currentUI = widget

        widget.show()

        for x in self.widgets:
            if x != widget:
                x.hide()

                

    def show_keyboard(self, target, widget):
        self.keyboardTarget = target
        self.keyboardTargetWidget = widget

        self.keyboardInput = target.text()
        self.keyboardUI.lbInput.setText(self.keyboardInput)

        self.show_widget(self.keyboardWidget)

    def accept_keyboard_input(self):
        if self.keyboardTarget:
            self.keyboardTarget.setText(self.keyboardInput)

        self.keyboardInput = ""
        self.keyboardUI.lbInput.setText("")

        self.show_widget(self.keyboardTargetWidget)

    def add_to_input(self, value):
        self.keyboardInput += value
        self.keyboardUI.lbInput.setText(self.keyboardInput)

    def remove_from_input(self):
        self.keyboardInput = self.keyboardInput[:-1]
        self.keyboardUI.lbInput.setText(self.keyboardInput)

    def close_keyboard(self):
        self.keyboardInput = ""
        self.keyboardUI.lbInput.setText("")

        if self.keyboardTargetWidget:
            self.show_widget(self.keyboardTargetWidget)


    def start_clock(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

    def update_clock(self):
        current_time = QTime.currentTime().toString("HH:mm:ss")

        current_date_raw = QDate.currentDate()
        current_day_raw = QDate.dayOfWeek(current_date_raw)
        
        current_day = ""

        match current_day_raw:
            case 1:
                current_day = "Poniedziałek"
            case 2:
                current_day = "Wtorek"
            case 3:
                current_day = "Środa"
            case 4:
                current_day = "Czwartek"
            case 5:
                current_day = "Piątek"
            case 6:
                current_day = "Sobota"
            case 7:
                current_day = "Niedziela"


        current_date = current_date_raw.toString("dd-MM-yyyy")

        self.homeUI.lbTime.setText(current_time)
        self.wKursieUI.lbTime.setText(current_time)
        self.homeUI.lbDay.setText(current_day)
        self.homeUI.lbDate.setText(current_date)

    def send_data_to_board(self, tresc):
        img = Image.open(f"DB/tresci/{tresc}").convert("L")
        width, height = img.size
        
        if width == 224 and height == 32:
            img = img.resize((112, 16), resample=0)  # NEAREST
        
        pixels = [x < 128 for x in np.array(img).flatten().tolist()]
        host = "http://192.168.0.89:5001"
        response = requests.post(
            f"{host}/update_grid",
            json={"pixels": pixels},
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()

    def _connect_touchbeep_all_buttons(self):
        from PySide6.QtWidgets import QAbstractButton

        long = {self.kursUI.btKursowkaAccept, self.kursUI.btLiniaWariantAccept}

        warn = {self.wKursieUI.btWymelduj}

        for widget in self.findChildren(QAbstractButton):
            if widget in long:
                widget.clicked.connect(self.play_longbeep)
            elif widget in warn:
                widget.clicked.connect(self.play_warnbeep)
            else:
                widget.clicked.connect(self.play_touchbeep)

    def play_touchbeep(self):
        self.touchbeep.stop()
        self.touchbeep.play()
    
    def play_longbeep(self):
        self.longbeep.stop()
        self.longbeep.play()

    def play_warnbeep(self):
        self.warnbeep.stop()
        self.warnbeep.play()
        


class ScalableWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("openPIXEL")

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)

        self.view.setFrameShape(QFrame.Shape.NoFrame)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setCentralWidget(self.view)

        self.ui = MainUI()
        self.scene.addWidget(self.ui)
        self.scene.setSceneRect(0, 0, UI_GEOMETRY_X, UI_GEOMETRY_Y)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.view.fitInView(
            self.scene.sceneRect(),
            Qt.AspectRatioMode.KeepAspectRatio
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScalableWindow()
    # window.resize(START_UI_GEOMETRY_X, START_UI_GEOMETRY_Y)
    window.show()
    window.view.fitInView(window.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)
    sys.exit(app.exec())