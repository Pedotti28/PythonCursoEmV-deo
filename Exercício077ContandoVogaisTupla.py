tupla = ('blue lock', 'manga', 'anime', 'programação', 'estudar', 'ler', 'jogar',
         'viajar','intercâmbio','futebol')
for palavras in tupla: #Aqui o for pegou todas as palavras dentro desta tupla
    print(f'\nNa palavra {palavras.upper()} temos: ', end='') #Aqui esse \n serviu para a pular linha, e o end= para não quebrar ela
    for letra in palavras: #Aqui o for pegou cada letra dentro das palavras e no if viu se tinha alguma vogal.
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
