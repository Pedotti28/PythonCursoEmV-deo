lista = []

for v in range(0,5):
    valor = int(input('Digite um valor: '))
    if v == 0 or valor > lista[-1]: #Esse lista[-1] pega o valor que está como ultimo da lista, na última posição.
        lista.append(valor)
        print('Adicionado na ultima posição...')
    else:
        cont = 0
        while cont < len(lista):
            if valor <= lista[cont]:
                lista.insert(cont,valor)
                print(f'Adicionado na posição {cont}')
                break
            cont += 1
print(lista)
