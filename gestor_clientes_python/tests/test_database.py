"""PRUEBAS EN LA BBDD"""
"""ES UN FILE POR CADA CLASE PRUEBA"""

"""
como ejecutar el test en terminal:  pytest -v

"""


import unittest
import database as db
import copy
import helpers
import config 
import csv 



class TestDatabase(unittest.TestCase):


    def setUp(self):
        db.Clientes.lista=[

            db.Cliente('1A', 'Gustavo', 'Gigante'),
            db.Cliente('2B', 'Juliana', 'Gigante'),
            db.Cliente('3C', 'Ornella', 'Gigante'),


          ]
        


    def test_buscar_cliente(self):

        cliente_existente= db.Clientes.buscar('1A')
        cliente_existente= db.Clientes.buscar('2B')
        cliente_inexistente= db.Clientes.buscar('x22')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)



    def test_crear_cliente(self):
        nuevo_cliente= db.Clientes.crear('4D', 'Lorena', 'Gonzalez')
        self.assertEqual(len(db.Clientes.lista),4)
        self.assertEqual(nuevo_cliente.dni,'4D') 
        self.assertEqual(nuevo_cliente.nombre,'Lorena') 
        self.assertEqual(nuevo_cliente.apellidos,'Gonzalez') 


    def test_modificar_cliente(self):
        cliente_a_modificar= copy.copy(db.Clientes.buscar('3C'))
        cliente_modificado= db.Clientes.modificar('3C','Ornella','Gonzalez')
        self.assertEqual(cliente_a_modificar.apellidos,'Gigante')
        self.assertEqual(cliente_modificado.apellidos, 'Gonzalez')


    def test_borrar_cliente(self): 
        cliente_borrado= db.Clientes.borrar('3C')
        cliente_rebuscado= db.Clientes.buscar('3C')
        self.assertEqual(cliente_borrado.dni,'3C')
        self.assertIsNone(cliente_rebuscado)


    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido('03C', db.Clientes.lista))  # DNI válido
        self.assertFalse(helpers.dni_valido('232324242332', db.Clientes.lista)) #DNI con formato erroneo
        self.assertFalse(helpers.dni_valido('1A',db.Clientes.lista)) #DNI ya existente 


    def test_escritura_csv(self):
        db.Clientes.borrar('1A')
        db.Clientes.modificar('2B','Fiorella','DiMarco')
        
        dni, nombre, apellidos= None, None, None 
        with open(config.DATABASE_PATH, newline='\n') as fichero: 
            reader= csv.reader(fichero, delimiter= ';')
            dni, nombre, apellidos = next(reader)

        self.assertEqual(dni, '2B')
        self.assertEqual(nombre,'Fiorella')
        self.assertEqual(apellidos,'DiMarco')
      

