from os.path import exists
from maquina_moore import Saida

class FiniteStateAutomata:
    def __init__(self,hardcoded=False):
        self.alphabet =  ("0","1", "2")
        self.last_input = None
        if hardcoded:
            return
        self.states = sorted([str(x) for x in input("Q - Nome dos Estados: ")])
        self.init_state = str(input("I - Estado Inicial: "))
        self.current_state = self.init_state
        self.final_states = [str(x) for x in input("F - Estados Finais: ")]
        self.transitions = self.get_transitions()

    def get_transitions(self, transitions):
        transitions = []
        total = 0
        curr_transition = str(input(f"Transição {total}: "))
        total+=1
        while curr_transition != "end":
            if self.check_transition_format(curr_transition):
                transitions.append(curr_transition)
            else:
                total-=1
            curr_transition = str(input(f"Transição {total}: (envie end para finalizar): "))
            
            total+=1
        return transitions

    def check_transition_format(self, transition):
        parts = transition.split(" ")
        if not (parts[0] in self.states and parts[2] in self.states and parts[4] in self.alphabet):
            print("Transição inválida. Tente novamente.")
            return 0
        return 1

    def run_transition(self, start, letter):
        for t in self.transitions:
            parts = t.split(" ")
            parts = {"start":parts[0],"end":parts[2],"letter":parts[4]}
            if start == parts["start"]:
                if letter == parts["letter"] or parts["letter"] == "\\":
                    return parts["end"]
        return False

    def get_saida_atual(self):
        select = {0:Saida.ATAQUE,1:Saida.DEFESA,2:Saida.CURA}
        return select[int(self.last_input) if self.last_input else Saida.VAZIO]

    def faz_transicao(self, _input):
        for t in self.transitions:
            parts = t.split(" ")
            parts = {"state":parts[0],"end":parts[2],"_input":parts[4]}
            if parts["state"] == self.current_state:
                if _input == parts["_input"] or parts["_input"] == "\\":
                    self.last_input = _input
                    self.current_state = parts["end"]

    def run_word(self,word):
        print(f"Palavra \"{word}\": ",end="")
        curr_state = self.init_state
        for letter in word:
            curr_state = self.run_transition(curr_state,letter)
            if not curr_state:
                print("X")
                return 1
        if curr_state in self.final_states:
            print("OK")
            return 0
        print("X")
        return 1

    def read_file(self, filename):
        with open(filename) as file:
            lines = file.readlines()
            ini_lines = [line[3:].strip("\n") for line in lines[0:3]]
            self.transitions = [line.strip("\n") for line in lines[3:]]
            self.states = ini_lines[0].split(" ")
            self.init_state = ini_lines[1]
            self.current_state =  self.init_state
            self.final_states = ini_lines[2].split(" ")

def tests():
    x = FiniteStateAutomata(True)
    file_name = "mef1.txt"#input('\nDigite o nome do arquivo de teste: ')
    while(not exists(file_name)):
        file_name = input('Arquivo não encontrado, digite novamente: ')
    print('\n\nResultado dos testes:\n\n')  
    x.read_file(file_name)
    print(x.transitions)
    x.run_word("012021")

if __name__ == "__main__":
    tests()