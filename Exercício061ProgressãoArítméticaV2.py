print('_'*20)
print('Progressão Arítmética')
print('_'*20)
t1 = int(input('Qual é o primeiro termo? '))
ra = int(input('Qual é a razão? '))
c = 1
while 10 >= c:
    pr = t1 + ra
    print('{}'.format(t1), end= ' → ')
    t1 = pr
    c += 1
print('ACABOU')