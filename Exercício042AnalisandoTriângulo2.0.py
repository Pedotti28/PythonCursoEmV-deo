print("\033[31m-=-\033[m"*20)
print('\033[7:40mANALISADOR DE TRIÂNGULOS\033[m')
print('\033[31m-=-\033[m'*20)

r1 = float(input('Qual o comprimento da primeira reta? '))
r2 = float(input('Qual o comprimento da segunda reta? '))
r3 = float(input('Qual o comprimento da terceira reta? '))

if r1 < r2 + r3 and r3 < r2 + r1 and r2 < r3 + r1:
    print('As retas PODEM formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('É um triângulo EQUILÁTERO.')
    if r1 == r2 and r1 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r2 != r1:
        print('É um triângulo ISÓSCELES.')
    if r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo ESCALENE.')
else:
    print('As retas NÃO podem formar um triângulo!')
