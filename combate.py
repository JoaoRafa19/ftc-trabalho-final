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

        # escolhe quem tem prioridade aleatoriamente
        player1 = random.choice([self.player1, self.player2])
        player2 = self.player1 if player1 == self.player2 else self.player2

        print(f"Duelista {player1.nome} tem prioridade!")
        while player1.vida > 0 and player2.vida > 0:
            print(f"Turno de: {[player1.nome, player2.nome][self.turno % 2]}")

            print(f"Vida restante de {player1.nome} = {player1.vida}")
            print(f"Vida restante de {player2.nome} = {player2.vida}")
            entrada = input("Qual leitura você deseja fazer? ")

            try:
                player1.maquina.faz_transicao(entrada)
                player2.maquina.faz_transicao(entrada)
            except Exception as e:
                print("Entrada inválida")
                input("\nPRESSIONE ENTER PARA CONTINUAR...")
                clear()
                continue

            print(f'Alcançou um estado de {player1.maquina.get_saida_atual().value} em {player1.nome}')
            print(f'Alcançou um estado de {player2.maquina.get_saida_atual().value} em {player2.nome}\n')

            if player1.maquina.get_saida_atual() == Saida.ATAQUE:
                player1.ataca(player2)
            elif player1.maquina.get_saida_atual() == Saida.CURA:
                player1.cura()

            if player2.maquina.get_saida_atual() == Saida.ATAQUE:
                player2.ataca(player1)
            elif player2.maquina.get_saida_atual() == Saida.CURA:
                player2.cura()

            self.turno += 1
            input("Pressione enter para continuar...")
            clear()

        if player1.vida <= 0:
            print(f"{player2.nome} Vitorioso!")
        else:
            print(f"{player1.nome} Vitorioso!")
