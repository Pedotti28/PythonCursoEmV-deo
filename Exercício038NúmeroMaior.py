n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 == n2:
    print('Não existe valor maior, os números são iguais.')
elif n1 > n2:
    print('O primeiro número({}) é maior que o segundo número({})'.format(n1,n2))
else:
    print('O segundo número({}) é maior que o primeior número({})'.format(n2,n1))