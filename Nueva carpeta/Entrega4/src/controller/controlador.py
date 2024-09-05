import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def conectar_db():
  
    return None


def agregar_usuario(nombre, apellido, documento_identidad, correo_electronico, telefono, fecha_ingreso, fecha_salida, salario):
    
    return None


def agregar_liquidacion(indemnizacion, vacaciones, cesantias, intereses_sobre_cesantias, prima_servicios, retencion_fuente, total_a_pagar, id_usuario):
   
    return None


def consultar_usuario(id_usuario):
    print("Simulación: No se encontró el usuario.")
    return None


def eliminar_usuario(id_usuario):
    
    print("Simulación: No se encontró el usuario.")
    return None


def eliminar_liquidacion(id_usuario):
    
    print("Simulación: No se encontraron los datos de liquidación para el usuario.")
    return None
