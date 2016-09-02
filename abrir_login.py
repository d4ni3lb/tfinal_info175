#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import login_ui
from PySide import QtGui, QtCore

class Main(QtGui.QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = login_ui.Ui_Form()
        self.ui.setupUi(self)
        self.connect_actions()


    def connect_actions(self):
        self.ui.pushButton.clicked.connect(self.action_aceptar)
        self.ui.pushButton_2.clicked.connect(self.action_cancelar)

    def action_cancelar(self):
        exit()

    def action_aceptar(self):
        print("Aceptaste")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())