#Escreva um programa que leia um valor em metros e o exiba
#convertido em centímetros e milímetros.
metros = int(input('Informe o valor em metros: '))
centi = metros * 100
mili = metros * 1000
print(' {} metros \n {} centímetros \n {} milímetros.'.format(metros,centi,mili))