# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empleados.ui'
#
# Created: Sat Sep 03 17:44:41 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(564, 413)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nuevoEmpleado = QtGui.QPushButton(self.widget)
        self.nuevoEmpleado.setObjectName("nuevoEmpleado")
        self.horizontalLayout.addWidget(self.nuevoEmpleado)
        self.editarEmpleado = QtGui.QPushButton(self.widget)
        self.editarEmpleado.setObjectName("editarEmpleado")
        self.horizontalLayout.addWidget(self.editarEmpleado)
        self.eliminarEmpleado = QtGui.QPushButton(self.widget)
        self.eliminarEmpleado.setObjectName("eliminarEmpleado")
        self.horizontalLayout.addWidget(self.eliminarEmpleado)
        self.label = QtGui.QLabel(self.widget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.irLocales = QtGui.QPushButton(self.widget)
        self.irLocales.setObjectName("irLocales")
        self.horizontalLayout.addWidget(self.irLocales)
        self.verticalLayout.addWidget(self.widget)
        self.grillaEmpleados = QtGui.QTableView(Form)
        self.grillaEmpleados.setSortingEnabled(True)
        self.grillaEmpleados.setObjectName("grillaEmpleados")
        self.verticalLayout.addWidget(self.grillaEmpleados)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Empleados", None, QtGui.QApplication.UnicodeUTF8))
        self.nuevoEmpleado.setText(QtGui.QApplication.translate("Form", "Nuevo Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.editarEmpleado.setText(QtGui.QApplication.translate("Form", "Editar Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminarEmpleado.setText(QtGui.QApplication.translate("Form", "Eliminar Empleado", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Ir a:", None, QtGui.QApplication.UnicodeUTF8))
        self.irLocales.setText(QtGui.QApplication.translate("Form", "Locales", None, QtGui.QApplication.UnicodeUTF8))

