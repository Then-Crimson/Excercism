import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Funciones de intercambio
# (se incluyen todas las funciones mencionadas en la sección anterior)

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    return int(amount // denomination)

def get_leftover_of_bills(amount, denomination):
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_rate = exchange_rate + (exchange_rate * spread / 100)
    exchanged_amount = budget / actual_rate
    number_of_bills = int(exchanged_amount // denomination)
    return number_of_bills * denomination

# Tasa de cambio base por moneda (ejemplo estático)
monedas = {
    "Euro (EUR)": 1.1,
    "Dólar (USD)": 1.0,
    "Yen Japonés (JPY)": 0.007,
    "Libra Esterlina (GBP)": 1.3,
    "Peso Mexicano (MXN)": 0.056,
}

# Funciones de interfaz

def calcular():
    try:
        budget = float(entry_budget.get())
        spread = int(entry_spread.get())
        denomination = int(entry_denomination.get())
        moneda = combo_monedas.get()
        exchange_rate = monedas[moneda]

        valor_intercambiable = exchangeable_value(budget, exchange_rate, spread, denomination)
        sobrante = get_leftover_of_bills(exchange_money(budget, exchange_rate + (exchange_rate * spread / 100)), denomination)

        label_resultado.config(text=f"Valor máximo intercambiable: {valor_intercambiable}")
        label_sobrante.config(text=f"Sobrante: {sobrante:.2f}")

    except Exception as e:
        messagebox.showerror("Error", f"Datos inválidos: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Divisas")

# Widgets

# Presupuesto
tk.Label(root, text="Presupuesto (budget):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_budget = tk.Entry(root)
entry_budget.grid(row=0, column=1, padx=5, pady=5)

# Comisión
tk.Label(root, text="Comisión (spread %):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_spread = tk.Entry(root)
entry_spread.grid(row=1, column=1, padx=5, pady=5)

# Denominación
tk.Label(root, text="Denominación del billete:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_denomination = tk.Entry(root)
entry_denomination.grid(row=2, column=1, padx=5, pady=5)

# Selector de Moneda
tk.Label(root, text="Selecciona la moneda:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
combo_monedas = ttk.Combobox(root, values=list(monedas.keys()))
combo_monedas.current(0)
combo_monedas.grid(row=3, column=1, padx=5, pady=5)

# Botón
boton_calcular = tk.Button(root, text="Calcular", command=calcular)
boton_calcular.grid(row=4, column=0, columnspan=2, pady=10)

# Resultado
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=5, column=0, columnspan=2)

label_sobrante = tk.Label(root, text="")
label_sobrante.grid(row=6, column=0, columnspan=2)

# Ejecutar la app
root.mainloop()
