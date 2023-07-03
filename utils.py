import os

def leArquivo(diretorio):
    estados = []
    estadosIniciais = []
    file = open(diretorio, "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    size = len(lines) - 2
    transicoes = [['' for _ in range(3)] for _ in range(size)]
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
            for k in range(len(split_string)):
                string = split_string[k]
                transicoes[(i-2)][k] = string
    return estados, estadosIniciais, transicoes



def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
