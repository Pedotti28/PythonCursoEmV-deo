from operator import index
nove = 0
dados = (int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')),
         int(input('Digite um valor: ')))
print(f'Você digitou os valores: {dados}')
print(f'O nùmero 9 foi digitado {dados.count(9)} vezes')
if 3 in dados:
    print(f'O número 3 está na {dados.index(3)+1}° posição.')
else:
    print('O número 3 não está em nenhuma posição.')
print(f'Os valores pares digitados foram: ',end='')

for d in dados:
    if d % 2 == 0:
        print(f'{d} ',end='')

