#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import db_control
import grid_ui
from PySide import QtGui, QtCore

class Main(QtGui.QMainWindow):
	def __init__(self):
		super(Main, self).__init__()
		self.ui = grid_ui.Ui_Form()
		self.ui.setupUi(self)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	main = Main()
	main.show()
	sys.exit(app.exec_())
