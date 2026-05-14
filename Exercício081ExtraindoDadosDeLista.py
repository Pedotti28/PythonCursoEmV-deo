lista = []
cinco = 0
while True:
    prox = ' '
    v = lista.append(int(input('Digite um valor: ')))
    if 5 in lista:
        cinco = 1
    while prox not in 'SN':
        prox = input('Quer continuar?[S/N] ').upper()
    if prox in 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são {lista}')
if cinco == 1:
    print(f'O número 5 está na lista, na posição {lista.index(5)}.')




