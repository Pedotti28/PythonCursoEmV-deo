n = int(input('Digite o valor do fatorial: '))
fat = n
mult = 1
while fat > 0:
    print('{}'.format(fat), end='')
    print(' x ' if fat > 1 else ' = ', end='')
    mult *= fat
    fat -= 1
print('{}'.format(mult))
