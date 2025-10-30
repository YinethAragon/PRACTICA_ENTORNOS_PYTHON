# src/algoritmo_b2.py
import pandas as pd

df = pd.DataFrame({"Producto": ["A", "B", "C"], "Precio": [10, 20, 30]})
print("Promedio de precios:", df["Precio"].mean())
