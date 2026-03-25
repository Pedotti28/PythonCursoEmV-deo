#Um professor quer sortear um dos seus alunos para apagar o quadro.Faça um programa que ajudade
#ele,lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = str(input(('Primeiro aluno: ')))
a2 = str(input(('Segundo aluno: ')))
a3 = str(input(('Terceiro aluno: ')))
a4 = str(input(('Quarto aluno: ')))
lista = [a1,a2,a3,a4]
sort = random.choice(lista)
print('O aluno escolhido foi {:!^30}'.format(sort))