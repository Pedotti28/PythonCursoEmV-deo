from random import randint
from time import sleep

contagem = 0
computador = randint(0 , 10)
print( '-'* 50)
print('Pensando em um número de 0 a 10...Tente adivinhar')
print('-'*50)
adivinha = int(input('O número é: '))
while adivinha != computador:
    sleep(2)
    if adivinha < computador:
        print(' Tente um número MAIOR...')
    else:
        print(' Tente um número MENOR...')
    contagem += 1
    adivinha = int(input('A nãooo, então ele é: '))
print('Foram necessários {} palpites para você adivinhar o número {}'.format(contagem, computador))
