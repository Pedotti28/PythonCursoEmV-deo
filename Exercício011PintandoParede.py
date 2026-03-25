#Faça um programa que leia a largura e a altura de uma parede
#em metros,calcule a sua área e a quantidade tinta necessária
#para pintá-la, sabendo que cada litro de tinta,pinta uma
#área de 2m².
alt = float(input('Informe a altura em metros da sua parede: '))
lar = float(input('Informe a largura em metros da sua parede: '))
area = alt * lar
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} \nA área da parede é {:.2f},e será preciso {:.2f} litros de tintas para pintar a parede.'.format(alt,lar,area,tinta))