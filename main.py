#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import login_ui
import db_control
import abrir_locales
from PySide import QtGui, QtCore

class Main(QtGui.QWidget):
    
    def __init__(self):
        super(Main, self).__init__()
        self.ui = login_ui.Ui_Form()
        self.isLoged = False
        self.ui.setupUi(self)
        self.connect_actions()


    def connect_actions(self):
        self.ui.pushButton.clicked.connect(self.action_aceptar)
        self.ui.pushButton_2.clicked.connect(self.action_cancelar)

    def action_cancelar(self):
        exit()

    def action_aceptar(self):
        datos = db_control.obtener_usuarios()
        for row in datos:
            if(row['username']==str(self.ui.lineEdit.text()) and row['pass']==str(self.ui.lineEdit_2.text())):
                self.isLoged=True
        if(self.isLoged):
            print("Login exitoso")
            self.setVisible(False)
            self.ventana_locales = abrir_locales.Locales()
            self.ventana_locales.show()


        else:
            self.msgBox = QtGui.QMessageBox()
            self.msgBox.setText(u"Nombre de usuario o contraseña no válidos.")
            self.msgBox.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())