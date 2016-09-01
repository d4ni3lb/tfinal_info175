# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_local.ui'
#
# Created: Thu Sep 01 10:22:14 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(306, 186)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.label_3 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 2)
        self.label_2 = QtGui.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Locales", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese nombre del local", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Ciudad:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_3.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese ciudad del local", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2.setPlaceholderText(QtGui.QApplication.translate("Form", "Ingrese dirección del local", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Direccion:", None, QtGui.QApplication.UnicodeUTF8))

