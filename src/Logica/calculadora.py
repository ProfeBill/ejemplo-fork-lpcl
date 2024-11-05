from datetime import datetime
import math

class Usuario:
    def __init__(self, nombre: str, cedula: str, motivo_finalizacion: str, salario_basico: float, fecha_inicio: str, fecha_ultimo_vacaciones: str):
        self.nombre = nombre
        self.cedula = cedula
        self.motiivo_finalizacion = motivo_finalizacion
        self.salario_basico = salario_basico
        self.fecha_inicio = fecha_inicio
        self.fecha_ultimo_vacaciones = fecha_ultimo_vacaciones
        self.dias_vacaciones_acumulados = 0

class ErrorDiasAcumulados(Exception):
    pass

class ErrorFecha(Exception):
    pass

class FloatError(Exception):
    pass

class EnteroError(Exception):
    pass

class ErrorDiasTrabajados(Exception):
    pass

class ErrorCesantia(Exception):
    pass

class CalculadorLiquidacion:
    DIAS_DEL_MES = 30
    DIAS_POR_AÑO = 360
    MESES_MAXIMOS = 12
    VACACIONES = 720 # se utiliza en razón a que matemáticamente representan los 15 días de vacaciones por cada 360 días trabajados.
    TASA_INTERES = 12 #Esta tasa está definida por ley y corresponde a una compensación anual por las cesantías acumuladas.
    DIAS_VACACIONES = 15 #La ley colombiana establece 15 días hábiles de vacaciones anuales.
    DIAS_POR_AÑO_ADICIONAL = 20 #Para cada año adicional después del primero, el empleador debe pagar 20 días de salario por año completo o fracción de año.
    RETENCION = 10 #Para simplificar este cálculo y no conocer los descuentos exactos de ley asumiremos que su salario está sujeto a una retención aproximada del 10%.

    def __init__(self, usuario: Usuario):
        """
        Metodo __init__ para definir la variable usuario que es un objeto de tipo Usuario
        """
        self.usuario = usuario

    def calcular_resultados(self) -> dict:
        """
        Calcula los resultados de la liquidación con base en el salario básico y fechas proporcionadas.

        :return: Un diccionario con los resultados de la liquidación.
        """
        # Validar y convertir los parámetros de entrada
        self.validar_float_positivo(self.usuario.salario_basico)
        self.validar_entero_positivo(self.usuario.dias_vacaciones_acumulados)
        self.validar_fecha(self.usuario.fecha_inicio)
        self.validar_fecha(self.usuario.fecha_ultimo_vacaciones)
        
        # Calcular días trabajados y años trabajados
        dias_trabajados = (self.validar_fecha(self.usuario.fecha_ultimo_vacaciones) - self.validar_fecha(self.usuario.fecha_inicio)).days
        anos_trabajados = dias_trabajados / CalculadorLiquidacion.DIAS_POR_AÑO
        
        # Calcular diferentes componentes de la liquidación
        indemnizacion = self.calcular_indemnizacion(anos_trabajados)
        vacaciones = self.calcular_vacaciones(dias_trabajados)
        cesantia = self.calcular_cesantia(dias_trabajados)
        intereses_cesantia = self.calcular_intereses_cesantia(cesantia, dias_trabajados)
        bonos = self.calcular_bono(dias_trabajados)
        retencion_impuesto = self.calcular_retencion_impuesto(cesantia, intereses_cesantia, bonos, vacaciones)
        
        # Calcular el total a pagar después de la retención de impuestos
        total_a_pagar = indemnizacion + vacaciones + cesantia + intereses_cesantia + bonos - retencion_impuesto
        
        return {
            "indemnizacion": indemnizacion,
            "vacaciones": vacaciones,
            "cesantia": cesantia,
            "bonos": bonos,
            "intereses_cesantia": intereses_cesantia,
            "retencion_impuesto": retencion_impuesto,
            "total_a_pagar": total_a_pagar
        }

    def validar_fecha(self, str_fecha):
        """
        Valida y convierte una cadena de fecha en un objeto datetime.
        
        :param str_fecha: Fecha en formato dd/mm/yyyy.
        :return: Objeto datetime.
        :raises ValueError: Si el formato de la fecha es inválido.
        """
        try:
            return datetime.strptime(str_fecha, "%d/%m/%Y")
        except:
            raise ErrorFecha(f"Formato de fecha inválido. Por favor use dd/mm/yyyy.")

    def validar_float_positivo(self, valor_str):
        """
        Valida y convierte una cadena a un número flotante positivo.
        
        :param valor_str: Cadena a convertir.
        :return: Número flotante positivo.
        :raises ValueError: Si la conversión falla o el número es negativo.
        """
        try:
            valor = float(valor_str)
            if valor < 0:
                raise FloatError(f"Error el valor no puede ser negativo.")
            return valor
        except:
            raise FloatError(f"Número inválido. El valor ingresado es {valor}. Por favor ingrese un valor numérico no negativo.")
        
    def validar_entero_positivo(self, valor_str):
        """
        Valida y convierte una cadena a un número flotante positivo.
        
        :param valor_str: Cadena a convertir.
        :return: Número flotante positivo.
        :raises ValueError: Si la conversión falla o el número es negativo.
        """
        try:
            valor = int(valor_str)
            if valor < 0:
                raise EnteroError(f"Error el valor no puede ser negativo.")
            return valor
        except:
            raise EnteroError(f"Número inválido. El valor ingresado es {valor}. Por favor ingrese un valor numérico no negativo.")


    def calcular_indemnizacion(self, anos_trabajados):
        """
        Calcula la indemnización por despido con base en el salario y los años trabajados.
        
        :param anos_trabajados: Años trabajados.
        :return: Indemnización calculada.
        """
        if self.usuario.motiivo_finalizacion.upper() == "RENUNCIA":
            indemnizacion = 0
            return indemnizacion
     
        if anos_trabajados < 1:
            indemnizacion = self.usuario.salario_basico

        parte_entera_minima = math.floor(anos_trabajados)
        parte_entera_maxima = math.ceil(anos_trabajados)

        if parte_entera_maxima > parte_entera_minima and parte_entera_minima > 1:
            diferencia = parte_entera_maxima - parte_entera_maxima
            fraccion_del_año = 0
            if diferencia == 1:
                fraccion_del_año = CalculadorLiquidacion.DIAS_POR_AÑO_ADICIONAL
            indemnizacion = self.usuario.salario_basico + ((((CalculadorLiquidacion.DIAS_POR_AÑO_ADICIONAL * parte_entera_minima)+ fraccion_del_año)*self.usuario.salario_basico/CalculadorLiquidacion.DIAS_DEL_MES))
        return indemnizacion

    def calcular_vacaciones(self, dias_trabajados):
        """
        Calcula el valor de las vacaciones no disfrutadas.
        
        :param dias_trabajados: Días trabajados.
        :return: Valor de las vacaciones calculado.
        :raises ValueError: Si los días trabajados son negativos.
        """
        if dias_trabajados < 0:
            raise ErrorDiasTrabajados(f"Erorr Los días trabajados no pueden ser negativos. Los dias trabajados son: {dias_trabajados}.")
        valor_vacaciones = self.usuario.salario_basico * (CalculadorLiquidacion.DIAS_VACACIONES/CalculadorLiquidacion.DIAS_POR_AÑO)
        return valor_vacaciones

    def calcular_cesantia(self, dias_trabajados):
        """
        Calcula la cesantía acumulada.
        
        :param dias_trabajados: Días trabajados.
        :return: Valor de la cesantía calculada.
        :raises ValueError: Si los días trabajados son negativos.
        """
        if dias_trabajados < 0:
            raise ErrorDiasTrabajados(f"Erorr Los días trabajados no pueden ser negativos. Los dias trabajados son: {dias_trabajados}.")
        cesantia = self.usuario.salario_basico * (dias_trabajados / CalculadorLiquidacion.DIAS_POR_AÑO)
        return cesantia

    def calcular_intereses_cesantia(self, cesantia, dias_trabajados):
        """
        Calcula el interés sobre la cesantía.
        
        :param cesantia: Monto de la cesantía.
        :param dias_trabajados: Días trabajados.
        :return: Interés sobre la cesantía calculado.
        :raises ValueError: Si el monto de cesantía o los días trabajados son negativos.
        """
        if cesantia < 0:
            raise ErrorCesantia(f"Error el monto de cesantía no puede ser negativo. El monto actual es: {cesantia}")
        if dias_trabajados < 0:
            raise ErrorDiasTrabajados(f"Erorr Los días trabajados no pueden ser negativos. Los dias trabajados son: {dias_trabajados}.")
        intereses_cesantia = cesantia * (CalculadorLiquidacion.TASA_INTERES/100)
        return intereses_cesantia

    def calcular_bono(self, dias_trabajados):
        """
        Calcula el bono proporcional.
        
        :param dias_trabajados: Días trabajados.
        :return: Bono calculado.
        :raises ValueError: Si los días trabajados son negativos.
        """
        if dias_trabajados < 0:
            raise ErrorDiasTrabajados(f"Erorr Los días trabajados no pueden ser negativos. Los dias trabajados son: {dias_trabajados}.")
        bono = self.usuario.salario_basico * (dias_trabajados / CalculadorLiquidacion.DIAS_POR_AÑO)
        return bono

    def calcular_retencion_impuesto(self, cesantias, intereses_cesantias, prima, vacaciones):
        """
        Calcula la retención en la fuente sobre el total de ingresos.
        
        :param ingreso_total: Ingresos totales.
        :return: Retención calculada.
        :raises ValueError: Si el ingreso total no es un número.
        """
        retencion = (cesantias + intereses_cesantias + prima + vacaciones)*(CalculadorLiquidacion.RETENCION/100) 
        return retencion



    def dias_de_vacacones_acumulados(self):
        fecha_actual  = datetime.now().date()
        self.usuario.dias_vacaciones_acumulados = fecha_actual - self.usuario.fecha_ultimo_vacaciones
        if self.usuario.dias_vacaciones_acumulados < 0:
            raise ErrorDiasAcumulados(f"Los dias acumulados tienen que ser mayor o igual a 0.")
        return