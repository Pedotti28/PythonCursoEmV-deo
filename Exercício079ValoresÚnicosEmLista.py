lista = []
cont = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado.')
    else:
        print('Número DUPLICADO.Tente novamente.')
    progress = input('Você quer continuar?(S/N) ').upper()
    if progress in 'N':
        break
print(lista)
