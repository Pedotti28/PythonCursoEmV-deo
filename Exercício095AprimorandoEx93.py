lista = []
cont = 0
while True:
    print('-' * 30)
    dados = {'nome': str(input('Nome do jogador: ')),}
    dados['partidas'] =  int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
    gols = []
    for g in range(dados["partidas"]):
        gols.append(int(input(f'Quantos gols na partida {g + 1}? ')))
    dados['gols'] = gols
    total = 0
    total += sum(dados["gols"])
    dados['total'] = total
    lista.append(dados.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        else:
            print('ERRO! Digite S ou N apenas.')
    if resp in 'N':
        break

print('-=' *30)
print()
print('-'*60)
for j in lista:
    print(f'{cont} {j["nome"]} marcou {j["gols"]} gols, no total {j["total"]} gols.')
    cont += 1
print('-' * 60)
while True:
    aproveitamento = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    while aproveitamento >= len(lista):
        print(f'ERRO! O jogador {aproveitamento} não existe.')
        aproveitamento = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if aproveitamento == 999:
        break
    print(f'LEVANTAMENTO DO JOGADOR {lista[aproveitamento]["nome"]}:')
    for c, v in enumerate(lista[aproveitamento]["gols"]):
        print(f' No jogo {c+1} {lista[aproveitamento]["nome"]} fez {v} gols.')
