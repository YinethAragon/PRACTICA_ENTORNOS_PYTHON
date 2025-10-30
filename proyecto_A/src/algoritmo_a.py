# src/algoritmo_a.py
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    lista = [10, 20, 30, 40]
    print("Lista:", lista)
    print("Promedio:", calcular_promedio(lista))
