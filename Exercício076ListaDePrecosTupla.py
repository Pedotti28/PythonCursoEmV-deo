listagem = ('Livro',68,'Unha',100,'Sílios',90,'Sombrancelha',50,'Corretivo',67,
            'Kindle',500,'Blush',59,'Bolsa',30,'Açaí',31.80)
cont = 0
print('-'*50)
print(f'{'LISTAGEM DE PREÇOS':^50}')
print('-'*50)
for li in range(0, len(listagem)):
    if li % 2 == 0:
      print(f'{listagem[li]:.<30}',end='')
    else:
        print(f'R${listagem[li]:>5.2f}')
print('-'*50)