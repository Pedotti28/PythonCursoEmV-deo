lista = []
par = []
impar = []
while True:
    prox = ' '
    v = int(input('Digite um valor: '))
    lista.append(v)
    if v % 2 == 0:
        par.append(v)
    if v % 2 == 1:
        impar.append(v)

    while prox not in 'SN':
        prox = input('Quer continuar?[S/N] ').upper()
    if prox == 'N':
            break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
