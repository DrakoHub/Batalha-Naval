# embarcacoes.py

class Embarcacao:
    def __init__(self, nome, tamanho, simbolo):
        self.nome = nome
        self.simbolo = simbolo
        self.tamanho = tamanho
        self.posicoes = []
        # status_posicoes armazena a posição e se foi atingida
        self.status_posicoes = {} 
        self.afundada = False

    def definir_posicao(self, posicoes):
        self.posicoes = posicoes
        # Inicializa o status de todas as posições como não atingidas (False)
        self.status_posicoes = {pos: False for pos in posicoes}

    def ataque(self, linha, coluna):
        posicao_atacada = (linha, coluna)
        
        # Verifica se a posição atacada pertence a esta embarcação
        if posicao_atacada in self.status_posicoes:
            if not self.status_posicoes[posicao_atacada]:
                self.status_posicoes[posicao_atacada] = True
                self.verificar_afundamento()
                return True, "Acerto" 
            return True, "Já Atingido"
        return False, "Erro"

    def verificar_afundamento(self):
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

def todas_embarcacoes_afundadas(lista_embarcacoes):
    return all(embarcacao.afundada for embarcacao in lista_embarcacoes)


