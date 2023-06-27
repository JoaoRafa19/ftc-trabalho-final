
def leArquivo(diretorio):
    estados = []
    estadosIniciais = []
    file = open(diretorio, "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    size = len(lines) - 2
    transicao = [['' for _ in range(3)] for _ in range(size)]
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
            split_string = lines[i].split(' ')
            split_string.pop(1)
            split_string.pop(2)
            for k in range(len(split_string)):
                string = split_string[k]
                transicao[(i-2)][k] = string
    return estados, estadosIniciais, transicao

diretorio = "arquivo.txt"
estados, estadosIniciais, transicao = leArquivo(diretorio)
print(estados)
