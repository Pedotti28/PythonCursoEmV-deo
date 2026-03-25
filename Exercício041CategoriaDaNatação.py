from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
categoria = 0
if idade < 9:
    categoira = 'MIRIM'
elif idade > 9 and idade < 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade < 19:
    categoria = 'JÚNIOR'
elif idade > 19 and idade < 25:
    categoria == 'SENIOR'
elif idade > 25:
    categoria == 'MASTER'
print('Você tem {} então você  é da categoria {} na natação.'.format(idade,categoria))