# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_local_b.ui'
#
# Created: Mon Sep 05 22:33:54 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 293)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.line_nombre_local = QtGui.QLineEdit(self.widget)
        self.line_nombre_local.setAlignment(QtCore.Qt.AlignCenter)
        self.line_nombre_local.setObjectName("line_nombre_local")
        self.gridLayout.addWidget(self.line_nombre_local, 0, 2, 1, 1)
        self.line_direccion = QtGui.QLineEdit(self.widget)
        self.line_direccion.setAlignment(QtCore.Qt.AlignCenter)
        self.line_direccion.setObjectName("line_direccion")
        self.gridLayout.addWidget(self.line_direccion, 2, 2, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Formulario local", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Dirección:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_nombre_local.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Ingrese nombre del local", None, QtGui.QApplication.UnicodeUTF8))
        self.line_direccion.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Ingrese dirección del local", None, QtGui.QApplication.UnicodeUTF8))

