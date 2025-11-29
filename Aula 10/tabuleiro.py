import numpy as np

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def obter_tamanho_tabuleiro():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da Matriz Quadrada, entre 1 a 26:\n"))
            if not 1 <= tamanho <= 26:
                print("Por favor, digite um número entre 1 e 26.")
                continue
            return tamanho
        except ValueError:
            print("Entrada Inválida")

def inicializar_tabuleiro(tamanho):
    cabecalhoDasColunas = list(alfabeto[:tamanho])
    # Modificado para usar np.full para criar um array NumPy
    tabuleiro = np.full((tamanho, tamanho), "~", dtype=str)
    return tabuleiro, cabecalhoDasColunas

def ImprimirTab(tabuleiro_jogo, cabecalho):
    print("   ", end="")
    for letra in cabecalho:
        print(f"{letra} ", end="")
    print()
 
    for i, linha in enumerate(tabuleiro_jogo):
        # Formatação para garantir que o número da linha tenha 2 dígitos (ex: 01, 10)
        print(f"{i + 1:02d} ", end="") 
        # A linha já é um array NumPy, a iteração funciona normalmente
        for celula in linha:
            print(f"{celula} ", end="")
        print()
