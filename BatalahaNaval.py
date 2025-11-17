alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Loop da Matriz
while True:
    try:
        tamanho = int(input("Digite o tamanho da Matriz Quadrada, entre 1 a 26:\n"))
        if not 1 <= tamanho <= 26:
            print("Por favor, digite um número entre 1 e 26.")
            continue
        break
    except ValueError:
        print("Entrada Inválida")

cabecalhoDasColunas = list(alfabeto[:tamanho])
tabuleiro = [["~"] * tamanho for _ in range(tamanho)]

# Classe Embarcação
class Embarcacao:
    def __init__(self, nome, tamanho, simbolo):
        self.nome = nome
        self.simbolo = simbolo
        self.tamanho = tamanho
        self.posicoes = []
        # status_posicoes armazena a posição (linha, coluna) e se foi atingida (True/False)
        self.status_posicoes = {} 
        self.afundada = False

    def definir_posicao(self, posicoes):
        """Define as posições da embarcação no tabuleiro."""
        self.posicoes = posicoes
        # Inicializa o status de todas as posições como não atingidas (False)
        self.status_posicoes = {pos: False for pos in posicoes}

    def ataque(self, linha, coluna):
        """Registra um ataque em uma posição e verifica se a embarcação foi afundada."""
        posicao_atacada = (linha, coluna)
        
        # Verifica se a posição atacada pertence a esta embarcação
        if posicao_atacada in self.status_posicoes:
            if not self.status_posicoes[posicao_atacada]:
                # Marca a posição como atingida
                self.status_posicoes[posicao_atacada] = True
                self.verificar_afundamento()
                return True, "Acerto"  # Acerto e era a primeira vez que atingia
            return True, "Já Atingido" # Acerto, mas já havia sido atingido
        return False, "Erro" # Erro, não pertence a esta embarcação

    def verificar_afundamento(self):
        """Verifica se a embarcação foi afundada (todas as posições atingidas)."""
        # Se todos os valores no dicionário status_posicoes forem True, a embarcação afundou
        if all(self.status_posicoes.values()):
            self.afundada = True
            return True
        return False

    def __repr__(self):
        return f"{self.nome} (Tamanho: {self.tamanho}, Afundada: {self.afundada})"

# Classes Embarcações (Subclasses)
class PortaAvioes(Embarcacao):
    def __init__(self):
        super().__init__("Porta-Aviões", 5, "P")

class NavioTanque(Embarcacao):
    def __init__(self):
        super().__init__("Navio-Tanque", 4, "N")

class Contratorpedeiro(Embarcacao):
    def __init__(self):
        super().__init__("Contratorpedeiro", 3, "C")

class Submarino(Embarcacao):
    def __init__(self):
        super().__init__("Submarino", 2, "S")

# Função para verificar se todas as embarcações foram afundadas (Passo 3)
def todas_embarcacoes_afundadas(lista_embarcacoes):
    """Verifica se todas as embarcações na lista foram afundadas."""
    # Retorna True se a lista estiver vazia ou se todas as embarcações estiverem afundadas
    return all(embarcacao.afundada for embarcacao in lista_embarcacoes)

# Imprimir o Tabuleiro
def ImprimirTab(tabuleiro_jogo, cabecalho):
    """Imprime o tabuleiro de jogo."""
    print("   ", end="")
    for letra in cabecalho:
        print(f"{letra} ", end="")
    print()
 
    for i, linha in enumerate(tabuleiro_jogo):
        print(f"{i + 1:02d} ", end="")
        for celula in linha:
            print(f"{celula} ", end="")
        print()

# --- Simulação de Inicialização e Posicionamento (Passo 5 - Inicialização) ---
# Criação dos objetos das embarcações
embarcacoes_do_jogo = [
    PortaAvioes(),
    NavioTanque(),
    Contratorpedeiro(),
    Submarino()
]

# Posicionamento manual para teste (Exemplo: Matriz 10x10)
# As posições são tuplas (linha_idx, coluna_idx)
if tamanho >= 5:
    # Porta-Aviões (5 posições) - Linha 0, Colunas 0 a 4
    embarcacoes_do_jogo[0].definir_posicao([(0, i) for i in range(5)])
    # Navio-Tanque (4 posições) - Linha 2, Colunas 0 a 3
    embarcacoes_do_jogo[1].definir_posicao([(2, i) for i in range(4)])
    # Contratorpedeiro (3 posições) - Linha 4, Colunas 0 a 2
    embarcacoes_do_jogo[2].definir_posicao([(4, i) for i in range(3)])
    # Submarino (2 posições) - Linha 6, Colunas 0 a 1
    embarcacoes_do_jogo[3].definir_posicao([(6, i) for i in range(2)])

    # Marca as posições das embarcações no tabuleiro para visualização (opcional, mas útil para teste)
    for embarcacao in embarcacoes_do_jogo:
        for r, c in embarcacao.posicoes:
            if 0 <= r < tamanho and 0 <= c < tamanho:
                tabuleiro[r][c] = embarcacao.simbolo
else:
    print("\nO tamanho da matriz é muito pequeno para posicionar todas as embarcações de teste.")
    print("O jogo continuará sem embarcações posicionadas para focar no loop principal.")
    embarcacoes_do_jogo = [] # Limpa a lista para o loop principal

# Loop de Jogo Principal (Passo 4)
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
            exit()
        
        if len(coord) < 2:
            print("Coordenada inválida! Formato esperado: LetraNúmero [ex: A1]")
            continue
        
        letra_col = coord[0]
        num_linha_str = coord[1:]

        if not letra_col.isalpha() or not num_linha_str.isdigit():
            print("Coordenada inválida! Use uma letra seguida de um número")
            continue

        try:
            col_idx = alfabeto.find(letra_col)
            linha_idx = int(num_linha_str) - 1

            if 0 <= linha_idx < tamanho and 0 <= col_idx < tamanho:
                break # Coordenada válida, sai do loop de coleta
            else:
                print(f"Coordenada fora dos limites! A matriz é {tamanho}x{tamanho}")

        except (ValueError, IndexError):
            print("Erro ao processar a coordenada. Tente novamente")
            
    # Processa o ataque
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
    
    if not acertou_alguma:
        # Se não acertou nenhuma embarcação, é água
        if tabuleiro[linha_idx][col_idx] == "~":
            tabuleiro[linha_idx][col_idx] = "O" # Marca erro (água) no tabuleiro
            mensagem_ataque = "Água!"
        elif tabuleiro[linha_idx][col_idx] == "O":
            mensagem_ataque = "Você já atirou nesta posição (Água)."
        else:
            # Se for um símbolo de embarcação, mas o ataque não foi registrado (erro de lógica/posicionamento)
            # Isso não deve acontecer com a lógica atual, mas é um bom fallback.
            mensagem_ataque = "Erro de lógica no ataque. Posição já ocupada, mas não registrada."

    print(f"\nResultado do ataque em {coord}: {mensagem_ataque}")
    turno += 1

# Fim do Jogo
print("\n--- FIM DO JOGO ---")
print("Parabéns! Todas as embarcações foram afundadas!")
ImprimirTab(tabuleiro, cabecalhoDasColunas)

