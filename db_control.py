#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
#Para conectar a la base de datos
	con = sqlite3.connect('locales.db')
    con.row_factory = sqlite3.Row #Propiedad row para defnir que tipo de objeto representa cada fila en los resultados del query, en este caso como Row de sqlite3
    return con


def locales():
#Mostrar en la grilla todos los locales de la bd
    con = conectar()
    c = con.cursor() #Definimos el cursor de la conexion
    query = "SELECT * FROM local" #Definimos la query
    resultado = c.execute(query) #La ejecutamos
    locales = resultado.fetchall() #Guardamos todos los resultados en "locales"
    con.close() #Cerrar la conexion
    return locales

def locales_por_ciudad(n_ciudad):
#Mostrar en la grilla los locales cuya ciudad coincida con la indicada en el argumento
    con = conectar()
    c = con.cursor()
    query = "SELECT nombre_l,ciudad.nombre_c FROM local JOIN ciudad on local.fk_id_ciudad = ciudad.id_ciudad WHERE ciudad.nombre_c LIKE ?"
    resultado = c.execute(query, n_ciudad) #Ejecutamos la query
    locales_ciudad = resultado.fetchall() #Guardamos todos los resultados
    con.close() #Cerramos la conexion
    return locales_ciudad
