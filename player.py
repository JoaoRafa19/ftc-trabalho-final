import random
from maquina_moore import Saida


class Player:
    def __init__(self, maquina , nome):
        self.nome = nome
        self.maquina = maquina
        self.vida = 100

    def ataca(self, player):
        if self.vida <= 0:
            return
        dano = random.randint(1, 33)
        print(f"Ataque do duelista {self.nome}: {dano}!")
        if player.maquina.get_saida_atual() == Saida.DEFESA:
            aparagem = int(random.random() * dano)
            dano -= aparagem
            print(f"Aparagem do duelista {player.nome}: {aparagem}!")

        print(f"Dano no duelista {player.nome}: {dano}")
        player.vida -= dano

    def cura(self):
        if self.vida <= 0:
            return
        valor = random.randint(1, 15)
        vida_total = self.vida + valor

        print(f"Cura no duelista {self.nome}: {valor}")
        if vida_total > 100:
            self.vida = 100
        else:
            self.vida = vida_total
