from maquinas.MaquinaMoore import MaquinaMoore
from maquinas.AutomatoDePilha import AutomatoDePilha
from maquina_estado_finito import FiniteStateAutomata
from utils import *
from combate import Combate
from player import Player


def inicializaPlayer(nomePlayer):
    tipoMaquina = input(
        "Digite o tipo de máquina: (1 - Moore, 2 - Automato de Pilha 3 - Estado Finito)")
    file1 = input("Digite o nome do arquivo: ")
    if tipoMaquina == '1':
        estados, estadosIniciais, transicoes = leArquivo(file1)
        maquina = MaquinaMoore(estados, estadosIniciais[0], transicoes)
    elif tipoMaquina == '2':
        estados, estadosIniciais, transicoes = leArquivoAp(file1)
        maquina = AutomatoDePilha(estados, estadosIniciais[0], transicoes)
    elif tipoMaquina == '3':
        maquina = FiniteStateAutomata(True)
        maquina.read_file(file1)

    return Player(maquina, nomePlayer)


def pvp():
    clear()
    file = "ap1.txt"
    estados, estados_iniciais, transicoes = leArquivoAp(file)

    player1 = inicializaPlayer('PILTOVER')
    player2 = inicializaPlayer('ZAUN')

    combate = Combate(player1, player2)
    combate.executa()

    # # m1.faz_transicao('1')
    # # m1.faz_transicao('0')


if __name__ == "__main__":
    pvp()
    # fileType = input("Digite 1 para PVP ou 2 para PVE: ")
    # if fileType == '1':
    #     pvp()
    # elif fileType == '2':
    #     pve()
