#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import db_control
import empleados_ui
import abrir_locales
from PySide import QtGui, QtCore

class Empleados(QtGui.QWidget):
    def __init__(self):
        super(Empleados, self).__init__()
        self.ui = empleados_ui.Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()
        self.load_grid()

    def connect_signals(self):
        self.ui.irLocales.clicked.connect(self.boton_locales)
        #Conexiones de los botones y widgets 


    def load_grid(self):
        #Algoritmo que muestra los datos en la grilla
        empleados = db_control.empleados()
        self.data = QtGui.QStandardItemModel(len(empleados), 6)
        self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"RUT"))
        self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Cargo"))
        self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Género"))
        self.data.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Sueldo"))
        self.data.setHorizontalHeaderItem(5, QtGui.QStandardItem(u"Local"))

        for r, row in enumerate(empleados):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['rut'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['nombre'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['cargo'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['genero'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['sueldo'])
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row['nombre_l'])

        self.ui.grillaEmpleados.setModel(self.data)
        
        #self.ui.grillaEmpleados.horizontalHeader().setResizeMode(1, self.ui.grillaEmpleados.horizontalHeader().Stretch)
        #self.ui.grillaEmpleados.horizontalHeader().setResizeMode(2, self.ui.grillaEmpleados.horizontalHeader().Stretch)
        
        self.ui.grillaEmpleados.setColumnWidth(0, 100)
        self.ui.grillaEmpleados.setColumnWidth(1, 220)
        self.ui.grillaEmpleados.setColumnWidth(2, 100)
        self.ui.grillaEmpleados.setColumnWidth(3, 150)
        self.ui.grillaEmpleados.setColumnWidth(4, 150)
        self.ui.grillaEmpleados.setColumnWidth(5, 200)

    def boton_locales(self):
        self.ventana_locales = abrir_locales.Locales()
        self.ventana_locales.show()
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    empleados = Empleados()
    empleados.show()
    sys.exit(app.exec_())
