from PyQt5 import QtWidgets, uic
import sys
from ui import Ui_Dialog

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from ui import Ui_Dialog


# create app
app = QtWidgets.QApplication(sys.argv)

# create dialog
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.setWindowTitle("Map Picker")
Dialog.setWindowIcon(QtGui.QIcon("logo.png"))
Dialog.show()


# hook logic
def reset():
    ui.vertigo_img.setStyleSheet("QPushButton {background-image: url(images/vertigo.png);"
                                 "border: none;}")

    ui.inferno_img.setStyleSheet("QPushButton {background-image: url(images/inferno.png);"
                                 "border: none;}")

    ui.overpass_img.setStyleSheet("QPushButton {background-image: url(images/overpass.png);"
                                  "border: none;}")
    ui.cobble_img.setStyleSheet("QPushButton {background-image: url(images/cobble.png);"
                                "border: none;}")
    ui.train_img.setStyleSheet("QPushButton {background-image: url(images/train.png);"
                               "border: none;}")
    ui.dust_img.setStyleSheet("QPushButton {background-image: url(images/dust.png);"
                              "border: none;}")
    ui.nuke_img.setStyleSheet("QPushButton {background-image: url(images/nuke.png);"
                              "border: none;}")
    ui.realty_img.setStyleSheet("QPushButton {background-image: url(images/rialto.png);"
                                "border: none;}")
    ui.lake_img.setStyleSheet("QPushButton {background-image: url(images/lake.png);"
                              "border: none;}")


def ban_map():
    if ui.vertigo_btn.isChecked():
        ui.vertigo_img.setStyleSheet("QPushButton {background-image: url(images/vertigo_ban.png);"
                                     "border: none;}")
    elif ui.inferno_btn.isChecked():
        ui.inferno_img.setStyleSheet("QPushButton {background-image: url(images/inferno_ban.png);"
                                     "border: none;}")
    elif ui.overpass_btn.isChecked():
        ui.overpass_img.setStyleSheet("QPushButton {background-image: url(images/overpass_ban.png);"
                                      "border: none;}")
    elif ui.cobble_btn.isChecked():
        ui.cobble_img.setStyleSheet("QPushButton {background-image: url(images/cobble_ban.png);"
                                    "border: none;}")
    elif ui.train_btn.isChecked():
        ui.train_img.setStyleSheet("QPushButton {background-image: url(images/train_ban.png);"
                                   "border: none;}")
    elif ui.dust_btn.isChecked():
        ui.dust_img.setStyleSheet("QPushButton {background-image: url(images/dust_ban.png);"
                                  "border: none;}")
    elif ui.nuke_btn.isChecked():
        ui.nuke_img.setStyleSheet("QPushButton {background-image: url(images/nuke_ban.png);"
                                  "border: none;}")
    elif ui.rialto_btn.isChecked():
        ui.realty_img.setStyleSheet("QPushButton {background-image: url(images/rialto_ban.png);"
                                    "border: none;}")
    elif ui.lake_btn.isChecked():
        ui.lake_img.setStyleSheet("QPushButton {background-image: url(images/lake_ban.png);"
                                  "border: none;}")


def pick_map():
    if ui.vertigo_btn.isChecked():
        ui.vertigo_img.setStyleSheet("QPushButton {background-image: url(images/vertigo_pick.png);"
                                     "border: none;}")
    elif ui.inferno_btn.isChecked():
        ui.inferno_img.setStyleSheet("QPushButton {background-image: url(images/inferno_pick.png);"
                                     "border: none;}")
    elif ui.overpass_btn.isChecked():
        ui.overpass_img.setStyleSheet("QPushButton {background-image: url(images/overpass_pick.png);"
                                      "border: none;}")
    elif ui.cobble_btn.isChecked():
        ui.cobble_img.setStyleSheet("QPushButton {background-image: url(images/cobble_pick.png);"
                                    "border: none;}")
    elif ui.train_btn.isChecked():
        ui.train_img.setStyleSheet("QPushButton {background-image: url(images/train_pick.png);"
                                   "border: none;}")
    elif ui.dust_btn.isChecked():
        ui.dust_img.setStyleSheet("QPushButton {background-image: url(images/dust_pick.png);"
                                  "border: none;}")
    elif ui.nuke_btn.isChecked():
        ui.nuke_img.setStyleSheet("QPushButton {background-image: url(images/nuke_pick.png);"
                                  "border: none;}")
    elif ui.rialto_btn.isChecked():
        ui.realty_img.setStyleSheet("QPushButton {background-image: url(images/rialto_pick.png);"
                                    "border: none;}")
    elif ui.lake_btn.isChecked():
        ui.lake_img.setStyleSheet("QPushButton {background-image: url(images/lake_pick.png);"
                                  "border: none;}")


ui.ban_btn.clicked.connect(ban_map)
ui.pick_btn.clicked.connect(pick_map)
ui.reset_btn.clicked.connect(reset)

# run main loop
sys.exit(app.exec_())
