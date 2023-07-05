from saida import Saida
from utils import clear

class Combate:
    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turno = 0
    
        
    def executa(self):
        while self.player1.vida > 0 and self.player2.vida > 0:
            clear()
            print("Turno de: {}".format([self.player1.nome, self.player2.nome][self.turno % 2]))
            
            print("Vida restante de {} = {}".format(self.player1.nome, self.player1.vida))
            print("Vida restante de {} = {}".format(self.player2.nome, self.player2.vida))
            entrada = input("Qual leitura você deseja fazer?")
            try:
                self.player1.maquina.faz_transicao(entrada)
                self.player2.maquina.faz_transicao(entrada)
            except Exception as e:
                print("Entrada inválida")
                input("\nPRESSIONE ENTER PARA CONTINUAR...")
                continue

            if self.turno % 2 == 0:
                saidaPlayer2 = self.player2.maquina.get_saida_atual()
                saidaPlayer1 = self.player1.maquina.get_saida_atual()
            else:
                saidaPlayer1 = self.player1.maquina.get_saida_atual()
                saidaPlayer2 = self.player2.maquina.get_saida_atual()
            
            if saidaPlayer1 == Saida.ATAQUE :
                dano = self.player2.recebe_dano(saidaPlayer2 != Saida.DEFESA)
                print("Dano no duelista {}:{}".format(self.player2.nome, dano))
            if saidaPlayer2 == Saida.ATAQUE:
                dano= self.player1.recebe_dano(saidaPlayer1 != Saida.DEFESA)
                print("Dano no duelista {}:{}".format(self.player1.nome, dano))
            
            if saidaPlayer1 == Saida.CURA:
                self.player1.cura()
            if saidaPlayer2 == Saida.CURA:
                self.player2.cura()
                
            self.turno += 1
            input("Pressione enter para continuar...")
        
        print("{} Vitorioso!".format(self.player2.nome if self.player1.vida <= 0 else self.player1.nome))
            

        