from random import randint
from time import sleep

computador = randint(0,5) #Faz o computador "PENSAR"
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO .......')
sleep(3)
if jogador == computador:
    print('PARABENSSS VOCÊ ME VENCEU!!')
else:
    print('HAHAHAHAHAHA VOCÊ ERROU O NÚMERO ERA {}!!! E NÃO {}.'.format(computador,jogador))
