import sys
sys.path.append("src")
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

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            CrearTabla()
            print("Tabla creada con éxito (o ya existente).")
        
        elif opcion == '2':
            cedula = input("Cedula del usuario a ingresar: ")
            nombre = input("Nuevo Nombre: ")
            basic_salary = input("Salario Básico: ")
            start_date = input("Fecha de Inicio (AAAA-MM-DD): ")
            last_vacation_date = input("Fecha de Últimas Vacaciones (AAAA-MM-DD): ")
            accumulated_vacation_days = input("Días de Vacaciones Acumulados: ")
            usuario = Usuario(nombre, cedula, basic_salary, accumulated_vacation_days, start_date, last_vacation_date)
            Insertar(usuario)
            print(f"Usuario {nombre} insertado con éxito.")
        
        elif opcion == '3':
            cedula = input("Cedula del usuario a actualizar: ")
            nombre = input("Nuevo Nombre: ")
            basic_salary = input("Salario Básico: ")
            start_date = input("Fecha de Inicio (AAAA-MM-DD): ")
            last_vacation_date = input("Fecha de Últimas Vacaciones (AAAA-MM-DD): ")
            accumulated_vacation_days = input("Días de Vacaciones Acumulados: ")

            usuario = Usuario(cedula, nombre, "", "", "", "", "", "", basic_salary, start_date, last_vacation_date, accumulated_vacation_days)
            Actualizar(usuario)
            print(f"Usuario con cédula {cedula} actualizado con éxito.")

        elif opcion == '4':
            cedula = input("Cedula del usuario a eliminar: ")
            Borrar(cedula)
            print(f"Usuario con cédula {cedula} eliminado con éxito.")
        
        elif opcion == '5':
            cedula = input("Cedula del usuario a buscar: ")
            resultado = BuscarUsuarios(cedula)
            print(resultado)

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    interfaz()
