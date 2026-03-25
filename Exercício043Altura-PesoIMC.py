altura = float(input('Altura em Metros: '))
peso = float(input('Peso em Kg: '))
imc = peso / (altura * altura)
print('Seu IMC é de \033[4:31m{:.1f}\033[m'.format(imc))
if imc <= 18.5:
    print('\033[4:34mVOCÊ ESTÁ ABAIXO DO PESO\033[m')
elif imc >= 18.5 and imc < 25:
    print('\033[4:34mVOCÊ ESTÁ COM O PESO IDEAL\033[m')
elif imc >= 25 and imc < 30:
    print('\033[4:34mVOCÊ ESTÁ COM SOBREPESO\033[m')
elif imc >= 30 and imc < 40:
    print('\033[4:34mVOCÊ ESTÁ COM OBESIDADE\033[m')
elif imc >= 40:
    print('\033[4:34mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA\033[m')