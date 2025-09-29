try:
    arquivo = open("notas.txt", "r")
    nomes = []
    linha = arquivo.readline()
    while linha:
        estudante = linha.split()
        if (len(estudante) >7):
            nomes.append(estudante[0])
        linha = arquivo.readline()
    arquivo.close()
    print("Estudantes: ", nomes)
except:
    print("Não foi possível abrir o arquivo.")