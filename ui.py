# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'normal.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(2120, 1218)
        Dialog.setStyleSheet("")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setEnabled(True)
        self.back.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.back.setStyleSheet("QPushButton {background-image: url(images/pikoban.png);\n"
"border: none;\n"
"}")
        self.back.setText("")
        self.back.setObjectName("back")
        self.vertigo_img = QtWidgets.QPushButton(Dialog)
        self.vertigo_img.setGeometry(QtCore.QRect(360, 90, 266, 150))
        self.vertigo_img.setStyleSheet("QPushButton {\n"
"background-image: url(images/vertigo.png);\n"
"border: none;\n"
"}")
        self.vertigo_img.setText("")
        self.vertigo_img.setObjectName("vertigo_img")
        self.inferno_img = QtWidgets.QPushButton(Dialog)
        self.inferno_img.setGeometry(QtCore.QRect(640, 90, 266, 150))
        self.inferno_img.setStyleSheet("QPushButton {background-image: url(images/inferno.png);\n"
"border: none;\n"
"}")
        self.inferno_img.setText("")
        self.inferno_img.setObjectName("inferno_img")
        self.overpass_img = QtWidgets.QPushButton(Dialog)
        self.overpass_img.setGeometry(QtCore.QRect(920, 90, 266, 150))
        self.overpass_img.setStyleSheet("QPushButton {background-image: url(images/overpass.png);\n"
"border: none;\n"
"}")
        self.overpass_img.setText("")
        self.overpass_img.setObjectName("overpass_img")
        self.cobble_img = QtWidgets.QPushButton(Dialog)
        self.cobble_img.setGeometry(QtCore.QRect(360, 360, 266, 150))
        self.cobble_img.setStyleSheet("QPushButton {background-image: url(images/cobble.png);\n"
"border: none;\n"
"}")
        self.cobble_img.setText("")
        self.cobble_img.setObjectName("cobble_img")
        self.dust_img = QtWidgets.QPushButton(Dialog)
        self.dust_img.setGeometry(QtCore.QRect(920, 360, 266, 150))
        self.dust_img.setStyleSheet("QPushButton {background-image: url(images/dust.png);\n"
"border: none;\n"
"}")
        self.dust_img.setText("")
        self.dust_img.setObjectName("dust_img")
        self.train_img = QtWidgets.QPushButton(Dialog)
        self.train_img.setGeometry(QtCore.QRect(640, 360, 266, 150))
        self.train_img.setStyleSheet("QPushButton {background-image: url(images/train.png);\n"
"border: none;\n"
"}")
        self.train_img.setText("")
        self.train_img.setObjectName("train_img")
        self.nuke_img = QtWidgets.QPushButton(Dialog)
        self.nuke_img.setGeometry(QtCore.QRect(360, 630, 266, 150))
        self.nuke_img.setStyleSheet("QPushButton {background-image: url(images/nuke.png);\n"
"border: none;\n"
"}")
        self.nuke_img.setText("")
        self.nuke_img.setObjectName("nuke_img")
        self.lake_img = QtWidgets.QPushButton(Dialog)
        self.lake_img.setGeometry(QtCore.QRect(920, 630, 266, 150))
        self.lake_img.setStyleSheet("QPushButton {background-image: url(images/lake.png);\n"
"border: none;\n"
"}")
        self.lake_img.setText("")
        self.lake_img.setObjectName("lake_img")
        self.realty_img = QtWidgets.QPushButton(Dialog)
        self.realty_img.setGeometry(QtCore.QRect(640, 630, 266, 150))
        self.realty_img.setStyleSheet("QPushButton {background-image: url(images/rialto.png);\n"
"border: none;\n"
"}")
        self.realty_img.setText("")
        self.realty_img.setObjectName("realty_img")
        self.ban_btn = QtWidgets.QPushButton(Dialog)
        self.ban_btn.setGeometry(QtCore.QRect(910, 910, 121, 81))
        self.ban_btn.setStyleSheet("")
        self.ban_btn.setObjectName("ban_btn")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(630, 910, 271, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nuke_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.nuke_btn.setObjectName("nuke_btn")
        self.gridLayout.addWidget(self.nuke_btn, 2, 0, 1, 1)
        self.cobble_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.cobble_btn.setObjectName("cobble_btn")
        self.gridLayout.addWidget(self.cobble_btn, 1, 0, 1, 1)
        self.vertigo_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.vertigo_btn.setObjectName("vertigo_btn")
        self.gridLayout.addWidget(self.vertigo_btn, 0, 0, 1, 1)
        self.inferno_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.inferno_btn.setObjectName("inferno_btn")
        self.gridLayout.addWidget(self.inferno_btn, 0, 1, 1, 1)
        self.overpass_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.overpass_btn.setObjectName("overpass_btn")
        self.gridLayout.addWidget(self.overpass_btn, 0, 2, 1, 1)
        self.train_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.train_btn.setObjectName("train_btn")
        self.gridLayout.addWidget(self.train_btn, 1, 1, 1, 1)
        self.dust_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.dust_btn.setObjectName("dust_btn")
        self.gridLayout.addWidget(self.dust_btn, 1, 2, 1, 1)
        self.rialto_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.rialto_btn.setObjectName("rialto_btn")
        self.gridLayout.addWidget(self.rialto_btn, 2, 1, 1, 1)
        self.lake_btn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.lake_btn.setObjectName("lake_btn")
        self.gridLayout.addWidget(self.lake_btn, 2, 2, 1, 1)
        self.pick_btn = QtWidgets.QPushButton(Dialog)
        self.pick_btn.setGeometry(QtCore.QRect(520, 910, 101, 81))
        self.pick_btn.setStyleSheet("")
        self.pick_btn.setObjectName("pick_btn")
        self.reset_btn = QtWidgets.QPushButton(Dialog)
        self.reset_btn.setGeometry(QtCore.QRect(1350, 910, 241, 71))
        self.reset_btn.setObjectName("reset_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.ban_btn.setText(_translate("Dialog", "BAN"))
        self.nuke_btn.setText(_translate("Dialog", "nuke"))
        self.cobble_btn.setText(_translate("Dialog", "cobble"))
        self.vertigo_btn.setText(_translate("Dialog", "vertigo"))
        self.inferno_btn.setText(_translate("Dialog", "inferno"))
        self.overpass_btn.setText(_translate("Dialog", "overpass"))
        self.train_btn.setText(_translate("Dialog", "train"))
        self.dust_btn.setText(_translate("Dialog", "dust"))
        self.rialto_btn.setText(_translate("Dialog", "rialto"))
        self.lake_btn.setText(_translate("Dialog", "lake"))
        self.pick_btn.setText(_translate("Dialog", "PICK"))
        self.reset_btn.setText(_translate("Dialog", "RESET ALL"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())