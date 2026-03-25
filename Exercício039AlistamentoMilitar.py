idade = int(input('Qual é sua idade? '))
flt = 18 - idade
ano = flt + 2026
alis = 2026 - idade
if idade < 18:
    print('Você irá se alistar no serviço militar daqui {} anos. Em {}.'.format(flt,ano))
elif idade == 18:
    print('Está na hora de você se alistar.')
elif idade > 18:
    print('Já passou do tempo de você se alistar ao serviço militar. Você se alistou em {}'.format(alis))