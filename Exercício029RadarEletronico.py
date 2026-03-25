carro = int(input('Qual a velocidade do carro? '))
if carro > 80:
    carro = (carro - 80) * 7
    print('Você ultrapassou o limite de 80Km/h!! Sua multa é de R${}'.format(carro))
else:
    print("Você não ultrapassou os 80Km/h, Dirija com segurança!!")