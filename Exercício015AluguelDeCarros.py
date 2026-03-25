dia = int(input('Quantos dias você ficou com o carro? '))
Km = float(input('Quantos Km você percorreu com o carro? '))
preço = 60 * dia + Km * 0.15
print("O total a pagar é de R${:.2f}!!".format(preço))