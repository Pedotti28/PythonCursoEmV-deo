#Faça um programa que leia o angulo qualquer e mostre na tela o valor do seno,cosseno tangente desse angulo.
from math import radians,sin,cos,tan
ang = float(input('Informe o ângulo que você deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {:.1f} tem o SENO de {:.2f}'.format(ang,seno))
print('O ângulo de {:.1f} tem o COSSENO de {:.2f}'.format(ang,cos))
print('O ângulo de {:.1f} tem a TANGENTE de {:.2f}'.format(ang,tang))