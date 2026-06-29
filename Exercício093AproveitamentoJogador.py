
dados = {    'nome': str(input('Nome do jogador: ')),}
dados['partidas'] =  int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
gols = []
for g in range(dados["partidas"]):
    gols.append(int(input(f'Quantos gols na partida {g + 1}? ')))
dados['gols'] = gols
total = 0
total += sum(dados["gols"])
dados['total'] = total
print('-=' *30)
print(dados)
print('-=' *30)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' *30)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for c, v in enumerate(gols):
    print(f'    => Na partida {c+1}, {dados["nome"]} fez {v} gols.')
print(f'Foi um total de {total} gols.')
print('-=' *30)
