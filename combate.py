import turnos
import random
from maquina_moore import Saida
from utils import clear

class Combate:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turno = 0

    def executa(self):
        clear()
        while self.player1.vida > 0 and self.player2.vida > 0:
            clear()
            print(f"Turno de: {[self.player1.nome, self.player2.nome][self.turno % 2]}")

            print(f"Vida restante de {self.player1.nome} = {self.player1.vida}")
            print(f"Vida restante de {self.player2.nome} = {self.player2.vida}")
            entrada = input("Qual leitura você deseja fazer? ")

            try:
                self.player1.maquina.faz_transicao(entrada)
                self.player2.maquina.faz_transicao(entrada)
            except:
                print("Entrada inválida")
                input("\nPRESSIONE ENTER PARA CONTINUAR...")
                continue

            if self.turno % 2 == 0:
                saidaPlayer2 = self.player2.maquina.get_saida_atual()
                saidaPlayer1 = self.player1.maquina.get_saida_atual()
            else:
                saidaPlayer1 = self.player1.maquina.get_saida_atual()
                saidaPlayer2 = self.player2.maquina.get_saida_atual()

            if saidaPlayer1 == Saida.DEFESA:
                self.player2.defende()
            if saidaPlayer2 == Saida.DEFESA:
                self.player1.defende()

            if saidaPlayer1 == Saida.ATAQUE:
                self.player1.ataca(self.player2)
            if saidaPlayer2 == Saida.ATAQUE:
                self.player2.ataca(self.player1)

            if saidaPlayer1 == Saida.CURA:
                self.player1.cura()
            if saidaPlayer2 == Saida.CURA:
                self.player2.cura()

            self.turno += 1
            input("Pressione enter para continuar...")

        if self.player1.vida <= 0:
            print(f"{self.player2.nome} Vitorioso!")
        else:
            print(f"{self.player1.nome} Vitorioso!")
