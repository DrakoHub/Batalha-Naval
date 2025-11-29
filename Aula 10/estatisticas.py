import numpy as np

# Constantes para os símbolos
SIMBOLO_ACERTO = 'X'
SIMBOLO_ERRO = 'O'
SIMBOLO_NAO_ATACADO = '~'

def contar_total(tabuleiro: np.ndarray) -> int:
    """Retorna o número total de posições do tabuleiro."""
    return tabuleiro.size

def contar_acertos(tabuleiro: np.ndarray) -> int:
    """Retorna o número de acertos (posições marcadas com 'X')."""
    return np.sum(tabuleiro == SIMBOLO_ACERTO)

def contar_erros(tabuleiro: np.ndarray) -> int:
    """Retorna o número de erros (posições marcadas com 'O')."""
    return np.sum(tabuleiro == SIMBOLO_ERRO)

def contar_nao_atacadas(tabuleiro: np.ndarray) -> int:
    """Retorna o número de posições não atacadas ('~')."""
    return np.sum(tabuleiro == SIMBOLO_NAO_ATACADO)

def calcular_porcentagem_acertos(acertos: int, erros: int) -> float:
    """Retorna a porcentagem de acertos considerando apenas as posições jogadas."""
    total_jogadas = acertos + erros
    if total_jogadas == 0:
        return 0.0
    return (acertos / total_jogadas) * 100

def estatisticas_tabuleiro(tabuleiro: np.ndarray) -> dict:
    """
    Calcula e agrupa todas as estatísticas do tabuleiro em um dicionário.
    """
    total = contar_total(tabuleiro)
    acertos = contar_acertos(tabuleiro)
    erros = contar_erros(tabuleiro)
    nao_atacadas = contar_nao_atacadas(tabuleiro)
    porcentagem_acertos = calcular_porcentagem_acertos(acertos, erros)
    
    return {
        "total_posicoes": total,
        "acertos": acertos,
        "erros": erros,
        "nao_atacadas": nao_atacadas,
        "porcentagem_acertos": porcentagem_acertos
    }

def ordenar_posicoes_atacadas(tabuleiro: np.ndarray) -> np.ndarray:
    """
    Localiza, constrói e ordena uma lista de tuplas (linha, coluna) das posições atacadas ('X' ou 'O').
    """
    # Cria uma máscara booleana para as posições atacadas ('X' ou 'O')
    mascara_atacadas = (tabuleiro == SIMBOLO_ACERTO) | (tabuleiro == SIMBOLO_ERRO)
    
    # Usa np.where para obter os índices (linhas e colunas) das posições True na máscara
    linhas, colunas = np.where(mascara_atacadas)
    
    # Combina as linhas e colunas em um array 2D de pares (linha, coluna)
    posicoes_atacadas = np.column_stack((linhas, colunas))
    
    # O np.where já retorna os índices em ordem de linha e depois coluna,
    # mas para garantir a ordenação explícita, podemos usar np.lexsort se necessário.
    # No entanto, np.where já fornece a ordem desejada (leitura linha por linha).
    
    return posicoes_atacadas
