import random

SAIDA_VAZIO = "vazio"
SAIDA_ATAQUE = "ataque"
SAIDA_DEFESA = "defesa"
SAIDA_CURA = "cura"

class Estado:
    def __init__(self, nome, saida, transicoes_dict):
        self.nome = nome
        self.saida = saida
        self.transicoes_dict = transicoes_dict


class MaquinaMoore:
    def __init__(self, estados, estadosIniciais, transicoes):
        self.nome_estado_inicial = estadosIniciais[0]
        self.lista_estados = self._parse_estados(estados, transicoes)
        self.nome_estado_atual = self.nome_estado_inicial

    def _parse_estados(self, estados, transicoes):
        lista_estados = []

        for estado in estados:
            transicoes_dict = dict()
            for transicao in transicoes[:]:
                nome_estado_atual, nome_estado_dest, entrada = transicao
                if nome_estado_atual == estado:
                    transicoes_dict[entrada] = nome_estado_dest
                    transicoes.remove(transicao)

            if estado == self.nome_estado_inicial:
                lista_estados.append(Estado(estado, SAIDA_VAZIO, transicoes_dict))
            else:
                lista_estados.append(
                    Estado(
                        estado,
                        random.choice((SAIDA_ATAQUE, SAIDA_DEFESA, SAIDA_CURA)),
                        transicoes_dict,
                    )
                )

        return lista_estados

    def _find_estado_atual(self):
         for estado in self.lista_estados:
            if estado.nome == self.nome_estado_atual:
                return estado

    def get_saida_atual(self):
        estado = self._find_estado_atual()
        return estado.saida

    def faz_transicao(self, entrada):
        estado = self._find_estado_atual()
        nome_estado_dest = estado.transicoes_dict[entrada]
        self.nome_estado_atual = nome_estado_dest
