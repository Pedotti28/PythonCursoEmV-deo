print('_'*20)
print('Progressão Arítmética')
print('_'*20)
t1 = int(input('Qual é o primeiro termo? '))
ra = int(input('Qual é a razão? '))
c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while total >= c:
        pr = t1 + ra
        print('{}'.format(t1), end= ' → ')
        t1 = pr
        c += 1
    print('PAUSE')
    mais = int(input('Quantos termos mais você quer? '))

print('Progressão finalizada com {} termos.'.format(total))

