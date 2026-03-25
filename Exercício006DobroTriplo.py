#Crie um algoritmo que leia um número e mostre o seu dobro,
#O triplo e a raiz quadrada.

n = int(input('Informe o número: '))
dobro = int(n * 2)     #dobro = n * 2
triplo = int(n * 3)    #triplo = n * 3
rq = (float(n**(1/2))) #rq = n ** (1/2)
print('O dobro de {0:=^20} é {1} o triplo é {2} \n A raiz quadrada é {3}'.format(n,dobro,triplo,rq))
