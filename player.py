import random


class Player:
    def __init__(self, maquina , nome):
        self.nome = nome
        self.maquina = maquina
        self.vida = 100
        
    def recebe_dano(self, defesa=False)->int:
        aparagem = random.randint(1, 100)
        dano = random.randint(1, 33)
        if defesa:
            dano = dano - (aparagem // 100 * dano)
        if self.vida > 0:
            self.vida -= dano
            print("Alcançou um estado de defesa em {}\nAparagem do duelista {}:{}!".format(self.nome, self.nome, aparagem))
        return dano
    
    
    def cura(self):
        vida_total = self.vida + random.randint(1, 15)
        if vida_total > 100:
            self.vida = 100
        else:
            self.vida = vida_total
    
            