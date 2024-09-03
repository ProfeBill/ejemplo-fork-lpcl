# test/test_calculadora.py

import unittest
from datetime import datetime
from src.model.calculadora import CalculadoraLiquidacion

class TestCalculadoraLiquidacion(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculadoraLiquidacion()

    def test_calculo_liquidacion(self):
        salario = 1500000
        fecha_inicio = "01/01/2024"
        fecha_fin = "01/01/2024"
        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin_dt = datetime.strptime(fecha_fin, "%d/%m/%Y")
        dias_trabajados = (fecha_fin_dt - fecha_inicio_dt).days
        tiempo_trabajado_anos = dias_trabajados / 365
        indemnizacion, _, _, _, _, _, _ = self.calculadora.calcular_resultados_prueba(
            salario_basico=salario,
            fecha_inicio_labores=fecha_inicio,
            fecha_ultimas_vacaciones=fecha_fin,
            dias_acumulados_vacaciones=0
        )
        meses_maximos = 12
        dias_por_anio = 20
        dias_maximos = meses_maximos * dias_por_anio
        dias_indemnizacion = min(tiempo_trabajado_anos * dias_por_anio, dias_maximos)
        liquidacion_esperada = round((salario * dias_indemnizacion) / 30, 2)
        self.assertEqual(indemnizacion, liquidacion_esperada)

    def test_calculo_indemnizacion(self):
        salario = 2500000
        meses_trabajados = 6
        tiempo_trabajado_anos = meses_trabajados / 12
        valor_indemnizacion = self.calculadora.calcular_indemnizacion(salario, tiempo_trabajado_anos)
        valor_esperado = round(salario * tiempo_trabajado_anos * 20 / 30, 2)
        self.assertEqual(valor_indemnizacion, valor_esperado)

    def test_calculo_vacaciones(self):
        salario = 1500000
        dias_acumulados_vacaciones = 10
        result = self.calculadora.calcular_vacaciones(salario, dias_acumulados_vacaciones)
        self.assertAlmostEqual(result, 500000.00, places=2)

    def test_calculo_cesantias(self):
        salario_mensual = 3000000
        dias_trabajados = 15
        result = self.calculadora.calcular_cesantias(salario_mensual, dias_trabajados)
        self.assertEqual(result, 1500000.00)

    def test_calculo_retencion(self):
        ingreso_laboral = 5000000
        result = self.calculadora.calcular_retencion(ingreso_laboral)
        self.assertEqual(result, 1930612.50)  # Ajusta este valor según tu lógica de cálculo

    def test_calculo_intereses_cesantias(self):
        cesantias = 1000000
        vacaciones = 500000
        result = self.calculadora.calcular_intereses_cesantias(cesantias, vacaciones)
        self.assertEqual(result, 180000.00)

    def test_calculo_prima(self):
        salario_mensual = 1800000
        dias_trabajados = 90
        result = self.calculadora.calcular_prima(salario_mensual, dias_trabajados)
        self.assertAlmostEqual(result, 900000.00, places=2)

    # Agrega aquí más casos de prueba incluyendo casos con entradas inválidas

    def test_calculo_indemnizacion_negativa(self):
        salario = 1500000
        tiempo_trabajado_anos = -1
        with self.assertRaises(ValueError):
            self.calculadora.calcular_indemnizacion(salario, tiempo_trabajado_anos)

    def test_calculo_vacaciones_negativas(self):
        salario = 1500000
        dias_acumulados_vacaciones = -10
        with self.assertRaises(ValueError):
            self.calculadora.calcular_vacaciones(salario, dias_acumulados_vacaciones)

    def test_calculo_cesantias_negativas(self):
        salario_mensual = 3000000
        dias_trabajados = -15
        with self.assertRaises(ValueError):
            self.calculadora.calcular_cesantias(salario_mensual, dias_trabajados)

    def test_calculo_retencion_negativa(self):
        ingreso_laboral = -5000000
        with self.assertRaises(ValueError):
            self.calculadora.calcular_retencion(ingreso_laboral)

    def test_calculo_intereses_cesantias_negativos(self):
        cesantias = -1000000
        vacaciones = 500000
        with self.assertRaises(ValueError):
            self.calculadora.calcular_intereses_cesantias(cesantias, vacaciones)

    def test_calculo_prima_negativa(self):
        salario_mensual = 1800000
        dias_trabajados = -90
        with self.assertRaises(ValueError):
            self.calculadora.calcular_prima(salario_mensual, dias_trabajados)

    # Más casos de prueba...

if __name__ == '__main__':
    unittest.main(verbosity=2)
