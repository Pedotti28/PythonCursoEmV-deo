sexo = str(input('Informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MmFf' :
    sexo = str(input('Digite novamente ae escreva: m para masculino e f para feminino: ')).strip().upper()[0]
print('Fim')