import sys
sys.path.append("src")
from Logica.calculadora import Usuario, CalculadorLiquidacion
from datetime import datetime
import traceback

# Define las clases Usuario y CalculadorLiquidacion aquí (copia el código que ya tienes)

def ingresar_datos_usuario():
    print("Ingrese los datos del empleado para calcular la liquidación.")
    nombre = input("Nombre del empleado: ")
    cedula = input("Cédula del empleado: ")
    motivo_finalizacion = input("Motivo de finalización de contrato (Ej: renuncia, despido, etc.): ")
    salario_basico = float(input("Salario básico: "))
    fecha_inicio = input("Fecha de inicio laboral (dd/mm/yyyy): ")
    fecha_ultimo_vacaciones = input("Fecha de las últimas vacaciones (dd/mm/yyyy): ")
    
    usuario = Usuario(
        nombre=nombre,
        cedula=cedula,
        motivo_finalizacion=motivo_finalizacion,
        salario_basico=salario_basico,
        fecha_inicio=fecha_inicio,
        fecha_ultimo_vacaciones=fecha_ultimo_vacaciones
    )
    return usuario

def mostrar_resultados(resultados):
    print("\nResultados de la liquidación:")
    for clave, valor in resultados.items():
        print(f"{clave.capitalize().replace('_', ' ')}: {valor:,.2f} COP")

def main():
    try:
        usuario = ingresar_datos_usuario()
        calculador = CalculadorLiquidacion(usuario)
        resultados = calculador.calcular_resultados()
        mostrar_resultados(resultados)
    except Exception as e:
        print(f"\nHa ocurrido un error: {e}")
        print(traceback.format_exc())  # Opcional: muestra más detalles del error para depuración

if __name__ == "__main__":
    main()
