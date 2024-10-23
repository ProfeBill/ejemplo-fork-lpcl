import sys 
sys.path.append("src")
from controller.controlador import Insertar, BuscarUsuarios, Borrar, Actualizar
from Logica.calculadora import Usuario

#caso de exito
usuario_valido = Usuario(
    cedula="12345678",
    nombre="Juan",
    basic_salary=1000,
    start_date="2023-01-01",
    last_vacation_date="2023-10-01",
    accumulated_vacation_days=5
)
Insertar(usuario_valido)

usuario_actualizado = Usuario(
    cedula="12345678",
    nombre="Juan Carlos",
    basic_salary=1200,
    start_date="2023-01-01",
    last_vacation_date="2023-10-01",
    accumulated_vacation_days=10
)
Actualizar(usuario_actualizado)



#caso de fallo
usuario_invalido = Usuario(
    cedula="",
    nombre="Juan",
    basic_salary=1000,
    start_date="2023-01-01",
    last_vacation_date="2023-10-01",
    accumulated_vacation_days=5
)
try:
    Insertar(usuario_invalido)
except Exception as e:
    print(e)

usuario_actualizado = Usuario(
    cedula="12345678",
    nombre="Juan Carlos",
    basic_salary=1200,
    start_date="2023-01-01",
    last_vacation_date="2023-10-01",
    accumulated_vacation_days=10
)
Actualizar(usuario_actualizado)

#borrar
cedula_existente = "12345678"
Borrar(cedula_existente)

cedula_inexistente = "00000000"
try:
    Borrar(cedula_inexistente)
except Exception as e:
    print(e)

#buscar
cedula_existente = "12345678"
resultado = BuscarUsuarios(cedula_existente)
print(resultado)

cedula_inexistente = "00000000"
resultado = BuscarUsuarios(cedula_inexistente)
print(resultado)
