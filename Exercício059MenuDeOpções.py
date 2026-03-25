val = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
somar = 0
multiplicar = 0
maior = 0
mais = 0
sair = False
while not sair:  #Aqui eu poderia ter substituido o while por 'while != 5' dai o programa teria ficado menor
    print('[ 1 ] Soma \n[ 2 ] Multiplicar \n[ 3 ] Maior \n[ 4 ] Novos valores \n[ 5 ] Sair do programa')
    seleçao = int(input('Digite o que você escolheu: '))
    if seleçao == 1:
        somar = val + val2
        print('{} + {} = {}'.format(val, val2, somar))
    if seleçao == 2:
        multiplicar = val * val2
        print('{} x {} = {}'.format(val, val2, multiplicar))
    if seleçao == 3:
        if val > val2 :
            maior = val
        else:
            maior = val2
        print('Entre {} e {} o MAIOR valor é {}'.format(val, val2,maior))
    if seleçao == 4:
        ex= int(input('Digite um novo valor: '))
        val = ex
        ex2 = int(input('Digite mais um novo valor: '))
        val2 = ex2
    if seleçao == 5:
        sair = True
    if seleçao > 5 or seleçao < 1:
        print('Você digitou errado, Digite novamente.')


