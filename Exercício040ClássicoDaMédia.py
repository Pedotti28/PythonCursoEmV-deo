nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
print('Sua média é de {:.1f}'.format(media))
if media < 5:
    print('VOCÊ ESTÁ REPROVADO!')
elif media > 5 and media < 7:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO.')
elif media > 7:
    print('VOCÊ FOI APROVADO!')
