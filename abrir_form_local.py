#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import db_control
import form_local_ui
from PySide import QtGui, QtCore

class FormularioLocales(QtGui.QDialog):
    reloadT = QtCore.Signal()
    identificador = False
    def __init__(self, id=None):
        super(FormularioLocales, self).__init__()
        self.ui = form_local_ui.Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.connect_signals()
        if(id == None):
            self.id=0
            self.identificador=False
            self.setWindowTitle("Nuevo Local")
            self.show()
        else:
            self.id=id
            self.identificador = True
            self.setWindowTitle("Editar Local")
            local = db_control.obtenerLocalID(id)
            for row in local:
                self.ui.lineNombreL.setText(row[u'nombre_l'])
                self.ui.lineDireccion.setText(row[u'direccion'])
                self.ui.lineCiudad.setText(row[u'ciudad'])

        self.setMaximumHeight(self.height()-1)
        self.setMaximumWidth(self.width()-1)

    def connect_signals(self):
        self.accepted.connect(self.action_aceptar)

    def action_cancelar(self):
        exit()

    def action_aceptar(self):
        print("aceptar")

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form_locales = FormularioLocales()
    form_locales.show()
    sys.exit(app.exec_())
