casa = float(input('Qual o \033[4:30:42mvalor da casa\033[m? R$'))
sal = float(input('Qual o seu \033[4:30:42msalário\033[m? R$'))
qanos = int(input('Em \033[4:30:43mquantos anos\033[m você irá \033[4:30:43mpagar a casa\033[m? '))
mes = qanos * 12
mensalidade = casa / mes
pcnt30 = (sal * 100)/30
if mensalidade > pcnt30:
    print('EMPRÉSTIMO \033[1:30:41mNEGADO\033[m!')
else:
    print('EMPRÉSTIMO \033[1:30:42mVALIDADO\033[m'.format(mensalidade))
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa,qanos,mensalidade))