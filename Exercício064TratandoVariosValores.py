soma = 0
cont = 0
n = 0
while n != 999:
    n = int(input('Digite um número(999 para parar): '))
    if n != 999: #ou inves disso eu poderia repetir o comando acima fora do while e deixer ele abaixo do cont
        soma += n
        cont += 1
print('Foram digitados {} valores e a soma deles é igual a {}'.format(cont,soma))