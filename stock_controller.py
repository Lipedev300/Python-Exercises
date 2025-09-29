#aqui definimos nossa base de dados em memória, é um tipo de variável que serve como um lista, onde vamos inserir nossos produtos
cellPhones = {
  "IPHONE 15": 10,
  "MOTOROLA G5": 7
}

# aqui exibe os menus no console
sair = 0
menu = 1
while sair != menu:
  print("1 - Conferir estoque.")
  print("2 - Inserir celular.")
  print("3 - Saída celular.")
  print("0 - Sair.")
  menu = int(input("Qual menu deseja acessar? 1. Conferir estoque. 2. Inserir celular. 3. Saída celular. 0. Sair"))
  if menu == 1:
    print("------------------------------------------ Celulares ----------------------------------------------------------")
    pattern = '{: >20} {: >25}'       
    print(pattern.format('Modelo','Quantidade'))
    print("")  
    for key, value in cellPhones.items():
      print(f'{key :>20} {value :>25}')
    print("---------------------------------------------------------------------------------------------------------------")  
  elif menu == 2:
    model = input("Digite o modelo: ").upper()
    quantitity = int(input("Digite a quantidade: "))
    if model in cellPhones:
      quantitity += cellPhones[model]
    cellPhones.update({model: quantitity})
  elif menu == 3:
    model = input("Digite o modelo: ").upper()
    quantitity = int(input("Digite a quantidade: "))
    if model in cellPhones:
      quantitity = cellPhones[model] - quantitity
    cellPhones.update({model: quantitity})
  elif menu == 0:
    print("O sistema encerrou!!")
  else:
    print("Menu invalido!!")