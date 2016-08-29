# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grid.ui'
#
# Created: Mon Aug 29 13:11:26 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(768, 492)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.signals = QtGui.QWidget(Form)
        self.signals.setObjectName("signals")
        self.horizontalLayout = QtGui.QHBoxLayout(self.signals)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(225, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.signals)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cb_filtro = QtGui.QComboBox(self.signals)
        self.cb_filtro.setObjectName("cb_filtro")
        self.horizontalLayout.addWidget(self.cb_filtro)
        self.buscador = QtGui.QLineEdit(self.signals)
        self.buscador.setObjectName("buscador")
        self.horizontalLayout.addWidget(self.buscador)
        self.pushButton = QtGui.QPushButton(self.signals)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.signals)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.signals)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        filtros = [
            {"id": "0", "name": "----"},
            {"id": "1", "name": "Ciudad"},
            {"id": "2", "name": "Region"}]

        for element in filtros:
            self.cb_filtro.addItem(element["name"],element["id"])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Filtro:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))

