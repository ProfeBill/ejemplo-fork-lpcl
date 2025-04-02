## Calculadora de Liquidaciones Finales
El proyecto tiene como objetivo desarrollar una aplicación en Python que permita calcular liquidaciones laborales. Esta herramienta facilita la identificación de los diferentes componentes que deben ser pagados a un empleado al finalizar su relación contractual, como indemnización, días de vacaciones no utilizados, intereses de liquidación, bonos por servicio y retenciones fiscales. La aplicación recibe información como el salario base, las fechas de inicio y fin del empleo, y los días de vacaciones acumulados para realizar los cálculos necesarios de acuerdo con las fórmulas y regulaciones actuales.

## Miembros del Equipo
Anderson Monsalve Monsalve
Dubin Andrés Soto Parodi

Modificado por :
William Velasquez

## Editado por:
Juan Diego Gomez - Juan Diego Usuga

## Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior
- `unittest` (incluido por defecto en Python)

## Cómo Ejecutar el Proyecto

### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local usando Git:
```markdown
https://github.com/JuanPyC/Calculadora-de-Liquidacion-definitiva

```
### Paso 4: Cómo configurar el archivo SecretConfig.py:
Datos secretos que no deben publicarse en el repositorio

Diligencie estos datos y guarde un archivo como SecretConfig.py en la raiz del proyecto
para poder ejecutar la aplicación de manera correcta

#### El Archivo debe de contener lo siguiente:
PGDATABASE = "ESCRIBA EL NOMBRE DE LA BASE DE DATOS"
PGUSER = "ESCRIBA EL USUARIO DE LA DB"
PGPASSWORD = "ESCRIBA LA CONSTRASEÑA"
PGHOST = "ESCRIBA LA DIRECCION DNS O DIRECCION IP DEL SERVIDOR"
PGPORT = 5432 # POR DEFECTO ES 5432, PERO PUEDE CAMBIAR EN SU DB

### Paso 3: Cómo correr las pruebas unitarias:
```markdown
python test/testcontroller.py
```

### Paso 4: Cómo operar la consola de la BD:
```markdown
python src/Consola/Consola_Base_de_datos.py
```