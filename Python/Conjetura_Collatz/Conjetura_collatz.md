# Conjetura de Collatz en Python

Este documento explica cómo resolver el problema de la Conjetura de Collatz utilizando Python. Además, incluye una interfaz gráfica con `tkinter` y pruebas unitarias con `unittest`.

## 📄 Enunciado del Problema
Dado un número entero positivo:

- Si es par, se divide entre 2.

- Si es impar, se multiplica por 3 y se suma 1.

- Se repite el proceso hasta que el número llegue a 1.

- Se debe contar la cantidad de pasos necesarios.

### Condicidones especiales

- Si el número es menor o igual a cero, se debe lanzar una excepción `ValueError` con un mensaje descriptivo.

## 💡 Implementación en Python

```py
# collatz.py
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1
    return count
```

## 💻 Interfaz Gráfica con Tkinter

```py
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
```

## 🔧 Pruebas Unitarias con Unittest

```py
# test_collatz.py
import unittest
from collatz import steps

class TestCollatz(unittest.TestCase):
    def test_known_values(self):
        self.assertEqual(steps(1), 0)
        self.assertEqual(steps(2), 1)
        self.assertEqual(steps(3), 7)
        self.assertEqual(steps(12), 9)

    def test_invalid_zero(self):
        with self.assertRaises(ValueError) as cm:
            steps(0)
        self.assertEqual(str(cm.exception), "Only positive integers are allowed")

    def test_negative_number(self):
        with self.assertRaises(ValueError) as cm:
            steps(-5)
        self.assertEqual(str(cm.exception), "Only positive integers are allowed")

if __name__ == '__main__':
    unittest.main()
```

## ▶️ Ejecución del proyecto
- Para ejecutar la interfaz gráfica:

```
python collatz_gui.py
```

- Para correr las pruebas unitarias:

```
python -m unittest test_collatz.py
```

## 🔄 Mejoras posibles

- Visualizar la secuencia completa de la conjetura.

- Guardar el historial de ejecuciones.

- Crear una versión web con Flask o Streamlit.

🌟 Con esto tienes una aplicación completa y funcional para resolver la conjetura de Collatz en Python, con interfaz gráfica y pruebas automáticas.