total = p_1k = p_barato = cont = 0
n_barato = ' '

while True:
    p = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    if cont == 0 or preco < p_barato:
        n_barato = p
        p_barato = preco

    if preco > 1000:
        p_1k += 1
    cont += 1
    total += preco
    s_n = ' '
    while s_n not in 'SN':
        s_n = input('Quer continuar? [S/N] ').upper().strip()[0]
    if s_n == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de gastos da compra foi de: {total:.2f}')
print(f'Temos {p_1k} produtos custando acima de R$1000,00.')
print(f'O produto mais barato foi a {n_barato} custando R${p_barato:.2f}')
