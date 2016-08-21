#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3



con = sqlite3.connect('locales.db')
con.row_factory = sqlite3.Row

c = con.cursor()
query = "SELECT * FROM local"
resultado = c.execute(query)
locales = resultado.fetchall()
con.close()
