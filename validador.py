#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
import string
import os


def valida_datos(nombre, direccion):
    '''Valida cada uno de los datos que se ingresan y devuelve una cadena string con los errores que tiene cada campo'''
    valida_nombre = valida_text(nombre, 'no_simbolos')
    valida_direccion = valida_text(direccion, 'no_simbolos')
    error="Campos Incorrectos:"
    if(valida_nombre==False):
        nom="*Nombre"
        error=error+nom
    if(valida_direccion==False):
        direccion="*Direccion"
        error=error+"  "+direccion
    return error
        

                

def valida_text(text,validacion):
    '''Función que evalua y valida el string 'text' dependiendo el valor del segundo parámetro:
    numeros: retorna 'True' si el string 'text' posee sólo numeros
    no_simbolos: retorna 'True' si el string 'text' posee sólo letras (mayusculas o minusculas o acentos) y/o números
    Retorna 'False' en caso contrario o si el string 'text' esta vacío'''

    Valido=True

    if (validacion=="numeros"):
        Cadena = "0123456789"

    if (validacion=="no_simbolos"):
        Cadena = " ,.-abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ0123456789"

    if (validacion=="texto"):
        Cadena = " abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ"

    i=0
    StringNum=str(text)
    
    if(len(StringNum)==0):
        Valido=False
    while(Valido and (i<len(StringNum))):
        if (not StringNum[i] in Cadena):
            Valido=False
        i=i+1
    return Valido
