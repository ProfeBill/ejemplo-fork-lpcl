import sys
sys.path.append("src")
from datetime import datetime
import locale
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# Set locale for currency formatting
locale.setlocale(locale.LC_ALL, 'es_CO.UTF-8')  # Ensure this is supported on your system

class SettlementCalculator:
    def calculate_results_test(self, base_salary, start_date, last_vacation_date, accumulated_vacation_days):
        if base_salary < 0 or accumulated_vacation_days < 0:
            raise ValueError("El salario o los días de vacaciones no pueden ser negativos.")
        
        indemnification = base_salary * 0.5
        vacations = base_salary * 0.1
        severance = base_salary * 0.2
        severance_interest = base_salary * 0.05
        bonuses = base_salary * 0.15
        tax_withholding = base_salary * 0.07
        total_payment = indemnification + vacations + severance + severance_interest + bonuses - tax_withholding
        return indemnification, vacations, severance, severance_interest, bonuses, tax_withholding, total_payment

class SettlementApp(App):
    def build(self):
        self.calculator = SettlementCalculator()

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.salary_input = TextInput(hint_text="Salario base (COP)", input_filter='float', multiline=False)
        self.start_date_input = TextInput(hint_text="Fecha de inicio (dd/mm/yyyy)", multiline=False)
        self.last_vacation_date_input = TextInput(hint_text="Fecha última vacación (dd/mm/yyyy)", multiline=False)
        self.vacation_days_input = TextInput(hint_text="Días acumulados de vacaciones", input_filter='int', multiline=False)

        self.layout.add_widget(self.salary_input)
        self.layout.add_widget(self.start_date_input)
        self.layout.add_widget(self.last_vacation_date_input)
        self.layout.add_widget(self.vacation_days_input)

        calculate_button = Button(text="Calcular Liquidación", on_press=self.calculate_settlement)
        self.layout.add_widget(calculate_button)

        self.result_label = Label(text="")
        self.layout.add_widget(self.result_label)

        add_user_button = Button(text="Agregar Usuario", on_press=self.open_add_user_window)
        self.layout.add_widget(add_user_button)

        return self.layout

    def calculate_settlement(self, instance):
        try:
            base_salary = float(self.salary_input.text)
            accumulated_vacation_days = int(self.vacation_days_input.text)
            start_date = datetime.strptime(self.start_date_input.text, "%d/%m/%Y")
            last_vacation_date = datetime.strptime(self.last_vacation_date_input.text, "%d/%m/%Y")

            results = self.calculator.calculate_results_test(base_salary, start_date, last_vacation_date, accumulated_vacation_days)

            # Format results as currency in COP
            formatted_results = [
                locale.currency(result, grouping=True) for result in results
            ]

            self.result_label.text = f"""
            Indemnización: {formatted_results[0]}
            Vacaciones: {formatted_results[1]}
            Cesantías: {formatted_results[2]}
            Interés cesantías: {formatted_results[3]}
            Bonificaciones: {formatted_results[4]}
            Retención de impuestos: {formatted_results[5]}
            Pago total: {formatted_results[6]}
            """
        except ValueError as e:
            self.show_popup("Error de entrada", f"⚠️ Entrada inválida: {e}")
        except Exception as e:
            self.show_popup("Error", f"Ocurrió un error: {e}")

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_label = Label(text=message)
        close_button = Button(text="Cerrar", size_hint_y=None, height=40, on_press=lambda *args: popup.dismiss())
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)
        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.4))
        popup.open()

    def open_add_user_window(self, instance):
        self.user_window = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.entry_name = TextInput(hint_text="Nombre", multiline=False)
        self.entry_last_name = TextInput(hint_text="Apellido", multiline=False)
        self.entry_id = TextInput(hint_text="Documento de identidad", multiline=False)
        self.entry_email = TextInput(hint_text="Email", multiline=False)
        self.entry_phone = TextInput(hint_text="Teléfono", multiline=False)
        self.entry_start_date = TextInput(hint_text="Fecha de inicio (dd/mm/yyyy)", multiline=False)
        self.entry_end_date = TextInput(hint_text="Fecha de fin (dd/mm/yyyy)", multiline=False)
        self.entry_salary = TextInput(hint_text="Salario (COP)", input_filter='float', multiline=False)

        self.user_window.add_widget(self.entry_name)
        self.user_window.add_widget(self.entry_last_name)
        self.user_window.add_widget(self.entry_id)
        self.user_window.add_widget(self.entry_email)
        self.user_window.add_widget(self.entry_phone)
        self.user_window.add_widget(self.entry_start_date)
        self.user_window.add_widget(self.entry_end_date)
        self.user_window.add_widget(self.entry_salary)

        add_button = Button(text="Registrar", on_press=self.add_user)
        self.user_window.add_widget(add_button)

        close_button = Button(text="Cerrar", on_press=lambda *args: user_popup.dismiss())
        self.user_window.add_widget(close_button)

        user_popup = Popup(title="Agregar Usuario", content=self.user_window, size_hint=(0.9, 0.9))
        user_popup.open()

    def add_user(self, instance):
        try:
            name = self.entry_name.text
            last_name = self.entry_last_name.text
            identity_document = self.entry_id.text
            email = self.entry_email.text
            phone = self.entry_phone.text
            start_date = self.entry_start_date.text
            end_date = self.entry_end_date.text
            salary = float(self.entry_salary.text)

            # Add user to list or perform further operations
            self.show_popup("Usuario Agregado", f"✔️ Usuario {name} {last_name} agregado exitosamente.")
        except ValueError:
            self.show_popup("Error", "⚠️ El salario debe ser un número.")

if __name__ == '__main__':
    SettlementApp().run()
