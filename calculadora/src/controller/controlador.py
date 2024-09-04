import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def conectar_db():
    pass

def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO usuarios (Nombre, Apellido, Documento_Identidad, Correo_Electronico, Telefono, Fecha_Ingreso, Fecha_Salida, Salario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario))
                conn.commit()
            conn.close()
    except Exception as error:
        print(f"Error al agregar el usuario: {error}")

def agregar_liquidacion(indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "INSERT INTO liquidacion (Indemnizacion, Vacaciones, Cesantias, Intereses_Sobre_Cesantias, Prima_Servicios, Retencion_Fuente, Total_A_Pagar, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cur.execute(sql, (indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario))
                conn.commit()
            conn.close()
    except Exception as error:
        print(f"Error al agregar la liquidación: {error}")

def consultar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "SELECT * FROM usuarios WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                usuario = cur.fetchone()
                
                sql = "SELECT * FROM liquidacion WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                liquidacion = cur.fetchone()
                
                if usuario:
                    print("Datos del usuario:")
                    print(f"ID_Usuario: {usuario[0]}")
                    print(f"Nombre: {usuario[1]}")
                    print(f"Apellido: {usuario[2]}")
                    print(f"Documento_Identidad: {usuario[3]}")
                    print(f"Correo_Electronico: {usuario[4]}")
                    print(f"Telefono: {usuario[5]}")
                    print(f"Fecha_Ingreso: {usuario[6]}")
                    print(f"Fecha_Salida: {usuario[7]}")
                    print(f"Salario: {usuario[8]}")
                    
                    if liquidacion:
                        print("\nDatos de la liquidación:")
                        print(f"Indemnización: {liquidacion[1]}")
                        print(f"Vacaciones: {liquidacion[2]}")
                        print(f"Cesantías: {liquidacion[3]}")
                        print(f"Intereses sobre cesantías: {liquidacion[4]}")
                        print(f"Prima de servicios: {liquidacion[5]}")
                        print(f"Retención en la fuente: {liquidacion[6]}")
                        print(f"Total a pagar: {liquidacion[7]}")
                else:
                    print("No se encontró el usuario.")
            conn.close()
    except Exception as error:
        print(f"Error al consultar el usuario: {error}")

def eliminar_usuario(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "DELETE FROM usuarios WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                conn.commit()
            conn.close()
    except Exception as error:
        print(f"Error al eliminar el usuario: {error}")

def eliminar_liquidacion(id_usuario):
    try:
        conn = conectar_db()
        if conn:
            with conn.cursor() as cur:
                sql = "DELETE FROM liquidacion WHERE ID_Usuario = %s"
                cur.execute(sql, (id_usuario,))
                conn.commit()
            conn.close()
    except Exception as error:
        print(f"Error al eliminar los datos de liquidación: {error}")
