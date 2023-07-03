import random
from maquina_moore import Saida


class Player:
    def __init__(self, maquina , nome):
        self.nome = nome
        self.maquina = maquina
        self.vida = 100

    def ataca(self, player)->int:
        print(f"Alcançou um estado de ataque em {self.nome}")
        dano = random.randint(1, 33)
        if player.maquina.get_saida_atual() == Saida.DEFESA:
            aparagem = int(random.random() * dano)
            dano -= aparagem
            print(f"Aparagem do duelista {player.nome}:{aparagem}!")

        print(f"Dano no duelista {player.nome}:{dano}")
        self.vida -= dano
        return dano

    def defende(self):
        print(f"Alcançou um estado de defesa em {self.nome}")

    def cura(self):
        valor = random.randint(1, 15)
        vida_total = self.vida + valor
        print(f"Alcançou um estado de cura em {self.nome}")
        print(f"Cura no duelista {self.nome}: {valor}")
        if vida_total > 100:
            self.vida = 100
        else:
            self.vida = vida_total
