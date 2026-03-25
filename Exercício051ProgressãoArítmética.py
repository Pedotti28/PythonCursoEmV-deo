print('_'*20)
print('Progressão Arítmética')
print('_'*20)
t1 = int(input('Qual é o primeiro termo? '))
ra = int(input('Qual é a razão? '))
d10 = (11- 1) * ra
for c in range(t1, d10,ra):
    pr = t1 + ra
    print('{}'.format(c), end= ' → ')
print('ACABOU')
