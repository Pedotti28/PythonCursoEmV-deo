#Faça um programa que leia quanto dinehiro uma pessoa tem na
#carteira e mostre quantos Doláres ela pode comprar.
real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dol = real / 6.11
print('Você pode comprar {:.2f} doláres com R${:.2f}!'.format(dol,real))