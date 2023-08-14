import random
import sys

n1 = int(input('Digite um número de 1 a 10: '))
sorteio = random.randint(1, 10)

if sorteio == n1:
    print('Número escolhido certo! ')
else:
    print('Número escolhido errado! ')


print('O número sorteado pelo sistema foi:  ', sorteio)

escolha = input('Coloque r para recomeçar e s para sair: ')

if (escolha == "r"):
    print("Voltando")
    import sorteio

    print("Saindo do programa...")
    sys.exit()





