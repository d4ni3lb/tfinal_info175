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
    query = "SELECT id_local, nombre_l AS Local ,ciudad.nombre_c AS Ciudad ,local.direccion, COUNT(nombre) AS Total_empleados FROM local inner join ciudad ON  local.fk_id_ciudad = ciudad.id_ciudad left join empleado ON  empleado.fk_id_local = local.id_local GROUP BY nombre_l;" #Definimos la query
    resultado = c.execute(query) #La ejecutamos
    locales = resultado.fetchall() #Guardamos todos los resultados en "locales"
    con.close() #Cerrar la conexion
    return locales

def obtenerLocalId(id):
        #Metodo para obtener un local especifico a traves de su ID'''
    con = conectar()
    c=con.cursor()
    query = "SELECT * FROM local WHERE id_local = ?"
    resultado = c.execute(query, [id])
    local = resultado.fetchall()
    con.close()
    return local

def locales_por_ciudad(n_ciudad):
#Mostrar en la grilla los locales cuya ciudad coincida con la indicada en el argumento
    con = conectar()
    c = con.cursor()
    n_ciudad = "%"+n_ciudad+"%"
    query = "SELECT id_local, nombre_l AS Local ,ciudad.nombre_c AS Ciudad ,local.direccion, COUNT(nombre) AS Total_empleados FROM local inner join ciudad ON local.fk_id_ciudad = ciudad.id_ciudad left join empleado ON empleado.fk_id_local = local.id_local WHERE ciudad.nombre_c LIKE ? GROUP BY nombre_l;"
    resultado = c.execute(query, [n_ciudad]) #Ejecutamos la query
    locales_ciudad = resultado.fetchall() #Guardamos todos los resultados
    con.close() #Cerramos la conexion
    return locales_ciudad

def obtener_usuarios():
#Devuelve la lista de usuarios y sus respectivas contraseñas para el login
    c = conectar()
    query = "SELECT * FROM usuarios"
    resultado = c.execute(query)
    usuarios = resultado.fetchall()
    return usuarios

def empleados():
#Mostrar en la grilla todos los locales de la bd
    con = conectar()
    c = con.cursor() #Definimos el cursor de la conexion
    query = "SELECT empleado.rut, empleado.nombre, empleado.cargo, empleado.genero, empleado.sueldo, local.nombre_l FROM empleado JOIN local ON empleado.fk_id_local = local.id_local" #Definimos la query
    resultado = c.execute(query) #La ejecutamos
    empleados = resultado.fetchall() #Guardamos todos los resultados en "locales"
    con.close() #Cerrar la conexion
    return empleados

def borrar_local(id_local):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM local WHERE id_local = ?"
    try:
        resultado = c.execute(query, [id_local])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def borrar_empleado(rut):
    exito = False
    con = conectar()
    c = con.cursor()
    query = "DELETE FROM empleado WHERE rut = ?"
    try:
        resultado = c.execute(query, [rut])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito

def agregar_local(nombre, direccion, fk_id_ciudad):
    """
    Método que permite agregar un local a la base de datos
    """
    con = conectar()
    c = con.cursor()
    c.execute("INSERT INTO local (nombre_l, direccion, fk_id_ciudad) VALUES(?, ?, ? )", (nombre, direccion, fk_id_ciudad))
    con.commit()

def editar_local(id, nombre, direccion, fk_id_local):
    """
    Método que permite editar un local en la base de datos
    """
    con = conectar()
    c=con.cursor()
    query = "UPDATE locale SET nombre = ?,direccion = ?, fk_id_local = ? WHERE id_local = ?"
    c.execute(query, [nombre,direccion,fk_id_local,id])
    con.commit()
