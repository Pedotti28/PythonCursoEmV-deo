cadastro = {
    'nome': str(input('Nome: ')),
    'idade': 2026 - int(input('Ano de Nascimento: ')),
    'cpts': int(input('Carteiro de trabalho (0 não tem): '))
}
if cadastro["cpts"] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salário'] = int(input('Salário: R$ '))
    cadastro['aposentadoria'] = cadastro["contratação"] - (2026 - cadastro["idade"]) + 35
print('=-' * 30)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
print('=-' * 30)
