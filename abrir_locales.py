#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import db_control
import locales_ui
import abrir_empleados
import abrir_form_local
from PySide import QtGui, QtCore

class Locales(QtGui.QWidget):
    def __init__(self):
        super(Locales, self).__init__()
        self.ui = locales_ui.Ui_Form()
        self.ui.setupUi(self)
        self.connect_signals()
        self.load_grid()


    def connect_signals(self):
        self.ui.buscador.textChanged.connect(self.onChanged)
        self.ui.irEmpleados.clicked.connect(self.boton_empleados)
        self.ui.botonNuevoL.clicked.connect(self.boton_nLocal)
        self.ui.botonEditar.clicked.connect(self.boton_editarLocal)

    def load_grid(self):
        locales = db_control.locales()
        self.data = QtGui.QStandardItemModel(len(locales), 4)
        self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Local"))
        self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Ciudad"))
        self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Dirección"))
        self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Total_empleados"))
        
        for r, row in enumerate(locales):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['Local'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['Ciudad'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['Direccion'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['Total_empleados'])
            
        self.ui.tableView.setModel(self.data)
        
        self.ui.tableView.horizontalHeader().setResizeMode(1, self.ui.tableView.horizontalHeader().Stretch)
        self.ui.tableView.horizontalHeader().setResizeMode(2, self.ui.tableView.horizontalHeader().Stretch)
        
        self.ui.tableView.setColumnWidth(0, 220)
        self.ui.tableView.setColumnWidth(1, 210)
        self.ui.tableView.setColumnWidth(2, 210)
        self.ui.tableView.setColumnWidth(3, 100)
        
    def load_filtered_grid1(self,text):
        if(text!=""):
            locales = db_control.locales_por_ciudad(text)
            
            self.data = QtGui.QStandardItemModel(len(locales), 4)
            self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Local"))
            self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Ciudad"))
            self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Dirección"))
            self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Total_empleados"))
            
            for r, row in enumerate(locales):
                index = self.data.index(r, 0, QtCore.QModelIndex())
                self.data.setData(index, row['Local'])
                index = self.data.index(r, 1, QtCore.QModelIndex())
                self.data.setData(index, row['Ciudad'])
                index = self.data.index(r, 2, QtCore.QModelIndex())
                self.data.setData(index, row['Direccion'])
                index = self.data.index(r, 3, QtCore.QModelIndex())
                self.data.setData(index, row['Total_empleados'])
                
            self.ui.tableView.setModel(self.data)
            
            self.ui.tableView.horizontalHeader().setResizeMode(1, self.ui.tableView.horizontalHeader().Stretch)
            self.ui.tableView.horizontalHeader().setResizeMode(2, self.ui.tableView.horizontalHeader().Stretch)
            
            self.ui.tableView.setColumnWidth(0, 220)
            self.ui.tableView.setColumnWidth(1, 210)
            self.ui.tableView.setColumnWidth(2, 210)
            self.ui.tableView.setColumnWidth(3, 100)
            
        else:
            self.load_grid()
            
    def onChanged(self,text):
        self.load_filtered_grid1(text)

    def boton_empleados(self):
            self.ventana_empleados = abrir_empleados.Empleados()
            self.ventana_empleados.show()
            self.close()

    def boton_nLocal(self):
        '''Metodo para lanzar el formulario de creacion del nuevo local'''
        self.ventana_formularioL = abrir_form_local.FormularioLocales()
        self.ventana_formularioL.reloadT.connect(self.load_grid)
        self.ventana_formularioL.exec_()

    def boton_editarLocal(self):
        '''Método usado para editar un local seleccionado desde la grilla'''
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: #No se ha seleccionado producto
            msgBox = QtGui.QMessageBox()
            msgBox.setWindowTitle("Error")
            msgBox.setText("Debe seleccionar un local.")
            msgBox.exec_()
            return False
        else:
            model = self.ui.tableView.model()
            id = model.index(index.row(), 8, QtCore.QModelIndex()).data()
            self.ventana_editarL = abrir_form_local.FormularioLocales(id)
            self.ventana_editarL.reloadT.connect(self.load_grid)
            self.ventana_editarL.exec_()
		

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	locales = Locales()
	locales.show()
	sys.exit(app.exec_())
