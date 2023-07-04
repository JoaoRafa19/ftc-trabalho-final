class Estado:
    def __init__(self, nome, saida, transicoes_dict):
        self.nome = nome
        self.saida = saida
        self.transicoes_dict = transicoes_dict
    
    def __str__(self):
        return f"Nome: {self.nome}, Saida: {self.saida}, Transicoes: {self.transicoes_dict}"

