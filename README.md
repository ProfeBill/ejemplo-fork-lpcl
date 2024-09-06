# Calculadora-de-Liquidacion-definitiva

El proyecto tiene como objetivo desarrollar una aplicación en Python que permita realizar el cálculo de liquidaciones laborales. Esta herramienta facilita la identificación de los diferentes conceptos que deben abonarse a un trabajador al finalizar su relación contractual, como compensación por despido, vacaciones no disfrutadas, cesantías, intereses de cesantías, prima de servicios y retenciones de impuestos. La aplicación recibe información como el salario base, las fechas de inicio y fin del trabajo, y los días acumulados de vacaciones, para efectuar los cálculos pertinentes conforme a las fórmulas y regulaciones actuales.

# integrantes

Anderson Monsalve Monsalve

Dubin Andres Soto Parodi

## Project Structure

- `src/`
  - `controller/`
    - `controlador.py`: Contains the controller logic that connects the views and the model.
  - `model/`
    - `calculadora.py`: Contains the `LiquidationCalculator` class, which performs the settlement calculations.
  - `view/`
    - `consola.py`: Console interface that allows user interaction.
    - `consolacontrolador.py`: Manages the interaction between the console and the controller.
- `test/`
  - `controllertest.py`: Contains unit tests for the controller.

## Requirements

Make sure you have installed:

- Python 3.8 or higher
- `unittest` (included by default in Python)

## How to Run the Project

### Step 1: Clone the repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/proyecto-liquidacion.git
cd proyecto-liquidacion
