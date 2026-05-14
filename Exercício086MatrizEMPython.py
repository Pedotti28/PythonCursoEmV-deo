lista = [[], [], []]
cont = 0
cont2 = 0

for c in range(0,9):
    n = int(input(f'Digite um valor para [{cont}][{cont2}]: '))
    lista[cont].append(n)
    cont2 += 1
    if cont2 == 3:
        cont += 1
        cont2 = 0
print('-='*30)
print(f'[ {lista[0][0]} ][ {lista[0][1]} ][ {lista[0][2]} ]\n[ {lista[1][0]} ][ {lista[1][1]} ][ {lista[1][2]} ]\n[ {lista[2][0]} ][ {lista[2][1]} ][ {lista[2][2]} ]')
