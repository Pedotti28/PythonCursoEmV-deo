from os.path import join

prase = input('Digite uma frase: ').strip().upper()
palavras = prase.split()
jo1n = "".join(palavras)
inverso = ''
for c in range(len(jo1n) - 1, -1, -1 ):
    inverso += (jo1n[c])
print(jo1n, inverso)
if inverso == jo1n:
    print('{} é um palíndromo pois o inverso da frase é igual a frase.'.format(prase))
else:
    print('{} não é um palíndromo pis o inverso da frase não é o mesmo da frase.')