import sys
sys.path.append("src")
from controller import controlador as Controlador
import unittest

class ControllerTest(unittest.TestCase):
    """
        Pruebas a la clase Controlador de la app
    """
    def setUp(self):
        """ Se ejecuta siempre antes de cada metodo de prueba """
        print("Invocando setUp")
        Controlador.BorrarFilas() # Asegura que antes de cada metodo de prueba, se borren todos los datos de la tabla

    def setUpClass():
        """ Se ejecuta al inicio de todas las pruebas """
        print("Invocando setUpClass")
        Controlador.CrearTabla()  # Asegura que al inicio de las pruebas, la tabla este creada

    def tearDown(self):
        """ Se ejecuta al final de cada test """
        print("Invocando tearDown")

    def tearDownClass():
        """ Se ejecuta al final de todos los tests """
        print("Invocando tearDownClass")
    

    #Test insert Valido
    def testInsert(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """
        # Pedimos crear un usuario
        print("Ejecutando testInsert")

        Usuario_prueba = Controlador.Usuario("Juan", "1040491961", 1300000, 20, "2023", "2023")

        Controlador.Insertar(Usuario_prueba)

        usuario_buscado = Controlador.BuscarUsuarios(Usuario_prueba.cedula)

        self.assertEqual(str(Usuario_prueba.nombre), usuario_buscado.nombre)
        self.assertEqual(str(Usuario_prueba.cedula), usuario_buscado.cedula)
        self.assertEqual(str(Usuario_prueba.basic_salary), usuario_buscado.basic_salary)
        self.assertEqual(str(Usuario_prueba.accumulated_vacation_days), usuario_buscado.accumulated_vacation_days)
        self.assertEqual(str(Usuario_prueba.start_date), usuario_buscado.start_date)
        self.assertEqual(str(Usuario_prueba.last_vacation_date), usuario_buscado.last_vacation_date)

    #Test insert Invalido 2 Usuarios con la misma primary key
    def testInsertFail(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """
        # Pedimos crear un usuario
        print("Ejecutando testInsert")
        Usuario_prueba = Controlador.Usuario("Juan", "1040491961", 1300000, 20, "2023", "2023")
        usuario_prueba2 = Controlador.Usuario("Pedro", "1040491961", 50000000, 20, "2023", "2023")

        Controlador.Insertar(Usuario_prueba)
        with self.assertRaises(Controlador.ErrorNoInsertado):
            Controlador.Insertar(usuario_prueba2)

        

    #Test Update
    def testUpdate(self):
        """
            Verifica la funcionalidad de actualizar
        """
        print("Ejecutando testUpdate")

        usuario_prueba = Controlador.Usuario("Juan", "1040491961", 1300000, 20, "2023", "2023")

        Controlador.Insertar(usuario_prueba)

        usuario_prueba.nombre = "Juan Diego"
        usuario_prueba.basic_salary = 2000000
        usuario_prueba.accumulated_vacation_days = 0
        usuario_prueba.start_date = "2023"
        usuario_prueba.last_vacation_date = "2023"

        Controlador.Actualizar(usuario_prueba)

        usuario_actualizado = Controlador.BuscarUsuarios(usuario_prueba.cedula)

        self.assertEqual(str(usuario_prueba.nombre), usuario_actualizado.nombre)
        self.assertEqual(str(usuario_prueba.cedula), usuario_actualizado.cedula)
        self.assertEqual(str(usuario_prueba.basic_salary), usuario_actualizado.basic_salary)
        self.assertEqual(str(usuario_prueba.accumulated_vacation_days), usuario_actualizado.accumulated_vacation_days)
        self.assertEqual(str(usuario_prueba.start_date), usuario_actualizado.start_date)
        self.assertEqual(str(usuario_prueba.last_vacation_date), usuario_actualizado.last_vacation_date)

    #Test Update Error No encuentra usuario para actualizar
    def testUpdateFail(self):
        """
            Verifica la funcionalidad de actualizar
        """
        print("Ejecutando testUpdate")

        usuario_prueba = Controlador.Usuario("Juan", "1040491961", 1300000, 20, "2023", "2023")
        usuario_prueba2 = Controlador.Usuario("Juan Diego", "1040", 2000000, 0, "2023", "2023")

        Controlador.Insertar(usuario_prueba)
        with self.assertRaises(Controlador.ErrorNoActualizado):
            Controlador.Actualizar(usuario_prueba2)
            

   #Test Delete
    def testDelete(self):
        """ Prueba la funcionalidad de borrar usuarios """
        print("Ejecutando testDelete")
        # 1. Crear el usuario e insertarlo
        usuario_prueba = Controlador.Usuario("Juan", "1040491961", 1300000, 20, "2023", "2023")
        Controlador.Insertar( usuario_prueba )

        # 2. Borrarlo
        Controlador.Borrar( usuario_prueba.cedula)

        # 3. Buscar para verificar que no exista
        with self.assertRaises(Controlador.ErrorNoEncontrado):
            Controlador.BuscarUsuarios(usuario_prueba.cedula)

    def testDeleteFail(self):
        """ Prueba la funcionalidad de borrar usuarios """
        print("Ejecutando testDelete")
        # 1. Crear el usuario e insertarlo
        usuario_prueba = Controlador.Usuario("Juan", "1040491961", 1300000, 20, "2023", "2023")
        Controlador.Insertar( usuario_prueba )
        str_error = "hola mundo"

        with self.assertRaises(Controlador.ErrorNoBorrado):
            Controlador.Borrar(str_error)

if __name__ == '__main__':
    unittest.main()