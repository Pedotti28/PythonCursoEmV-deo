from random import randint
lista = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for jg in range(quant):
    lista.append([])
    print(f'Jogo {jg + 1}: ',end='')
    for n in range(0,6):
        num = (randint(1,60))
        while num  in lista[jg]:
            num = (randint(1,60))
        lista[jg].append(num)
    lista[jg].sort()
    print(lista[jg])
print(' GOOD LUCK '.center(35,'='))