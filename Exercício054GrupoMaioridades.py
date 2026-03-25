maiores = 0
menores = 0
people = 1
ano_atual = int(input('Em que ano estamos?'))
for c in range(7):
    nascimento = int(input('Em que ano a {} nasceu?'.format(people)))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
    people = people + 1
print('{} pessoas20 ja atingiram a maior idade e {} pessoas ainda não.'.format(maiores, menores))