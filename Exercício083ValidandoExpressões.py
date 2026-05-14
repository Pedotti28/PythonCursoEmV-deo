ex = input(str('Digite uma expressão: '))
lista = []
for simb in ex:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')

if len(lista) == 0:
    print('Sua expressão está válida.')
if len(lista) > 0:
    print('Sua expressão está errada.')


