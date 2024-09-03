

from datetime import datetime

class CalculadoraLiquidacion:
    def calcular_resultados_prueba(self, salario_basico, fecha_inicio_labores, fecha_ultimas_vacaciones, dias_acumulados_vacaciones):
        fecha_inicio = datetime.strptime(fecha_inicio_labores, "%d/%m/%Y")
        fecha_fin = datetime.strptime(fecha_ultimas_vacaciones, "%d/%m/%Y")
        dias_trabajados = (fecha_fin - fecha_inicio).days
        tiempo_trabajado_anos = dias_trabajados / 365
        indemnizacion = round((salario_basico * tiempo_trabajado_anos * 20) / 30, 2)
        vacaciones = round(salario_basico / 30 * dias_acumulados_vacaciones, 2)
        cesantias = round(salario_basico / 30 * dias_trabajados, 2)
        intereses_cesantias = round(cesantias * 0.12, 2)
        prima = round(salario_basico * (dias_trabajados / 180), 2)
        retencion = self.calcular_retencion(salario_basico)
        return indemnizacion, vacaciones, cesantias, intereses_cesantias, prima, retencion, salario_basico

    def calcular_indemnizacion(self, salario, tiempo_trabajado_anos):
        return round(salario * tiempo_trabajado_anos * 20 / 30, 2)

    def calcular_vacaciones(self, salario, dias_acumulados_vacaciones):
        if dias_acumulados_vacaciones < 0:
            raise ValueError("Los días acumulados de vacaciones no pueden ser negativos")
        return round(salario / 30 * dias_acumulados_vacaciones, 2)

    def calcular_cesantias(self, salario_mensual, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días trabajados no pueden ser negativos")
        return round(salario_mensual / 30 * dias_trabajados, 2)

    def calcular_retencion(self, ingreso_laboral):
        if ingreso_laboral < 0:
            raise ValueError("El ingreso laboral no puede ser negativo")
        valor_uvt = 39205
        ingreso_uvt = ingreso_laboral / valor_uvt
        base_uvt = ingreso_uvt - 2300
        return round(base_uvt * 0.39 * valor_uvt + 770 * valor_uvt, 2)

    def calcular_intereses_cesantias(self, cesantias, vacaciones):
        if cesantias < 0 or vacaciones < 0:
            raise ValueError("Cesantías y vacaciones no pueden ser negativos")
        return round((cesantias + vacaciones) * 0.12, 2)

    def calcular_prima(self, salario_mensual, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días trabajados no pueden ser negativos")
        return round(salario_mensual * (dias_trabajados / 180), 2)
