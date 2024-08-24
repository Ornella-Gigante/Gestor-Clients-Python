"""FICHERO QUE CONTROLARÁ LOS DATOS Y HARÁ UNA INTERFAZ PARA CREAR Y BORRAR DATOS"""

import csv 
import config

class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni= dni
        self.nombre=nombre
        self.apellidos=apellidos 

    def __str__(self):
        return f"({self.dni} {(self.nombre)} ({self.apellidos})"
    
    def to_dict(self):
        return {'dni': self.dni, 'nombre': self.nombre, 'apellidos':self.apellidos}
    


class Clientes: 

    lista=[]

    """usamos WITH para poder abrir el fichero csv"""

    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader= csv.reader(fichero, delimiter=';')
        for dni, nombre, apellidos in reader:
            cliente= Cliente(dni, nombre, apellidos)
            lista.append(cliente)

    """Creación de métodos estáticos de la clase Clientes para CRUD de la BBDD"""

    @staticmethod
    def buscar(dni):
        for cliente in Clientes.lista:
            if cliente.dni== dni:
                return cliente 
            


    @staticmethod
    def crear(dni, nombre, apellidos):
        cliente= Cliente(dni, nombre, apellidos)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente 
    

    @staticmethod
    def modificar(dni, nombre, apellidos):
        for indice,cliente in enumerate(Clientes.lista):
            if cliente.dni==dni:
                Clientes.lista[indice].nombre= nombre
                Clientes.lista[indice].apellidos= apellidos 
                Clientes.guardar()
                return Clientes.lista[indice]
            

    @staticmethod
    def borrar(dni):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni:
                cliente= Clientes.lista.pop(indice)
                Clientes.guardar()
                return cliente
            


    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero: 
            writer= csv.writer(fichero, delimiter=';')
            for cliente in Clientes.lista:
                writer.writerow((cliente.dni, cliente.nombre, cliente.apellidos))


