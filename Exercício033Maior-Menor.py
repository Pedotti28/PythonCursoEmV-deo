n1 = int(input('Escolha um número: '))
n2 = int(input('Escolha mais um número: '))
n3 = int(input('Escolha o último número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O número menor digitado é {}!'.format(menor))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O número maior digitado é {}!'.format(maior))