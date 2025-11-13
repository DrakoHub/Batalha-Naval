alfabeto= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Loop da Matriz
while True:
    try:
        tamanho = int(input("Digite o tamanho da Matriz Quadrada, entre 1 a 26:\n"))
        if not 1 <= tamanho <= 26:
                print("Por favor, digite um número entre 1 e 26.")
                continue
        break
    except Error:
        print("Entrada Inválida")
cabecalhoDasColunas = list(alfabeto[:tamanho])
tabuleiro = [["~"] * tamanho for _ in range(tamanho)]

#Imprimir o Tabuleiro
def ImprimirTab():
    print("   ", end="")
    for letra in cabecalhoDasColunas:
        print(f"{letra} ", end="")
    print()
 
    for i, linha in enumerate(tabuleiro):
        print(f"{i + 1:02d} ", end="")
        for celula in linha:
            print(f"{celula} ", end="")
        print()

#Loop de Substituição
while True:
    ImprimirTab()
    Esc1 = input("Agora, Você quer adicionar substituir um valor no Tabuleiro?\n [s/n] \n")
    if Esc1 == "n" or Esc1 == "N":
        print("Encerrando o programa")
        break
    coord = input("Digite a coordenada [Use esse modelo 'A1', 'B2']:")
    if len(coord) < 2:
            print("Coordenada inválida! Formato esperado: LetraNúmero [ex: A1]")
            continue
    letra_col = coord[0]
    num_linha_str = coord[1:]

    if not letra_col.isalpha() or not num_linha_str.isdigit():
        print("Coordenada inválida! Use uma letra seguida de um número")
        continue

    #Encontrando os Indexes assosiados aos numeros e letras
    try:
        col_idx = alfabeto.find(letra_col)
        linha_idx = int(num_linha_str) - 1

        if 0 <= linha_idx < tamanho and 0 <= col_idx < tamanho:
            tabuleiro[linha_idx][col_idx] = "X"
        else:
            print(f"Coordenada fora dos limites! A matriz é {tamanho}x{tamanho}")

    except (ValueError, IndexError):
        print("Erro ao processar a coordenada. Tente novamente")
