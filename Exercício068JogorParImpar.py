from random import randint
V = 0
while True:
    n = int(input('Escolha seu número: '))
    par_im = ' '
    while par_im not in 'PI':
        par_im = input('Par ou Ímpar?[P/I] ').upper().strip()[0]
        print('-'*40)
    computador = randint(0, 10)
    resultado = n + computador
    print(f'Você jogou {n} e o computador jogou {computador}, Total é {resultado}')
    if par_im == 'P':
        if resultado % 2 == 0:
            print('Você ganhou, MEUS PARABÉNS!!')
            V += 1
        else:
            print('PERDEU TROXA HAHAHAHAHHAAH.')
            break
    if par_im == 'I':
        if resultado % 2 == 1:
            print('Você ganhou, MEUS PARABÉNS!!')
            V += 1
        else:
            print('PERDEU TROXA HAHAHAHAHHAAH.')
            break
    print('-' * 40)
print ('-='* 20)
print('                 GAME OVER            ')
print(f'Você venceu {V} vezes. Meus parabéns')
print ('-='* 20)
