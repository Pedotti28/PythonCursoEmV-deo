#Crie um algoritmo que leia duas notas e informe sua média.
n1 = float(input('Informe sua primeira nota: '))
n2 = float(input('Informe sua segunda nota: '))
media = (n1 + n2)/2
print('A média das suas notas foi {:!^30.1f}'.format(media))