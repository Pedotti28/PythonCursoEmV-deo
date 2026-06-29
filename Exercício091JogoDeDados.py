from operator import itemgetter
from random import randint
d = {}
for c in range (1,5):
    d[f'Jogador{c}'] = randint(1,6)
for k, v in d.items():
    print(f'{k} tirou {v}')
ranking = list()
ranking = sorted(d.items(), key= itemgetter(1), reverse=True)
print(ranking)
for k, v in enumerate(ranking):
    print(f'{k+1} lugar: {v[0]} com {v[1]} pontos.')
