from datetime import datetime

class LiquidacionCalculator:
    def __init__(self, uvt_value=39205):
        self.uvt_value = uvt_value

    def calcular_liquidacion(self, salario, fecha_inicio, fecha_fin, vacaciones_pendientes):
        # Cálculo de días trabajados
        start_date = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        end_date = datetime.strptime(fecha_fin, "%d/%m/%Y")
        dias_totales = (end_date - start_date).days
        años_trabajados = dias_totales / 365

        # Cálculo de cada componente
        indemnizacion = self.calcular_indemnizacion(salario, años_trabajados)
        vacaciones = self.calcular_vacaciones(salario, dias_totales)
        cesantias = self.calcular_cesantias(salario, dias_totales)
        intereses_cesantias = self.calcular_intereses_cesantias(cesantias, vacaciones_pendientes)
        prima = self.calcular_prima(salario, dias_totales)
        retencion = self.calcular_retencion_total(indemnizacion + vacaciones + cesantias + intereses_cesantias + prima)

        total_pagar = indemnizacion + vacaciones + cesantias + intereses_cesantias + prima - retencion

        return indemnizacion, vacaciones, cesantias, intereses_cesantias, prima, retencion, total_pagar

    def calcular_indemnizacion(self, salario, años_trabajados):
        dias_indemnizacion_max = 12 * 20
        dias_indemnizacion = min(años_trabajados * 20, dias_indemnizacion_max)
        return round((salario * dias_indemnizacion) / 30, 2)

    def calcular_vacaciones(self, salario, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días trabajados no pueden ser negativos")
        return round((salario * dias_trabajados) / 720, 2)

    def calcular_cesantias(self, salario, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días trabajados no pueden ser negativos")
        return round((salario * dias_trabajados) / 360, 2)

    def calcular_intereses_cesantias(self, cesantias, dias_vacaciones):
        if cesantias < 0 or dias_vacaciones < 0:
            raise ValueError("Las cesantías o los días de vacaciones no pueden ser negativos")
        return round((cesantias * dias_vacaciones * 0.12) / 360, 2)

    def calcular_prima(self, salario, dias_trabajados):
        if dias_trabajados < 0:
            raise ValueError("Los días trabajados no pueden ser negativos")
        return round(salario * (dias_trabajados / 360), 2)

    def calcular_retencion_total(self, ingreso_total):
        if not isinstance(ingreso_total, (int, float)):
            raise ValueError("El ingreso total debe ser numérico")
        retencion = 0
        ingreso_en_uvt = ingreso_total / self.uvt_value

        if ingreso_en_uvt <= 95:
            return retencion
        elif ingreso_en_uvt <= 150:
            base = ingreso_en_uvt - 95
            retencion = base * 0.19 * self.uvt_value
        elif ingreso_en_uvt <= 360:
            base = ingreso_en_uvt - 150
            retencion = base * 0.28 * self.uvt_value + 10 * self.uvt_value
        elif ingreso_en_uvt <= 640:
            base = ingreso_en_uvt - 360
            retencion = base * 0.33 * self.uvt_value + 69 * self.uvt_value
        elif ingreso_en_uvt <= 945:
            base = ingreso_en_uvt - 640
            retencion = base * 0.35 * self.uvt_value + 162 * self.uvt_value
        elif ingreso_en_uvt <= 2300:
            base = ingreso_en_uvt - 945
            retencion = base * 0.37 * self.uvt_value + 268 * self.uvt_value
        else:
            base = ingreso_en_uvt - 2300
            retencion = base * 0.39 * self.uvt_value + 770 * self.uvt_value
        
        return round(retencion, 2)