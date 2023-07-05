import os 

def leArquivoAp(diretorio):
    estados = []
    estadosIniciais = []
    transicoes = []
    file = open(diretorio, "r")
    lines = []
    
    for i, line in enumerate(file):
        if(line[0] == 'Q' and i == 0):
            line = line.strip()
            strip = line.split(":")[1].strip().split(" ")
            for state in strip:
                estados.append(state)
        elif (i == 1):
            line = line.strip()
            strip = line.split(":")[1].strip().split(" ")
            for state in strip:
                estadosIniciais.append(state)
        else:
            line = line.strip()
            state, transition =  line.split('->')
            state = state.strip()
            transition = transition.strip()
            # le | desempilha | destino | empilha
            transition = [item.strip() for item in transition.split('|')]
            transicoes.append([state, transition])
            
    return estados, estadosIniciais, transicoes

def leArquivo(diretorio):
    estados = []
    estadosIniciais = []
    file = open(diretorio, "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    size = len(lines) - 2
    transicoes = list()
    for i in range(len(lines)):
        if(i == 0):
            split_string = lines[i].split(' ')
            for k in range(len(split_string)-1):
                estados.append(split_string[k+1])
        elif(i == 1):
            split_string = lines[i].split(' ')
            for k in range(len(split_string) - 1):
                estadosIniciais.append(split_string[k + 1])
        else:
            if lines[i] == '---':
                break

            split_string = lines[i].split(' ')
            split_string.pop(1)
            split_string.pop(2)

            e_atual = split_string.pop(0)
            e_dest = split_string.pop(0)
            for entrada in split_string:
                transicoes.append([e_atual, e_dest, entrada])
    return estados, estadosIniciais, transicoes



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
