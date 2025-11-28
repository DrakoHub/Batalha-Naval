from tabuleiro import obter_tamanho_tabuleiro, inicializar_tabuleiro, ImprimirTab, alfabeto
from embarcacoes import PortaAvioes, NavioTanque, Contratorpedeiro, Submarino, todas_embarcacoes_afundadas

def posicionar_embarcacoes_teste(tamanho, tabuleiro, embarcacoes_do_jogo):
    if tamanho >= 5:
        # Porta-Aviões (5 posições) - Linha 0, Colunas 0 a 4
        embarcacoes_do_jogo[0].definir_posicao([(0, i) for i in range(5)])
        # Navio-Tanque (4 posições) - Linha 2, Colunas 0 a 3
        embarcacoes_do_jogo[1].definir_posicao([(2, i) for i in range(4)])
        # Contratorpedeiro (3 posições) - Linha 4, Colunas 0 a 2
        embarcacoes_do_jogo[2].definir_posicao([(4, i) for i in range(3)])
        # Submarino (2 posições) - Linha 6, Colunas 0 a 1
        embarcacoes_do_jogo[3].definir_posicao([(6, i) for i in range(2)])

        # Marca as posições das embarcações no tabuleiro para visualização
        for embarcacao in embarcacoes_do_jogo:
            for r, c in embarcacao.posicoes:
                if 0 <= r < tamanho and 0 <= c < tamanho:
                    tabuleiro[r][c] = embarcacao.simbolo
    else:
        print("\nO tamanho da matriz é muito pequeno para posicionar todas as embarcações de teste.")
        print("O jogo continuará sem embarcações posicionadas para focar no loop principal.")
        embarcacoes_do_jogo.clear() # Garante que a lista está vazia

def processar_ataque(coord, tamanho, tabuleiro, embarcacoes_do_jogo):
    
    # 1. Validação e Conversão da Coordenada
    letra_col = coord[0]
    num_linha_str = coord[1:]

    try:
        col_idx = alfabeto.find(letra_col)
        linha_idx = int(num_linha_str) - 1

        if not (0 <= linha_idx < tamanho and 0 <= col_idx < tamanho):
            return False, f"Coordenada fora dos limites! A matriz é {tamanho}x{tamanho}"

    except (ValueError, IndexError):
        return False, "Erro ao processar a coordenada. Tente novamente"

    # 2. Execução do Ataque
    acertou_alguma = False
    mensagem_ataque = "Água" # Mensagem padrão se não acertar nada
    
    for embarcacao in embarcacoes_do_jogo:
        acerto, status = embarcacao.ataque(linha_idx, col_idx)
        
        if acerto:
            acertou_alguma = True
            if status == "Acerto":
                mensagem_ataque = "ACERTOU uma parte do " + embarcacao.nome + "!"
                tabuleiro[linha_idx][col_idx] = "X" # Marca acerto no tabuleiro
                if embarcacao.afundada:
                    mensagem_ataque += f" E AFUNDOU o {embarcacao.nome}!"
                    # Opcional: Mudar o símbolo no tabuleiro para indicar afundamento (ex: 'F')
                    for r, c in embarcacao.posicoes:
                        tabuleiro[r][c] = 'F'
                break # Sai do loop de embarcações, pois já acertou uma
            elif status == "Já Atingido":
                mensagem_ataque = "Você já havia atingido esta parte da embarcação."
                break
    
    # 3. Atualização do Tabuleiro e Mensagem de Água
    if not acertou_alguma:
        # Se não acertou nenhuma embarcação, é água
        if tabuleiro[linha_idx][col_idx] == "~":
            tabuleiro[linha_idx][col_idx] = "O" # Marca erro (água) no tabuleiro
            mensagem_ataque = "Água!"
        elif tabuleiro[linha_idx][col_idx] == "O":
            mensagem_ataque = "Você já atirou nesta posição (Água)."
        else:
            # Caso o símbolo seja de uma embarcação ('P', 'N', 'C', 'S'), mas o ataque não foi registrado
            # Isso pode acontecer se a lógica de posicionamento estiver incorreta
            mensagem_ataque = "Erro de lógica no ataque. Posição já ocupada, mas não registrada."

    return True, mensagem_ataque

def loop_principal_jogo(tamanho, tabuleiro, cabecalhoDasColunas, embarcacoes_do_jogo):
    print("\n--- INÍCIO DO JOGO DE BATALHA NAVAL ---")
    turno = 1
    while not todas_embarcacoes_afundadas(embarcacoes_do_jogo):
        print(f"\n--- TURNO {turno} ---")
        ImprimirTab(tabuleiro, cabecalhoDasColunas)
        
        # Exibe o status das embarcações
        print("\nStatus das Embarcações:")
        for emb in embarcacoes_do_jogo:
            print(f"- {emb}")

        # Coleta a coordenada de ataque do usuário
        while True:
            coord = input("Digite a coordenada de ataque (Ex: A1, B2) ou 'sair' para encerrar:\n").upper()
            if coord == 'SAIR':
                print("Encerrando o jogo a pedido do usuário.")
                return # Sai da função, encerrando o jogo
            
            if len(coord) < 2 or not coord[0].isalpha() or not coord[1:].isdigit():
                print("Coordenada inválida! Formato esperado: LetraNúmero [ex: A1]")
                continue
            
            # Tenta processar o ataque
            sucesso, mensagem = processar_ataque(coord, tamanho, tabuleiro, embarcacoes_do_jogo)
            
            print(f"\nResultado do ataque em {coord}: {mensagem}")
            
            if sucesso:
                break # Coordenada válida e processada, sai do loop de coleta
            else:
                # Se não foi sucesso, a mensagem contém o erro de validação
                print(mensagem)

        turno += 1

    print("\n--- FIM DO JOGO ---")
    print("Parabéns! Todas as embarcações foram afundadas!")
    ImprimirTab(tabuleiro, cabecalhoDasColunas)

if __name__ == "__main__":
    # 1. Inicialização do Tabuleiro
    tamanho = obter_tamanho_tabuleiro()
    tabuleiro, cabecalhoDasColunas = inicializar_tabuleiro(tamanho)

    # 2. Criação das Embarcações
    embarcacoes_do_jogo = [
        PortaAvioes(),
        NavioTanque(),
        Contratorpedeiro(),
        Submarino()
    ]

    # 3. Posicionamento (Simulação)
    posicionar_embarcacoes_teste(tamanho, tabuleiro, embarcacoes_do_jogo)

    # 4. Loop Principal
    if embarcacoes_do_jogo: # Só inicia o loop se houver embarcações
        loop_principal_jogo(tamanho, tabuleiro, cabecalhoDasColunas, embarcacoes_do_jogo)
    else:
        print("Jogo encerrado devido à falta de embarcações para jogar.")
