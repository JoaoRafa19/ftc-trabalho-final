from saida import Saida

class Estado:

    def __init__(self, nome_estado, transicoes, saida):
        self.nome = nome_estado
        self.transicoes = transicoes
        self.saida = saida




class Transicao:
    
    def __init__(self, simbolo_a_ser_lido, simbolo_a_desempilhar, estado_destino, simbolo_a_empilhar):

        self.simbolo_a_ser_lido = simbolo_a_ser_lido
        self.simbolo_a_desempilhar = simbolo_a_desempilhar
        self.estado_destino = estado_destino
        self.simbolo_a_empilhar = simbolo_a_empilhar

    def __str__(self):
        # le | desempilha | destino | empilha
        return "> {} | {} | {} | {}".format(self.simbolo_a_ser_lido, self.simbolo_a_desempilhar, self.estado_destino, self.simbolo_a_desempilhar)

class AutomatoDePilha:

    def __init__(self, estados, estado_inicial, transicoes):

        self._nome_estado_inicial = estado_inicial
        self._pilha = []
        self._nome_estado_atual = self._nome_estado_inicial
        self._estado_atual = None
        self._lista_estados = self._parse_estados(estados, transicoes)

    def empilha(self, simbolo):
        # Empilha o simbolo
        self._pilha.append(simbolo)
    
    def desempilha(self):
        # Desempilha o simbolo do topo da pilha
        if not self.pilha_vazia():
            self._pilha.pop()
    
    def _parse_estados(self, estados, transicoes):
        # Cria os estados e suas transicoes
        _estados = []
        saidas = [Saida.DEFESA,  Saida.CURA, Saida.ATAQUE]
        for estado in estados:
            transicoes_dict = []
            for transicao in transicoes:
                if estado.strip() == transicao[0].strip():
                    _transicao = Transicao(
                        transicao[1][0], transicao[1][1], transicao[1][2], transicao[1][3])
                    transicoes_dict.append(_transicao)

            _estado = Estado(estado, transicoes_dict, Saida.VAZIO if estado == self._nome_estado_inicial else saidas[int(transicao[1][0])])
            _estados.append(_estado)
        return _estados
    
    def get_estados(self):
        # Retorna a lista de estados
        return self._lista_estados

    def _find_estado_atual(self):
        # Retorna o estado atual
        for estado in self._lista_estados:
            if estado.nome == self._nome_estado_atual:
                self._estado_atual = estado
                return self._estado_atual
    
    def get_saida_atual(self):
        # Retorna a saida do estado atual
        return self._estado_atual.saida

    def pilha_vazia(self) -> bool:
        # Verifica se a pilha esta vazia
        return self._pilha.__len__() == 0

    def faz_transicao(self, entrada):
        # Realiza transicao da maquina
        estado = self._find_estado_atual()
        for transicao in estado.transicoes:
            
            if not self.pilha_vazia():
                if transicao.simbolo_a_ser_lido == entrada and transicao.simbolo_a_desempilhar == self._pilha[-1]:
                    self._nome_estado_atual = transicao.estado_destino
                    self._estado_atual = self._find_estado_atual()
                    des = self.desempilha()
                    if transicao.simbolo_a_empilhar != '*':
                        self.empilha(transicao.simbolo_a_empilhar)
                    return self.get_saida_atual()
            else:
                if transicao.simbolo_a_ser_lido == entrada and transicao.simbolo_a_desempilhar == '*':
                    self._nome_estado_atual = transicao.estado_destino
                    self._estado_atual = self._find_estado_atual()
                    if transicao.simbolo_a_empilhar != '*':
                        self.empilha(transicao.simbolo_a_empilhar)
                    return self.get_saida_atual()
        
