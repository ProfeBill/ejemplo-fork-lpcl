import unittest
import sys
sys.path.append("src")
from Logica.calculadora import CalculadorLiquidacion
from Logica.calculadora import Usuario
import math

class IndemizacionTest(unittest.TestCase):
    #En estos test vamos a comprobar las funcionalidades de la clase CalculadorLiquidacion
    def testindemnizacion1(self):
        #Valores de entrada
        nombre_empleado =  "Juan"
        cedula = "1234567890"
        motivo_de_finalizacion_contrato = "renuncia"
        Salario_basico = 4000000
        Fecha_de_inicio_laboral = "10/11/2023"
        Fechas_ultimas_vacaciones = "4/4/2024"
        #Ejecucion del programa
        usuario = Usuario(nombre_empleado, cedula, motivo_de_finalizacion_contrato,Salario_basico, Fecha_de_inicio_laboral, Fechas_ultimas_vacaciones)
        calculadora = CalculadorLiquidacion(usuario)
        resultados: dict = calculadora.calcular_resultados()

        #Resultados esperados
        indemnizacion = 0
        vacaciones= 166667
        cesantias = 1622223
        primas = 1622223
        intereses_cesantias = 194667
        retencion_en_la_fuente = 360578
        total_a_pagar = 3245200

        #valores de salida 
        Valor_indemnizacion = resultados.get("indemnizacion")
        Valor_vacaciones = resultados.get("vacaciones")
        Valor_cesantias = resultados.get("cesantia")
        Valor_primas = resultados.get("bonos")
        Valor_intereses_cesantias = resultados.get("intereses_cesantia")
        Valor_retencion_en_la_fuente = resultados.get("retencion_impuesto")
        Valor_total_a_pagar = resultados.get("total_a_pagar")

        #verificaciones
        self.assertEqual(indemnizacion, Valor_indemnizacion)
        self.assertEqual(vacaciones, math.ceil(Valor_vacaciones))
        self.assertEqual(cesantias, math.ceil(Valor_cesantias))
        self.assertEqual(primas, math.ceil(Valor_primas))
        self.assertEqual(intereses_cesantias,math.ceil(Valor_intereses_cesantias))
        self.assertEqual(retencion_en_la_fuente, math.ceil(Valor_retencion_en_la_fuente))
        self.assertEqual(total_a_pagar, math.ceil(Valor_total_a_pagar))

if __name__ == '__main__':
    unittest.main()