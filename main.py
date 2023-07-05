from MaquinaMoore import MaquinaMoore
from AutomatoDePilha import AutomatoDePilha
from FiniteStateAutomata import FiniteStateAutomata
from utils import *
from combate import Combate
from player import Player

intro = """
                             
\t\t\t\t   @@@@@@@@  @@@@@@@   @@@@@@@  
\t\t\t\t   @@@@@@@@  @@@@@@@  @@@@@@@@  
\t\t\t\t   @@!         @@!    !@@       
\t\t\t\t   !@!         !@!    !@!       
\t\t\t\t   @!!!:!      @!!    !@!       
\t\t\t\t   !!!!!:      !!!    !!!       
\t\t\t\t   !!:         !!:    :!!       
\t\t\t\t   :!:         :!:    :!:       
\t\t\t\t    ::          ::     ::: :::  
\t\t\t\t    :           :      :: :: :

                                   
 |`    _  _| _  _ _  _  _ _|_ _  _   _| _   _|_ _  _  _. _    _| _    _ _  _ _ |_  _ _|_ _ 
 |-|_|| |(_|(_|| | |(/_| | | (_)_\\  (_|(_|   | (/_(_)| |(_|  (_|(_)  (_(_)| | ||_)(_| | (/_
 """

win = """
|----------------------------------------------------------|
| dP     dP dP d888888P  .88888.   888888ba  dP  .d888888  |
| 88     88 88    88    d8'   `8b  88    `8b 88 d8'    88  |
| 88    .8P 88    88    88     88 a88aaaa8P' 88 88aaaaa88a |
| 88    d8' 88    88    88     88  88   `8b. 88 88     88  |
| 88  .d8P  88    88    Y8.   .8P  88     88 88 88     88  |
| 888888'   dP    dP     `8888P'   dP     dP dP 88     88  |
|----------------------------------------------------------|
"""

def inicializaPlayer(nomePlayer):
    print("\t\t",intro)
    print(f'Player: {nomePlayer}')
    tipoMaquina = input(
        "Digite o tipo de máquina:\n\t1 - Máquina de Moore\n\t2 - Autômato de Pilha\n\t3 - Máquina de Estado Finito\n> ")
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
    print(win)
    # # m1.faz_transicao('1')
    # # m1.faz_transicao('0')


if __name__ == "__main__":
    pvp()
    # fileType = input("Digite 1 para PVP ou 2 para PVE: ")
    # if fileType == '1':
    #     pvp()
    # elif fileType == '2':
    #     pve()
