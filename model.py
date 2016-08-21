#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
	con = sqlite3.connect('locales.db')
    con.row_factory = sqlite3.Row
    return con


def locales():
	
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM local"
    resultado = c.execute(query)
    locales = resultado.fetchall()
    con.close()
    return locales

def alumno(rut):
    con = conectar()
    c = con.cursor()
    query = "SELECT * FROM alumnos WHERE rut = ?"
    resultado = c.execute(query, [rut])
    alumno = resultado.fetchone()
    con.close()
    return alumno
