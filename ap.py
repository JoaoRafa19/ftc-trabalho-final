'''
Q P F # total states
a # input word symbols
Z Y # stack symbols
Q # starting state
Z # starting stack
F # accepting states
F # E - accepts with empty stack or F - accepts with accepting state
Q a Z Q YZ # list of productions (current state, read from word, take from stack, next state, add to stack)
Q a Y Q YY
Q e Z P Z
Q e Y P Y 
P a Z P e 
P a Y P e
P e Z F e
'''


class AutomatoDePilha:

    def __init__(self, estados, estado_inicial, transicoes):
        self._nome_estado_inicial = estado_inicial
        pilha = []

    def _parse_estados(self, estados, transicoes):
        estados = []
        saidas = [saida for saida in Saida]
        print(saidas)

    def get_estados(self):
        pass

    def get_saida_atual(self):
        pass

    def get_estado_atual(self):
        pass

    def faz_transicao(self, entrada):
        pass
