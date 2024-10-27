import unittest
from unittest.mock import patch 
from datetime import datetime 
import os  
import sys  

# Obtiene el directorio actual del archivo
current_directory = os.path.dirname(os.path.abspath(__file__))
# Define la ruta al directorio src
src_path = os.path.join(current_directory, '..', 'src')
# Agrega la ruta src al sistema de búsqueda de módulos
sys.path.insert(0, src_path)
# Importa la clase LiquidationCalculator del módulo model.calculadora
from Logica.calculadora import LiquidationCalculator

class TestLiquidationCalculator(unittest.TestCase):
    def setUp(self):
        # Inicializa una instancia de LiquidationCalculator para usar en las pruebas
        self.calculator = LiquidationCalculator()

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion(self, mock_calculate_test_results):
        # Simula el retorno de resultados de liquidación
        mock_calculate_test_results.return_value = {
            "indemnity": 3000000,
            "vacations": 500000,
            "severance": 400000,
            "severance_interest": 200000,
            "bonuses": 1000000,
            "tax_retention": 150000,
            "total_to_pay": 5000000
        }
        
        # Llama al método para calcular los resultados de la liquidación
        result = self.calculator.calculate_test_results(
            basic_salary=1500000,
            start_date="01/01/2022",
            last_vacation_date="01/01/2024",
            accumulated_vacation_days=0
        )
        
        # Verifica que el valor de indemnidad sea el esperado
        self.assertEqual(result['indemnity'], 3000000)

    @patch('model.calculadora.LiquidationCalculator.calculate_indemnity')
    def test_calculo_indemnizacion(self, mock_calculate_indemnity):
        # Simula el retorno del cálculo de indemnización
        mock_calculate_indemnity.return_value = 1000000
        
        salary = 2500000  # Salario de entrada
        worked_years = 0.5  # Años trabajados
        
        # Calcula el valor de la indemnización
        indemnity_value = self.calculator.calculate_indemnity(salary, worked_years)
        
        # Verifica que el valor de indemnización sea el esperado
        self.assertEqual(indemnity_value, 1000000)

    @patch('model.calculadora.LiquidationCalculator.calculate_vacations')
    def test_calculo_vacaciones(self, mock_calculate_vacations):
        # Simula el retorno del cálculo de vacaciones
        mock_calculate_vacations.return_value = 20833.33
        
        salary = 1500000  # Salario de entrada
        days_worked = 10  # Días trabajados
        
        # Calcula las vacaciones
        result = self.calculator.calculate_vacations(salary, days_worked)
        
        # Verifica que el resultado sea casi igual al esperado
        self.assertAlmostEqual(result, 20833.33, places=2)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_calculo_cesantias(self, mock_calculate_severance):
        # Simula el retorno del cálculo de cesantías
        mock_calculate_severance.return_value = 125000
        
        monthly_salary = 3000000  # Salario mensual
        days_worked = 15  # Días trabajados
        
        # Calcula las cesantías
        result = self.calculator.calculate_severance(monthly_salary, days_worked)
        
        # Verifica que el resultado de cesantías sea el esperado
        self.assertEqual(result, 125000)

    @patch('model.calculadora.LiquidationCalculator.calculate_bonus')
    def test_calculo_prima(self, mock_calculate_bonus):
        # Simula el retorno del cálculo de prima
        mock_calculate_bonus.return_value = 55555.56
        
        monthly_salary = 2000000  # Salario mensual
        days_worked = 10  # Días trabajados
        
        # Calcula la prima
        result = self.calculator.calculate_bonus(monthly_salary, days_worked)
        
        # Verifica que el resultado de la prima sea el esperado
        self.assertEqual(result, 55555.56)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_calculo_retencion(self, mock_calculate_tax_retention):
        # Simula el retorno del cálculo de retención de impuestos
        mock_calculate_tax_retention.return_value = 242349.75
        
        labor_income = 5000000  # Ingreso laboral
        
        # Calcula la retención de impuestos
        result = self.calculator.calculate_tax_retention(labor_income)
        
        # Verifica que el resultado de la retención sea el esperado
        self.assertEqual(result, 242349.75)

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_formato_fecha_invalido_calculo_liquidacion(self, mock_calculate_test_results):
        # Simula una excepción por formato de fecha inválido
        mock_calculate_test_results.side_effect = ValueError("Formato de fecha inválido")
        
        salary = 2000000  # Salario de entrada
        start_date = "01-01-2022"  # Fecha de inicio inválida
        end_date = "15-01-2022"  # Fecha de fin
        
        # Verifica que se lance una excepción por fecha inválida
        with self.assertRaises(ValueError):
            self.calculator.calculate_test_results(salary, start_date, end_date, 0)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance_interest')
    def test_calculo_intereses_cesantias_valor_negativo(self, mock_calculate_severance_interest):
        # Simula una excepción por valor de cesantías negativo
        mock_calculate_severance_interest.side_effect = ValueError("Valor de cesantías negativo")
        
        severance = -10000  # Valor de cesantías negativo
        vacation = 20000  # Valor de vacaciones
        
        # Verifica que se lance una excepción por valor negativo
        with self.assertRaises(ValueError):
            self.calculator.calculate_severance_interest(severance, vacation)

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion_fecha_invalida(self, mock_calculate_test_results):
        # Simula una excepción por fecha inválida en liquidación
        mock_calculate_test_results.side_effect = ValueError("Fecha inválida")
        
        basic_salary = 500000  # Salario básico
        start_date = "01/01/2023"  # Fecha de inicio
        last_vacation_date = "30/02/2024"  # Fecha de vacaciones inválida
        
        # Verifica que se lance una excepción por fecha inválida
        with self.assertRaises(ValueError):
            self.calculator.calculate_test_results(basic_salary, start_date, last_vacation_date, 10)

    @patch('model.calculadora.LiquidationCalculator.calculate_indemnity')
    def test_motivo_invalido_calculo_indemnizacion(self, mock_calculate_indemnity):
        # Simula una excepción por motivo inválido en el cálculo de indemnización
        mock_calculate_indemnity.side_effect = ValueError("Indemnización inválida")
        
        salary = 2000000  # Salario de entrada
        worked_years = 0.5  # Años trabajados
        
        # Verifica que se lance una excepción por motivo inválido
        with self.assertRaises(ValueError):
            self.calculator.calculate_indemnity(salary, worked_years)

    @patch('model.calculadora.LiquidationCalculator.calculate_vacations')
    def test_dias_trabajados_negativos_calculo_vacaciones(self, mock_calculate_vacations):
        # Simula una excepción por días trabajados negativos
        mock_calculate_vacations.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000  # Salario mensual
        days_worked = -5  # Días trabajados negativos
        
        # Verifica que se lance una excepción por días negativos
        with self.assertRaises(ValueError):
            self.calculator.calculate_vacations(monthly_salary, days_worked)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_dias_trabajados_negativos_calculo_cesantias(self, mock_calculate_severance):
        # Simula una excepción por días trabajados negativos
        mock_calculate_severance.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000  # Salario mensual
        days_worked = -10  # Días trabajados negativos
        
        # Verifica que se lance una excepción por días negativos
        with self.assertRaises(ValueError):
            self.calculator.calculate_severance(monthly_salary, days_worked)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_formato_ingreso_laboral_invalido_calculo_retencion(self, mock_calculate_tax_retention):
        # Simula una excepción por formato de ingreso laboral inválido
        mock_calculate_tax_retention.side_effect = ValueError("Formato de ingreso laboral inválido")
        
        labor_income = "5000000"  # Ingreso laboral en formato inválido
        
        # Verifica que se lance una excepción por formato inválido
        with self.assertRaises(ValueError):
            self.calculator.calculate_tax_retention(labor_income)

    @patch('model.calculadora.LiquidationCalculator.calculate_bonus')
    def test_calculo_prima_dias_negativos(self, mock_calculate_bonus):
        # Simula una excepción por días trabajados negativos en el cálculo de prima
        mock_calculate_bonus.side_effect = ValueError("Días trabajados negativos")
        
        monthly_salary = 2000000  # Salario mensual
        days_worked = -15  # Días trabajados negativos
        
        # Verifica que se lance una excepción por días negativos
        with self.assertRaises(ValueError):
            self.calculator.calculate_bonus(monthly_salary, days_worked)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_calculo_retencion_maximo_rango(self, mock_calculate_tax_retention):
        # Simula el retorno del cálculo de retención en el máximo rango
        mock_calculate_tax_retention.return_value = 2000000
        
        labor_income = 5000000000  # Ingreso laboral alto
        value_uvt = 39205  # Valor de UVT
        self.calculator.uvt_value = value_uvt  # Asigna el valor de UVT
        
        # Calcula la retención
        withholding = self.calculator.calculate_tax_retention(labor_income)
        
        # Verifica que la retención sea la esperada
        self.assertEqual(withholding, 2000000)

    # Nuevos casos de prueba adicionales
    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion_dias_acumulados(self, mock_calculate_test_results):
        # Simula el retorno de resultados de liquidación con días acumulados
        mock_calculate_test_results.return_value = {
            "indemnity": 2500000,
            "vacations": 400000,
            "severance": 300000,
            "severance_interest": 150000,
            "bonuses": 800000,
            "tax_retention": 100000,
            "total_to_pay": 4000000
        }
        
        # Llama al método para calcular los resultados de la liquidación
        result = self.calculator.calculate_test_results(
            basic_salary=1200000,
            start_date="01/01/2022",
            last_vacation_date="01/01/2024",
            accumulated_vacation_days=10
        )
        
        # Verifica que el valor de vacaciones sea el esperado
        self.assertEqual(result['vacations'], 400000)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_calculo_cesantias_menor_salario(self, mock_calculate_severance):
        # Simula el retorno del cálculo de cesantías para un salario menor
        mock_calculate_severance.return_value = 50000
        
        monthly_salary = 1000000  # Salario mensual
        days_worked = 5  # Días trabajados
        
        # Calcula las cesantías
        result = self.calculator.calculate_severance(monthly_salary, days_worked)
        
        # Verifica que el resultado de cesantías sea el esperado
        self.assertEqual(result, 50000)

    @patch('model.calculadora.LiquidationCalculator.calculate_bonus')
    def test_calculo_prima_mayor_salario(self, mock_calculate_bonus):
        # Simula el retorno del cálculo de prima para un salario mayor
        mock_calculate_bonus.return_value = 111111.11
        
        monthly_salary = 3000000  # Salario mensual
        days_worked = 10  # Días trabajados
        
        # Calcula la prima
        result = self.calculator.calculate_bonus(monthly_salary, days_worked)
        
        # Verifica que el resultado de la prima sea el esperado
        self.assertEqual(result, 111111.11)

    @patch('model.calculadora.LiquidationCalculator.calculate_tax_retention')
    def test_calculo_retencion_ajustada(self, mock_calculate_tax_retention):
        # Simula el retorno del cálculo de retención ajustada
        mock_calculate_tax_retention.return_value = 50000
        
        labor_income = 1000000  # Ingreso laboral
        
        # Calcula la retención
        result = self.calculator.calculate_tax_retention(labor_income)
        
        # Verifica que el resultado de la retención sea el esperado
        self.assertEqual(result, 50000)

    @patch('model.calculadora.LiquidationCalculator.calculate_severance')
    def test_calculo_cesantias_mayor_dias(self, mock_calculate_severance):
        # Simula el retorno del cálculo de cesantías para más días trabajados
        mock_calculate_severance.return_value = 200000
        
        monthly_salary = 1500000  # Salario mensual
        days_worked = 30  # Días trabajados
        
        # Calcula las cesantías
        result = self.calculator.calculate_severance(monthly_salary, days_worked)
        
        # Verifica que el resultado de cesantías sea el esperado
        self.assertEqual(result, 200000)

    @patch('model.calculadora.LiquidationCalculator.calculate_test_results')
    def test_calculo_liquidacion_varios_parametros(self, mock_calculate_test_results):
        # Simula el retorno de resultados de liquidación con varios parámetros
        mock_calculate_test_results.return_value = {
            "indemnity": 3500000,
            "vacations": 600000,
            "severance": 450000,
            "severance_interest": 225000,
            "bonuses": 1200000,
            "tax_retention": 180000,
            "total_to_pay": 6000000
        }
        
        # Llama al método para calcular los resultados de la liquidación
        result = self.calculator.calculate_test_results(
            basic_salary=1600000,
            start_date="01/01/2022",
            last_vacation_date="01/01/2024",
            accumulated_vacation_days=5
        )
        
        # Verifica que el total a pagar sea el esperado
        self.assertEqual(result['total_to_pay'], 6000000)

if __name__ == '__main__':
    unittest.main(verbosity=2)  

