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
        nombre = str(self.ui.lineNombreL.text())
        direccion = str(self.ui.linedireccion.text())
        ciudad = str(self.ui..currentText())
        peso = self.ui.peso_auto.text()
        if(self.change_image):
            autos = controller.getAutos()
            autosIds = [0]
            for i in autos:
                actual = int(i['id_auto'])
                autosIds.append(actual)
        else:
            if(self.id==0):
                imagen = "0"
                else:
                    imagen = str(self.id)+".jpg"
                    fecha_creacion = str(self.ui.cb_creacion_auto.currentIndex()+1919)
                    fk_id_marca = self.ui.marca_auto.currentIndex()
                    fk_id_tipo = 0
                    datos = controller.getTipos()
                    tiposBD = ["----"]
                    for i in datos:
                        actual = [str(i['nombre'])]
                        tiposBD.append(actual)
                    tipo = str(self.ui.tipo_auto.text())
                    for i,tipoBD in enumerate(tiposBD):
                        if (tipoBD[0] == tipo):
                            fk_id_tipo = i
                    if (fk_id_tipo == 0):
                        controller.agregarInfoTipos(tipo,int(self.ui.sb_n_puertas.value()))
                    datos = controller.getTipos()
                    tiposBD = ["----"]
                    for i in datos:
                        actual = [str(i['nombre'])]
                        tiposBD.append(actual)
                    tipo = str(self.ui.tipo_auto.text())
                    for i,tipoBD in enumerate(tiposBD):
                        if (tipoBD[0] == tipo):
                            fk_id_tipo = i

                    Valida= General_Utils.validaDatos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion)
                    print Valida
                    if(Valida!="Campos Incorrectos:"):
                        self.errorMessageDialog = QtGui.QErrorMessage(self)
                        self.errorMessageDialog.setWindowTitle("ERROR")
                        self.errorMessageDialog.showMessage(Valida)
                    if(Valida=="Campos Incorrectos:"):
                        rendimiento=int(rendimiento)
                        peso=int(peso)
                        if self.identificador == False:
                            controller.agregarInfoAutos(modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_tipo, fk_id_marca)
                            self.setVisible(False)
                        else:
                            controller.editarInfoAutos(self.id, modelo, color, motor, peso, descripcion, rendimiento, imagen, fecha_creacion, fk_id_tipo, fk_id_marca)
                            self.setVisible(False)
                    self.reloadT.emit()

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    form_locales = FormularioLocales()
    form_locales.show()
    sys.exit(app.exec_())
