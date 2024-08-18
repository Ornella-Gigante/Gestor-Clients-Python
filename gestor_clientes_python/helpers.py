"""CONTENDRÁ FUNCIONES AUXILIARES DE USO GENERAL, COMUNES, EN TODO EL PROYECTO"""

"""

La función limpiar_pantalla() limpia la pantalla de la terminal o consola,
independientemente del sistema operativo en el que se esté ejecutando el script de Python.
La función utiliza el comando adecuado según el sistema operativo detectado.

"""

import os 
import re 
import platform

def limpiar_pantalla():
    os.system('cls') if platform.system()== "Windows" else os.system('clear')



"""
Función para leer texto por teclado 

"""

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None 

    while True:
        texto = input(">")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        


"""
fUNCIÓN PARA VERIFICAR QUE EL dni INGRESADO SEA VÁLIDO 

"""


def dni_valido(dni, lista):
    if not re.match('[0-9]{2}[A-Z]', dni):
        print("DNI incorrecto, debe cumplir el formato especificado.")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI utilizado ya por otro cliente")
            return False
    return True