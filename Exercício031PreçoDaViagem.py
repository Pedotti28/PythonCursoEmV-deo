viagem = float(input('Qual a distância da viagem? '))
preco = viagem * 0.50
if viagem > 200:
    preco = viagem * 0.45
    print("O preço de sua viagem teve um disconto por ser mais longa então ficou R${:.2f}".format(preco))
else:
    print('O preço da sua viagem ficou R${:.2f}'.format(preco))