import unittest
from datetime import datetime
import os
import sys

directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_src = os.path.join(directorio_actual, '..', 'src')
sys.path.insert(0, ruta_src)

from model.calculadora import CalculadoraLiquidacion

class LiquidacionTests(unittest.TestCase):

    def setUp(self):
        self.calc = CalculadoraLiquidacion()

    def test_liquidacion_correcta(self):
        salario = 1500000
        fecha_inicio = "01/01/2022"
        fecha_fin = "01/01/2023"
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin_dt = datetime.strptime(fecha_fin, "%d/%m/%Y")
        dias_trabajados = (fecha_fin_dt - fecha_inicio_dt).days
        años_trabajados = dias_trabajados / 365

        indemnizacion, *_ = self.calc.calcular_resultados_prueba(
            salario_basico=salario,
            fecha_inicio_labores=fecha_inicio,
            fecha_ultimas_vacaciones=fecha_fin,
            dias_acumulados_vacaciones=0
        )

        dias_por_anio = 20
        max_dias_indemnizacion = min(años_trabajados * dias_por_anio, 12 * dias_por_anio)
        liquidacion_calculada = round((salario * max_dias_indemnizacion) / 30, 2)

        self.assertEqual(indemnizacion, liquidacion_calculada)

    def test_indemnizacion(self):
        salario = 2500000
        meses_trabajados = 6
        años_trabajados = meses_trabajados / 12
        resultado_indemnizacion = self.calc.calcular_indemnizacion(salario, años_trabajados)
        esperado = round(salario * años_trabajados * 20 / 30, 2)

        self.assertEqual(resultado_indemnizacion, esperado)

    def test_vacaciones(self):
        salario = 1500000
        dias_trabajados = 10
        valor_vacaciones = self.calc.calcular_vacaciones(salario, dias_trabajados)

        self.assertAlmostEqual(valor_vacaciones, 20833.33, places=2)

    def test_cesantias(self):
        salario = 3000000
        dias = 15
        cesantias = self.calc.calcular_cesantias(salario, dias)

        self.assertEqual(cesantias, 125000)

    def test_retencion(self):
        ingreso = 5000000
        retencion_calculada = self.calc.calcular_retencion(ingreso)

        self.assertEqual(retencion_calculada, 242349.75)

    def test_fechas_invalidas(self):
        salario = 2000000
        fecha_incorrecta = "01-01-2022"
        fecha_fin = "15-01-2022"

        with self.assertRaises(ValueError):
            self.calc.calcular_resultados_prueba(salario, fecha_incorrecta, fecha_fin, 0)

    def test_indemnizacion_salario_negativo(self):
        salario = -2000000
        meses = 6
        años = meses / 12

        with self.assertRaises(ValueError):
            self.calc.calcular_indemnizacion(salario, años)

    def test_vacaciones_dias_negativos(self):
        salario = 2000000
        dias = -5

        with self.assertRaises(ValueError):
            self.calc.calcular_vacaciones(salario, dias)

    def test_retencion_ingreso_invalido(self):
        ingreso = "cinco millones"

        with self.assertRaises(ValueError):
            self.calc.calcular_retencion(ingreso)

    def test_retencion_maxima(self):
        ingreso_alto = 5000000000  
        valor_uvt = 39205 
        self.calc.valor_uvt = valor_uvt

        retencion = self.calc.calcular_retencion(ingreso_alto)
        ingreso_uvt = ingreso_alto / valor_uvt
        base_uvt = ingreso_uvt - 2300
        esperado = round(base_uvt * 0.39 * valor_uvt + 770 * valor_uvt, 2)

        self.assertEqual(retencion, esperado)

if __name__ == '__main__':
    unittest.main(verbosity=2)