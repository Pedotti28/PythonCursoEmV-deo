#Crie um programa que leia o noe completo de uma pessoa e mostre: O nome com todas as letras
#maíusculas.  O nome com todas minúsculas.   Quantas letras no todo(sem considerar espaços).
#Quantas letras tem o primeiro nome.
nome = input('Qual seu nome completo: ').strip()
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
divido = nome.split()
print('Seu nome {} tem ao todo {} letras'.format(nome, len(nome) - nome.count(' ')))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(divido[0], nome.find(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(divido[0], len(divido[0])))
