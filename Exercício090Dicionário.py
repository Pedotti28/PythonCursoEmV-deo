di = {}
di['Nome'] = str(input('Nome: '))
di['Média'] = float(input(f'Média de {di["Nome"]}: '))

if di["Média"] >= 6:
    di['Situação'] = 'Aprovado'
elif 5 <= di["Média"] < 7:
    di['Situação'] = 'Recuperação'
else:
    di['Situação'] = 'Reprovado'
for k, v in di.items():
    print(f'{k} é igual a {v}')