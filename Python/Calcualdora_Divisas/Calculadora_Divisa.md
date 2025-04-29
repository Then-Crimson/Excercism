# Calculadora de Divisas en Python (con Interfaz Gráfica)

Esta guía explica paso a paso cómo crear una calculadora de intercambio de divisas usando Python y Tkinter.
## 1. Funciones de Lógica de Divisas
`código en línea`

1.1. `exchange_money(budget, exchange_rate)`
Convierte el presupuesto según la tasa de cambio.

```
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate
```
1.2. `get_change(budget, exchanging_value)`
Calcula el dinero sobrante tras un intercambio.

```
def get_change(budget, exchanging_value):
    return budget - exchanging_value
```

1.3. `get_value_of_bills(denomination, number_of_bills)`
Calcula el valor total de los billetes recibidos.

```
def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
```

1.4. `get_number_of_bills(amount, denomination)`
Determina cuántos billetes completos puedes recibir.

```
def get_number_of_bills(amount, denomination):
    return int(amount // denomination)
```

1.5. `get_leftover_of_bills(amount, denomination)`
Calcula el sobrante que no puede convertirse en billetes.

```
def get_leftover_of_bills(amount, denomination):
    return amount % denomination
```

1.6. `exchangeable_value(budget, exchange_rate, spread, denomination)`
Calcula el valor máximo intercambiable considerando la comisión (spread).

```
def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_rate = exchange_rate + (exchange_rate * spread / 100)
    exchanged_amount = budget / actual_rate
    number_of_bills = int(exchanged_amount // denomination)
    return number_of_bills * denomination
```