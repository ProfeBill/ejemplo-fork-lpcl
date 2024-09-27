import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def connect_db():
    return None


def add_user(first_name, last_name, id_number, email, phone, start_date, end_date, salary):
    return None


def add_settlement(indemnity, vacation, severance, severance_interest, service_bonus, tax_withholding, total_payment, user_id):
    return None


def consult_user(user_id):
    print("Simulation: User not found.")
    return None


def delete_user(user_id):
    print("Simulation: User not found.")
    return None


def delete_settlement(user_id):
    print("Simulation: No settlement data found for the user.")
    return None
