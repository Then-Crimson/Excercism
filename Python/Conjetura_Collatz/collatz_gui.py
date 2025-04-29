# collatz_gui.py
import tkinter as tk
from tkinter import messagebox
from collatz import steps

def calcular_collatz():
    try:
        numero = int(entry.get())
        resultado = steps(numero)
        label_resultado.config(text=f"Pasos necesarios: {resultado}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception:
        messagebox.showerror("Error", "Ingresa un número entero válido.")

root = tk.Tk()
root.title("Conjetura de Collatz")

tk.Label(root, text="Ingresa un número entero positivo:").pack(pady=10)
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calcular", command=calcular_collatz).pack(pady=10)

label_resultado = tk.Label(root, text="")
label_resultado.pack()

root.mainloop()
