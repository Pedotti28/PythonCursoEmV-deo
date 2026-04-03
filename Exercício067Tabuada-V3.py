while True:
    print('-'*20)
    t = int(input('Qual tabuada quer ver? '))
    print('-'*20)
    cont = 0
    if t < 0:
        break
    while cont <= 10:
        print(f'{t} x {cont} = {t * cont}')
        cont += 1
