mais_velho = ''
mulheres_menos_20 = 0
soma_idade = 0
int_velho = 0
for p in range(1, 5):
    print('Pessoa {}'.format(p))

    nome = input('NOME : ')
    idade = int(input("IDADE: "))
    sexo = input('SEXO M/F :').upper()

    if sexo == 'M' and  idade > int_velho:
            int_velho = idade
            mais_velho = nome
    if sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1
    soma_idade += idade

soma_idade = soma_idade / 4
print('A média da idade do grupo é: {}'.format(soma_idade))
print('O cara mais velho tem {} e se chama: {}'.format(int_velho, mais_velho))
print('{} mulher/es tem menos de 20 anos.'.format(mulheres_menos_20))