from random import randint
itens = 'Pedra', 'Papel', 'Tesoura'
computador = randint(0,2)
print('''PEDRA,PAPEL TESOUUUURA!!
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jokempo = int(input('Qual você escolheu? (Digite o número.) '))
print('-=-'*11)
print('O computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jokempo]))
print('-=-'*11)
if computador == 0:
    if jokempo == 0:
        print('EMPATOU')
    if jokempo == 1:
        print('VOCÊ VENCEUU!!')
    if jokempo == 2:
        print('COMPUTADOR GANHOU!')
if computador == 1:
    if jokempo == 0:
        print('COMPUTADOR GANHOU!')
    if jokempo == 1:
        print('EMPATOU')
    if jokempo == 2:
        print('VOCÊ GANHOUU!!')
if computador == 2:
    if jokempo == 0:
        print('VOCÊ GANHOU!!')
    if jokempo == 1:
        print('VOCÊ PERDEU!')
    if jokempo == 2:
        print('EMPATOU')
