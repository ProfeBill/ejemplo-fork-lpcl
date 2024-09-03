

from controller.controlador import conectar_db, agregar_usuario, agregar_liquidacion, consultar_usuario, eliminar_usuario

def menu():
    while True:
        print("\nMenú:")
        print("1. Conectar a DB")
        print("2. Agregar usuario")
        print("3. Agregar liquidación")
        print("4. Consultar usuario")
        print("5. Eliminar usuario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            conectar_db()
        elif opcion == '2':
            usuario = input("Ingrese el nombre del usuario: ")
            agregar_usuario(usuario)
        elif opcion == '3':
            liquidacion = input("Ingrese los detalles de la liquidación: ")
            agregar_liquidacion(liquidacion)
        elif opcion == '4':
            usuario_id = input("Ingrese el ID del usuario: ")
            print(consultar_usuario(usuario_id))
        elif opcion == '5':
            usuario_id = input("Ingrese el ID del usuario: ")
            eliminar_usuario(usuario_id)
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
