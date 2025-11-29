import tkinter as tk
from tkinter import messagebox
import numpy as np
from tabuleiro import obter_tamanho_tabuleiro, inicializar_tabuleiro, alfabeto
from embarcacoes import PortaAvioes, NavioTanque, Contratorpedeiro, Submarino, todas_embarcacoes_afundadas
from estatisticas import estatisticas_tabuleiro

class TkinterGameUI:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.root = tk.Tk()
        self.root.title("Batalha Naval")
        self.root.geometry("800x700")
        
        # Inicializar componentes do jogo
        self.tabuleiro, self.cabecalhoDasColunas = inicializar_tabuleiro(tamanho)
        self.embarcacoes_do_jogo = [
            PortaAvioes(),
            NavioTanque(),
            Contratorpedeiro(),
            Submarino()
        ]
        
        # Posicionar embarcações de teste
        self.posicionar_embarcacoes_teste()
        
        # Variáveis de controle
        self.jogo_ativo = True
        self.turno = 1
        
        # Configurar a interface
        self.setup_ui()
        
    def posicionar_embarcacoes_teste(self):
        """Posiciona as embarcações no tabuleiro para teste"""
        if self.tamanho >= 5:
            # Porta-Aviões (5 posições) - Linha 0, Colunas 0 a 4
            self.embarcacoes_do_jogo[0].definir_posicao([(0, i) for i in range(5)])
            # Navio-Tanque (4 posições) - Linha 2, Colunas 0 a 3
            self.embarcacoes_do_jogo[1].definir_posicao([(2, i) for i in range(4)])
            # Contratorpedeiro (3 posições) - Linha 4, Colunas 0 a 2
            self.embarcacoes_do_jogo[2].definir_posicao([(4, i) for i in range(3)])
            # Submarino (2 posições) - Linha 6, Colunas 0 a 1
            self.embarcacoes_do_jogo[3].definir_posicao([(6, i) for i in range(2)])

            # Marca as posições das embarcações no tabuleiro para visualização
            for embarcacao in self.embarcacoes_do_jogo:
                for r, c in embarcacao.posicoes:
                    if 0 <= r < self.tamanho and 0 <= c < self.tamanho:
                        self.tabuleiro[r, c] = embarcacao.simbolo
    
    def setup_ui(self):
        """Configura a interface gráfica"""
        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = tk.Label(main_frame, text="BATALHA NAVAL", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Frame do tabuleiro
        board_frame = tk.Frame(main_frame)
        board_frame.pack(pady=10)
        
        # Criar grade de botões para o tabuleiro
        self.botoes = []
        
        # Cabeçalho das colunas (letras)
        for j in range(self.tamanho + 1):
            if j == 0:
                # Canto superior esquerdo vazio
                empty_label = tk.Label(board_frame, text="", width=3, height=1)
                empty_label.grid(row=0, column=0)
            else:
                col_label = tk.Label(board_frame, text=self.cabecalhoDasColunas[j-1], width=3, height=1, font=("Arial", 10, "bold"))
                col_label.grid(row=0, column=j)
        
        # Criar botões do tabuleiro
        for i in range(self.tamanho):
            row_buttons = []
            
            # Rótulo da linha (número)
            row_label = tk.Label(board_frame, text=str(i+1), width=3, height=1, font=("Arial", 10, "bold"))
            row_label.grid(row=i+1, column=0)
            
            for j in range(self.tamanho):
                btn = tk.Button(
                    board_frame, 
                    text="~", 
                    width=3, 
                    height=1,
                    font=("Arial", 10),
                    command=lambda row=i, col=j: self.handle_click(row, col)
                )
                btn.grid(row=i+1, column=j+1, padx=1, pady=1)
                row_buttons.append(btn)
            
            self.botoes.append(row_buttons)
        
        # Área de mensagens
        self.message_label = tk.Label(main_frame, text="Clique em uma célula para atacar!", font=("Arial", 12), wraplength=600)
        self.message_label.pack(pady=10)
        
        # Frame de informações
        info_frame = tk.Frame(main_frame)
        info_frame.pack(pady=10)
        
        # Informações do turno
        self.turno_label = tk.Label(info_frame, text=f"Turno: {self.turno}", font=("Arial", 12))
        self.turno_label.pack(side=tk.LEFT, padx=20)
        
        # Status das embarcações
        self.embarcacoes_label = tk.Label(info_frame, text=self.get_embarcacoes_status(), font=("Arial", 10), justify=tk.LEFT)
        self.embarcacoes_label.pack(side=tk.LEFT, padx=20)
        
        # Frame de controles
        control_frame = tk.Frame(main_frame)
        control_frame.pack(pady=10)
        
        # Botões de controle
        novo_jogo_btn = tk.Button(control_frame, text="Novo Jogo", command=self.novo_jogo, font=("Arial", 10))
        novo_jogo_btn.pack(side=tk.LEFT, padx=5)
        
        estatisticas_btn = tk.Button(control_frame, text="Estatísticas", command=self.mostrar_estatisticas, font=("Arial", 10))
        estatisticas_btn.pack(side=tk.LEFT, padx=5)
        
        sair_btn = tk.Button(control_frame, text="Sair", command=self.sair, font=("Arial", 10))
        sair_btn.pack(side=tk.LEFT, padx=5)
    
    def get_embarcacoes_status(self):
        """Retorna o status das embarcações como string formatada"""
        status = "Embarcações:\n"
        for emb in self.embarcacoes_do_jogo:
            status += f"- {emb.nome}: {'AFUNDADO' if emb.afundada else 'ATIVO'}\n"
        return status
    
    def handle_click(self, row, col):
        """Processa o clique em uma célula do tabuleiro"""
        if not self.jogo_ativo:
            return
            
        # Verificar se a posição já foi atacada
        if self.tabuleiro[row, col] in ['X', 'O', 'F']:
            self.message_label.config(text="Esta posição já foi atacada!")
            return
        
        # Converter coordenadas para formato de string (ex: A1)
        coord = f"{self.cabecalhoDasColunas[col]}{row+1}"
        
        # Processar ataque
        acertou_alguma = False
        mensagem_ataque = "Água"
        
        for embarcacao in self.embarcacoes_do_jogo:
            acerto, status = embarcacao.ataque(row, col)
            
            if acerto:
                acertou_alguma = True
                if status == "Acerto":
                    mensagem_ataque = f"ACERTOU uma parte do {embarcacao.nome}!"
                    self.tabuleiro[row, col] = "X"
                    self.botoes[row][col].config(text="X", bg="red", fg="white")
                    
                    if embarcacao.afundada:
                        mensagem_ataque += f" E AFUNDOU o {embarcacao.nome}!"
                        # Marcar todas as posições da embarcação como afundada
                        for r, c in embarcacao.posicoes:
                            self.tabuleiro[r, c] = 'F'
                            self.botoes[r][c].config(text="F", bg="darkred", fg="white")
                    break
                elif status == "Já Atingido":
                    mensagem_ataque = "Você já havia atingido esta parte da embarcação."
                    break
        
        # Se não acertou nenhuma embarcação, é água
        if not acertou_alguma:
            if self.tabuleiro[row, col] == "~":
                self.tabuleiro[row, col] = "O"
                self.botoes[row][col].config(text="O", bg="blue", fg="white")
                mensagem_ataque = "Água!"
            else:
                mensagem_ataque = "Erro de lógica no ataque."
        
        # Atualizar interface
        self.message_label.config(text=f"Ataque em {coord}: {mensagem_ataque}")
        self.embarcacoes_label.config(text=self.get_embarcacoes_status())
        
        # Verificar se todas as embarcações foram afundadas
        if todas_embarcacoes_afundadas(self.embarcacoes_do_jogo):
            self.jogo_ativo = False
            self.message_label.config(text=f"PARABÉNS! Você afundou todas as embarcações em {self.turno} turnos!")
            messagebox.showinfo("Fim do Jogo", f"Parabéns! Todas as embarcações foram afundadas em {self.turno} turnos!")
        
        self.turno += 1
        self.turno_label.config(text=f"Turno: {self.turno}")
    
    def mostrar_estatisticas(self):
        """Exibe as estatísticas do jogo"""
        stats = estatisticas_tabuleiro(self.tabuleiro)
        
        estatisticas_texto = (
            f"--- ESTATÍSTICAS DO TABULEIRO ---\n"
            f"Total de posições: {stats['total_posicoes']}\n"
            f"Acertos: {stats['acertos']}\n"
            f"Erros: {stats['erros']}\n"
            f"Posições não atacadas: {stats['nao_atacadas']}\n"
            f"Porcentagem de acertos: {stats['porcentagem_acertos']:.2f}%"
        )
        
        messagebox.showinfo("Estatísticas", estatisticas_texto)
    
    def novo_jogo(self):
        """Reinicia o jogo com um novo tabuleiro"""
        if messagebox.askyesno("Novo Jogo", "Tem certeza que deseja iniciar um novo jogo?"):
            self.tabuleiro, self.cabecalhoDasColunas = inicializar_tabuleiro(self.tamanho)
            self.embarcacoes_do_jogo = [
                PortaAvioes(),
                NavioTanque(),
                Contratorpedeiro(),
                Submarino()
            ]
            self.posicionar_embarcacoes_teste()
            
            # Resetar interface
            for i in range(self.tamanho):
                for j in range(self.tamanho):
                    self.botoes[i][j].config(text="~", bg="SystemButtonFace", fg="black")
            
            self.jogo_ativo = True
            self.turno = 1
            self.turno_label.config(text=f"Turno: {self.turno}")
            self.embarcacoes_label.config(text=self.get_embarcacoes_status())
            self.message_label.config(text="Novo jogo iniciado! Clique em uma célula para atacar.")
    
    def sair(self):
        """Fecha o jogo"""
        if messagebox.askyesno("Sair", "Tem certeza que deseja sair do jogo?"):
            self.root.quit()
    
    def run(self):
        """Inicia a interface gráfica"""
        self.root.mainloop()

if __name__ == "__main__":
    game_ui = TkinterGameUI(10)
    game_ui.run()