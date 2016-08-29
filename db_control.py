#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def conectar():
#Para conectar a la base de datos
	con = sqlite3.connect('locales')
	con.row_factory = sqlite3.Row #Propiedad row para defnir que tipo de objeto representa cada fila en los resultados del query, en este caso como Row de sqlite3
	return con


def locales():
#Mostrar en la grilla todos los locales de la bd
    con = conectar()
    c = con.cursor() #Definimos el cursor de la conexion
    query = "SELECT nombre_l AS Local ,ciudad.nombre_c AS Ciudad ,local.direccion, COUNT(nombre) AS Total_empleados FROM local,ciudad LEFT join  empleado on local.fk_id_ciudad = ciudad.id_ciudad and empleado.fk_id_local = local.id_local GROUP BY nombre_l;" #Definimos la query
    resultado = c.execute(query) #La ejecutamos
    locales = resultado.fetchall() #Guardamos todos los resultados en "locales"
    con.close() #Cerrar la conexion
    return locales

def locales_por_ciudad(n_ciudad):
#Mostrar en la grilla los locales cuya ciudad coincida con la indicada en el argumento
	con = conectar()
	c = con.cursor()
	n_ciudad = "%"+n_ciudad+"%"
	query = "SELECT nombre_l AS Local ,ciudad.nombre_c AS Ciudad ,local.direccion, COUNT(nombre) AS Total_empleados FROM local ,empleado join ciudad  on local.fk_id_ciudad = ciudad.id_ciudad and  empleado.fk_id_local = local.id_local WHERE ciudad.nombre_c LIKE ? GROUP BY nombre_l"
	resultado = c.execute(query, [n_ciudad]) #Ejecutamos la query
	locales_ciudad = resultado.fetchall() #Guardamos todos los resultados
	con.close() #Cerramos la conexion
	return locales_ciudad
