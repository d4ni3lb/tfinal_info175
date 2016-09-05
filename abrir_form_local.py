#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import db_control
import validador
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
        nombre = unicode(self.ui.line_nombre_local.text())
        direccion = unicode(self.ui.line_direccion.text())
        ciudad = unicode(self.ui.box_ciudad.currentText())
        fk_id_ciudad = self.ui.box_ciudad.currentIndex()
        fk_id_region = self.ui.box_region.currentIndex()

        if(fk_id_ciudad == 0):
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR")
            self.errorMessageDialog.showMessage("Debe elegir ciudad")

        if(fk_id_region == 0):
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR")
            self.errorMessageDialog.showMessage(u"Debe elegir región")

        valido= validador.valida_datos(nombre, direccion)
        print valido
        if(valido!="Campos Incorrectos:"):
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR")
            self.errorMessageDialog.showMessage(valido)
        if(valido=="Campos Incorrectos:"):
            if self.identificador == False:
                db_control.agregar_local(nombre,direccion,fk_id_ciudad)
                self.setVisible(False)
            else:
                db_control.editar_local(nombre,direccion,fk_id_ciudad)
                self.setVisible(False)
        self.reloadT.emit()
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form_locales = FormularioLocales()
    form_locales.show()
    sys.exit(app.exec_())
