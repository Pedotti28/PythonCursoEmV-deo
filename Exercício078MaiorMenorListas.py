
lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if maior < lista[c]:
            maior = lista[c]
        if menor > lista[c]:
            menor = lista[c]

print(f'Você digitou os valores {lista}')
print(f'O maior número da lista é {maior} que estão nas posições ',end='')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}',end='...')
print(f'\n O menor número da lista é {menor} que está nas posições ',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}',end='...')