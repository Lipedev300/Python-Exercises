import time
from threading import Thread

#criando função
def contaNumeros(nome):
    print(f"Thread {nome}: Iniciando contagem agora")
    for i in range(1, 10):
        print(i)
        time.sleep(2)

def contaNumerosa(nome):
    for i in range(1, 10):
        print(f"Contagem {nome}: iniciando contagem")
        time.sleep(3)

#criando threads
t1 = Thread(target= contaNumeros, args=("1",))
t2 = Thread(target= contaNumerosa, args=("2",))

#iniciando threads
t1.start()
t2.start()

#aguardando as threads terminarem a execução
t1.join()
t2.join()

#mensagem final do programa principal
print("Programa principal encerrado, até breve")