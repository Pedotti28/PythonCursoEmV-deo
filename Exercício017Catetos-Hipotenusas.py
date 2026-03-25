#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
#,calcule e mostre o comprimento da hipotenusa
c1 = float(input('Quanto mede o cateto oposto? '))
c2 = float(input('Quanto mede o cateto adjacente? '))
hi = (c1 ** 2 + c2 ** 2) ** 1/2
print('A hipotenusa vai medir {:.2f}!'.format(hi))
                    #or
# import math
# c1 = float(input('Quanto mede o cateto oposto? '))
# c2 = float(input('Quanto mede o cateto adjacente? '))
# math.hypot(c1, c2)
# print('A hipotenusa vai medir {:.2f}!'.format(hi))       #more easy