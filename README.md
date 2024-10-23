## Calculadora de Liquidaciones Finales
El proyecto tiene como objetivo desarrollar una aplicación en Python que permita calcular liquidaciones laborales. Esta herramienta facilita la identificación de los diferentes componentes que deben ser pagados a un empleado al finalizar su relación contractual, como indemnización, días de vacaciones no utilizados, intereses de liquidación, bonos por servicio y retenciones fiscales. La aplicación recibe información como el salario base, las fechas de inicio y fin del empleo, y los días de vacaciones acumulados para realizar los cálculos necesarios de acuerdo con las fórmulas y regulaciones actuales.

## Miembros del Equipo
Anderson Monsalve Monsalve

Dubin Andrés Soto Parodi

## Estructura del Proyecto

- `src/`
  - `controller/`
    - `controlador.py`: Contiene la lógica del controlador que conecta las vistas y el modelo.
  - `model/`
    - `calculadora.py`: Contiene la clase `LiquidationCalculator`, que realiza los cálculos de liquidación.
  - `Gui/`
    - `kivy_test.py`: Es donde se encuentra la interfaz de nuestro programa.
  - `view/`
    - `consola.py`: Interfaz de consola que permite la interacción del usuario.
    - `consolacontrolador.py`: Gestiona la interacción entre la consola y el controlador.
- `test/`
  - `controllertest.py`: Contiene pruebas unitarias para el controlador.

## Requisitos

Asegúrate de tener instalado:

- Python 3.8 o superior
- `unittest` (incluido por defecto en Python)

## Cómo Ejecutar el Proyecto

### Paso 1: Clonar el repositorio

Clona este repositorio en tu máquina local usando Git:

```bash
git clone https://github.com/tu-usuario/proyecto-liquidacion.git
cd proyecto-liquidacion

cd src/view

python consola.py

python -m unittest test.controllertest

python src/view/consolacontrolador.py
python src/model/Gui/kivy_test.py
```

### Paso 2: Cómo operar la consola y el controlador

Primero ejecuta `consola.py`, que se encuentra en la carpeta `src/view`. Este mismo proceso se realiza con la carpeta `src/view/consolacontrolador.py`.

### Paso 3: Para que Kivy funcione

Lo primero que debes hacer es instalar Kivy y, una vez hecho esto, haz clic en Ejecutar y la calculadora aparecerá con la interfaz gráfica. Para verla correctamente, colócala en la pestaña grande. La carpeta para ejecutar se encuentra en la GUI, con el nombre `kivy_test.py`. Ahí se ejecutará.