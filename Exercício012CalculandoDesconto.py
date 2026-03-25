#Faça um algoritmo que leia o preço de um produto e motre seu
#preço,com 5% de desconto.
preço = float(input('Qual o preço do produto? '))
des = preço -(preço * 5/100)
print('Você recebeu um desconto de 5% em seu produto agora ele custa R${:.2f}'.format(des))
