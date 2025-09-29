#Este programa simples calcula a média de uma lista de números usando python

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0

for i in lista:
    soma += i

media = soma / len(lista)
print("A média dos números dessa lista é: ", media)