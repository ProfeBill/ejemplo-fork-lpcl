import sys
sys.path.append("src")
from controller.controlador import *
from Logica.calculadora import Usuario
from controller.controlador import CrearTabla, Insertar, Actualizar, Borrar, BuscarUsuarios
def interfaz():
    print("=== Sistema de Gestión de Usuarios ===")
    while True:
        print("\nOpciones:")
        print("1. Crear Tabla")
        print("2. Insertar Usuario")
        print("3. Actualizar Usuario")
        print("4. Borrar Usuario")
        print("5. Buscar Usuario")
        print("6. Salir")

def menu():
    while True:
        print("\n--- Menú de Usuario ---")
        print("1. Crear tabla")
        print("2. Borrar todas las filas")
        print("3. Insertar usuario")
        print("4. Actualizar usuario")
        print("5. Borrar usuario")
        print("6. Buscar usuario")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            CrearTabla()
        elif opcion == '2':
            BorrarFilas()
        elif opcion == '3':
            cedula = input("Ingrese cédula: ")
            nombre = input("Ingrese nombre: ")
            basic_salary = float(input("Ingrese salario básico: "))
            start_work_date = input("Ingrese fecha de inicio: ")
            last_vacation_date = input("Ingrese fecha de última vacaciones: ")
            accumulated_vacation_days = int(input("Ingrese días de vacaciones acumulados: "))
            usuario = Usuario(nombre, cedula, basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days)
            Insertar(usuario)
        elif opcion == '4':
            cedula = input("Ingrese la cédula del usuario a actualizar: ")
            usuario = BuscarUsuarios(cedula)
            if usuario:
                nombre = input("Ingrese nuevo nombre (deje vacío para no cambiar): ")
                if nombre:
                    usuario.nombre = nombre
                basic_salary = input("Ingrese nuevo salario básico (deje vacío para no cambiar): ")
                if basic_salary:
                    usuario.basic_salary = float(basic_salary)
                start_work_date = input("Ingrese nueva fecha de inicio (deje vacío para no cambiar): ")
                if start_work_date:
                    usuario.start_work_date = start_work_date
                last_vacation_date = input("Ingrese nueva fecha de última vacaciones (deje vacío para no cambiar): ")
                if last_vacation_date:
                    usuario.last_vacation_date = last_vacation_date
                accumulated_vacation_days = input("Ingrese nuevos días de vacaciones acumulados (deje vacío para no cambiar): ")
                if accumulated_vacation_days:
                    usuario.accumulated_vacation_days = int(accumulated_vacation_days)
                Actualizar(usuario)
        elif opcion == '5':
            cedula = input("Ingrese la cédula del usuario a borrar: ")
            Borrar(cedula)
        elif opcion == '6':
            cedula = input("Ingrese la cédula del usuario a buscar: ")
            try:
                usuario = BuscarUsuarios(cedula)
                print(f"Usuario encontrado: {usuario.nombre}, Cédula: {usuario.cedula}, Salario: {usuario.basic_salary}, Fecha de inicio: {usuario.start_date}, Última vacaciones: {usuario.last_vacation_date}, Días acumulados: {usuario.accumulated_vacation_days}")
            except ErrorNoEncontrado as e:
                print(e)
        elif opcion == '7':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
