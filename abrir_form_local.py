#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import db_control
import form_local_ui
from PySide import QtGui, QtCore

class FormularioLocales(QtGui.QWidget):
    def __init__(self):
        super(FormularioLocales, self).__init__()
        self.ui = form_local_ui.Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()

    def connect_signals(self):
        self.ui.pushButton.clicked.connect(self.action_aceptar)
        self.ui.pushButton_2.clicked.connect(self.action_cancelar)

    def action_cancelar(self):
        exit()

    def action_aceptar(self):
        print("aceptar")

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form_locales = FormularioLocales()
    form_locales.show()
    sys.exit(app.exec_())
