lista = [[], [], []]
cont = cont2 = par = last_column = maior = 0
for c in range(0,9):
    n = int(input(f'Digite um valor para [{cont}][{cont2}]: '))
    if n % 2 == 0:
        par += n
    if cont2 == 2:
        last_column += n
    lista[cont].append(n)
    cont2 += 1
    if cont2 == 3:
        cont += 1
        cont2 = 0
for num in lista[1]:
    if num > maior:
        maior = num
print('-='*30)
print(f'[ {lista[0][0]} ][ {lista[0][1]} ][ {lista[0][2]} ]\n[ {lista[1][0]} ][ {lista[1][1]} ][ {lista[1][2]} ]\n[ {lista[2][0]} ][ {lista[2][1]} ][ {lista[2][2]} ]')
print('-='*30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da 3° coluna é {last_column}')
print(f'O maior valor da 2° linha é {maior}')