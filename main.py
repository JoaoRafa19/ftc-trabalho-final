from MaquinaMoore import MaquinaMoore
from utils import *
from combate import Combate
from player import Player




def pvp():
    clear()
    file1 = "maquina1.txt"
    estados, estadosIniciais, transicoes = leArquivo(file1)    
    m1 = MaquinaMoore(estados, estadosIniciais[0], transicoes)
    estados, estadosIniciais, transicoes = leArquivo(file1)
    m2 = MaquinaMoore(estados, estadosIniciais[0], transicoes)
    nomeJogador1 = input("Digite o nome do jogador 1: ")
    nomeJogador2 = input("Digite o nome do jogador 2: ")
    player1 = Player(m1, nomeJogador1)
    player2 = Player(m2, nomeJogador2)

    combate = Combate(player1, player2)
    combate.executa()
    
    # # m1.faz_transicao('1')
    # # m1.faz_transicao('0')



    # print(m1.get_estado_atual(), m1.get_saida_atual())


def pve():
    pass

if __name__ == "__main__":
    pvp()
