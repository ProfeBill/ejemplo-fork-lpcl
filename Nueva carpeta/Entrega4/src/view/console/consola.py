from datetime import datetime

class SettlementCalculator:
    def calculate_results_test(self, base_salary, start_date, last_vacation_date, accumulated_vacation_days):
        
        if base_salary < 0:
            raise ValueError("The base salary cannot be negative.")
        if accumulated_vacation_days < 0:
            raise ValueError("Accumulated vacation days cannot be negative.")
        
        
        indemnification = base_salary * 0.5
        vacations = base_salary * 0.1
        severance = base_salary * 0.2
        severance_interest = base_salary * 0.05
        bonuses = base_salary * 0.15
        tax_withholding = base_salary * 0.07
        total_payment = indemnification + vacations + severance + severance_interest + bonuses - tax_withholding
        return indemnification, vacations, severance, severance_interest, bonuses, tax_withholding, total_payment


calculator = SettlementCalculator()

def get_input(prompt, type_func):
    while True:
        try:
            value = type_func(input(prompt))
            if value < 0:
                raise ValueError("The value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


base_salary = get_input("Enter the base salary in Colombian pesos: ", float)
start_date = None
last_vacation_date = None

while start_date is None:
    try:
        start_date = datetime.strptime(input("Enter the start date of employment (dd/mm/yyyy): "), "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in dd/mm/yyyy format.")

while last_vacation_date is None:
    try:
        last_vacation_date = datetime.strptime(input("Enter the date of the last vacation (dd/mm/yyyy): "), "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please enter the date in dd/mm/yyyy format.")

accumulated_vacation_days = get_input("Enter the accumulated vacation days: ", int)

try:
    indemnification, vacations, severance, severance_interest, bonuses, tax_withholding, total_payment = calculator.calculate_results_test(
        base_salary=base_salary,
        start_date=start_date,
        last_vacation_date=last_vacation_date,
        accumulated_vacation_days=accumulated_vacation_days
    )

    print(f"Indemnification: COP {indemnification:,.2f}")
    print(f"Vacations: COP {vacations:,.2f}")
    print(f"Severance: COP {severance:,.2f}")
    print(f"Interest on Severance: COP {severance_interest:,.2f}")
    print(f"Service Bonus: COP {bonuses:,.2f}")
    print(f"Tax Withholding: COP {tax_withholding:,.2f}")
    print(f"Total Payment: COP {total_payment:,.2f}")

except ValueError as e:
    print("Error:", e)
