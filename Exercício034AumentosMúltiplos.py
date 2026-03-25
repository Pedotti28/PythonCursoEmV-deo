sal = float(input('Qual é o valor do seu \033[4:30:42msalário\033[m? '))
a10 = 0
if sal > 1250:
    a10 = (sal * 10) / 100
    sal = sal + a10
if sal < 1250:
    a10 = (sal * 15) / 100
    sal = sal + a10
print('Você recebeu um aumento de \033[4:30:42mR${:.2f}\033[m e agora seu salário é de \033[4:30:42mR${:.2f}\033[m'.format(a10,sal))