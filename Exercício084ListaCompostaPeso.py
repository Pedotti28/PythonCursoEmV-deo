nome_peso = []
lista = []
maipeso = menpeso = 0
while True:
    nome_peso.append(str(input('Nome: ')))
    nome_peso.append(float(input('Peso: ')))
    if len(lista) == 0:
        maipeso = menpeso = nome_peso[1]
    else:
        if nome_peso[1] >= maipeso:
            maipeso = nome_peso[1]
        if nome_peso[1] <= menpeso:
            menpeso = nome_peso[1]
    lista.append(nome_peso[:])
    nome_peso.clear()


    prox = str(input('Você quer continuar?[S/N] ')).upper()
    while prox not in 'SN':
        prox = str(input('Você quer continuar?[S/N] ')).upper()
    if prox == 'N':
        break
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maipeso}Kg. Peso de ',end='')
for v in lista:
    if v[1] == maipeso:
        print(v[0],end=' ')
print(f'\nO menor peso foi de {menpeso}Kg. Peso de ',end='')
for v in lista:
    if v[1] == menpeso:
        print(v[0],end=' ')
