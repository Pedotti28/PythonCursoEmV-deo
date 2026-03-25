#Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e seu antecessor
n = int(input('Informe o número: '))
ant = int(n - 1)
suc = int(n + 1)
print('SUCESSOR DE {0} = {1:!^30} \n ANTECESSOR DE {0} = {2:!^30}'.format(n,suc,ant))
#n = int(input('Informe o número: '))    outro tipo e mais simples.
#print('SUCESSOR DE {0} = {1:!^30} \n ANTECESSOR DE {0} = {2:!^30}'.format(n,n+1,n-1))