from datetime import datetime

class Usuario:
    def __init__(self, nombre: str, cedula: str, basic_salary: float, accumulated_vacation_days: int, start_date: str, last_vacation_date: str):
        self.nombre = nombre
        self.cedula = cedula
        self.basic_salary = basic_salary
        self.accumulated_vacation_days = accumulated_vacation_days
        self.start_date = start_date
        self.last_vacation_date = last_vacation_date

class LiquidationCalculator:
    UVT_VALUE = 39205
    DIAS_DEL_AÑO = 365
    DIAS_DEL_MES = 30
    DAYS_PER_YEAR = 360
    MAX_MONTHS = 12

    def __init__(self, usuario: Usuario):
        """
        Inicializa el calculador de liquidaciones con el valor de la UVT.
        
        :param uvt_value: Valor de la Unidad de Valor Tributario (UVT), por defecto 39205.
        """
        self.usuario = usuario

    def calculate_test_results(self):
        """
        Calcula los resultados de la liquidación con base en el salario básico y fechas proporcionadas.
        
        :param self.basic_salary: Salario básico mensual del empleado.
        :param start_date: Fecha de inicio del empleo en formato dd/mm/yyyy.
        :param last_vacation_date: Fecha del último período de vacaciones en formato dd/mm/yyyy.
        :param self.accumulated_vacation_days: Días de vacaciones acumulados.
        :return: Un diccionario con los resultados de la liquidación.
        """
        # Validar y convertir los parámetros de entrada
        self.validate_positive_float(self.usuario.basic_salary)
        self.validate_positive_integer(self.usuario.accumulated_vacation_days)
        self.validate_date(self.usuario.start_date)
        self.validate_date(self.usuario.last_vacation_date)
        
        # Calcular días trabajados y años trabajados
        days_worked = (int(self.usuario.last_vacation_date) - int(self.usuario.start_date))
        years_worked = days_worked / LiquidationCalculator.DIAS_DEL_AÑO
        
        # Calcular diferentes componentes de la liquidación
        indemnity = self.calculate_indemnity(self.usuario.basic_salary, years_worked)
        vacations = self.calculate_vacations(self.usuario.basic_salary, days_worked)
        severance = self.calculate_severance(self.usuario.basic_salary, days_worked)
        severance_interest = self.calculate_severance_interest(severance, self.usuario.accumulated_vacation_days)
        bonuses = self.calculate_bonus(self.usuario.basic_salary, days_worked)
        tax_retention = self.calculate_tax_retention(indemnity + vacations + severance + severance_interest + bonuses)
        
        # Calcular el total a pagar después de la retención de impuestos
        total_to_pay = indemnity + vacations + severance + severance_interest + bonuses - tax_retention
        
        return {
            "indemnity": indemnity,
            "vacations": vacations,
            "severance": severance,
            "severance_interest": severance_interest,
            "bonuses": bonuses,
            "tax_retention": tax_retention,
            "total_to_pay": total_to_pay
        }

    def validate_date(self, str_date):
        """
        Valida y convierte una cadena de fecha en un objeto datetime.
        
        :param date_str: Fecha en formato dd/mm/yyyy.
        :return: Objeto datetime.
        :raises ValueError: Si el formato de la fecha es inválido.
        """
        try:
            return datetime.strptime(str_date, "%d/%m/%Y")
        except ValueError:
            raise ValueError("Invalid date format. Please use dd/mm/yyyy.")

    def validate_positive_float(self, value_str):
        """
        Valida y convierte una cadena a un número flotante positivo.
        
        :param value_str: Cadena a convertir.
        :return: Número flotante positivo.
        :raises ValueError: Si la conversión falla o el número es negativo.
        """
        try:
            value = float(value_str)
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError:
            raise ValueError("Invalid number. Please enter a non-negative numeric value.")

    def validate_positive_integer(self, value_str):
        """
        Valida y convierte una cadena a un número entero positivo.
        
        :param value_str: Cadena a convertir.
        :return: Número entero positivo.
        :raises ValueError: Si la conversión falla o el número es negativo.
        """
        try:
            value = int(value_str)
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError:
            raise ValueError("Invalid integer. Please enter a non-negative integer value.")

    def calculate_indemnity(self, years_worked):
        """
        Calcula la indemnización por despido con base en el salario y los años trabajados.
        
        :param self.basic_salary: Salario básico mensual.
        :param years_worked: Años trabajados.
        :return: Indemnización calculada.
        """
        max_days = LiquidationCalculator.MAX_MONTHS * LiquidationCalculator.DAYS_PER_YEAR
        indemnity_days = min(years_worked * LiquidationCalculator.DAYS_PER_YEAR, max_days)
        indemnity = (self.usuario.basic_salary * indemnity_days) / LiquidationCalculator.DIAS_DEL_MES
        return indemnity

    def calculate_vacations(self, monthly_salary, days_worked):
        """
        Calcula el valor de las vacaciones no disfrutadas.
        
        :param monthly_salary: Salario mensual.
        :param days_worked: Días trabajados.
        :return: Valor de las vacaciones calculado.
        :raises ValueError: Si los días trabajados son negativos.
        """
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        vacation_value = (monthly_salary * days_worked) / (LiquidationCalculator.DAYS_PER_YEAR*2)
        return vacation_value

    def calculate_severance(self, monthly_salary, days_worked):
        """
        Calcula la cesantía acumulada.
        
        :param monthly_salary: Salario mensual.
        :param days_worked: Días trabajados.
        :return: Valor de la cesantía calculada.
        :raises ValueError: Si los días trabajados son negativos.
        """
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        severance = (monthly_salary * days_worked) / LiquidationCalculator.DAYS_PER_YEAR
        return severance

    def calculate_severance_interest(self, severance, days_worked):
        """
        Calcula el interés sobre la cesantía.
        
        :param severance: Monto de la cesantía.
        :param days_worked: Días trabajados.
        :return: Interés sobre la cesantía calculado.
        :raises ValueError: Si el monto de cesantía o los días trabajados son negativos.
        """
        if severance < 0:
            raise ValueError("Severance amount cannot be negative")
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        severance_interest = (severance * days_worked * 0.12) / LiquidationCalculator.DAYS_PER_YEAR
        return severance_interest

    def calculate_bonus(self, monthly_salary, days_worked):
        """
        Calcula el bono proporcional.
        
        :param monthly_salary: Salario mensual.
        :param days_worked: Días trabajados.
        :return: Bono calculado.
        :raises ValueError: Si los días trabajados son negativos.
        """
        if days_worked < 0:
            raise ValueError("Days worked cannot be negative")
        bonus = monthly_salary * (days_worked / LiquidationCalculator.DAYS_PER_YEAR)
        return bonus

    def calculate_tax_retention(self, total_income):
        """
        Calcula la retención en la fuente sobre el total de ingresos.
        
        :param total_income: Ingresos totales.
        :return: Retención calculada.
        :raises ValueError: Si el ingreso total no es un número.
        """
        if not isinstance(total_income, (int, float)):
            raise ValueError("Total income must be a number")
        retention = 0
        total_income = float(total_income)
        income_uvt = total_income / self.uvt_value

        # Cálculo de la retención según la base gravable en UVT
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
        
        return retention
