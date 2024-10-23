import sys
sys.path.append("src")
from Logica.calculadora import Usuario
import psycopg2
import SecretConfig

def ObtenerCursor( ) :
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()

#Creacion de tabla
def CrearTabla():
    """
    Crea la tabla de usuarios, en caso de que no exista
    """    
    sql = ""
    with open("sql/crear-usuarios.sql","r") as f:
        sql = f.read()

    cursor = ObtenerCursor()

    try:
        cursor.execute( sql )
        cursor.connection.commit()
    except:
        # SI LLEGA AQUI, ES PORQUE LA TABLA YA EXISTE
        cursor.connection.rollback()

#Insertar en la BD
def Insertar( usuario : Usuario ):
    """ Guarda un Usuario en la base de datos """

    try:

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = ObtenerCursor()
        cursor.execute(f"""
        insert into usuarios (
            cedula,   nombre,  apellido,  telefono,  correo, direccion, codigo_municipio, codigo_departamento
        )
        values 
        (
            '{usuario.cedula}',  '{usuario.nombre}', '{usuario.apellido}', '{usuario.telefono}', '{usuario.correo}', '{usuario.direccion}', '{usuario.codigo_municipio}', '{usuario.codigo_departamento}'
        );
                       """)
        
        InsertarUsuario( usuario )

        # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
        # pero si necesitan commit() para hacer los cambios persistentes
        cursor.connection.commit()
    except  :
        cursor.connection.rollback() 
        raise Exception("No fue posible insertar el usuario : " + usuario.cedula )
    
def InsertarUsuario(usuario: Usuario):
    """
    Guarda la lista de familiares asociados a un Usuario
    """
    cursor = ObtenerCursor()

    cursor.execute(f"""
    insert into usuarios(
        nombre, cedula, basic_salary, start_work_date, last_vacation_date, accumulated_vacation_days; 
    )
    values (
    '{ usuario.nombre }',
    '{ usuario.cedula}',
    '{ usuario.basic_salary}',
    '{ usuario.start_date}',
    '{ usuario.last_vacation_date}',
    '{ usuario.accumulated_vacation_days}'
    )""")

#Modificar Datos

def Actualizar( usuario : Usuario ):
    """
    Actualiza los datos de un usuario en la base de datos

    El atributo cedula nunca se debe cambiar, porque es la clave primaria
    """
    cursor = ObtenerCursor()
    cursor.execute(f"""
        update usuarios
        set 
            nombre='{usuario.nombre}',
            basic_salary='{usuario.basic_salary}',
            start_work_date='{usuario.start_date}',
            last_vacation_date='{usuario.last_vacation_date}',
            accumulated_vacation_days='{usuario.accumulated_vacation_days}',
        where cedula='{usuario.cedula}'
    """)

    cursor.connection.commit()

def Borrar( usuario: Usuario ):
    """ Elimina la fila que contiene a un usuario en la BD """
    sql = f"delete from usuarios where cedula = '{usuario.cedula}'"
    cursor = ObtenerCursor()
    cursor.execute( sql )
    cursor.connection.commit()

#Consultar

def BuscarUsuarios( usuario: Usuario ):
    """
    Carga de la DB las filas de la tabla usuarios
    """
    cursor = ObtenerCursor()
    cursor.execute(f""" select nombre, cedula, basic_salary, start_work_date, last_vacation_date, 
        accumulated_vacation_days from usuarios where cedula_usuario = '{ usuario.cedula }' """)
    
    lista = cursor.fetchall()

    if lista is None:
        return f"El usuario no existe en la BD"
    
    return f"El nombre del usuario es: {lista[0]}, Cedula: {lista[1]}, Salario Basico {lista[2]}, Fecha Primer dia de trabajo: {lista[3]},
            Ultimo dia de vacaciones: {list[4]}, Dias de vacaciones acumulados: {lista[5]}"
