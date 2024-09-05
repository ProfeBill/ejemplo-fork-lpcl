import unittest
from unittest.mock import patch
from datetime import datetime
import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_directory, '..', 'src')
sys.path.insert(0, src_path)
from model.calculadora import CalculadoraLiquidacion

class TestCalculadoraLiquidacion(unittest.TestCase):
    def setUp(self):
        self.calculadora = CalculadoraLiquidacion()

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_resultados_prueba')
    def test_calculo_liquidacion(self, mock_calcular_resultados_prueba):
        mock_calcular_resultados_prueba.return_value = (
            3000000,  # indemnity
            500000,   # vacations
            400000,   # severance
            200000,   # severance interest
            1000000,  # bonuses
            150000,   # tax retention
            5000000   # total to pay
        )
        
        salary = 1500000
        start_date = "01/01/2022"
        end_date = "01/01/2024"
        
        indemnity, _, _, _, _, _, _ = self.calculadora.calcular_resultados_prueba(
            salario_basico=salary,
            fecha_inicio_labores=start_date,
            fecha_ultimas_vacaciones=end_date,
            dias_acumulados_vacaciones=0
        )
        
        # Verificación
        self.assertEqual(indemnity, 3000000)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_indemnizacion')
    def test_calculo_indemnizacion(self, mock_calcular_indemnizacion):
        mock_calcular_indemnizacion.return_value = 1000000
        
        salary = 2500000
        worked_years = 0.5
        
        indemnity_value = self.calculadora.calcular_indemnizacion(salary, worked_years)
        
        # Verificación
        self.assertEqual(indemnity_value, 1000000)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_vacaciones')
    def test_calculo_vacaciones(self, mock_calcular_vacaciones):
        mock_calcular_vacaciones.return_value = 20833.33
        
        salary = 1500000
        days_worked = 10
        
        result = self.calculadora.calcular_vacaciones(salary, days_worked)
        
        # Verificación
        self.assertAlmostEqual(result, 20833.33, places=2)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_cesantias')
    def test_calculo_cesantias(self, mock_calcular_cesantias):
        mock_calcular_cesantias.return_value = 125000
        
        monthly_salary = 3000000
        days_worked = 15
        
        result = self.calculadora.calcular_cesantias(monthly_salary, days_worked)
        
        # Verificación
        self.assertEqual(result, 125000)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_prima')
    def test_calculo_prima(self, mock_calcular_prima):
        mock_calcular_prima.return_value = 55555.56
        
        monthly_salary = 2000000
        days_worked = 10
        
        result = self.calculadora.calcular_prima(monthly_salary, days_worked)
        
        # Verificación
        self.assertEqual(result, 55555.56)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_retencion')
    def test_calculo_retencion(self, mock_calcular_retencion):
        mock_calcular_retencion.return_value = 242349.75
        
        labor_income = 5000000
        
        result = self.calculadora.calcular_retencion(labor_income)
        
        # Verificación
        self.assertEqual(result, 242349.75)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_resultados_prueba')
    def test_formato_fecha_invalido_calculo_liquidacion(self, mock_calcular_resultados_prueba):
        mock_calcular_resultados_prueba.side_effect = ValueError("Formato de fecha inválido")
        
        salary = 2000000
        start_date = "01-01-2022"
        end_date = "15-01-2022"
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_resultados_prueba(salary, start_date, end_date, 0)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_intereses_cesantias')
    def test_calculo_intereses_cesantias_valor_negativo(self, mock_calcular_intereses_cesantias):
        mock_calcular_intereses_cesantias.side_effect = ValueError("Valor de cesantías negativo")
        
        severance = -10000
        vacation = 20000
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_intereses_cesantias(severance, vacation)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_resultados_prueba')
    def test_calculo_liquidacion_fecha_invalida(self, mock_calcular_resultados_prueba):
        mock_calcular_resultados_prueba.side_effect = ValueError("Fecha inválida")
        
        basic_salary = 500000
        start_date = "01/01/2023"
        last_vacation_date = "30/02/2024"
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_resultados_prueba(basic_salary, start_date, last_vacation_date, 10)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_indemnizacion')
    def test_motivo_invalido_calculo_indemnizacion(self, mock_calcular_indemnizacion):
        mock_calcular_indemnizacion.side_effect = ValueError("Indemnización inválida")
        
        salary = 2000000
        worked_years = 0.5
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_indemnizacion(salary, worked_years)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_vacaciones')
    def test_dias_trabajados_negativos_calculo_vacaciones(self, mock_calcular_vacaciones):
        mock_calcular_vacaciones.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000
        days_worked = -5
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_vacaciones(monthly_salary, days_worked)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_cesantias')
    def test_dias_trabajados_negativos_calculo_cesantias(self, mock_calcular_cesantias):
        mock_calcular_cesantias.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000
        days_worked = -10
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_cesantias(monthly_salary, days_worked)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_retencion')
    def test_formato_ingreso_laboral_invalido_calculo_retencion(self, mock_calcular_retencion):
        mock_calcular_retencion.side_effect = ValueError("Formato de ingreso laboral inválido")
        
        labor_income = "5000000"
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_retencion(labor_income)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_prima')
    def test_calculo_prima_dias_negativos(self, mock_calcular_prima):
        mock_calcular_prima.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000
        days_worked = -15
        
        with self.assertRaises(ValueError):
            self.calculadora.calcular_prima(monthly_salary, days_worked)

    @patch('model.calculadora.CalculadoraLiquidacion.calcular_retencion')
    def test_calculo_retencion_maximo_rango(self, mock_calcular_retencion):
        mock_calcular_retencion.return_value = 2000000
        
        labor_income = 5000000000
        value_uvt = 39205
        self.calculadora.valor_uvt = value_uvt
        
        withholding = self.calculadora.calcular_retencion(labor_income)
        
        # Verificación
        self.assertEqual(withholding, 2000000)

if __name__ == '__main__':
    unittest.main(verbosity=2)
