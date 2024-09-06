from datetime import datetime

class LiquidationCalculator:
    def __init__(self, uvt_value=39205):
        self.uvt_value = uvt_value

    def calculate_test_results(self, basic_salary, start_date, last_vacation_date, accumulated_vacation_days):
        # Validar entradas
        basic_salary = self.validate_positive_float(basic_salary)
        accumulated_vacation_days = self.validate_positive_integer(accumulated_vacation_days)
        start_date = self.validate_date(start_date)
        last_vacation_date = self.validate_date(last_vacation_date)
        
        # Calcular días trabajados y años trabajados
        days_worked = (last_vacation_date - start_date).days
        years_worked = days_worked / 365
        
        # Realizar cálculos
        indemnity = self.calculate_indemnity(basic_salary, years_worked)
        vacations = self.calculate_vacations(basic_salary, days_worked)
        severance = self.calculate_severance(basic_salary, days_worked)
        severance_interest = self.calculate_severance_interest(severance, accumulated_vacation_days)
        bonuses = self.calculate_bonus(basic_salary, days_worked)
        tax_retention = self.calculate_tax_retention(indemnity + vacations + severance + severance_interest + bonuses)
        total_to_pay = indemnity + vacations + severance + severance_interest + bonuses - tax_retention
        
        # Retornar todos los valores calculados
        return {
            "indemnity": indemnity,
            "vacations": vacations,
            "severance": severance,
            "severance_interest": severance_interest,
            "bonuses": bonuses,
            "tax_retention": tax_retention,
            "total_to_pay": total_to_pay
        }

    # Validar fecha en formato 'dd/mm/yyyy'
    def validate_date(self, date_str):
        try:
            return datetime.strptime(date_str, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use dd/mm/yyyy.")

    # Validar que el valor sea un flotante positivo
    def validate_positive_float(self, value_str):
        try:
            value = float(value_str)
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError:
            raise ValueError("Invalid number. Please enter a non-negative numeric value.")

    # Validar que el valor sea un entero positivo
    def validate_positive_integer(self, value_str):
        try:
            value = int(value_str)
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError:
            raise ValueError("Invalid integer. Please enter a non-negative integer value.")

    # Cálculo de indemnización
    def calculate_indemnity(self, basic_salary, years_worked):
        days_per_year = 360
        max_months = 12
        max_days = max_months * days_per_year
        indemnity_days = min(years_worked * days_per_year, max_days)
        indemnity = (basic_salary * indemnity_days) / 30
        return round(indemnity, 2)

    # Cálculo de vacaciones
    def calculate_vacations(self, monthly_salary, days_worked):
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        vacation_value = (monthly_salary * days_worked) / 720
        return round(vacation_value, 2)

    # Cálculo de cesantías
    def calculate_severance(self, monthly_salary, days_worked):
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        severance = (monthly_salary * days_worked) / 360
        return round(severance, 2)

    # Cálculo del interés sobre las cesantías
    def calculate_severance_interest(self, severance, days_worked):
        if severance < 0:
            raise ValueError("Severance amount cannot be negative")
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        severance_interest = (severance * days_worked * 0.12) / 360
        return round(severance_interest, 2)

    # Cálculo de primas
    def calculate_bonus(self, monthly_salary, days_worked):
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        bonus = monthly_salary * (days_worked / 360)
        return round(bonus, 2)

    # Cálculo de retención en la fuente
    def calculate_tax_retention(self, total_income):
        if not isinstance(total_income, (int, float)):
            raise ValueError("Total income must be a number")
        retention = 0
        total_income = float(total_income)
        income_uvt = total_income / self.uvt_value

        if income_uvt <= 95:
            pass
        elif income_uvt <= 150:
            base_uvt = income_uvt - 95
            retention = base_uvt * 0.19 * self.uvt_value
        elif income_uvt <= 360:
            base_uvt = income_uvt - 150
            retention = base_uvt * 0.28 * self.uvt_value + 10 * self.uvt_value
        elif income_uvt <= 640:
            base_uvt = income_uvt - 360
            retention = base_uvt * 0.33 * self.uvt_value + 69 * self.uvt_value
        elif income_uvt <= 945:
            base_uvt = income_uvt - 640
            retention = base_uvt * 0.35 * self.uvt_value + 162 * self.uvt_value
        elif income_uvt <= 2300:
            base_uvt = income_uvt - 945
            retention = base_uvt * 0.37 * self.uvt_value + 268 * self.uvt_value
        else:
            base_uvt = income_uvt - 2300
            retention = base_uvt * 0.39 * self.uvt_value + 770 * self.uvt_value
        
        return round(retention, 2)
