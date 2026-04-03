i18 = homem = m_20 = 0

while True:
    s_n = sexo = ' '
    print('-'*40)
    print('           CADASTRE UMA PESSOA')
    print('-'*40)
    ida = int(input('Idade: '))
    if ida >= 18:
        i18 += 1
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F] ').upper().strip()[0]
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and ida < 20:
        m_20 += 1
    while s_n not in 'SN':
        s_n = input('Quer continuar? [S/N] ').upper().strip()[0]
    if s_n == 'N':
        break
print('====== FIM DO PROGRAMA ====== ')
print(f'Total de pessoas com mais de 18 anos: {i18}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {m_20} mulheres com menos de 20 anos.')