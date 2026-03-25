print('_'*20)
print('Sequência Fibonacci')
print('_'*20)
termos = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
soma = 0
cont = 1
while cont <= 10:
    print('{}'.format(n1), end= ' → ')
    soma = n1 + n2
    n1 = n2
    n2 = soma
    cont += 1
print('FIM')