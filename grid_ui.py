# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid.ui'
#
# Created: Thu Sep 01 10:34:28 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(767, 539)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signals = QtGui.QWidget(Form)
        self.signals.setObjectName("signals")
        self.horizontalLayout = QtGui.QHBoxLayout(self.signals)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.signals)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb_filtro = QtGui.QComboBox(self.signals)
        self.cb_filtro.setObjectName("cb_filtro")
        self.horizontalLayout.addWidget(self.cb_filtro)
        self.buscador = QtGui.QLineEdit(self.signals)
        self.buscador.setObjectName("buscador")
        self.horizontalLayout.addWidget(self.buscador)
        self.botonEliminar = QtGui.QPushButton(self.signals)
        self.botonEliminar.setObjectName("botonEliminar")
        self.horizontalLayout.addWidget(self.botonEliminar)
        self.botonNuevoL = QtGui.QPushButton(self.signals)
        self.botonNuevoL.setObjectName("botonNuevoL")
        self.horizontalLayout.addWidget(self.botonNuevoL)
        self.botonEditar = QtGui.QPushButton(self.signals)
        self.botonEditar.setObjectName("botonEditar")
        self.horizontalLayout.addWidget(self.botonEditar)
        self.label_2 = QtGui.QLabel(self.signals)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.irEmpleados = QtGui.QPushButton(self.signals)
        self.irEmpleados.setObjectName("irEmpleados")
        self.horizontalLayout.addWidget(self.irEmpleados)
        self.verticalLayout.addWidget(self.signals)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        
        filtros = [
            {"id": "0", "name": "----"},
            {"id": "1", "name": "Ciudad"},
            {"id": "2", "name": u"Región"}]

        for element in filtros:
            self.cb_filtro.addItem(element["name"],element["id"])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Locales", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Filtro:", None, QtGui.QApplication.UnicodeUTF8))
        self.botonEliminar.setText(QtGui.QApplication.translate("Form", "Eliminar", None, QtGui.QApplication.UnicodeUTF8))
        self.botonNuevoL.setText(QtGui.QApplication.translate("Form", "Nuevo local", None, QtGui.QApplication.UnicodeUTF8))
        self.botonEditar.setText(QtGui.QApplication.translate("Form", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Ir a:", None, QtGui.QApplication.UnicodeUTF8))
        self.irEmpleados.setText(QtGui.QApplication.translate("Form", "Empleados", None, QtGui.QApplication.UnicodeUTF8))

