#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import db_control
import grid_ui
from PySide import QtGui, QtCore

class Main(QtGui.QWidget):
	def __init__(self):
		super(Main, self).__init__()
		self.ui = grid_ui.Ui_Form()
		self.ui.setupUi(self)
		self.load_grid()


	def load_grid(self):
		locales = db_control.locales()

		self.data = QtGui.QStandardItemModel(len(locales), 4)
		self.data.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Local"))
		self.data.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Ciudad"))
		self.data.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Dirección"))
		self.data.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Total_empleados"))
		self.ui.tableView.setModel(self.data)

		for r, row in enumerate(locales):
			index = self.data.index(r, 0, QtCore.QModelIndex())
			self.data.setData(index, row['Local'])
			index = self.data.index(r, 1, QtCore.QModelIndex())
			self.data.setData(index, row['Ciudad'])
			index = self.data.index(r, 2, QtCore.QModelIndex())
			self.data.setData(index, row['Direccion'])
			index = self.data.index(r, 3, QtCore.QModelIndex())
			self.data.setData(index, row['Total_empleados'])

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	main.show()
	sys.exit(app.exec_())
