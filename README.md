##  Final Settlement Calculator
The project aims to develop a Python application that allows the calculation of labor settlements. This tool facilitates identifying the different components that must be paid to an employee upon the termination of their contractual relationship, such as severance pay, unused vacation days, severance, severance interest, service bonuses, and tax withholdings. The application receives information such as the base salary, start and end dates of employment, and accumulated vacation days to perform the necessary calculations according to current formulas and regulations.

## Team Members
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

cd src/view

python consola.py

