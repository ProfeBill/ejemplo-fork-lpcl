

import unittest
from calculadora.settlement_calculator import SettlementCalculator # type: ignore

class TestSettlementCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = SettlementCalculator()

    def test_calculate_indemnification(self):
        salary = 2000000
        years_worked = 2
        result = self.calculator.calculate_indemnification(salary, years_worked)
        expected = round(salary * years_worked * 20 / 30, 2)
        self.assertEqual(result, expected)

    def test_calculate_vacations(self):
        salary = 1500000
        days_worked = 15
        result = self.calculator.calculate_vacations(salary, days_worked)
        expected = round(salary * (days_worked / 360), 2)
        self.assertEqual(result, expected)

    def test_calculate_severance(self):
        salary = 1500000
        days_worked = 30
        result = self.calculator.calculate_severance(salary, days_worked)
        expected = round(salary * (days_worked / 360), 2)
        self.assertEqual(result, expected)

    def test_calculate_severance_interest(self):
        severance = 50000
        vacations = 20000
        result = self.calculator.calculate_severance_interest(severance, vacations)
        expected = round((severance + vacations) * 0.12, 2)
        self.assertEqual(result, expected)

    def test_calculate_bonuses(self):
        salary = 1500000
        days_worked = 45
        result = self.calculator.calculate_bonuses(salary, days_worked)
        expected = round(salary * (days_worked / 360), 2)
        self.assertEqual(result, expected)

    def test_calculate_tax_withholding(self):
        income = 5000000
        result = self.calculator.calculate_tax_withholding(income)
        expected = round(income * 0.05, 2)
        self.assertEqual(result, expected)

    def test_calculate_results_test_valid(self):
        base_salary = 1500000
        start_date = "01/01/2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = 0
        results = self.calculator.calculate_results_test(
            base_salary,
            start_date,
            last_vacation_date,
            accumulated_vacation_days
        )
        self.assertEqual(len(results), 7)

    def test_calculate_results_test_invalid_date_format(self):
        base_salary = 1500000
        start_date = "01-01-2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = 0
        with self.assertRaises(ValueError):
            self.calculator.calculate_results_test(
                base_salary,
                start_date,
                last_vacation_date,
                accumulated_vacation_days
            )

    def test_calculate_results_test_negative_salary(self):
        base_salary = -1500000
        start_date = "01/01/2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = 0
        with self.assertRaises(ValueError):
            self.calculator.calculate_results_test(
                base_salary,
                start_date,
                last_vacation_date,
                accumulated_vacation_days
            )

    def test_calculate_results_test_negative_days(self):
        base_salary = 1500000
        start_date = "01/01/2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = -5
        with self.assertRaises(ValueError):
            self.calculator.calculate_results_test(
                base_salary,
                start_date,
                last_vacation_date,
                accumulated_vacation_days
            )

    def test_calculate_vacations_negative_days(self):
        salary = 1500000
        days_worked = -10
        with self.assertRaises(ValueError):
            self.calculator.calculate_vacations(salary, days_worked)

    def test_calculate_severance_negative_days(self):
        salary = 1500000
        days_worked = -10
        with self.assertRaises(ValueError):
            self.calculator.calculate_severance(salary, days_worked)

    def test_calculate_severance_interest_negative_values(self):
        severance = -50000
        vacations = 20000
        with self.assertRaises(ValueError):
            self.calculator.calculate_severance_interest(severance, vacations)

    def test_calculate_bonuses_negative_days(self):
        salary = 1500000
        days_worked = -15
        with self.assertRaises(ValueError):
            self.calculator.calculate_bonuses(salary, days_worked)

    def test_calculate_tax_withholding_negative_income(self):
        income = -5000000
        with self.assertRaises(ValueError):
            self.calculator.calculate_tax_withholding(income)

    def test_calculate_results_test_date_out_of_range(self):
        base_salary = 1500000
        start_date = "01/01/2022"
        last_vacation_date = "32/12/2022"  # Fecha inválida
        accumulated_vacation_days = 0
        with self.assertRaises(ValueError):
            self.calculator.calculate_results_test(
                base_salary,
                start_date,
                last_vacation_date,
                accumulated_vacation_days
            )

    def test_calculate_results_test_zero_years_worked(self):
        base_salary = 1500000
        start_date = "01/01/2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = 0
        results = self.calculator.calculate_results_test(
            base_salary,
            start_date,
            last_vacation_date,
            accumulated_vacation_days
        )
        self.assertEqual(results[0], 0)  # Indemnización debería ser 0 si no se ha trabajado ningún año

    def test_calculate_results_test_zero_days_worked(self):
        base_salary = 1500000
        start_date = "01/01/2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = 0
        results = self.calculator.calculate_results_test(
            base_salary,
            start_date,
            last_vacation_date,
            accumulated_vacation_days
        )
        self.assertEqual(results[1], 0)  # Vacaciones deberían ser 0 si no se ha trabajado ningún día

    def test_calculate_results_test_zero_vacation_days(self):
        base_salary = 1500000
        start_date = "01/01/2022"
        last_vacation_date = "01/01/2023"
        accumulated_vacation_days = 0
        results = self.calculator.calculate_results_test(
            base_salary,
            start_date,
            last_vacation_date,
            accumulated_vacation_days
        )
        self.assertEqual(results[2], 0)  # Cesantías deberían ser 0 si no se ha trabajado ningún día

if __name__ == '__main__':
    unittest.main(verbosity=2)
