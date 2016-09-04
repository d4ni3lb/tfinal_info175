# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_local.ui'
#
# Created: Sun Sep 04 13:23:21 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
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
        self.lineCiudad = QtGui.QLineEdit(self.widget)
        self.lineCiudad.setObjectName("lineCiudad")
        self.gridLayout.addWidget(self.lineCiudad, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineDireccion = QtGui.QLineEdit(self.widget)
        self.lineDireccion.setObjectName("lineDireccion")
        self.gridLayout.addWidget(self.lineDireccion, 2, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineNombreL = QtGui.QLineEdit(self.widget)
        self.lineNombreL.setInputMask("")
        self.lineNombreL.setText("")
        self.lineNombreL.setObjectName("lineNombreL")
        self.gridLayout.addWidget(self.lineNombreL, 0, 2, 1, 1)
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
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineCiudad.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Ingrese ciudad del local", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Direccion:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineDireccion.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Ingrese dirección del local", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Ciudad:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineNombreL.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Ingrese nombre del local", None, QtGui.QApplication.UnicodeUTF8))

