#Faça um algoritmo que leia o salário de um funcionário e
#mostre seu novo salário, com 15% de aumento.
sal = int(input('Informe seu salário: '))
aumento = sal +((sal * 15)/100)
print('Você recebeu um aumento!!!Agora seu salário é de R${:.2f}'.format(aumento))