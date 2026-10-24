import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from cria_menu import cria_menu

def exercicio3():
    def calcular_area_retangulo(base, altura):
        if base < 0 or altura < 0:
            raise ValueError("Nem altura nem a base podem ser negativas")
        return base * altura


    value_altura = input("Digite o valor da altura: ")
    valueBase = input("Digite o valor da base: ")

    try:
        print(calcular_area_retangulo(float(valueBase), float(value_altura)))
    except ValueError as erro:
        print(f"Erro: {erro}")


lista = [
    ("Exercicio 3", exercicio3)
]

cria_menu(lista)