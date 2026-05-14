n_extenso = ('zero','um','dois','três','quatro','cinco',
             'seis','sete','oito','nove','dez','onze',
             'doze','treze','quatorze','quinze',
             'dezesseis','dezessete','dezoito','dezenove','vinte')
answer = 'S'
while answer in 'S':
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            print(f'Você digito o número {n_extenso[n]}.')
            answer = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
        if answer == 'N':
            break
