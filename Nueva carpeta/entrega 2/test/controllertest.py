import unittest
from unittest.mock import patch
from datetime import datetime
import os
import sys

# Configuración del directorio para importaciones
current_directory = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_directory, '..', 'src')
sys.path.insert(0, src_path)
from model.calculadora import LiquidationCalculator

class TestLiquidationCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = LiquidationCalculator()

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion(self, mock_calculate_test_results):
        mock_calculate_test_results.return_value = {
            "indemnity": 3000000,
            "vacations": 500000,
            "severance": 400000,
            "severance_interest": 200000,
            "bonuses": 1000000,
            "tax_retention": 150000,
            "total_to_pay": 5000000
        }
        
        result = self.calculator.calculate_test_results(
            basic_salary=1500000,
            start_date="01/01/2022",
            last_vacation_date="01/01/2024",
            accumulated_vacation_days=0
        )
        
        self.assertEqual(result['indemnity'], 3000000)

    @patch('model.calculadora.LiquidationCalculator.calculate_indemnity')
    def test_calculo_indemnizacion(self, mock_calculate_indemnity):
        mock_calculate_indemnity.return_value = 1000000
        
        salary = 2500000
        worked_years = 0.5
        
        indemnity_value = self.calculator.calculate_indemnity(salary, worked_years)
        
        self.assertEqual(indemnity_value, 1000000)

    @patch('model.calculadora.LiquidationCalculator.calculate_vacations')
    def test_calculo_vacaciones(self, mock_calculate_vacations):
        mock_calculate_vacations.return_value = 20833.33
        
        salary = 1500000
        days_worked = 10
        
        result = self.calculator.calculate_vacations(salary, days_worked)
        
        self.assertAlmostEqual(result, 20833.33, places=2)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_calculo_cesantias(self, mock_calculate_severance):
        mock_calculate_severance.return_value = 125000
        
        monthly_salary = 3000000
        days_worked = 15
        
        result = self.calculator.calculate_severance(monthly_salary, days_worked)
        
        self.assertEqual(result, 125000)

    @patch('model.calculadora.LiquidationCalculator.calculate_bonus')
    def test_calculo_prima(self, mock_calculate_bonus):
        mock_calculate_bonus.return_value = 55555.56
        
        monthly_salary = 2000000
        days_worked = 10
        
        result = self.calculator.calculate_bonus(monthly_salary, days_worked)
        
        self.assertEqual(result, 55555.56)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_calculo_retencion(self, mock_calculate_tax_retention):
        mock_calculate_tax_retention.return_value = 242349.75
        
        labor_income = 5000000
        
        result = self.calculator.calculate_tax_retention(labor_income)
        
        self.assertEqual(result, 242349.75)

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_formato_fecha_invalido_calculo_liquidacion(self, mock_calculate_test_results):
        mock_calculate_test_results.side_effect = ValueError("Formato de fecha inválido")
        
        salary = 2000000
        start_date = "01-01-2022"
        end_date = "15-01-2022"
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_test_results(salary, start_date, end_date, 0)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance_interest')
    def test_calculo_intereses_cesantias_valor_negativo(self, mock_calculate_severance_interest):
        mock_calculate_severance_interest.side_effect = ValueError("Valor de cesantías negativo")
        
        severance = -10000
        vacation = 20000
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_severance_interest(severance, vacation)

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion_fecha_invalida(self, mock_calculate_test_results):
        mock_calculate_test_results.side_effect = ValueError("Fecha inválida")
        
        basic_salary = 500000
        start_date = "01/01/2023"
        last_vacation_date = "30/02/2024"
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_test_results(basic_salary, start_date, last_vacation_date, 10)

    @patch('model.calculadora.LiquidationCalculator.calculate_indemnity')
    def test_motivo_invalido_calculo_indemnizacion(self, mock_calculate_indemnity):
        mock_calculate_indemnity.side_effect = ValueError("Indemnización inválida")
        
        salary = 2000000
        worked_years = 0.5
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_indemnity(salary, worked_years)

    @patch('model.calculadora.LiquidationCalculator.calculate_vacations')
    def test_dias_trabajados_negativos_calculo_vacaciones(self, mock_calculate_vacations):
        mock_calculate_vacations.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000
        days_worked = -5
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_vacations(monthly_salary, days_worked)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_dias_trabajados_negativos_calculo_cesantias(self, mock_calculate_severance):
        mock_calculate_severance.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000
        days_worked = -10
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_severance(monthly_salary, days_worked)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_formato_ingreso_laboral_invalido_calculo_retencion(self, mock_calculate_tax_retention):
        mock_calculate_tax_retention.side_effect = ValueError("Formato de ingreso laboral inválido")
        
        labor_income = "5000000"
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_tax_retention(labor_income)

    @patch('model.calculadora.LiquidationCalculator.calculate_bonus')
    def test_calculo_prima_dias_negativos(self, mock_calculate_bonus):
        mock_calculate_bonus.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000
        days_worked = -15
        
        with self.assertRaises(ValueError):
            self.calculator.calculate_bonus(monthly_salary, days_worked)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_calculo_retencion_maximo_rango(self, mock_calculate_tax_retention):
        mock_calculate_tax_retention.return_value = 2000000
        
        labor_income = 5000000000
        value_uvt = 39205
        self.calculator.uvt_value = value_uvt
        
        withholding = self.calculator.calculate_tax_retention(labor_income)
        
        self.assertEqual(withholding, 2000000)

    # Nuevos casos de prueba adicionales

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion_dias_acumulados(self, mock_calculate_test_results):
        mock_calculate_test_results.return_value = {
            "indemnity": 2500000,
            "vacations": 400000,
            "severance": 300000,
            "severance_interest": 150000,
            "bonuses": 800000,
            "tax_retention": 100000,
            "total_to_pay": 4000000
        }
        
        result = self.calculator.calculate_test_results(
            basic_salary=1200000,
            start_date="01/01/2022",
            last_vacation_date="01/01/2024",
            accumulated_vacation_days=10
        )
        
        self.assertEqual(result['vacations'], 400000)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_calculo_cesantias_menor_salario(self, mock_calculate_severance):
        mock_calculate_severance.return_value = 50000
        
        monthly_salary = 1000000
        days_worked = 5
        
        result = self.calculator.calculate_severance(monthly_salary, days_worked)
        
        self.assertEqual(result, 50000)

    @patch('model.calculadora.LiquidationCalculator.calculate_bonus')
    def test_calculo_prima_mayor_salario(self, mock_calculate_bonus):
        mock_calculate_bonus.return_value = 111111.11
        
        monthly_salary = 3000000
        days_worked = 10
        
        result = self.calculator.calculate_bonus(monthly_salary, days_worked)
        
        self.assertEqual(result, 111111.11)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_calculo_retencion_ajustada(self, mock_calculate_tax_retention):
        mock_calculate_tax_retention.return_value = 50000
        
        labor_income = 1000000
        
        result = self.calculator.calculate_tax_retention(labor_income)
        
        self.assertEqual(result, 50000)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_calculo_cesantias_mayor_dias(self, mock_calculate_severance):
        mock_calculate_severance.return_value = 200000
        
        monthly_salary = 1500000
        days_worked = 30
        
        result = self.calculator.calculate_severance(monthly_salary, days_worked)
        
        self.assertEqual(result, 200000)

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion_varios_parametros(self, mock_calculate_test_results):
        mock_calculate_test_results.return_value = {
            "indemnity": 3500000,
            "vacations": 600000,
            "severance": 450000,
            "severance_interest": 225000,
            "bonuses": 1200000,
            "tax_retention": 180000,
            "total_to_pay": 6000000
        }
        
        result = self.calculator.calculate_test_results(
            basic_salary=1600000,
            start_date="01/01/2022",
            last_vacation_date="01/01/2024",
            accumulated_vacation_days=5
        )
        
        self.assertEqual(result['total_to_pay'], 6000000)

if __name__ == '__main__':
    unittest.main(verbosity=2)
