#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import db_control
import empleados_ui
from PySide import QtGui, QtCore

class Empleados(QtGui.QWidget):
    def __init__(self):
        super(Empleados, self).__init__()
        self.ui = empleados_ui.Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()
        self.load_grid()

    def connect_signals(self):
        print("conexion botones")
        #Conexiones de los botones y widgets


    def load_grid(self):
        empleados = db_control.empleados()
        #Algoritmo que muestra los datos en la grilla



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    empleados = Empleados()
    empleados.show()
    sys.exit(app.exec_())
