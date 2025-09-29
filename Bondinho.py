"""
 Este algoritmo simples é baseado em um cenário de viagem escolar de ônibus, em que existem alunos e monitores, e a viagem só é possível se o número de pessoas no ônibus é menor ou igual a 50.
 Caso a viagem seja possível, é impresso "s" no console, e caso contrário, é impresso "n".
 Para esse algoritmo foram usados conceitos de variáveis e condicionais if/else
 """

alunos = 40
monitores = 15

if (alunos + monitores) < 50:
    print("s")
else:
    print("n")