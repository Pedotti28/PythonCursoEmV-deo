s_n = ''
lista = []
media = 0
while True:
    dados = {'nome': input('Nome: '),
    'sexo': input('Sexo: [M/F] ').upper()[0],
    'idade': int(input('Idade: '))}
    lista.append(dados.copy())
    s_n = input('Quer continuar? [S/N] ').upper()[0]
    if s_n not in 'SN':
        s_n = input('Quer continuar? [S/N] ').upper()[0]
    if s_n in 'N':
        break
print('=-'*30)
print(f'- O grupo tem {len(lista)} pessoas.')

for people in lista:
    media += people["idade"]
media = media / len(lista)
print(f'- A média de idade é de {media} anos.')

mulheres = []
print('- As mulheres cadastradas foram: ',end='')
for people in lista:
    if people["sexo"] in 'F':
        print(f'{people["nome"]}',end= " ")
print()
print('- Lista das pessoas acima da média:\n')
for people in lista:
    if people["idade"] > media:
        print(f'nome = {people["nome"]}; sexo = {people["sexo"]}; idade = {people["idade"]};\n')
print('<< ENCERRADO >>')