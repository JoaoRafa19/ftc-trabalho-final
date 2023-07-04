import random
from maquina_moore import Saida


class Player:
    def __init__(self, maquina , nome):
        self.nome = nome
        self.maquina = maquina
        self.vida = 100

    def ataca(self, player)->int:
        dano = random.randint(1, 33)
        print(f"Ataque do duelista {self.nome}: {dano}!")
        if player.maquina.get_saida_atual() == Saida.DEFESA:
            aparagem = int(random.random() * dano)
            dano -= aparagem
            print(f"Aparagem do duelista {player.nome}: {aparagem}!")

        print(f"Dano no duelista {player.nome}: {dano}")
        player.vida -= dano
        return dano

    def cura(self):
        valor = random.randint(1, 15)
        vida_total = self.vida + valor
        if self.vida <= 0:
            print(f"Duelista {self.nome} com vida negativa! Não é possível curar!")
            return

        print(f"Cura no duelista {self.nome}: {valor}")
        if vida_total > 100:
            self.vida = 100
        else:
            self.vida = vida_total
