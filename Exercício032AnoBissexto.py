ano = int(input('Qual ano você quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[7:40m{}\033[m é \033[4:34mBISSEXTO\033[m.'.format(ano))
else:
    print("O ano \033[71999:40m{}\033[m NÃO é \033[4:31mBISSEXTO\033[m.".format(ano))