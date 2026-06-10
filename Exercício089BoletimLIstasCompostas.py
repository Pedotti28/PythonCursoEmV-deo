lista = []

while True:
    nome = input('Nome: ')
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])

    prox = ' '
    while prox not in 'SN':
        prox = input('Quer continuar? [S/N] ').upper()
    if prox in 'N':
        break

print('-=' * 40)
print(f'{"No.":<4}{"Nome":<10}{"MEDIA":>8}')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-' * 35)
opc = int(input('Mostrar notas de qual aluno? (999 Interrompe): '))
if opc == 999:
    print('FINALIZANDO...')
if opc <= len(lista) - 1:
    print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')