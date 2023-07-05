import random
import enum
import itertools
from estado import Estado
from saida import Saida

class MaquinaMoore:
    def __init__(self, estados, estados_inicial, transicoes):
        self._nome_estado_inicial = estados_inicial
        self._lista_estados = self._parse_estados(estados, transicoes)
        self._nome_estado_atual = self._nome_estado_inicial

    def _parse_estados(self, estados, transicoes):
        lista_estados = []
        _transicoes = transicoes.copy()

        saidas = (Saida.ATAQUE, Saida.DEFESA, Saida.CURA)
        # iterador circular, sempre que chamar next(cycler) vai ir pro proximo valor de saidas
        # se acabar os valores comeca do comeco de novo(por isso é circular)
        cycler = itertools.cycle(saidas)

        for estado in estados:
            transicoes_dict = dict()
            for transicao in _transicoes[:]:
                nome_estado_atual, nome_estado_dest, entrada = transicao
                if nome_estado_atual == estado:
                    transicoes_dict[entrada] = nome_estado_dest
                    _transicoes.remove(transicao)

            if estado == self._nome_estado_inicial:
                lista_estados.append(
                    Estado(estado, Saida.VAZIO, transicoes_dict))
            else:
                lista_estados.append(
                    Estado(
                        estado,
                        next(cycler),
                        transicoes_dict,
                    )
                )

        return lista_estados

    def get_estados(self):
        return self._lista_estados



    def _find_estado_atual(self):
        for estado in self._lista_estados:
            if estado.nome == self._nome_estado_atual:
                return estado

    # get saida do estado atual da maquina
    def get_saida_atual(self):
        estado = self._find_estado_atual()
        return estado.saida

    # get estado atual da maquina
    def get_estado_atual(self):
        return self._nome_estado_atual

    # faz uma transicao de acordo com a entrada
    def faz_transicao(self, entrada):
        estado = self._find_estado_atual()
        nome_estado_dest = estado.transicoes_dict[entrada]
        self._nome_estado_atual = nome_estado_dest
        return self.get_saida_atual()
