from saida import Saida
import random
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

            saidaPlayer1 = player1.maquina.get_saida_atual()
            saidaPlayer2 = player2.maquina.get_saida_atual()

            if saidaPlayer1.value == Saida.ATAQUE.value:
                player1.ataca(player2)
            elif saidaPlayer1.value == Saida.CURA:
                player1.cura()

            if saidaPlayer2.value == Saida.ATAQUE.value:
                player2.ataca(player1)
            elif saidaPlayer2.value == Saida.CURA.value:
                player2.cura()

            self.turno += 1
            input("Pressione enter para continuar...")
            clear()

        print(f"Vida final de {player1.nome} = {player1.vida}")
        print(f"Vida final de {player2.nome} = {player2.vida}")
        if player1.vida <= 0:
            print(f"{player2.nome} Vitorioso!")
        else:
            print(f"{player1.nome} Vitorioso!")
